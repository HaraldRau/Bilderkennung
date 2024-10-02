from PIL import Image

img = Image.open("Kastanie.png")

pixels = img.getdata(band=0)

for i in range(64):
	if i % 8 == 0:
		print(end = "\n")
	print(pixels[i],end = ";")
print(end = "\n")
