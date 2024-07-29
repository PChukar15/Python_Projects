from abc import ABC, abstractmethod


class problem(ABC):
    def prob(self, title):
        print("My {} has got me on Warhammer now.".format(title))

    @abstractmethod
    def state(self, title):
        pass


class Statment(problem):
    def state(self, title):
        print("My {} really doesn't like it ".format(title))


obj = Statment()
obj.prob("dad")
obj.state("wallet")
