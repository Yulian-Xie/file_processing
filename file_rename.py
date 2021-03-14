# -*- coding: utf-8 -*-
import os
import cv2
#file dir
path='F:\\image-processing\\image1'

file_name_num=1

for file in os.listdir(path):
    print('file_name before：', file)
    if os.path.isfile(os.path.join(path,file))==True:
#new_name
        new_name=file.replace(file,"%.6d.bmp"%file_name_num)
        print('file_name after：',new_name)
#rename
        os.rename(os.path.join(path,file),os.path.join(path, new_name))
        # cv2.imwrite(new_dir+new_name, image1_file)
        file_name_num+=1
#end

