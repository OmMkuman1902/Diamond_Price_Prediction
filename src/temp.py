from sklearn.tree import DecisionTreeRegressor,DecisionTreeClassifier
dic={"decisiontreereg":DecisionTreeRegressor(),"decisiontreeclassi":DecisionTreeClassifier()}
lis=['decisiontreereg','decisiontreeclassi']


for i in range(len(dic)):
    print(dic[lis[i]])