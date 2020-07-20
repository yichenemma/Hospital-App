class Node:
    def __init__(self, content):
        self.content = content
        self.prev = None
        self.next = None


    def __str__(self):
        return str(self.content)


class History:
    def __init__(self):
        self.start = None
        self.end = None
        self.search = self.start

    def add(self, text):
        # create new doubly-linked node
        text = Node(text)
        if self.start == None:
            self.start = text
            self.end = text

        else:
            self.end.next = text
            text.prev = self
            self.end = text

    def __str__(self):
        return "Start: " + str(self.start) + " End: " + str(self.end)

class Current_Note:

    def __init__(self,content):

        self.content = content


    # clears all the notes and rewrite
    def update_note(self, updates):
        self.content = updates


    # add more notes to it
    def add_note(self, add):
        self.content += add

    def __str__(self):
        return str(self.content)


class Patient:
    def __init__(self, name, birth, medical_condition):  # obtained from user
        self.name = name
        self.birth = birth
        self.history = History()
        self.current = Current_Note("headache")
        # self.ID = identification
        self.condition = medical_condition
        self.priority = False
        self.note = Current_Note(" ")


    # move current to history and clear up the note
    def move_to_his(self):
        self.history.add(self.current.content)
        self.current.update_note(None)

    def emergency(self):
        self.priority = True
            


    def __str__(self):
        return "Name: " + self.name + "\n" + \
               "Birthday: " + self.birth + "\n" + \
               "Medical History: " + str(self.history) + "\n" + \
               "Medical Condition: " + self.condition + "\n" +\
               "Current Note: " + str(self.note) + "\n"+\
               'prority: ' + str(self.priority)

#if __name__ == '__main__':
p1 = Patient("tom", "2000-12-03", "normal")
print(p1)
p1.move_to_his()
print(p1.history)
p1.history.add("migraine")
print(p1.history)





