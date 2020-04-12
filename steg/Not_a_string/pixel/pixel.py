import Image

img = Image.open( "QR.png" )
width, height = img.size
pixel = img.load()
result = ""

def magic( pixel ):
	k = 1.158371
	res = (pixel[0]&0x1f)*k+(pixel[1]&0x3f)*k+(pixel[2]&0x7f)*k
	return int( res )

for w in range(width):
	for h in range(height):
		result += chr( magic( pixel[w,h] ) )
		
open("pixel.enc","wb").write( result )