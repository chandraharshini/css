def print_lines_in_reverse(file_name): 
    try: 
        # Open the file for reading 
        with open(file_name, 'r') as file: 
            # Read all lines 
            lines = file.readlines() 
        # Print each line in reverse order 
        for line in lines: 
            print(line.strip()[::-1]) 
    except Exception as e: 
        print(f"An error occurred: {e}") 
# Example usage 
file_name = 'input.txt' # Replace with your file name 
print_lines_in_reverse(file_name) 
 
