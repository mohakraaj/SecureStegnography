import cv
def main():
	img=cv.LoadImage('/Users/MAC/Desktop/img.jpg',1);

	cv.Set2D(img,123,123,(100,100,100,0));

	cv.SaveImage('saved.jpg',img);

	img2=cv.LoadImage('saved.jpg',1);

	print cv.Get2D(img2,123,123);
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

def bit_list(n):
    l=[]
    while n:
        k=n & 255
        n=n>>8
        l.append(k)
    return l

def list_bit(l):
    n=0L
    i=len(l)-1
    while i>=0:
        n=n<<8 | l[i] 
        i-=1
    return n    
# returns a copy of the word shifted n bytes (chars)
# positive values for n shift bytes left, negative values shift right
def rotate(word, n):
    return word[n:]+word[0:n]

# iterate over each "virtual" row in the state table and shift the bytes
# to the LEFT by the appropriate offset
def shiftRows(state):
    for i in range(4):
        state[i*4:i*4+4] = rotate(state[i*4:i*4+4],i)

# iterate over each "virtual" row in the state table and shift the bytes
# to the RIGHT by the appropriate offset
def shiftRowsInv(state):
    for i in range(4):
        state[i*4:i*4+4] = rotate(state[i*4:i*4+4],-i)

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


if __name__ == '__main__':
	main()