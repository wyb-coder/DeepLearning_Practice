import torch.optim
import torchvision.datasets
from torch import nn
from torch.nn import Conv2d, Sequential, MaxPool2d, Flatten, Linear
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10("./data", train=False,
                                       transform=torchvision.transforms.ToTensor(),
                                       download=True)
dataloader = DataLoader(dataset, batch_size=32)

class CnnTest(nn.Module):
    def __init__(self):
        super(CnnTest, self).__init__()
        self.test_model = Sequential(
            Conv2d(3, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 64, 5, padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(1024, 64),
            Linear(64, 10)
        )

    def forward(self, x):
        x = self.test_model(x)
        return x

loss = nn.CrossEntropyLoss()
model = CnnTest()
optim = torch.optim.SGD(model.parameters(), lr=0.01)        # 优化器
for epoch in range(20):
    total_loss = 0
    for data in dataloader:
        imgs, target = data
        outputs = model(imgs)
        one_loss = loss(outputs, target)
        optim.zero_grad()
        one_loss.backward()
        optim.step()
        total_loss += one_loss
    print(total_loss)



