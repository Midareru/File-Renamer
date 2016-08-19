import os
import imghdr

def main():
	path = "./files"
	count = 1

	for root, dirs, files in os.walk(path):
		for i in files:
			img_type = imghdr.what(os.path.join(root, i))
			os.rename(os.path.join(root, i), os.path.join(root, str(count) + "." + img_type))
			count += 1

	count = 1
	for root, dirs, files in os.walk(path):
		for i in dirs:
			os.rename(os.path.join(root, i), os.path.join(root, str(count)))
			count += 1

main()
print "done"
