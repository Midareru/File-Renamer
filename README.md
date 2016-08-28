MangaRock app allows users to download chapers.

However they name their chaper folders with cryptic URL numbers, and don't add file extions to the images.
This program looks at the file type of each image, and adds their file extension (png, jpeg, gif, ect).
It also names the folders from 1, making it more readable.

Also included is a repair tool for replacing images that failed to correcty download.

Should work fine on Linux or Windows, using python 2.7 or 3.

Usage:

1)  Move your downloaded folders into the folder "files"
2)  in the console enter "sh run.sh" or "python run.py"
3)	If you get corruption warnings, redownload the effected files/chapters
3)	Place the redownloaded files into the "repair" folder AS THEY ARE. 
	(Don't rename files/folders, the script handles this itself)
4)	Run "sh repair.sh" or "python repair.py"

If you still have corrupted files, run main.py again to update the corupted file list
then repeat from step #3.

Files:

main.py - renames the files
repair.py - replaces corupted images

clear.sh - deletes the contents of "files"
run.sh - runs main.py

log.txt - paths to corupt images within "files"
repair_log.txt - log of renamer.py, you can read this if you're having issues with it.
