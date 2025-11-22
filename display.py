def display_array(arr): 
    """Display the contents of the array.""" 
    print("Current array:", arr) 
 
def append_to_array(arr, item): 
    """Append an item to the array.""" 
    arr.append(item) 
    print(f"Appended '{item}' to the array.") 
 
def insert_to_array(arr, index, item): 
    """Insert an item at a specific index in the array.""" 
    arr.insert(index, item) 
    print(f"Inserted '{item}' at index {index}.") 
 
def reverse_array(arr): 
    """Reverse the order of the items in the array.""" 
    arr.reverse() 
    print("Reversed the array.") 
 
def main(): 
    # Create an array (list) 
    array = [] 
 
    # Display initial array 
    display_array(array) 
 
    # Append items 
    append_to_array(array, 'apple') 
    append_to_array(array, 'banana') 
 
    # Display after appending 
    display_array(array) 
 
    # Insert an item at index 1 
    insert_to_array(array, 1, 'orange') 
 
    # Display after inserting 
    display_array(array) 
 
    # Reverse the array 
    reverse_array(array) 
 
    # Display final array 
    display_array(array) 
 
 
if __name__ == "__main__": 
    main() 

