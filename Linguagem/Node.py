
class Node:
    i = 0
    def __init__(self):
        self.value = None
        self.children = []

    @staticmethod
    def newId():
        Node.i += 1
        return Node.i

    def Evaluate(self):
        self.children[0].Evaluate()