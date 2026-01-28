# Brandon Knorr
# Mod 2 Lab 1 
# due: 1/28

# Functions 
    # store code
    # 1. def
    # 2. function_name
    # 3. () optional parameters
    #       parameters are variables used within the function
    # 4. : declare the scope of the function
    #       scope is a subset of code
    # 5. Body of the function (stored code)
    # 6. Optional return statement 
    #       sends value back to the function call
    #       once you hit a return statement the function ends

def test_function():
    print('this is a test')
    return 123

test_function()

print(test_function())

def get_area(length, width):
    area = length * width
    return area


def calculate_area_from_user():
    length = float(input('What is the length? '))
    width = float(input('What is the width? '))
    area = get_area(length, width)
    print(f'The area is {area}')

calculate_area_from_user()


