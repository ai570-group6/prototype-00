import os
import glob
import sys
import numpy as np
from PIL import Image

def save_image(img_array, path):
    img = Image.fromarray(img_array)
    img.save(path)

def preprocess_image(img_array):

    # threshold 
    img_array[img_array < 20] = 0
    img_array[img_array > 120] = 255
    
    return img_array

def preprocess_files(root, target_path):
    for path in glob.glob(root + '/*'):
        print(path)
        img = Image.open(path)
        img_array = np.array(img)
        img_array = preprocess_image(img_array)
        file_name = os.path.basename(path)
        save_image(img_array, os.path.join(target_path, file_name))

preprocess_files(sys.argv[1], sys.argv[2])

