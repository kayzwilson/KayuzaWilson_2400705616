length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
def calculate_area(length, width):
    area = length * width
    return area

area = calculate_area(length, width)
print("The area of the rectangle is:", area)