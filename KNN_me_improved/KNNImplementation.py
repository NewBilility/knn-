import csv
import random
import math
import operator

def loadDataset(filename,split,trainingSet=[],testSet=[]):
   # with open(filename,"rb") as csvfile:
    with open(filename,"rt") as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        print("hahahaha  len is "+str(len(dataset)))
        for x in range(len(dataset)-1):
       # for x in range(len(dataset)):
            for y in range(4):
                print("hahahahahahahah "+str(dataset[x][y]))
                dataset[x][y] = float(dataset[x][y])
            if random.random()<split:#将文件中的数据进行区分  一部分为训练集  一部分为测试集
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

          
def euclideanDistance(instance1,instance2,length):#这个函数用来计算距离
    distance = 0
    for x in range(length):
        distance += pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)

def getNeighbors(trainingSet,testInstance,k):
    distances = []
    length = len(testInstance)-1#测试集的维度减1 因为测试集还没有结果
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance,trainingSet[x],length)
        distances.append((trainingSet[x],dist))#计算所有点到测试数据的距离 保存到列表中
    distances.sort(key = operator.itemgetter(1)) #对列表进行排序  以距离作为排序的依据
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])#将列表中的元素元组放入neighbors列表中
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]#将neighbors中的元组元素赋值给response
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet,predictions):#将得到的正确数据计数 并与测试集的长度求差 得到一个正确率
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:#-1表示对应最后一个值
            correct += 1
    return (correct/float(len(testSet)))*100.0
        
def main():
     trainingSet=[]
     testSet=[]
     split = 0.5
     loadDataset(r"G:\irisdata.txt",split,trainingSet,testSet)#字符串前面的r表示原始字符串
     print("Train set: "+repr(len(trainingSet)))
     print("Test set: "+repr(len(testSet)))

     predictions=[]
     k=13
     for x in range(len(testSet)):
         neighbors = getNeighbors(trainingSet,testSet[x],k)
         result = getResponse(neighbors)
         predictions.append(result)
         print("> predicted= "+repr(result)+", actual= "+repr(testSet[x][-1]))
     accuracy = getAccuracy(testSet, predictions)
     print("Accuracy: "+repr(accuracy)+"%")
     
main()   
    
