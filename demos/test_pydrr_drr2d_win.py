#  DEMO script (python version) for DRR
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
## generate synthetic data
#This synthetic data was used in Huang et al., 2016, Damped multichannel singular spectrum analysis for 3D random noise attenuation, Geophysics, 81, V261-V270.
import numpy as np
import matplotlib.pyplot as plt
import pydrr as pd #lo: local orthogonalization

## please first download the data from https://github.com/aaspip/data/blob/main/hevents.mat

#load data
import scipy
from scipy import io
datas=scipy.io.loadmat("hevents.mat")
d=datas['d'];
d=d/d.max();
d0=d;

[n1,n2]=d.shape;
np.random.seed(201415)
n=0.1*np.random.randn(n1,n2);
dn=d0+n;

## Comparison between RR and DRR
d1=pd.drr3d(dn,0,120,0.004,6,4,1);	#RR 
noi1=dn-d1;

n1win=50;n2win=20;n3win=1;r1=0.5;r2=0.5;r3=0.5;
d2=pd.drr3d_win(dn,0,120,0.004,2,4,1,n1win,n2win,n3win,r1,r2,r3); #Windowed DRR or LDRR
noi2=dn-d2;

print('SNR of DRR is %g'%pd.snr(d0,d1));
print('SNR of LDRR is %g'%pd.snr(d0,d2));

## plot results
fig = plt.figure(figsize=(10, 4))
ax = fig.add_subplot(1,6,1)
plt.imshow(d0,cmap='jet',clim=(-0.1, 0.1),aspect=0.2);ax.set_xticks([]);ax.set_yticks([]);
plt.title('Clean data');
ax = fig.add_subplot(1,6,2)
plt.imshow(dn,cmap='jet',clim=(-0.1, 0.1),aspect=0.2);ax.set_xticks([]);ax.set_yticks([]);
plt.title('Noisy data');
ax = fig.add_subplot(1,6,3)
plt.imshow(d1,cmap='jet',clim=(-0.1, 0.1),aspect=0.2);ax.set_xticks([]);ax.set_yticks([]);
plt.title('Denoised (DRR)');
ax = fig.add_subplot(1,6,4)
plt.imshow(noi1,cmap='jet',clim=(-0.1, 0.1),aspect=0.2);ax.set_xticks([]);ax.set_yticks([]);
plt.title('Noise (DRR)');
ax = fig.add_subplot(1,6,5)
plt.imshow(d2,cmap='jet',clim=(-0.1, 0.1),aspect=0.2);ax.set_xticks([]);ax.set_yticks([]);
plt.title('Denoised (LDRR)');
ax = fig.add_subplot(1,6,6)
plt.imshow(noi2,cmap='jet',clim=(-0.1, 0.1),aspect=0.2);ax.set_xticks([]);ax.set_yticks([]);
plt.title('Noise (LDRR)');
plt.savefig('test_pydrr_drr2d_win.png',format='png',dpi=300);
plt.show()












