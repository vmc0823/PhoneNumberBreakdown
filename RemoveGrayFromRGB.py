# Read the values for red, green, and blue
red = int(input())
green = int(input())
blue = int(input())

# Find the smallest value among red, green, and blue (the gray part)
gray = min(red, green, blue)

# Subtract the gray part from each value
red -= gray
green -= gray
blue -= gray

# Output the adjusted values
print(red, green, blue)