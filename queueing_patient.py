from login import *

class Queue:
    def __init__(self):
        self.front = None
        self.rare = None

    def __str__(self):
        return "First: " + str(self.front) + "Last: " + str(self.rare)

    def add(self, patient):

        # make a patient doubly linked node
        pNode = Node(patient)
        
        if self.front == None:
            self.front = patient
            self.rare = patient
        else:
            self.rare.next = pNode
            pNode.prev = self.rare
            self.rare = pNode

    def retrive(self):
        temp = self.front
        self.front = self.front.next
        self.front.prev = None
        temp.next = None
        return temp


    def priorized(self,patient):
        pNode = Node(patient)
        self.front.prev = pNode
        pNode.next = self.front
        self.front = pNode
        
    def isEmptyQueue(self):
        if self.front == None:
            return True
        else:
            return False
