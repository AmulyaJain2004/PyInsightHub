import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def circumference(self):
        return (2*(math.pi)*self.radius)
    
    def area(self):
        return ((math.pi)*math.pow(self.radius,2))
        
def main():
    radius = int(input("Enter the radius of circle: -\n"))
    
    circle = Circle(radius)
    
    print(f"Area of circle is: {circle.area()}")
    
if __name__ == "__main__":
    main()
