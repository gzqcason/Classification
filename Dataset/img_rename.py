import os

import cv2
import matplotlib.pyplot as plt

class imgrename():
    def __init__(self,r,s):
        self.path = r + '/' + s
    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)

        n = 0
        for i in filelist:
            if i.endswith('.jpg'):
                old_name = os.path.join(os.path.abspath(self.path), i)
                new_name = os.path.join(os.path.abspath(self.path), s+ str('{:0>3d}'.format(n)) + '.jpg')
                os.rename(old_name, new_name)
                n += 1
        print('total %d to rename & converted %d jpgs' % (total_num, n))

PHASE=['train','val']
SPECIES = ['rabbits', 'rats', 'chickens']

for i in PHASE:
    for s in SPECIES:
        new_name = imgrename(i,s)
        new_name.rename()
