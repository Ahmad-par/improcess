from PIL import Image
from numpy import *
from pylab import *
import os, sys, random

def get_imlist(path):
    """Returns a list of filenames for all jpg images in a directory."""

    imlist = []
    for filename in os.listdir(path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            f = os.path.join(path,filename)
            imlist.append(f)
    return imlist
    
def compute_average(imlist, n):
    """compute the average of a list of images"""
    # open first image and make into array of type float
    try:
        imlist = random.sample(imlist, n)
    except ValueError:
        print 'ERROR: The number of images in the specified folder must be \
greater or equal to the second argument'
        sys.exit(1)

    averageim = array(Image.open(imlist[0]), 'f')

    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print imname + '...skipped'
    averageim /= len(imlist)

    return array(averageim, 'uint8')

for imfile in os.listdir(sys.argv[1]):
    if imfile.endswith('.jpg') or imfile.endswith('.png'):
        pil_im = Image.open(os.path.join(sys.argv[1],imfile))
        if pil_im.size != (800, 800):
            pil_im = pil_im.resize((800,800))
            pil_im.save(os.path.join(sys.argv[1],imfile))

imlist = get_imlist(sys.argv[1])
im = compute_average(imlist,int(sys.argv[2]))
imshow(im)
axis('off')
axis('equal')
show()
