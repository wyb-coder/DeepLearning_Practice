from torchvision import transforms
from PIL import Image
img = Image.open('./data/hymenoptera_data/train/ants/0013035.jpg')

t1 = transforms.ToTensor()(img)
print(t1)