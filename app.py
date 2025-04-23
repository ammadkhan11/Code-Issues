class Student:
    # default constructor
    section="A"
    name="anonymous"
    def __init__(self):
        pass
    def __init__(self, full_name, marks):
        self.name=full_name
        self.marks =marks
    def hello(self):
        print("Hello", self.name)
    def get_marks(self):
        return self.marks
    
s1 = Student("Daniyal",93)
print(s1.name,s1.marks,s1.section)

s1.hello()
print(s1.get_marks())
