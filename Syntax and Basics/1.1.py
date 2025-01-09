shape = input("What is the shape? ")
if shape.lower() =='square':
    side=int(input("what is the length of one side? "))
    if side<=0:
        print("Invalid input")
    area= side*side
    perimeter = 4*side
    print("Area of given " + shape + " is " + str(area))
    print("Perimeter of given " + shape + " is " + str(perimeter))
elif shape.lower() =='rectangle':
    length = int(input("What is the length? "))
    breadth = int(input("What is the breadth? "))
    if length <= 0 or breadth<=0:
        print("Invalid input")
    area= length*breadth
    perimeter= 2*(length+breadth)
    print("Area of given " + shape + " is " + str(area))
    print("Perimeter of given " + shape + " is " + str(perimeter))
elif shape.lower() =='parallelogram':
    length = int(input("What is the length? "))
    breadth = int(input("What is the breadth? "))
    height = int(input("What is the height? "))
    if length <= 0 or breadth<=0 or height<=0:
        print("Invalid input")
    area= height*breadth
    perimeter= 2*(length+breadth)
    print("Area of given " + shape + " is " + str(area))
    print("Perimeter of given " + shape + " is " + str(perimeter))
elif shape.lower() =='triangle':
    height = int(input("What is the height? "))
    base = int(input("What is the base? "))
    s1 = int(input("What is the second side? "))
    s2 = int(input("What is the third side? "))
    if height <= 0 or base <=0 or s1<=0 or s2<=0:
        print("Invalid input")
    area= 0.5*base*height
    perimeter= (base+s1+s2)
    print("Area of given " + shape + " is " + str(area))
    print("Perimeter of given " + shape + " is " + str(perimeter))
elif shape.lower() =='circle':
    radius = int(input("What is the radius? "))
    if radius <= 0:
        print("Invalid input")
    area= 3.14*radius*radius
    perimeter= 2*3.14*radius
    print("Area of given " + shape + " is " + str(area))
    print("Perimeter of given " + shape + " is " + str(perimeter))
else:
    print("Invalid input")
