# ALGORITM-A1
Sorts any given string into alphabetical order


FUNCTION: split(string: str):
    converts string into an array
    
FUNCTION: sort_alphabetical_order(string: str)
    sorts a given string into alphabetic order and returns a new one that is sorted
    
FUNCTION: list_to_string(array)
    converts a list to a string
    
    
ctypes was used because python does not have array type, with ctypes imported we can specify return type for function split( string: str )


TO BE FIXED:
    currently we have to lowercase the string before we sort them because capital letters have a higher dec number then lowercase, meaning if we input 
    cBa it will ( B will have the lowest value ) therefor it will print out Bac
    
    

    
