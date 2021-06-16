import ctypes

def split(string: str) -> ctypes.Array:
    return [char for char in str]

def list_to_string(array) -> str:
    str = ""
    for i in array:
        str += i
    return str

def sort_alphabetical_order(string: str) -> str:
    array = split(string)
    array_sorted = sorted(array)
    new_string = list_to_string(array_sorted)
    return new_string

str = input(" input any text you would like to sort in alphabetical order! ")
new_str = sort_alphabetical_order(str)
print(new_str)
