import os
import numpy as np
from sklearn.cluster import KMeans
from mahotas.features import surf
from PIL import Image
from sklearn.externals import joblib
from pylab import *
import csv
import pandas


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
	pathDir = os.listdir(filepath)
	pathDir.sort(key=lambda x: int(x[:-4]))
	# for allDir in pathDir:
	# 	child = os.path.join('%s%s' % (filepath, allDir))
	# 	print(child)
	ar = list()
	temp1 = 0
	temp2 = 0
	i = 0
	for i in range(1, len(pathDir) - 1):
		# print(filepath + pathDir[i])
		# chdir(os.path.dirname(filepath + pathDir[i]))
		# print(os.path.getsize(filepath + "\\"+pathDir[i]))
		if i < 3:
			# print(filepath + "\\" + pathDir[i - 1])
			before = getGreyPicsFeatures(filepath + "\\" + pathDir[i - 1])
			before = np.array(before)
			# print(filepath + "\\" + pathDir[i + 1])
			next = getGreyPicsFeatures(filepath + "\\" + pathDir[i + 1])
			next = np.array(next)
			if i % 2 == 1:
				temp1 = next
			else:
				temp2 = next
		else:
			if i % 2 == 1:
				before = temp1
				next = getGreyPicsFeatures(filepath + "\\" + pathDir[i + 1])
				next = np.array(next)
				temp1 = next
			else:
				before = temp2
				next = getGreyPicsFeatures(filepath + "\\" + pathDir[i + 1])
				next = np.array(next)
				temp2 = next
			# print(filepath + "\\" + pathDir[i - 1])
			# print(filepath + "\\" + pathDir[i + 1])
		mins = linalg.norm(before - next)
		# print(mins)
		# mins = abs(os.path.getsize(filepath + "\\" + pathDir[i]) - os.path.getsize(filepath + "\\" + pathDir[i + 1]))
		# print(mins)
		ar.append(mins)
	# ar.append((mins, mins))
	return ar


def getGreyPicsFeatures(path):
	image = array(Image.open(path).convert('L'), 'f')
	return surf.surf(image)[0]


if __name__ == '__main__':
	# Change to your captures storeage dictory
	filePath2 = "C:\\Users\\Ting\\AppData\\Roaming\\PotPlayerMini64\\Captwo\\FF"

	data = eachFile(filePath2)
	df2 = pandas.DataFrame({'A': data}, )
	# print(df2)
	df2.to_csv('moneyTest.csv', index=False)
# csvfile = open('C:\\FFOutput\\money.csv', 'wb')  # 打开方式还可以使用file对象
# writer = csv.writer(csvfile)
# writer.writerow(['cap', 'terburse'])
# writer.writerows(data)
# csvfile.close()
# for i in range(len(data)):
# 	print(data[i])


# feature = [[float(x) for x in row[:]] for row in data]
# # 调用kmeans类
# clf = KMeans(n_clusters=3)
# s = clf.fit(feature)
#
# result = clf.labels_.tolist()
# for i in range(len(result)):
# 	print(str(i + 2) + " : " + str(result[i]))

# 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
# print(clf.inertia_)
