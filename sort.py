def sort_words_in_file(source_file, output_file): 
    try: 
        # Read words from the source file 
        with open(source_file, 'r') as file: 
            words = file.read().split() 
        # Convert words to lowercase 
        lower_case_words = [word.lower() for word in words] 
        # Sort the words 
        sorted_words = sorted(set(lower_case_words)) 
        # Write sorted words to the output file 
        with open(output_file, 'w') as file: 
            for word in sorted_words: 
                file.write(f"{word}\n") 
        print(f"Sorted words written to {output_file}") 
    except Exception as e: 
        print(f"An error occurred: {e}") 
# Example usage 
source_file = 'input.txt' # Replace with your source file name 
output_file = 'output.txt' # Replace with your desired output file name 
sort_words_in_file(source_file, output_file) 
