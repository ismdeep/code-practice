# coding: utf-8
# author: ismdeep
# dateime: 2019-05-16 15:31:19
# filename: app.py
# blog: https://ismdeep.com
import trees
import treePlotter

data_set, labels = trees.createDataSet2('lenses.txt')
myTree = trees.createTree(data_set, labels)
print(myTree)
treePlotter.createPlot(myTree)
print(trees.classify(myTree, labels, ['young', 'myope', 'no', 'reduced']))

# treePlotter.createPlot(myTree)
# myTree = treePlotter.retrieveTree(0)
# print(myTree)
# print(treePlotter.getNumLeafs(myTree))
# print(treePlotter.getTreeDepth(myTree))
# print(treePlotter.createPlot(myTree))
