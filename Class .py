#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


class Point3D():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d,%d,%d)" % (self.x, self.y, self.z)
my_point = Point3D(1,2,3)
print(my_point)

#question 1


# In[3]:


class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def rectangle_area(self):
        return self.length*self.width
    def rectangle_perimeter(self):
        return  2* (self.length+self.width)
    
    
    #qyestion 2

my_rectangle = Rectangle(3,4)
print(my_rectangle.rectangle_area())
print(my_rectangle.rectangle_perimeter())


# In[36]:


class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Balance=",self.balance)
        
        
        #qesution 4


# In[ ]:




