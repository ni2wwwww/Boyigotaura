# telegram_bot.py
# Save this code as telegram_bot.py in the same directory as gates.py and gates.json

import logging
import asyncio
import inspect
import json
import re

from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes, ApplicationBuilder

# Import all gateway functions from your gates.py file
# The 'as gates' part gives it a namespace to avoid function name collisions.
import gates

# --- Configuration ---
# It's recommended to use environment variables for the token in production.
# For this script, we will prompt the user to enter it.
TELEGRAM_BOT_TOKEN = "7248159727:AAEzc2CNStU6H8F3zD4Y5CFIYRSkyhO_TiQ" # Will be filled by user input

# --- Logging Setup ---
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Gateway Analysis and Command Mapping ---
# I will infer command names from your python function names and their content.
# This makes the bot modular. Add a function to gates.py, and a new command is born!
GATEWAY_COMMAND_MAP = {
    # Function Name in gates.py -> /command_name for Telegram
    'vip': 'chargebee_vip',
    'stc': 'chargebee_stc',
    'pay': 'paypal_braintree',
    'sa': 'punctualkart_auth',
    'xc': 'layerpanel_auth_cvc',
    'sf': 'layerpanel_auth_ccn',
    'info': 'bin',
    'sd': 'bizinkonline_auth',
    'scc': 'ladymcadden_auth',
    'sh': 'square_harmony',
    'pv': 'privatecheck',
    'vbv': 'vbv',
    'br': 'paintsupply_braintree',
    'brr': 'kits_braintree',
    'be': 'brandmark_braintree',
    'sff': 'kaffakoffee_auth',
    'b3': 'ruckshop_braintree',
    'cvv': 'scrapbook_braintree',
    'auth': 'firefly_auth',
    'ccx': 'bigbattery_auth',
    'pp': 'paypal_charge',
    'gg': 'paintsupply_auth_v2',
    'sq': 'square_redwood',
    'au': 'tradechem_auth',
    'cn': 'paintsupply_ccn',
    'sv': 'brandcrowd_charge',
    'stn': 'brandcrowd_token',
}

# --- Bot Command Handlers ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message when the /start command is issued."""
    commands = await context.bot.get_my_commands()
    help_text = "👋 Welcome! This bot provides access to multiple payment gateways.\n\n"
    help_text += "Here are the available commands:\n"
    for command in commands:
        help_text += f"/{command.command}\n"
    help_text += "\nUsage: `/{command} CARD|MM|YY|CVC`"
    await update.message.reply_text(help_text)


def create_gateway_handler(gateway_function):
    """
    A factory function to create a unique command handler for each gateway function.
    This is the core of the modular approach.
    """
    async def gateway_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user_input = " ".join(context.args)
        command = update.message.text.split()[0].lstrip('/')

        # Basic validation for card format
        card_pattern = r"^\d{15,16}[|]\d{1,2}[|]\d{2,4}[|]\d{3,4}$"
        bin_pattern = r"^\d{6,16}$"

        if not user_input:
            await update.message.reply_text(f"❌ Please provide input.\nUsage: `/{command} CARD|MM|YY|CVC`")
            return

        # Special handling for BIN check which takes only card number
        if gateway_function.__name__ == 'info':
             if not re.match(bin_pattern, user_input):
                 await update.message.reply_text(f"❌ Invalid format for BIN check.\nUsage: `/{command} CARD_NUMBER`")
                 return
        # Handling for other card-based functions
        elif '|' in user_input and not re.match(card_pattern, user_input):
            await update.message.reply_text(f"❌ Invalid card format.\nUsage: `/{command} CARD|MM|YY|CVC`")
            return

        # Let the user know we're working on it
        processing_message = await update.message.reply_text("⏳ Processing, please wait...")

        try:
            # Execute the gateway function
            logger.info(f"Executing function '{gateway_function.__name__}' with input: {user_input}")
            
            # The gateway functions from gates.py are synchronous, so we run them
            # without blocking the main asyncio event loop.
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(None, gateway_function, user_input)

            # Format the result for output
            if isinstance(result, (list, tuple)):
                response_text = "\n".join(str(item) for item in result)
            else:
                response_text = str(result)
            
            logger.info(f"Function '{gateway_function.__name__}' returned: {response_text}")
            
            # Send the result back to the user by editing the "Processing" message
            await context.bot.edit_message_text(
                chat_id=update.effective_chat.id,
                message_id=processing_message.message_id,
                text=f"✅ **Result for `/{command}`:**\n\n`{response_text}`"
            )

        except Exception as e:
            logger.error(f"Error executing gateway '{gateway_function.__name__}': {e}", exc_info=True)
            await context.bot.edit_message_text(
                chat_id=update.effective_chat.id,
                message_id=processing_message.message_id,
                text=f"🛑 An error occurred while processing your request for `/{command}`."
            )

    return gateway_command_handler


# --- Main Bot Logic ---

def main() -> None:
    """Start the Telegram bot."""
    
    # Get bot token from user
    global TELEGRAM_BOT_TOKEN
    token_input = input("Please enter your Telegram Bot Token: ").strip()
    if not token_input:
        print("Token cannot be empty. Exiting.")
        return
    TELEGRAM_BOT_TOKEN = token_input

    # Create the Application
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Add the /start command handler
    application.add_handler(CommandHandler("start", start))
    
    # --- Dynamically create and register handlers for each gateway ---
    bot_commands = []
    
    # Get all functions from the imported 'gates' module
    all_functions = inspect.getmembers(gates, inspect.isfunction)

    for func_name, func_obj in all_functions:
        # Check if the function is a gateway we should create a command for
        if func_name in GATEWAY_COMMAND_MAP:
            command_name = GATEWAY_COMMAND_MAP[func_name]
            
            # Create a specific handler for this gateway function
            handler = create_gateway_handler(func_obj)
            
            # Register the command handler with the bot
            application.add_handler(CommandHandler(command_name, handler))
            
            # Add to the list of commands for Telegram's UI
            bot_commands.append(BotCommand(command_name, f"Executes the {func_name} gateway."))
            logger.info(f"Registered command '/{command_name}' for function '{func_name}'")

    # Set the bot's commands in the Telegram UI
    # This needs to be done in an async context
    async def set_bot_commands():
        await application.bot.set_my_commands(bot_commands)
        logger.info("Bot command list updated successfully.")

    # Run the setup function
    loop = asyncio.get_event_loop()
    if loop.is_running():
        loop.create_task(set_bot_commands())
    else:
        loop.run_until_complete(set_bot_commands())


    # --- Run the bot ---
    print("\nBot is starting... Press Ctrl+C to stop.")
    application.run_polling()


if __name__ == '__main__':
    try:
        with open('gates.json', 'r') as f:
            json.load(f)
        print("✅ gates.json loaded successfully.")
    except FileNotFoundError:
        print("❌ ERROR: gates.json not found. Please make sure it's in the same directory.")
    except json.JSONDecodeError:
        print("❌ ERROR: gates.json is not a valid JSON file.")
    else:
        main()
