#  DEMO script (python version) for 2D diffraction separation via the localized damped rank-reduction method (LDRR)
#  
#  Copyright (C) 2022 Yangkang Chen
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details: http://www.gnu.org/licenses/
#  

import numpy as np
import matplotlib.pyplot as plt
import pydrr as pd #pd: DRR


## Please download data from https://github.com/aaspip/data/blob/main/diffr_syn_2d.mat
# data is observed data
# diffr is the ground-truth diffraction data

#load data
import scipy
from scipy import io
datas=scipy.io.loadmat("diffr_syn_2d.mat")
data=datas['data'];
diffr=datas['diffr']; #ground-truth
[n1,n2]=data.shape;
data=data/data.max();


## perform diffraction separation
#This example is introduced in Wang et al., 2020.
lf=0;hf=120;dt=0.004;verb=0;N=5;K=4; # N is a scalar (Nmax) or a vector (Nmin,Nmax);
n1win=200;n2win=100;n3win=1;r1=0.5;r2=0.5;r3=0.5;mode=2;#mode=2 means using the singular value ratio criterion
d1=pd.drr3d_win_auto(data,lf,hf,dt,N,K,verb,mode,n1win,n2win,n3win,r1,r2,r3);#reflection from LDRR 
diffr1=data-d1; #diffraction from LDRR 

# Quick visualization
# figure;drr_imagesc([data,diffr,diffr1,data-diffr,d1]);

## SNR of the separated diffraction
# drr_snr(diffr,diffr1)

print('SNR is %g'%pd.snr(diffr,diffr1));

## plot results
fig = plt.figure(figsize=(14, 6))
ax = fig.add_subplot(1,5,1)
plt.imshow(data,cmap='jet',clim=(-0.1, 0.1),aspect=0.8);ax.set_xticks([]);ax.set_yticks([]);
plt.title('Data');
ax = fig.add_subplot(1,5,2)
plt.imshow(diffr,cmap='jet',clim=(-0.1, 0.1),aspect=0.8);ax.set_xticks([]);ax.set_yticks([]);
plt.title('Ground-truth diffraction');
ax = fig.add_subplot(1,5,3)
plt.imshow(data-diffr,cmap='jet',clim=(-0.1, 0.1),aspect=0.8);ax.set_xticks([]);ax.set_yticks([]);
plt.title('Ground-truth reflection');
ax = fig.add_subplot(1,5,4)
plt.imshow(diffr1,cmap='jet',clim=(-0.1, 0.1),aspect=0.8);ax.set_xticks([]);ax.set_yticks([]);
plt.title('LDRR diffraction');
ax = fig.add_subplot(1,5,5)
plt.imshow(data-diffr1,cmap='jet',clim=(-0.1, 0.1),aspect=0.8);ax.set_xticks([]);ax.set_yticks([]);
plt.title('LDRR reflection');
plt.savefig('test_pydrr_drr2d_diffraction.png',format='png',dpi=300);
plt.show()




