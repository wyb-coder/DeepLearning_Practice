from PIL import Image
import numpy as np
img = Image.open('./data/hymenoptera_data/train/ants/0013035.jpg')
img = np.array(img)
print(img)