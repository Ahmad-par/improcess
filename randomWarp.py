""" Warp an image based on three random points."""

from numpy import *
from PIL import Image
from pylab import *
import warp, sys, random
from matplotlib.tri import Triangulation

pil_im = Image.open(sys.argv[1])

if pil_im.size[0] > pil_im.size[1]:
    ratio = pil_im.size[0]/pil_im.size[1]
    fromim = array(pil_im.resize((300,int(300/ratio))))
else:
    ratio = pil_im.size[1]/pil_im.size[0]
    fromim = array(pil_im.resize((int(300/ratio),300)))
                
nbr_ims = int(sys.argv[2])

if len(fromim.shape) == 3:
    toim = int64(ones((fromim.shape[0],fromim.shape[1],fromim.shape[2])) * 255)
else:
    toim = int64(ones((fromim.shape[0],fromim.shape[1])) * 255)

m,n = fromim.shape[:2]
y_range = range(int(0.3*m),int(m-0.3*m))
x_range = range(int(0.3*n),int(n-0.3*n))
y = [0,0,0,int(m/2),int(m/2),int(m/2),m,m,m] 
x = [0,int(n/2),n,0,int(n/2),n,0,int(n/2),n]
tri = Triangulation(x,y)
fp = int64(vstack((y,x,ones((1,len(x))))))

figure()
for i in range(minimum(9,nbr_ims)): 
    tpx =[0,int(n/2),n,0,random.sample(x_range,1)[0],n,0,int(n/2),n]
    tpy = [0,0,0,int(m/2),random.sample(y_range,1)[0],int(m/2),m,m,m]
    tp = int64(vstack((tpy,tpx,ones((1,len(tpx))))))
    try:
        im = warp.pw_affine(fromim,toim,fp,tp,tri)
        subplot(3,3,i+1)
        imshow(im)
        axis('off')
        axis('equal')
        if len(fromim.shape) == 2:
            gray()
    except Exception:
        err = 'Image #' + str(i+1) + ' had a problem.'
        print err
        
show()
