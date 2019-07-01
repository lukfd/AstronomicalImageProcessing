# coloring img using bw rgb filters

from PIL import Image
import PIL.Image as Image

def Main():
	# read image from file
	picturesname = ["NGC7331"]  # can also be .png
	rgbcolors = ["Red","Green","Blue"]
	imgred = Image.open(str(picturesname[0])+"_"+str(rgbcolors[0])+".jpg")
	imggreen = Image.open(str(picturesname[0])+"_"+str(rgbcolors[1])+".jpg")
	imgblue = Image.open(str(picturesname[0])+"_"+str(rgbcolors[2])+".jpg")

	pixels = Finilize(imgred,imggreen,imgblue)

	# get resolution of image
	width, height = imgred.size
	# create colored img
	#img = imgred
	imgred.putdata(list(map(tuple, pixels)))

	# save new image to a file
	imgred.save(str(picturesname[0])+"_"+"Final.bmp") # MUST be .bmp

def getNumberOfPixels(img):
	result = (img.width)*(img.height)
	return result

def getPixels(img):
	return list(map(list, img.getdata()))

def Colorfilter(pixels):
	for i in range(len(pixels)):	
		pixelvalue = int (pixels[i][0])
	return pixelvalue

def Finilize(redfilter,greenfilter,bluefilter):
	wholeimg = []
	#onepixel = []
	red = getPixels(redfilter)
	green = getPixels(greenfilter)
	blue = getPixels(bluefilter)
	# combine filters & putting together
	for i in range (len(red)):
		onepixel = [red[i][0],green[i][0],blue[i][0]]
		wholeimg.append(onepixel)
	print(wholeimg)	
	return list(wholeimg)

Main()


