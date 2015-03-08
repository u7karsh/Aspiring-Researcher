# Aspiring-Researcher
All source codes developed during Aspiring Researcher Challenge
======

##Details

###grab_cut.py

This tool finds all jpeg files in the folder and starts processing them one by one.
It first attempts to find the foreground by selecting a bounding box decided by
height and weight percentages hardcoded in the code. For our implementation, we have used
10% for both height and width.

Once the grabcut algo outputs the foreground, it is upto the user to select or
reject. To select the image, press 'y'. This will save the image to a folder (by default processed/)
and will move on to process another image.

If we click 'n' or reject, we will have to correct the image by either drawing boundary to a
background or foreground. To draw boundary to a background, click 'b' to start bg sampling tool.
Click 'f' to select foreground sampling tool. Once satisfied, click 'n' too reprocess the image.

details on grabcut algo can be found at http://docs.opencv.org/trunk/doc/py_tutorials/py_imgproc/py_grabcut/py_grabcut.html
