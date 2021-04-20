""" Animate an image based on warping that image with a grid of 3x3 points."""

from numpy import *
from PIL import Image
from pylab import *
import warp, sys
from matplotlib.tri import Triangulation

pil_im = Image.open(sys.argv[1])
nbr_frames = int(sys.argv[3])

if pil_im.size[0] > pil_im.size[1]:
    ratio = pil_im.size[0]/pil_im.size[1]
    w = minimum(pil_im.size[0], 400)
    fromim = array(pil_im.resize((w,int(w/ratio))))
else:
    ratio = pil_im.size[1]/pil_im.size[0]
    h = minimum(pil_im.size[1],400)
    fromim = array(pil_im.resize((int(h/ratio),h)))

if len(fromim.shape) == 3:
    toim = int64(ones((fromim.shape[0],fromim.shape[1],fromim.shape[2])) * 255)
else:
    toim = int64(ones((fromim.shape[0],fromim.shape[1])) * 255)

x,y = meshgrid(range(5),range(5))
x = int(fromim.shape[1]/4) * x.flatten()
y = int(fromim.shape[0]/4) * y.flatten()
tri = Triangulation(x,y)
fp = int64(vstack((y,x,ones((1,len(x))))))
im_list = []
xp = x[[6,7,8,11,12,13,16,17,18]]
yp = y[[6,7,8,11,12,13,16,17,18]]

for i in range(nbr_frames):
    tpx = x
    tpy = y
    figure()
    axis('off')
    imshow(fromim)
    plot(xp,yp,'ro')
    if len(fromim.shape) == 3:
        gray()
    X = ginput(9)
    tpx[[6,7,8,11,12,13,16,17,18]] = [c[0] for c in X]
    tpy[[6,7,8,11,12,13,16,17,18]] = [c[1] for c in X]
    tp = int64(vstack((tpy,tpx,ones((1,len(tpx))))))   
    im = warp.pw_affine(fromim,toim,fp,tp,tri)
    im_list.append(Image.fromarray(uint8(im)))
    close()

im_list[0].save(sys.argv[2], append_images=im_list[1:], save_all=True, duration=100, loop=0)
  
