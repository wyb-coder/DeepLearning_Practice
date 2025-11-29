import torch
import os
from PIL import Image
from torch.utils.data import Dataset


class MyData(Dataset):
    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.file_path = os.path.join(self.root_dir, self.label_dir)
        self.image_list = os.listdir(self.file_path)

    def __getitem__(self, item_index):
        image_name = self.image_list[item_index]
        image_path = os.path.join(self.root_dir, self.label_dir, image_name)
        image = Image.open(image_path)
        label = self.label_dir
        return image, label

    def __len__(self):
        return len(self.image_list)

train_root_dir = './data/hymenoptera_data/train'
ants_label_dir = 'ants'
ants_dataset = MyData(train_root_dir, ants_label_dir)
image, label = ants_dataset[0]
image.show()










