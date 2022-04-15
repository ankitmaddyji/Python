<<<<<<< HEAD
import random
def gamewin(comp,you):
 if comp==you:
    return None
 elif (comp=='s'):
   if you=='g':
      return True
   elif you=='w':
     return False


 elif (comp=='w'):
   if you=='s':
      return True
   elif you=='g':
     return False


 elif (comp=='g'):
   if you=='w':
      return True
   elif you=='s':
     return False

comp=print("comp turn snake(s) ,gun(g) ,water(w)")

randint=random.randint(1,3)
if randint==1:
    comp='s'
elif randint==2:
    comp='w'
elif randint==3:
    comp='g'

you=input("your turn snake(s) ,gun(g) ,water(w)")
a=gamewin(comp,you)

if a==None:
    print("tie")
elif a:
    print("you win!")
else:
    print("you lose")
print(f"computer turn {comp}")
print(f"your turn {you}")
=======
