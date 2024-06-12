class MyBook:
    def __init__(self, title):
        self.title = title

    def myfunc(self):
        print("I've been reading " + self.title + " recently. The books are incredible!")


p1 = MyBook("The Witcher")
p1.myfunc()
