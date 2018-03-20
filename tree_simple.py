from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO

allElectronicsData = open(r"G:\AllElectronics.csv",'rt')#读取表格数据集，rt作为读取方式
reader = csv.reader(allElectronicsData)
headers = next(reader)#Python3.x特殊用法

# print(headers)

featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1,len(row)-1):
        rowDict[headers[i]]=row[i]
    featureList.append(rowDict)

print(featureList)
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()

print("dummyX: "+str(dummyX))
# print(vec.get_feature_names())
# 
# print("labelList: "+str(labelList))
lb = preprocessing.LabelBinarizer()

dummyY = lb.fit_transform(labelList)

#print("dummyY: "+str(dummyY))
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)

print("clf: "+str(clf))
#生成一个.dot文件可以看到生成的决策树
with open("allElectronicInformationGainOri.dot",'w') as f:
    f = tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file = f)
#将列表由一维转化为二维
oneRowX = dummyX[0, :].reshape(1,-1)
newRowX = oneRowX
print("oneRowX: "+str(oneRowX))
#相应的二维 数据集中 将年龄改为中年
newRowX[0][0] = 1
newRowX[0][2] = 0

print("newRowX: " + str(newRowX))
#预测数据集的结果
predictedY = clf.predict(newRowX)
print("predictedY : "+ str(predictedY))

