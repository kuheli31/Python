#Input height and width and coverage as arguments where 1 jar can paint 7 sq.metre 
#so find the number of jars needed to print the user input wall .

import math

def paint(height, width, coverage):
    area = height * width  # Calculate the area to paint
    jars_needed = math.ceil(area / coverage)  # Calculate the number of jars
    print(jars_needed)

# Example usage
paint(10, 50, coverage=7)  # Output: Number of jars needed
