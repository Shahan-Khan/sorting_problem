# Comparision Based Approach

# import os

# def divide_file(file_path, chunk_size):
#     chunk_files = []
#     chunk = []
#     chunk_index = 0

#     with open(file_path, 'r') as file:
#         for line in file:
#             chunk.append(int(line.strip()))
#             if len(chunk) >= chunk_size:
#                 chunk.sort()  # Sort the chunk in memory
#                 chunk_file_path = f"chunk_{chunk_index}.txt"
#                 with open(chunk_file_path, 'w') as chunk_file:
#                     for number in chunk:
#                         chunk_file.write(f"{number}\n")
#                 chunk_files.append(chunk_file_path)
#                 chunk = []
#                 chunk_index += 1

#     if chunk:
#         chunk.sort()  # Sort the last chunk if any
#         chunk_file_path = f"chunk_{chunk_index}.txt"
#         with open(chunk_file_path, 'w') as chunk_file:
#             for number in chunk:
#                 chunk_file.write(f"{number}\n")
#         chunk_files.append(chunk_file_path)

#     return chunk_files


# def merge_chunks_with_reopen(chunk_files, output_file_path):
#     current_elements = []  # List to store the current smallest element from each chunk file 
    
#     # Step 1: Initialize current_elements with the first line from each file
#     for chunk_file in chunk_files:
#         with open(chunk_file, 'r') as fp:
#             line = fp.readline().strip()
#             if line:
#                 current_elements.append((int(line), chunk_file, fp.tell()))
    
#     with open(output_file_path, 'w') as output_file:
#         while current_elements:
#             # Find the smallest element among current_elements
#             smallest_index = 0  # Initially assuming that the smallest element is at the first position
#             for i in range(1, len(current_elements)):  # Begin a loop starting from the second element
#                 if current_elements[i][0] < current_elements[smallest_index][0]:
#                     smallest_index = i
            
#             # Write the smallest element to the output file
#             smallest_value, smallest_file, position = current_elements[smallest_index]
#             output_file.write(f"{smallest_value}\n")
            
#             # Reopen the corresponding file, read the next element
#             with open(smallest_file, 'r') as smallest_fp:
#                 smallest_fp.seek(position)
#                 next_line = smallest_fp.readline().strip()
#                 new_position = smallest_fp.tell()
            
#             if next_line:
#                 # Update the current_elements list with the new element and position
#                 current_elements[smallest_index] = (int(next_line), smallest_file, new_position)
#             else:
#                 # Remove the file entry if it's exhausted
#                 del current_elements[smallest_index]
    
#     # Clean up remaining chunk files
#     for chunk_file in chunk_files:
#         os.remove(chunk_file)

# # Example usage:
# file_path = 'unsorted.txt'
# chunk_size = 10000  # Adjust based on available memory
# chunk_files = divide_file(file_path, chunk_size)
# merge_chunks_with_reopen(chunk_files, 'sorted.txt')



# Heap Based Approach

import os
import heapq

def divide_file(file_path, chunk_size):
    chunk_files = []  # empty list to store the names of chunk files
    chunk = []  # list to store lines read from the file
    chunk_index = 0  # to keep track of the number of chunks.

    with open(file_path, 'r') as file:
        for line in file:  # Reads the file line by line in a loop.
            chunk.append(int(line.strip()))
            if len(chunk) >= chunk_size:  # Checks if the chunk list has reached the chunk_size.
                chunk.sort()  # Sort the chunk in memory
                chunk_file_path = f"chunk_{chunk_index}.txt"
                with open(chunk_file_path, 'w') as chunk_file:
                    for number in chunk:
                        chunk_file.write(f"{number}\n")
                chunk_files.append(chunk_file_path)
                chunk = []
                chunk_index += 1

    if chunk:
        chunk.sort()  # Sort the last chunk if any
        chunk_file_path = f"chunk_{chunk_index}.txt"
        with open(chunk_file_path, 'w') as chunk_file:
            for number in chunk:
                chunk_file.write(f"{number}\n")
        chunk_files.append(chunk_file_path)

    return chunk_files


def merge_chunks(chunk_files, output_file_path):
    min_heap = []  # empty list for the heap
    file_pointers = []  # empty list to store file pointers.

    # Open all chunk files and initialize the heap
    for chunk_file in chunk_files:  # Iterate over each chunk file
        fp = open(chunk_file, 'r')  # Open the file
        file_pointers.append(fp)  # Store the file pointer in file_pointers.
        line = fp.readline().strip()  # Read the first line from each chunk file
        if line:
            heapq.heappush(min_heap, (int(line), chunk_file, fp))  # Convert the line to an integer and pushes a tuple

    with open(output_file_path, 'w') as output_file:
        while min_heap:
            smallest_value, smallest_file, fp = heapq.heappop(min_heap)  # Pop the smallest element (a tuple) from the heap
            output_file.write(f"{smallest_value}\n")  # Write the smallest value to the output file.

            next_line = fp.readline().strip()  # Reads the next line from the file pointer 
            if next_line:
                heapq.heappush(min_heap, (int(next_line), smallest_file, fp))  # Convert the next line to an integer and push it to heap 

    # Close all file pointers and remove chunk files
    for fp in file_pointers:  # close each file pointer.
        fp.close()
    for chunk_file in chunk_files: # remove each chunk file.
        os.remove(chunk_file)

file_path = 'unsorted.txt'
chunk_size = 3 # Adjust the chunk size based on avalaible memory (Give the chunk size as the number of lines)
chunk_files = divide_file(file_path, chunk_size)
merge_chunks(chunk_files, 'sorted.txt')



