import sys
import string

if len(sys.argv) != 2:
	sys.exit()

def cubemap(digits):
	if len(digits) != 3:
		raise IndexError
	if not digits.isnumeric():
		raise ValueError
	a=int(digits[0])-1
	b=int(digits[1])-1
	c=int(digits[2])-1
	if a < 0 or a > 5 or b < 0 or b > 5 or c < 0 or c > 5:
		raise OverflowError
	return a*36+b*6+c

digits=sys.argv[1]
passphrase=[]
glyph=''.join([string.ascii_uppercase,string.digits,string.ascii_lowercase,'!@#$%^&*()'])

for off in range(0,len(digits),3):
	try:
		n = cubemap(digits[off:off+3]) % len(glyph)
		passphrase.append(glyph[n])
	except IndexError:
		break

sys.stdout.write(''.join(passphrase))
