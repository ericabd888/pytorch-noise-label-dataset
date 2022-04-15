import torch
import torch.nn as nn
import torchvision.transforms as transforms
import random
import torchvision
from torch.utils.data import DataLoader, Dataset
import numpy as np
import matplotlib.pyplot as plt
from .utils import MySubset, train_test_split, Display_img
classes_name = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
class NoiseLabelDataset(Dataset):
    def __init__(self, MyData, xtype=None, ytype=None, ErrorRate=0.2, ShowErrorLabel=False, transform=None):   
        self.xtype = xtype
        self.ytype = ytype
        self.ShowErrorL = ShowErrorLabel
        DataLen = len(MyData)
        DataIdx = [i for i in range(DataLen)]
        random.shuffle(DataIdx)
        self.LabelSet = set(MyData.targets)

        print(self.LabelSet)
        self.transform = transform
        ErrorNumber = int(DataLen * ErrorRate)
        self.ErrorIdx = set(DataIdx[:ErrorNumber])
        self.MyData = MyData
        
    def __getitem__(self, index):
        x, y = self.MyData[index]
        if self.ShowErrorL:
            ErrorLabel = False
        if index in self.ErrorIdx:
            CurrentNum = y
            self.LabelSet.remove(CurrentNum)
            DeleteNum = random.choice(list(self.LabelSet))
            y = DeleteNum
            ErrorLabel = True
            self.LabelSet.add(CurrentNum)
        if self.xtype:
            x = x.type(xtype)
        if self.ytype:
            y = y.type(ytype)
        if self.transform:
            x = self.transform(x)
        if self.ShowErrorL:
            return [x, y, ErrorLabel]
        else:
            return [x, y]
        
    def __len__(self, train=True):
        return len(self.MyData)