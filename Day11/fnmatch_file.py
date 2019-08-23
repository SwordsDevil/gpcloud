#fnmatch modul
#2019/08/19

import fnmatch
import os

picture = ('*.png','*.jpeg','*.jpg','*.gif')
for files in os.listdir('files'):
    for image in picture:
        if fnmatch.fnmatch(files,image):
            print(files)

images = []
for image in picture:
    result = fnmatch.filter(os.listdir('files'),image)
    images.extend(result)
print(images)


result = fnmatch.translate('*.jpg')
print(result)