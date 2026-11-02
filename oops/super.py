# super()= function 

class Shape:
     def __init__(self,color,filled):
        self.color=color
        self.filled=filled

     def describe(self):
      print(f"it is {self.collor}and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)  #used super() function 
        self.radius=radius
        

class Square(Shape):
   def __init__(self,color,filled,radius):
           self.color= color
           self.filled=filled
           self.radius=radius

   def describe(self):
        print(f"it is a circle with an area of {3.14* self.radius*self.radius}cm^2")
        super().describe() # with this we can print both describe 

class Traingle(Shape):
     def __init__(self,color,filled,radius):
         self.color= color 
         self.filled=filled
         self.radius=radius 


#with super function 
circle = Circle(color="red",filled=True,radius=5)

print(circle.color,circle.filled,f"{circle.radius}cm")

# without super function
triangle = Traingle("green",False,6)
print(triangle.color,triangle.filled,triangle.radius)

