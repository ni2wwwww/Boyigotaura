
import requests

def GetStr(string, start, end):
    string = ' ' + string
    ini = string.find(start)
    if ini == -1:
        return ''
    ini += len(start)
    end_idx = string.find(end, ini)
    if end_idx == -1:
        return ''
    return string[ini:end_idx].strip()

def check_key(sk):
    skval = '100'

    data = {
       "card[number]": "5278540001668044",
       "card[exp_month]": "10",
       "card[exp_year]": "2024",
       "card[cvc]": "252"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    auth = (sk, '')

    response1 = requests.post('https://api.stripe.com/v1/tokens', data=data, headers=headers, auth=auth)
    r1 = response1.text
    msg = GetStr(r1, '"message": "', '"')

    response2 = requests.get('https://api.stripe.com/v1/balance', auth=auth)
    r2 = response2.text

    currn = GetStr(r2, '"currency": "', '"')
    balance = GetStr(r2, '"amount":', ',')
    pending = GetStr(r2, '"pending": [{\n      "amount":', ',')
    if not pending:
        pending = GetStr(r2, '"livemode": true,\n  "pending": [\n    {\n      "amount":', ',')
    if pending:
        try:
            pending = float(pending) / float(skval)
        except ValueError:
            pending = 0
    
    if 'usd' in r2:
        currn = '$'
        currf = '🇺🇸'
        currs = 'USD'
    elif 'inr' in r2:
        currn = '₹'
        currf = '🇮🇳'
        currs = 'INR'
    elif 'cad' in r2:
        currn = '$'
        currf = '🇨🇦'
        currs = 'CAD'
    elif 'aud' in r2:
        currn = 'A$'
        currf = '🇦🇺'
        currs = 'AUD'
    elif 'aed' in r2:
        currn = 'د.إ'
        currf = '🇦🇪'
        currs = 'AED'
    elif 'sgd' in r2:
        currn = 'S$'
        currf = '🇸🇬'
        currs = 'SGD'
    elif 'nzd' in r2:
        currn = '$'
        currf = '🇳🇿'
        currs = 'NZD'
    elif 'eur' in r2:
        currn = '€'
        currf = '🇪🇺'
        currs = 'EUR'
    elif 'gbp' in r2:
        currn = '£'
        currf = '🇬🇧'
        currs = 'GBP'
    else:
        currn = 'N/A'
        currf = 'N/A'
        currs = currn

    if "rate_limit" in r1:
        result = f'''𝐑𝐚𝐭𝐞 𝐋𝐢𝐦𝐢𝐭 ⚠️
𝐊𝐞𝐲 ➜ {sk}
𝐑𝐞𝐬𝐮𝐥𝐭 ➜ Request rate limit exceeded.
𝐁𝐚𝐥𝐚𝐧𝐜𝐞 ➜ {balance} {currn}
𝐏𝐞𝐧𝐝𝐢𝐧𝐠 𝐀𝐦𝐨𝐮𝐧𝐭 ➜ {pending} {currn}
𝐂𝐮𝐫𝐫𝐞𝐧𝐜𝐲 ➜ {currs} {currf}'''
    elif "tok" in r1 or "Your card was declined." in r1:
        result = f'''𝐋𝐢𝐯𝐞 𝐊𝐞𝐲 ✅
𝐊𝐞𝐲 ➜ {sk}
𝐑𝐞𝐬𝐮𝐥𝐭 ➜ Request rate limit exceeded.
𝐁𝐚𝐥𝐚𝐧𝐜𝐞 ➜ {balance} {currn}
𝐏𝐞𝐧𝐝𝐢𝐧𝐠 𝐀𝐦𝐨𝐮𝐧𝐭 ➜ {pending} {currn}
𝐂𝐮𝐫𝐫𝐞𝐧𝐜𝐲 ➜ {currs} {currf}'''
    elif "Invalid API Key provided" in r1:
        result = f'''𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐀𝐏𝐈 𝐊𝐞𝐲 ❌
𝐊𝐞𝐲 ➜ {sk}
𝐑𝐞𝐬𝐮𝐥𝐭 ➜ Invalid API Key Provided.'''
    elif "testmode_charges_only" in r1:
        result = f'''𝐓𝐞𝐬𝐭 𝐌𝐨𝐝𝐞 ❌
𝐊𝐞𝐲 ➜ {sk}
𝐑𝐞𝐬𝐮𝐥𝐭 ➜ Your account cannot currently make live charges.
𝐁𝐚𝐥𝐚𝐧𝐜𝐞 ➜ {balance} {currn}
𝐏𝐞𝐧𝐝𝐢𝐧𝐠 𝐀𝐦𝐨𝐮𝐧𝐭 ➜ {pending} {currn}
𝐂𝐮𝐫𝐫𝐞𝐧𝐜𝐲 ➜ {currs} {currf}'''
    elif "api_key_expired" in r1:
        result = f'''𝐄𝐱𝐩𝐢𝐫𝐞𝐝 𝐊𝐞𝐲 ❌
𝐊𝐞𝐲 ➜ {sk}
𝐑𝐞𝐬𝐮𝐥𝐭 ➜ Expired API Key Provided.'''
    else:
        result = f'''𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 𝐍𝐨𝐭 𝐋𝐢𝐬𝐭𝐞𝐝 ⚠️
𝐊𝐞𝐲 ➜ {sk}
𝐑𝐞𝐬𝐮𝐥𝐭 ➜ {msg}
𝐁𝐚𝐥𝐚𝐧𝐜𝐞 ➜ {balance} {currn}
𝐏𝐞𝐧𝐝𝐢𝐧𝐠 𝐀𝐦𝐨𝐮𝐧𝐭 ➜ {pending} {currn}
𝐂𝐮𝐫𝐫𝐞𝐧𝐜𝐲 ➜ {currs} {currf}'''
    return result