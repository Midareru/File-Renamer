import os
import imghdr
from shutil import copyfile


log_path = "repair_log.txt"  # Log for this tool
corrupted_log = "log.txt"  # What files need to be replaced
repair_source = "./repair"  # Path to folder with non corrupt files
repair_dest = "./files"  # Path to folder with corrupt files

output = open(log_path, "wr")


def log(text):
	print(text)
	output.write(text + "\n")


def main():
	with open(corrupted_log, "r") as f:
		for line in f:
			# Create path for the replacement file
			repair_path = line.split(repair_dest)
			repair_path = repair_path[1].strip("\n")
			repair_path = repair_source + repair_path
			# Strip trailing \n from file
			corrupt_path = line.strip("\n")

			print("repairing: " + corrupt_path)

			# Check we have the reqired files
			if not os.path.isfile(corrupt_path):
				log("Failed to find corrupt file: " + corrupt_path)
			elif not os.path.isfile(repair_path):
				log("Failed to find replacement file:" + repair_path)
			elif imghdr.what(repair_path) is None:
				log("Unable to determine type of replacement image!")
				log(repair_path)
			else:
				try:
					# Delete corrupt file
					os.remove(corrupt_path)
					# Copy over file
					copyfile(repair_path, corrupt_path)
					# Add the file extension to the moved file
					os.rename(corrupt_path, corrupt_path + "." + imghdr.what(corrupt_path))
					log("Repair suceeded.")
				except OSError:
					log("OS Error: " + corrupt_path + ", " + repair_path)

main()
output.close()
print("Done.")
