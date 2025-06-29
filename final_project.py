# Crete a GIF Project

import imageio.v3 as iio

filenames = ['team-pic1.png', 'team-pic2.png'] 
images = [] 

for filename in filenames: 
    images.append(iio.imread(filename)) 
iio.imwrite('teamgif', images, duration = 500, loop = 0) 
