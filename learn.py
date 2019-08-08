import json
import matplotlib.pyplot as plt
import numpy
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

def read_json(path,data,target):
    with open(path) as f:
        content = json.load(f)
        for p in content:
            if p['MAL'] == True:
                target.append(1)
            else:
                target.append(0)
            arr = list()
            for item in p:
                if item != "MD5" and item != "MAL":
                    arr.append(p[item])
            data.append(arr)

def train(train_data,train_target,test_data,test_target,visualize=False):

	clf = tree.DecisionTreeClassifier()
	clf.fit(numpy.array(train_data),numpy.array(train_target))

	if visualize == True:
		plt.figure()
		tree.plot_tree(clf)
		plt.savefig("result.png")

	predicted = clf.predict(test_data)
	
	true_positive = 0
	true_negative = 0
	false_positive = 0
	false_negative = 0
	for i in range(len(test_data)):
		if predicted[i] == 1 and test_target[i] == 1:
			true_positive += 1
		elif predicted[i] == 0 and test_target[i] == 0:
			true_negative += 1
		elif predicted[i] == 1 and test_target[i] == 0:
			false_positive += 1
		else:
			false_negative += 1
	return true_positive,true_negative,false_positive,false_negative

def learn():
	train_target = list()
	test_target = list()
	train_data = list()
	test_data = list()

	read_json("train.json",train_data,train_target)
	read_json("test.json",test_data,test_target)

	result = train(train_data,train_target,test_data,test_target)
	print("Accuracy %f" % ((result[0] + result[1])/(result[0] + result[1] + result[2] + result[3])))



if __name__=='__main__':
	learn()
