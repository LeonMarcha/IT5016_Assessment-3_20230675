# this program was made to understand running code with a class

class Student:
    def __init__(self, sn, sa, sg):
        self.sn = sn
        self.sa = sa
        self.sg = sg

    def get_name(self):
        return self.sn

    def set_name(self, sn):
        self.sn = sn

    def get_age(self):
        return self.sa

    def set_age(self, sa):
        self.sa = sa

    def get_gen(self):
        return self.sg

    def set_gen(self, sg):
        self.sg = sg

    def get_all(self):
        all_details = self.sn, self.sa, self.sg
        return " ".join(all_details)


# class Main(Student):
#  make class that includes response and status

Name = "Geoff"
Age = "29"
Sex = "F"
student1 = Student("Taz", "19", "F")
student2 = Student(Name, Age, Sex)

# exploring ways to show all parameters in one print
print(student2.get_name(),
      student2.get_age(),
      student2.get_gen()
      )

print(student1.get_all())

print(student1.get_gen())
print(student1.sn)
# sn can be used instead of getName
student1.set_name("Taz Khan")
print(student1.get_name())
