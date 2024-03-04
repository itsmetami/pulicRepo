# import random
# ran = random.randint(0,1)
#
# class proposal:
#     def __init__(self,content,dateOFmerage,numOfChildren,typeHOUSE):
#         self.contentOfProp = content
#         self.date = dateOFmerage
#         self.numC = numOfChildren
#         self.balay = typeHOUSE
#
#     def yes(self):
#         print("YES!!")
#         print("number of children", self.numC)
#         print("type of house", self.balay)
#         print("date of merage", self.date)
#
#     def no(self):
#         print("NO")
#         print("thank you for your love")
#
#
# proposalllcontent = input("enter your mesage to the girl you love")
# numC = input("enter number of kids you want")
# Balay = input("enter type of hous you like")
# dateKakasal = input("enter when ang kasal")
#
#
#
# if ran == 1:
#    f = proposal(proposalllcontent, dateKakasal, numC, Balay).yes()
# else:
#    f = proposal(proposalllcontent, dateKakasal, numC, Balay).no()
#
# listahan = []
#
#
#
#
#





class student:
    def __init__(self, name, yearlvl, age, gender):
        self.name=name
        self.yearlvl = yearlvl
        self.age=age
        self.gender = gender

    def erticalNmae(self):

        for k in self.name:
            print(k)


karenMay = student("karen May", "2nd year", 21, "lalaki").erticalNmae()
Reuben = student("Reuben","3rd year", 21, "babae").erticalNmae()

listahn = [Reuben]

