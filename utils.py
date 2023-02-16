import numpy as np

def arrayToImage(image):
    image = (image*255).astype(int)
    image = np.transpose(image[[2,1,0],:,:], (1,2,0))
    return image
    