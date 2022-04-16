# Noise Label Dataset
## Installation
```bash=
pip install 'git+https://github.com/ericabd888/NoiseLabelDataset'
```
## Package Support
1. NoiseLabelDataset (Create Pytorch Dataset in Partial Noise Label)
2. train_test_split (Random split data in Train, Validation(if you need), Test)
3. Display_img (display your dataset picture)
4. MySubset (Support Data.targets to see all your label)
## Args
```python=
def __init__(self, MyData, xtype=None, ytype=None, ErrorRate=0.2, ShowErrorLabel=False, transform=None): 

MyData <-- Pytorch Dataset obj
xtype <-- Your X Data type
ytype <-- Your Y Data type
ErrorRate <-- NoiseLabel ErrorRate
ShowErrorLabel <-- (True/False) True can Mark your data is it is ErrorLabel
transform <-- pytorch transform trick
```
## Describe Support Pytorch Dataset, to convert to Noise Label Dataset, and easy to train
## Example
* MySubset
```python=
from NoiseLabelDataset import MySubset
import torchvision
Dataset = torchvision.datasets.CIFAR10(root='data', train=True, download=True)

TempSet = MySubset(Dataset, [i for i in range(15)])
print(TempSet.targets)
```
* train_test_split
```python=
TrainSet, ValidSet, TestSet = train_test_split(TempSet, TestRate=0.2, ValidRate=0.2)
```
* NoiseLabelDataset
```python=
from NoiseLabelDataset import NoiseLabelDataset
NoiseSet = NoiseLabelDataset(TrainSet, ErrorRate=0.5, ShowErrorLabel=True)
for i in NoiseSet:
  print(i)
```
* Display_img
```python=
# Use Display_img to show the different between Normal and Noise Dataset
from NoiseLabelDataset import Display_img
classes_name = classes_name = ['airplane', 'automobile', 'bird', 'cat', 'deer', 
'dog', 'frog', 'horse', 'ship', 'truck']

Display_img(TrainSet, ClassesName=classes_name, FileLoc="normal.png")
Display_img(NoiseSet, ClassesName=classes_name, FileLoc="noise.png", NeedSpecialize=True)
```
## Result
* Normal Dataset
![](https://i.imgur.com/Pjo5vTz.png)
* Noise Dataset
![](https://i.imgur.com/m9idgW4.png)
