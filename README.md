<h2>About:</h2>
MangaRock app allows users to download chapers. However they name their chaper folders with cryptic URL numbers, and don't add file extions to the images. With new versions of the app, they now include an ad image at the start of every chapter.

This program looks at the file type of each image, and adds their file extension (png, jpeg, gif, ect), renames the folders from 1, and deletes the ad imgage.

<b>Included is a repair tool for replacing images that failed to correcty download.</b>

<h2>Usage:</h2>
<ol>
<li>Move your downloaded folders into the folder "files"</li>
<li>in the console enter "sh run.sh" or "python run.py"</li>
<li>If you get corruption warnings, redownload the effected files/chapters</li>
<li>Place the redownloaded files into the "repair" folder AS THEY ARE (Don't rename files/folders, the script handles this itself)</li>
<li>Run "sh repair.sh" or "python repair.py"</li>
</ol>
<i>If you still have corrupted files, run main.py again to update the corupted file list
then repeat from step #3.</i>

Should work fine on Linux or Windows, using <b>Python</b> 2.7 or 3.

<h2>Files:</h2>
<ul>
<li>main.py - renames the files</li>
<li>repair.py - replaces corupted images</li>
<li>clear.sh - deletes the contents of "files"</li>
<li>run.sh - runs main.py</li>
<li>log.txt - paths to corupt images within "files"</li>
<li>repair_log.txt - log of renamer.py, you can read this if you're having issues with it.</li>
</ul>
