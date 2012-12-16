import cv,cv2
import hashlib

width=500
height=424
img='/Users/MAC/Desktop/img.png'	
output_img='/Users/MAC/Desktop/img1.png'
non_volatile=[]
pixel=cv2.imread(img)

def read_bits(inpute,outpute):
	o=0
	i=0
	while outpute:
		o=outpute & 1
		inpute[i]=inpute[i]^o
		outpute =outpute>>1
		i+=16
	return inpute

def list_bits(l):
    n=0L
    i=len(l)-1
    while i>=0:
        n=n<<8 | l[i] 
        i-=1
    return n 

def binary(n):
	k=[0 for i in range(8)]
	i=0
	while i<8:
		k[7-i]=(n&1)
		n=n>>1
		i+=1
	return k

def byte_int(byte):
	n=0
	for ele in byte:
		n=n<<1
		n=n|ele	
	return n

def get_NonVolatile():
	for i in range(len(pixel)):
		for j in range(len(pixel[i])):
			non_volatile.append(pixel[i][j][0]>>1)
			non_volatile.append(pixel[i][j][1]>>1)
			non_volatile.append(pixel[i][j][2]>>1)
	md5 = hashlib.md5()
	md5.update(str(non_volatile))
	return md5.hexdigest()

def get_bitstream_str(stream):
	block=[]
	#print "printing stream" ,list(stream)
	for c in list(stream):
		block.extend(binary(ord(c)))
	#print "Printing block",block 	
	return block		

def modify_volatile(binnumber):
	i=0
	j=0
	size=len(binnumber)
#	print "Yooo the size is -----------:",binnumber

	while i<size  and j<len(pixel):
		k=0
		while i<size and k<len(pixel[j]):
			l=0
			while i<size and l<3:
				if binnumber[i]==1:
					pixel[j][k][l]=pixel[j][k][l] | 1
				elif binnumber[i]==0:
					pixel[j][k][l]=pixel[j][k][l] & 0
				else :
					print "Some Major error Happening "
				i+=1
				l+=1
			k+=1	
		j+=1	
	cv2.imwrite(output_img,pixel)				

def get_addedbits():
	output_pixel=cv2.imread(output_img)
	byte=[]
	length=1
	block=[]
	bits=[]
	size=0
	for i in range(len(output_pixel)):
		for j in range(len(output_pixel[i])):
			for k in range(3):
				byte.append(output_pixel[i][j][k]&1)
				bits.append(output_pixel[i][j][k]&1)
				if (len(byte)==8):
				#	print byte
					c=byte_int(byte)
				#	print c 
					if(chr(c)=='\0'):
						#print bits
						return block
					byte=[]		
					block.append(c)
				size+=1	
	return block				

def image_read():	
	for i in range(len(pixel)):
		for j in range(len(pixel[0])):
			print(pixel[i][j])

if __name__ == '__main__':
#	outpute=27
#	inpute=[4,8,16,32,64,128]
#	inpute=read_bits(inpute,outpute)
#	print inpute, outpute    	
	try:
		if pixel is None:
			print ("Yooo i think u missed image :P")
	except:
		exit()
	modify_volatile()
	get_addedbits()	
#	get_NonVolatile()
#	print (non_volatile)
#	binnumber=[0 for i in range(400)]
#	modify_volatile(binnumber)
	#print bin(pixel[0][0])

#	print bin(pixel[0][0]>>1)
#	print bin(pixel[0][0]<<1)