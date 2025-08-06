import re
def reg(cc):
	regex = r'\d+'
	matches = re.findall(regex, cc)
	match = ''.join(matches)
	n = match[:16]
	mm = match[16:18]
	yy = match[18:20]
	cvc = match[20:23]
	if n.startswith("3"):
		n = match[:15]
		mm = match[15:17]
		cvc = match[19:24]
		yy = match[17:19]
	if yy == '20':
		yy = match[18:22]
		cvc = match[22:25]
		if n.startswith("3"):
			n = match[:15]
			mm = match[15:17]
			cvc = match[21:25]
			yy = match[17:21]
	cc = f"{n}|{mm}|{yy}|{cvc}"
	if n.startswith("3"):
		if not re.match(r'^\d{15}$', n):
			return
	else:
		if not re.match(r'^\d{16}$', n):
			return
	if not re.match(r'^\d{3,4}$', cvc):
		return
	return cc
	