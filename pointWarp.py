""" Warp an image based on user-defined points.
   This version includes just 4-, 6- and 8-point-warping."""

from numpy import *
from PIL import Image
from pylab import *
import warp, sys
from matplotlib.tri import Triangulation

fromim = array(Image.open(sys.argv[1]))
points = int(sys.argv[2])

if len(fromim.shape) == 3:
    toim = int64(ones((fromim.shape[0],fromim.shape[1],fromim.shape[2])) * 255)
else:
    toim = int64(ones((fromim.shape[0],fromim.shape[1])) * 255)

if points == 4:
    m,n = fromim.shape[:2]
    y = [0,0,m,m]
    x = [0,n,0,n]
    tri = Triangulation(x,y)
    fp = vstack((y,x,ones((1,len(x)))))
    print 'Specify 4 destination points to warp...'
    print 'Select them from left to right in a row'
    figure()
    imshow(fromim)
    axis('off')
    axis('equal')
    plot(x,y,'o')
    x = ginput(4)
    tpx = []
    tpy = []
    for i in x:
        tpx.append(i[0])
        tpy.append(i[1])

    tp = int64(vstack((tpy,tpx,ones((1,len(tpx))))))
    im = warp.pw_affine(fromim,toim,fp,tp,tri)
    figure()
    imshow(im)
    axis('off')
    axis('equal')
    show()
        
elif points == 6:
    m,n = fromim.shape[:2]
    y = [0,0,0,m,m,m]
    x = [0,int(n/2),n,0,int(n/2),n]
    tri = Triangulation(x,y)
    fp = vstack((y,x,ones((1,len(x)))))
    print 'Specify 6 destination points to warp...'
    print 'Select them from left to right in a row'
    figure()
    imshow(fromim)
    axis('off')
    axis('equal')
    plot(x,y,'o')
    x = ginput(6)
    tpx = []
    tpy = []
    for i in x:
        tpx.append(i[0])
        tpy.append(i[1])

    tp = int64(vstack((tpy,tpx,ones((1,len(tpx))))))
    im = warp.pw_affine(fromim,toim,fp,tp,tri)
    figure()
    imshow(im)
    axis('off')
    axis('equal')
    show()

elif points == 8:
    m,n = fromim.shape[:2]
    y = [0,0,0,0,m,m,m,m]
    x = [0,int(n/4),int(0.75*n),n,0,int(n/4),int(0.75*n),n]
    tri = Triangulation(x,y)
    fp = vstack((y,x,ones((1,len(x)))))
    print 'Specify 8 destination points to warp...'
    print 'Select them from left to right in a row'
    figure()
    imshow(fromim)
    axis('off')
    axis('equal')
    plot(x,y,'o')
    x = ginput(8)
    tpx = []
    tpy = []
    for i in x:
        tpx.append(i[0])
        tpy.append(i[1])

    tp = int64(vstack((tpy,tpx,ones((1,len(tpx))))))
    im = warp.pw_affine(fromim,toim,fp,tp,tri)
    figure()
    imshow(im)
    axis('off')
    axis('equal')
    show()

elif points == 9:
    m,n = fromim.shape[:2]
    y = [0,0,0,int(m/2),int(m/2),int(m/2),m,m,m]
    x = [0,int(n/2),n,0,int(n/2),n,0,int(n/2),n]
    tri = Triangulation(x,y)
    fp = vstack((y,x,ones((1,len(x)))))
    print 'Specify 9 destination points to warp...'
    print 'Select them from left to right in a row'
    figure()
    imshow(fromim)
    axis('off')
    axis('equal')
    plot(x,y,'o')
    x = ginput(9)
    tpx = []
    tpy = []
    for i in x:
        tpx.append(i[0])
        tpy.append(i[1])

    tp = int64(vstack((tpy,tpx,ones((1,len(tpx))))))
    im = warp.pw_affine(fromim,toim,fp,tp,tri)
    figure()
    imshow(im)
    axis('off')
    axis('equal')
    show()
