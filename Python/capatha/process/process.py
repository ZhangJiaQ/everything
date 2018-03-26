from PIL import Image

def get_imgry():
	# make grayscale conversion and make binary sequence
	image = Image.open('1.bmp')
	imgry = image.convert('L')
	table = get_bin_table()
	out = imgry.point(table, '1')

	# find pic width and highth
	print(imgry.width)


def sum_9_righon(img, x, y):
	pass


def get_bin_table(threshold=140):
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table


if __name__ == '__main__':
	get_imgry()
