# mystuff is a module which is a seperate file which can contain it's own apple function 
# Mystuff40 is a container in the same file which can contain apple function which is different from 
# the apple function on line8  
# every function have a behaviour when you want different behaviours then we have to use classes or seperate modules 

class Mystuff40:      # class name shoud start ONLY with capital letter 
    def apple():
        print("I AM APPLES! ")
print(Mystuff40)
#def apple():
#    print("I AM APPLES NO2! ")
#apple()
#Mystuff40.apple()
# this is just a variable

#import mystuff # it excutes all the contents from mystuff
#import challenge24_07_1
#mystuff.apple()
#print(mystuff.tangerine) # modules also work like dictionary but it uses dot insted of square brackets 
#import challenge24_07_1
#challenge24_07_1.get_grade(100)

#name = {"NAME" : "A", "AGE" : "6"} 
#print(name["AGE"])

import challenge23_07_1
print(challenge23_07_1.names)

#import challenge23_07_3
#challenge23_07_3.cost(90)

import mystuff
mystuff.players[0]
print(mystuff.players[1], "it comes from mystuff.py")



