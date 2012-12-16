"Rsa code for encryption and decryption "

from random import randrange, getrandbits
import math

p=0
q=0
totient=0
e=0
d=0
def miller_rabin(n,test=10):
	p=getrandbits(n)
#	print "random ",p 
	if p%2==0:
		return miller_rabin(n,test)
	m=(p-1)/find_factor(p-1)
	r=int(math.log(((p-1)/m),2))
	flag=0
	t=0
	while t<test:
		a=randrange(2,p)
		q=0
#		print "A",a 
		if int(pow(a,m,p))==1:
			flag=1
#		print "entering "	
		while q<r and flag==0:
#			print q
			if int(pow(a,(2**q)*m,p))==p-1:
				flag=1		
			q+=1	
		if flag==0:
			return miller_rabin(n,test)
		t+=1
#		print t	
	return p	

def gen_Rsa(p,q):
	"""Generate public and private keys"""
	n= p*q
	if n < 65537:
		return (3, inv(3, totient), n)
	else:
		return (65537, inv(65537,totient), n)    

def xgcd(x, y):
	"""Extended Euclidean Algorithm"""
	s1, s0 = 0, 1
	t1, t0 = 1, 0
	while y:
		q = x // y
		x, y = y, x % y
		s1, s0 = s0 - q * s1, s1
		t1, t0 = t0 - q * t1, t1
	return x, s0, t0      

def text2Int(text):
    """Convert a text string into an integer"""
    return reduce(lambda x, y : (x << 8) + y, map(ord, text))

def int2Text(number, size):
    """Convert an integer into a text string"""
    text = "".join([chr((number >> j) & 0xff)
                    for j in reversed(range(0, size << 3, 8))])
    return text.lstrip("\x00")

def int2List(number, size):
    """Convert an integer into a list of small integers"""
    return [(number >> j) & 0xff
            for j in reversed(range(0, size << 3, 8))]

def list2Int(listInt):
    """Convert a list of small integers into an integer"""
    return reduce(lambda x, y : (x << 8) + y, listInt)

def modSize(mod):
    """Return length (in bytes) of modulus"""
    modSize = len("{:02x}".format(mod)) // 2
    return modSize

def encrypt_text(ptext, pk, mod):
    """Encrypt message with public key"""
    size = modSize(mod)
    output = []
    while ptext:
        nbytes = min(len(ptext), size - 1)
        aux1 = text2Int(ptext[:nbytes])
        assert aux1 < mod
        aux2 = pow(aux1, pk, mod)
        output += int2List(aux2, size + 2)
        ptext = ptext[size:]
    return output

def decrypt_text(ctext, sk, p, q):
    """Decrypt message with private key
    using the Chinese Remainder Theorem"""
    mod = p * q
    size = modSize(mod)
    output = ""
    while ctext:
        aux3 = list2Int(ctext[:size + 2])
        assert aux3 < mod
        m1 = pow(aux3, sk % (p - 1), p)
        m2 = pow(aux3, sk % (q - 1), q)
        h = (inv(q, p) * (m1 - m2)) % p
        aux4 = m2 + h * q
        output += int2Text(aux4, size)
        ctext = ctext[size + 2:]
    return output

def inv(p, q):
    """Multiplicative inverse"""
    s, t = xgcd(p, q)[0:2]
    assert s == 1
    if t < 0:
    	t += q
    return t

def rsa_encrypt(number):
	global p,q,totient,n,d
	p=miller_rabin(128,6)
	q=miller_rabin(128,6)
	totient=(p-1)*(q-1)
	e,d,n=gen_Rsa(p,q)
	aux1=pow(number,e,n)
	print "Message:",aux1,"\nNumber:",n,"\nKey:",d

def rsa_decrypt(number,n,d): 
	"""Decrypt message with private key
	using the Chinese Remainder Theorem"""
	aux1=pow(number,d,n)
	return aux1

def find_factor(p):
	k=1
	while p%2==1:
		p/=k
		k*=2
	return k

if __name__ == '__main__':
	
	number=8585943545935473768754324567876543276543276543L
	print number
	output=rsa_encrypt(number)
	print output
	print rsa_decrypt(output)
