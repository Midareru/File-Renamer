import os
import imghdr
from shutil import copyfile


log_path = "repair_log.txt" # Log for this tool
corupted_log = "log.txt" # What files need to be replaced
repair_source = "./repair" # Path to folder with non corupt files
repair_dest = "./files" # Path to folder with corrupt files

output = open(log_path, "wr")

def log(text):
	print(text)
	output.write(text + "\n")


def main():
	# First, check to see if the replacemnt folders need renaming
	if not os.path.isdir(repair_source + "/1"):
		count = 1
		for root, dirs, files in os.walk(repair_source):
			try:
				for i in sorted(dirs, key=int):
					os.rename(os.path.join(root, i), os.path.join(root, str(count)))
					count += 1
			except OSError:
				log("Unable to rename repair folder/s")
		log("Renamed replacement folders")
	
	# Replace all files
	with open(corupted_log, "r") as f:
		for line in f:
			# Create path for the replacement file
			repair_path = line.split(repair_dest)
			repair_path = repair_path[1].strip("\n")
			repair_path = repair_source + repair_path
			# Strip trailing \n from file
			corupt_path = line.strip("\n")

			print("repairing: " + corupt_path)

			# Check we have the reqired files
			if not os.path.isfile(corupt_path):
				log("Failed to find corrupt file: " + corupt_path)
			elif not os.path.isfile(repair_path):
				log("Failed to find replacement file:" + repair_path)
			elif imghdr.what(repair_path) is None:
				log("Unable to determine type of replacement image!")
				log(repair_path)
			else:
				try:
					# Delete corupt file
					os.remove(corupt_path) 
					# Copy over file
					copyfile(repair_path, corupt_path)
					# Add the file extension to the moved file
					os.rename(corupt_path, corupt_path + "." + imghdr.what(corupt_path))
					log("Repair suceeded.")
				except OSError:
					log("OS Error: " + corupt_path + ", " + repair_path)

main()
output.close()
print("Done.")
