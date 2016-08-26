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
				try:
					os.remove(os.path.join(root, i)) # Delete ad
				except OSError:
					print("failed to delete: " + os.path.join(root, i) + "\n")
			else:
				# Add image extension
				if img_type is None:
					print("Possible corupted file: " + os.path.join(root, i) + "\n")
				else:
					try:
						os.rename(os.path.join(root, i), os.path.join(root, i + "." + img_type))
					except OSError:
						print("Failed to rename file: " + os.path.join(root, i) + "\n")

	# Renaming folders
	for root, dirs, files in os.walk(path):
		for i in dirs:
			try:
				os.rename(os.path.join(root, i), os.path.join(root, str(count)))
			except OSError:
				print("Failed to rename folder: " + os.path.join(root, i) + "\n")
			count += 1		
main()
print "done"
