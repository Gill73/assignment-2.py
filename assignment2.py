# '''Assignment 2
# This assignment covers your intermediate profiency with
#     Python. It engages your ability to transform
#     data without affecting anything outside the program.
# This assignment places heavy emphasis on Python data structures.
# '''

#     '''Item 1.
#     Specific Filter. 2 points.
#     Returns the elements of a list that are greater than the integer 50.
#     This is called "filtering" each number based on whether it is greater than 50. 
#         Filtering is a very common pattern in high-level (i.e., human-readable)
#         programming.
#     For this number:
#         1. The parameter l will be a list of either floats or ints.
#     
#     Parameters
#     ----------
#     l: list
#         a list of numbers (floats or ints)
#     Returns
#     -------
#     list
#         a list of elements in l that are greater than the integer 50
    
    # Write your code below this line
    
def specific_filter(l):
    new_list = []
    for x in l:
        if x > 50:
            new_list.append(x)
    return new_list
        
print(specific_filter([54,23,54,22,1,54.67]))



# '''Item 2.
#     General Filter. 3 points.
#     Returns the elements of a list that return True when passed to a filtering function.
#     This is how general filters are done.
#     For this number:
#         1. The parameter l will be a list of any data type.
#         2. The filter_function is just a function that has been passed as an argument to 
#             the general_filter function. It accepts a single argument and returns either
#             True or False.
#     
#     Parameters
#     ----------
#     l: list
#         a list of any data type
#     filter_function: function
#         a function which accepts any data type and returns bool
#     Returns
#     -------
#     a list of elements in l that are greater than the integer 50
#     '''
    # Write your code below this line

def filter_function(filter_function):
    if type(filter_function) == int and filter_function > 50:
        return True
    elif type(filter_function) == float and filter_function > 50:
        return True
    
def general_filter(l,filter_function):
    new_list = []
    for item in l:
        if filter_function(item) == True:
            new_list.append(item)
    return new_list
            
print(general_filter([4,"hello",67,78.10,"baby shark",87],filter_function))    
        





# '''Item 3.
#     Specific Map. 2 points.
#     Accepts a list of numbers. Returns another list which contains the squares of the
#         numbers.
#     This is called "mapping" each number to its square. Mapping is a very common pattern
#         in high-level (i.e., human-readable) programming.
#     For this number:
#         1. The parameter l will be a list of either floats or ints.
#     Example:
#     specific_map([1, 2, 3, 4, 5]) -> [1, 4, 9, 16, 25]
#     
#     Parameters
#     ----------
#     l: list
#         a list of numbers (floats or ints)
#     Returns
#     -------
#     list
#         a list of the squares of the elements in l
#     Write your code below this line

def specific_map(l):
    u = map(square,l)
    return list(u)
    
def square(x):
    return x * x
    
    
print(specific_map([45,2,3,46,9]))





#     Item 4.
#     General Map. 3 points.
#     Accepts a list of any data type. Returns another list which uses a function to map
#         the first lists's elements to the second list.
#     This is how general maps are done.
#     
#     Parameters
#     ----------
#     l: list
#         a list of any data type
#     map_function: function
#         a function which accepts one argument and returns any data type
#     Returns
#     -------
#     list
#         a list which contains the mapped elements of l
#    
# Write your code below this line
#For `general_map`, the function should return a new list with the modified items from the input list.



def general_map(l,map_function):
    u = map(map_function,l)
    return list(u)

def map_function(x):
    return f"hi, {x}!"
    
print(general_map(["Gill","Cam",76,90.000,"Mikasa"],map_function))

