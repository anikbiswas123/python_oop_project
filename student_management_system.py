# create a student class

class Student:

#constructor
    def __init__(self,name,rollno,m1,m2):
        self.name=name
        self.rollno=rollno
        self.m1=m1
        self.m2=m2

    # creata a function add data
    def add_student(self,name,RollNo,mark_1,marks_2):
        st=Student(name,RollNo,mark_1,marks_2)
        mylist.append(st)

    #cteaye a function display
    def display(self,ob):
        print("display student list ")
        print("\n")
        print("student name :",ob.name)
        print(" Roll No :",ob.rollno)
        print("Mark_1 :",ob.m1)
        print("Mark_2 :",ob.m2)
        print("\n")

    #create a function seacrch()
    def search(self,rn):
       for i in range(mylist.__len__()):
           if (mylist[i].rollno)== rn:
               return  i
        #create a  function delect()
    def delect(self,rn):
        i=std.search(rn)
        del mylist[i]

   #create a function update
    def update(self,rn,new_rn):
        i=std.search(rn)
        new_roll=new_rn
        mylist[i].rollno=new_roll

#create student list
mylist=[]

#create student object
std=Student('',0,0,0)


print("insered data in sudent list ")
std.add_student("sumilon biswas",21,70,80)
std.add_student("joya bain ",23,50,60)
std.add_student("tanbir islam",25,60,70)
std.add_student("Rakib vai",29,70,80)

print("\n")

# print("display student list")
# for i in range(len(mylist)):
#     std.display(mylist[i])

print("searching the student list ")
s=std.search(21)
std.display(mylist[s])

# print("delect a item ")
# std.delect(21)
# print(mylist.__len__())
# print("after delecting a student list ")
# for i  in range(mylist.__len__()):
#     std.display(mylist[i])
#
#
# print("update student list ")
#
# std.update(21,30)
# print(mylist.__len__())
# print("update list values of student list ")
# for i in range(mylist.__len__()):
#     std.display(mylist[i])
#

