import os
import imghdr
import sys

# Store folder names here for easy reading later
corrupted_dirs = []

# Get the folder name from the path
def get_dirname(path):
	path = path.split('/')
	return path[2]

# Returns an input string, with non digit chars removed
def get_numeric(input_text):
	text = ""
	for c in input_text:
		if c.isdigit():
			text += c

	return text


# Renames folders to names with only numerals
def clean_folders(path):
	for root, dirs, files in os.walk(path):
		for i in dirs:
			try:
				name = get_numeric(i)  # Strip non-numeric chars
				os.rename(os.path.join(root, i), os.path.join(root, name))
			except OSError:
				print("Failed to rename: " + i)

	print("Finished cleaning folders.")


def main():
	remove_ad = True  # Remove the extra image ad at the start of each chapter.
	path = "./files"
	log_path = "log.txt"  # Store corrupted file list
	count = 1
	corrupted = False

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
			print("sanitise folder names? (y/n)")

			clean = ""

			# For comparability reasons, find out if we use input() or raw_input()
			if sys.version_info[0] < 3:
				clean = raw_input()
			else:
				clean = input()

			if "y" in clean:
				print("Removing non numerics from folder names")
				clean_folders(path)  # Makes folders numeric only
				print("Trying again...")
				return main()  # Use recursion to try again
			else:
				print("Exiting.")
				return False

	# Clear log file, and set it for read/write
	logfile = open(log_path, "w")

	# Renaming files
	for root, dirs, files in os.walk(path):
		for i in files:
			img_type = imghdr.what(os.path.join(root, i))

			if i == '0' and remove_ad is True:
				try:
					os.remove(os.path.join(root, i))  # Delete ad
				except OSError:
					print("failed to delete: " + os.path.join(root, i) + "\n")
			else:
				# Add image extension
				if img_type is None:
					print("Possible corrupted file: " + os.path.join(root, i))
					logfile.write(os.path.join(root, i) + "\n")
					# Log the effected chapter/s
					corrupted_dirs.append(get_dirname(os.path.join(root, i)))
					corrupted = True
				else:
					try:
						# Skip files that already have an extension
						if "." in i:
							pass
						else:
							os.rename(os.path.join(root, i), os.path.join(root, i + "." + img_type))
					except OSError:
						print("Failed to rename file: " + os.path.join(root, i) + "\n")

	# Close the log file, saving the contents
	logfile.close()
	print("done")
	return corrupted


corrupted = main()

# Prompt the user to use the repair tool if we had corrupt files
if corrupted:
	print("Risk of corrupt files, redownload effected chapters and place into ./repair")
	print("Use repair.py to fix the corrupt files.")
	print("Effected chapters:")
	# Convert to set to remove duplicate chapters
	chapters = set(corrupted_dirs)
	for chapter in sorted(chapters, key=int):
		print(chapter)
