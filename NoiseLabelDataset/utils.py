import torch
import torch.nn as nn
import torchvision.transforms as transforms
import random
import torchvision
from torch.utils.data import DataLoader, Dataset
import numpy as np
import matplotlib.pyplot as plt

class MySubset(Dataset):
    r"""
    Subset of a dataset at specified indices.

    Arguments:
        dataset (Dataset): The whole Dataset
        indices (sequence): Indices in the whole set selected for subset
        labels(sequence) : targets as required for the indices. will be the same length as indices
    """
    def __init__(self, dataset, indices):
        self.dataset = dataset
        self.indices = indices
        self.targets = []
    def __getitem__(self, idx):
        image = self.dataset[self.indices[idx]][0]
        label = self.dataset[self.indices[idx]][1]
        self.targets.append(label)
        return [image, label]
    def __len__(self):
        return len(self.indices)
    
def train_test_split(WholeData, TestRate=0.2, ValidRate=None):
    DataLen = len(WholeData)
    WholeIdx = [idx for idx in range(DataLen)]
    random.shuffle(WholeIdx)
    TestNumber = int(DataLen*(TestRate))
    TestIdx = WholeIdx[:TestNumber]
    TrainIdx = WholeIdx[TestNumber:]
    if ValidRate is not None:
        ValidNumber = int(len(TrainIdx)*ValidRate)
        ValidIdx = TrainIdx[:ValidNumber]
        TrainIdx = TrainIdx[ValidNumber:]
        
        TrainSet = MySubset(WholeData, TrainIdx)
        ValidSet = MySubset(WholeData, ValidIdx)
        TestSet = MySubset(WholeData, TestIdx)
        return TrainSet, ValidSet, TestSet
    else:
        TrainSet = MySubset(WholeData, TrainIdx)
        TestSet = MySubset(WholeData, TestIdx)
        return TrainSet, TestSet
classes_name = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
def Display_img(DataSet, ClassesName=classes_name, ImgSize=(2.5, 2.5), TitleSize=14, 
                SubTitleSize=10, FileLoc="MyPic.png", NeedSpecialize=False):
    LEN = len(DataSet)
    assert(not(len(DataSet[0]) != 3 and NeedSpecialize )), 'Please Make Sure Your DataSet have ShowErrorLabel, because NeedSpecial is True'
    col, row = 5, LEN//5 + 1 if LEN % 5 != 0 else LEN // 5
    fig, axs = plt.subplots(row, col, figsize=(col*ImgSize[0], row*ImgSize[1]))
    fig.suptitle('Show Data', fontsize=TitleSize)
    axs = axs.ravel()
    for i in range(LEN):
        axs[i].imshow(DataSet[i][0])
        color = "red" if NeedSpecialize and DataSet[i][2] else "black"
        axs[i].set_title(ClassesName[DataSet[i][1]], fontsize=SubTitleSize, color=color)
        axs[i].axis('off')
    fig.savefig(FileLoc)
    plt.show()