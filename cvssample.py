import pandas as pd


cvsFile = pd.read_csv("C:\\Users\\tami\\Desktop\\kurt\\QuizScore.csv")
print(cvsFile)
X = cvsFile.drop(columns=["Sex"])
Y = cvsFile["Name"]







# cvsFile.fillna("reuben", inplace=True)
# from flask ---->> library
# import random ----->> packages
# random.randint ----->>> modules