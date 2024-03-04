import pandas as pd


datasFromCSV = pd.read_csv("C:\\Users\\tami\\Desktop\\kurt\\QuizScore.csv")
toStr = str(datasFromCSV)

toList = toStr.split("\n")

n0 =toList[1].split("  ")
n1 =toList[2].split("  ")
n2 =toList[3].split("  ")
n3 =toList[4].split("  ")
n4 =toList[5].split("  ")
n5 =toList[6].split("  ")
n6 =toList[7].split("  ")
n7 =toList[8].split("  ")
n8 =toList[9].split("  ")
n9 =toList[10].split("  ")




darray =[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9]
copyOflist =[]
for k in range(len(darray)):
    newVal = darray[k]



    for j in range(len(newVal)):
        print(newVal[j])
        if newVal[j]=="NaN":
            copyOflist.append("Karen may Gaytano")
        else:
            copyOflist.append(newVal[j])



print("copy")

for k in copyOflist:

    print(k)













