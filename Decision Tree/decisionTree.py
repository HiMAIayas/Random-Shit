import numpy as np
from collections import Counter 

def entropy(label):
    uniqueLabel, uniqueCount = np.unique(label,return_counts=True)
    uniqueProb = uniqueCount/len(label)
    return -np.sum(uniqueProb*np.log(uniqueProb)/np.log(2))


def information_gain(data,label,feature):
    unique_values = np.unique(data[:,feature])
    total_H = entropy(label)
    
    weight_entropy = 0
    for value in unique_values:
        sub_target = label[np.where(data[:,feature]==value)]
        weight_entropy+= len(sub_target)/len(label)*entropy(sub_target)
    
    return total_H - weight_entropy


def id3(data,label,features):
    if len(np.unique(label))==1:
        return Node(None,label[0])
    if len(features)==0:
        most_common_label = Counter(label).most_common(1)[0][0] #[(value, count)]
        return Node(None,most_common_label)

    best_feature = max(features,key= lambda x:information_gain(data,label,x)) #find feature with best IG
    unique_values = np.unique(data[:,best_feature])
    rootNode = Node(data,label)
    rootNode.split_feature = best_feature
    
    for value in unique_values:
        
        sub_index = np.where(data[:,best_feature]==value)
        sub_data = data[sub_index]
        sub_label = label[sub_index]
        
        if len(sub_data)==0:
            most_common_label = Counter(label).most_common(1)[0][0]
            childNode = Node(None,most_common_label)
        else:
            remain_feature = [i for i in features if i!= best_feature]
            childNode = id3(sub_data,sub_label,remain_feature)
        
        rootNode.children[value]=childNode
    return rootNode
            

class Node:
    def __init__(self,data,label):
        self.data = data
        self.label = label
        self.children = {}
        self.split_feature = None
        
    def printNode(self,curSpace=0):
        if self.data is None:
            print(" ==>",self.label)
        else:
            print()
            for value in self.children.keys():
                print(curSpace*"  "+"|-",end="")
                print(self.split_feature,":",value,end="")
                self.children[value].printNode(curSpace=curSpace+1)
   
    def target(self,valueList):
        cur = self
        while not (cur.data is None):
            cur = cur.children[valueList[cur.split_feature]]
        return cur.label

data = np.array([
    ['sunny', 'hot', 'high', 'false'],
    ['sunny', 'hot', 'high', 'true'],
    ['rainy', 'cool', 'normal', 'true'],
    ['sunny', 'mild', 'high', 'false'],
    ['rainy', 'mild', 'high', 'true'],
    ['overcast', 'hot', 'high', 'false'],
    ['rainy', 'mild', 'high', 'false'],
    ['rainy', 'cool', 'normal', 'false'],
    ['overcast', 'cool', 'normal', 'true'],
    ['sunny', 'cool', 'normal', 'false'],
    ['rainy', 'mild', 'normal', 'false'],
    ['sunny', 'mild', 'normal', 'true'],
    ['overcast', 'mild', 'high', 'true'],
    ['overcast', 'hot', 'normal', 'false']
])
label1 = np.array(['no','no','no','no','no','yes','yes','yes','yes','yes','yes','yes','yes','yes'])

#feature 0: Outlook
#feature 1: Temp
#feature 2: Humidity
#feature 3: Windy

node = id3(data,label1,[0,1,2,3])
print(node.printNode())