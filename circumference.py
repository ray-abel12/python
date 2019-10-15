# Calculate the area and circumference of a c i r c l e from i t s radius .
# Step 1: Prompt f o r a radius .
# Step 2: Apply the area formula .
# Step 3: Print out the r e s u l t s .

import math
radius_str = input("Enter the radius of your circle: ")
radius_int = int(radius_str)

circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

print ("The cirumference is:",circumference, \
", and the area is:",area)
