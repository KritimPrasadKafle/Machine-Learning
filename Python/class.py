class Human:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots a flim")

    def speaks(self):
        print(self.name,"says how are you?")

tom = Human("tom cruise",19,"actor")
tom.do_work()
tom.speaks()

maria = Human("Maria Sharapova",14, "tennis Player")
maria.do_work()
maria.speaks()

