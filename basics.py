class k :


    def __init__(self, a,b,c ):
        self.name = a
        self.age = b
        self.gender = c

    def details(self):
        print("name:", self.name,"\nage:",self.age,"\ngender:",self.gender )

    def ask(self):
        print( "who are you")

    def waayLang(self):
        print(self.name , "mango")


reuben = k("reuben", 12, "Male")
reuben.details()
reuben.ask()
reuben.waayLang()

tami = k("tami", 21, "Male")
tami.details()
tami.ask()
tami.waayLang()

while True:


    if input("Enter X to start any key to stop").lower() == "x"  :
        name = input("name:")
        age = input("age:")
        gender = input("gender:")

        sample = k(name, age, gender)
        sample.details()
        sample.ask()
    else:
        break

