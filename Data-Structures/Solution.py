from typing import List, Tuple, Dict, Set

# Create variables
my_list = [1, 2, 3, 4, 5]
my_tuple = ("apple", "banana", "cherry")
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
my_set = {1.0, 2.0, 3.0}

# Define functions
def find_max(lst: List[int]) -> int:
    #Return the maximum value in a given list.
    return max(lst)

def remove_duplicates(lst: List[int]) -> List[int]:
    #Remove duplicate elements from a given list and return a new list with unique elements.
    return list(set(lst))

def reverse_tuple(tup: Tuple[str, str, str]) -> Tuple[str, str, str]:
    #Reverse the order of elements in a given tuple and return a new tuple.
    return tup[::-1]

def dict_to_list(dct: Dict[str, str]) -> List[Tuple[str, str]]:
    #Convert a dictionary to a list of tuples where each tuple contains a key-value pair.
    return list(dct.items())

def set_intersection(set1: Set[float], set2: Set[float]) -> Set[float]:
    #Return a new set containing the elements that are present in both set1 and set2.
    return set1.intersection(set2)

# Test functions
print(find_max(my_list)) # Output: 5
print(remove_duplicates(my_list)) # Output: [1, 2, 3, 4, 5]
print(reverse_tuple(my_tuple)) # Output: ("cherry", "banana", "apple")
print(dict_to_list(my_dict)) # Output: [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
print(set_intersection(my_set, {2.0, 3.0, 4.0})) # Output: {2.0, 3.0}
