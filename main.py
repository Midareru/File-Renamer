import os
import imghdr


def main():
	remove_ad = True # Remove the extra image ad at the start of each chapter.
	path = "./files"
	log_path = "log.txt" # Store corupted file list
	count = 1
	corrupted = False

	# Clear log file, and set it for read/write
	logfile = open(log_path, "wr")

	# Renaming folders
	for root, dirs, files in os.walk(path):
		# We need to rename these in numeric order!
		try:
			for i in sorted(dirs, key=int):
				try:
					os.rename(os.path.join(root, i), os.path.join(root, str(count)))
				except OSError:
					print("Failed to rename folder: " + os.path.join(root, i) + "\n")
				count += 1	
		except ValueError:
			print("Can't sort non-numeric folder names, operation failed.")
			return

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
					print("Possible corupted file: " + os.path.join(root, i))
					logfile.write(os.path.join(root, i) + "\n")
					corrupted = True
				else:
					try:
						# Skip files that already have an extension
						if "." in i:
							print("skipping " + i)
						else:
							os.rename(os.path.join(root, i), os.path.join(root, i + "." + img_type))
					except OSError:
						print("Failed to rename file: " + os.path.join(root, i) + "\n")

	# Close the log file, saving the contents
	logfile.close()
	return corrupted


corrupted = main()
print "Done."

# Prompt the user to use the repair tool if we had corrupt files
if corrupted:
	print("Risk of corrupt files, redownload effected chapters and place into ./repair")
	print("Use repair.py to fix the corrupt files.")
