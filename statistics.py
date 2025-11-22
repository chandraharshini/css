def compute_file_statistics(file_name): 
    try: 
        with open(file_name, 'r') as file: 
            lines = file.readlines() 
        num_lines = len(lines) # Count lines 
        num_words = 0 # Initialize word count 
        num_characters = 0 # Initialize character count 
        for line in lines: 
            num_words += len(line.split()) # Count words in the line 
            num_characters += len(line) # Count characters in the line 
        print(f"Number of lines: {num_lines}") 
        print(f"Number of words: {num_words}") 
        print(f"Number of characters: {num_characters}") 
    except Exception as e: 
        print(f"An error occurred: {e}") 
# Example usage 
file_name = 'input.txt' # Replace with your file name 
compute_file_statistics(file_name) 
 
 
