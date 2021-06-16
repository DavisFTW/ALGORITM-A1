import ctypes

def split( string: str ) -> ctypes.Array:
    return [char for char in string]

def list_to_string( array ) -> str:
    str = ""
    for i in array:
        str += i
    return str

def sort_alphabetical_order(input_string : str) -> str:

    input_string = input_string.lower() # FIXME: without this we will get wrong results as capital chars have a lower number then lowercase
    array = split(input_string)

    n = len(array)

    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                temp_var = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp_var
                
    
    new_string = list_to_string(array)
    return new_string

str = input(" input any text you would like to sort in alphabetical order! ")


new_string = sort_alphabetical_order(str)
print(new_string)
