task=1
# # class Sathish():
# #     def anna(self):
# #         print("this is name")
# # annayya=Sathish()
# # annayya.anna()

# # result=this is name

task=2

class Akka():
    Name=("vijaya laxmi")
    def sister(self):
        print(self.Name)
obj=Akka()
obj.sister()

#  result=vijaya laxmi       


class Vijaya():
    def __init__(self,a,b,c):
        self.e=a
        self.f=b
        self.g=c
    def Vara(self):
        print(self.e,self.f,self.g)
obj=Vijaya(1,2,3)
obj.Vara()



class Mobile():
    def __init__(self, Camera, Ram, Rom, Price):
        self.camera=Camera
        self.ram=Ram
        self.rom=Rom
        self.price=Price
    def Features(self):
        print('Size of the Camera:',self.camera)
        print('Size of the Ram:',self.ram)
        print('Size of the Rom:', self.rom)
        print('Name of the Price:', self.price)

obj=Mobile("13mp", "4gb", 512, 12000)
obj.Features()

result-
Size of the Camera: 13mp
Size of the Ram: 4gb
Size of the Rom: 512
Name of the Price: 12000




inheritance practice
which is helpfull for reduce the coding time and lenght with the help of parent
properties to child properties

types
single, multi level, heirachy, multiple
single: one parent and one child

example:

class Parent:
    def output(self):
        print ('this is parent class')
class Child(Parent):
    def childoutput(self):
        print ('this is child class')
i=Child()
i.output()
i.childoutput()

result
this is parent class
this is child class


multi level: level 1, lvel 2, level 3 like-GF,F, CHILD
example:

class Musalayya:
    def output(self):
        print('this is musalayya class')
class Masenu(Musalayya):
    def outputM(self):
        print ('this is masenu class')
class Srinu(Masenu):
    def child2(self):
        print('this is srinu class')

i=Srinu()
i.output()
i.outputM()
i.child2()

result-
this is musalayya class
this is masenu class
this is srinu class


multiple 
example:

class Masenu:
    def output(self):
        print ('this is dady class')
class Kondamma:
    def outputK(self):
        print('this is mother class')
class Srinu(Masenu,Kondamma):
    def child(self):
        print ('this class is mine')
i=Srinu()
i.output()
i.outputK()
i.child()

this is dady class
this is mother class
this class is mine

polymorphism=many+forms
mothed overloading=1
 mothed over ridding=2
overloading


class Methodoverloading:
    def sri(self, a=None, b=None, c=None):
        print(a,b,c)
i=Methodoverloading()
i.sri(1,2,3)
i.sri(1,2)
i.sri(1)
i.sri()

result:
1 2 3
1 2 None
1 None None
None None None


encapsalisation
public