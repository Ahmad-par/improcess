# improcess
Contains 4 apps to warp your images

/* In order to run the programs in this repository, you must have Python 2.7 installed.*/

/* After installing Python 2.7 open your Terminal (Command Prompt for Windows users)
   and go to the folder you have cloned the repository into and run "pip install -r requirements.txt"
   to install all the dependencies for the projects.*/
   
/* warp.py is a helper utility. Don't try to modify it unknowingly or else the apps will not work.*/


*************** randomWarp.py *****************

command: "python randomWarp.py <image_file_path> <nbr_of_ims>"

<image_file_path> : Absolute or relative path of the image you want to test

<nbr_of_ims>: Number of images you want to output

Description: Warps your image based on three random points the number of times you have specified in the second argument.

Note: This program does'nt create an image file on your disk but instead displays a window 
   containing the result so you can decide whether you want to save it or not.


*************** averageImage.py *****************

command: "python averageImage.py <dir_path> <nbr_of_ims>"

<dir_path>: Absolute or relative path of the folder containing image files

<nbr_of_ims>: Number of images you want to randomly select from the specified folder

Description: Computes an average image based on image files randomly selected from the folder.

Warning: The number of images in the specified folder must be at least equal to the second argument or else you will get an error.

Note: This program does'nt create an image file on your disk but instead displays a window 
   containing the result so you can decide whether you want to save it or not.


*************** pointWarp.py *****************

command: "python pointWarp.py <image_file_path> <n>"

<image_file_path> : Absolute or relative path of the image you want to test

<n>: Number of points in the grid. It should be 4, 6, 8 or 9.

Description: Warps an image based on user-defined points. This version includes just 4-, 6-, 8- and 9-point-warping. Specify the points from 
             left to right in a row near or far from the corresponding blue dots.  

Warning: The points you specify must be within the image domain or else the program would crash.

Note: This program does'nt create an image file on your disk but instead displays a window 
   containing the result so you can decide whether you want to save it or not.


*************** animatedGif.py *****************

command: "python animatedGif.py <image_file_path_in> <image_file_path_out> <n>"

<image_file_path_in>: Absolute or relative path of the image you want to make a gif animation from

<image_file_path_out>: Absolute path of the output image file(with .gif extension)

<n>: Number of frames making up our gif

Description: After running the command, first frame with a grid of 3x3 red dots in the middle is displayed. You should specify the corresponding 
             displacement of each point from left to right in a row. This process will repeat n times(3rd argument) so each frame of the gif
             animation is built. In the end gif image is saved to hard disk wherever you specified in the 2nd argument.

Warning: The points you specify must be within the image domain or else the program would crash.
