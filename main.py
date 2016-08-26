import os
import imghdr

def main():
	remove_ad = True # Remove the extra image ad at the start of each chapter.
	path = "./files"
	count = 1

	# Renaming files
	for root, dirs, files in os.walk(path):
		for i in files:
			img_type = imghdr.what(os.path.join(root, i))
			if i == '0' and remove_ad == True:
				os.remove(os.path.join(root, i)) # Delete ad
			else:
				# Add image extension
				os.rename(os.path.join(root, i), os.path.join(root, i + "." + img_type))

	# Renaming folders
	for root, dirs, files in os.walk(path):
		for i in dirs:
			os.rename(os.path.join(root, i), os.path.join(root, str(count)))
			count += 1

main()
print "done"
