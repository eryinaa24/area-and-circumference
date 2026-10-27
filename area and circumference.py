PI=3.14159

radius=float(input("Enter a radius in meters: "))
while radius<0 or radius>1000:
    print("Invalid radius. Please enter a radius between 0 to 1000 meters.")
    radius=float(input("Enter a radius in meters: "))

area=PI*radius**2
circumference=2*PI*radius

print(f"{area:.2f}")
print(f"{circumference:.2f}")
