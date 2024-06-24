#Large File Sorting

##Overview

This project demonstrates a Python implementation to sort large files that exceed available RAM using a merge sort approach with heap operations. It efficiently merges sorted chunks of a large file into a single sorted output file, minimizing memory usage and maximizing performance.
##Features

    - Divides the large file into manageable chunks.
    - Sorts each chunk independently using Python's built-in sorting capabilities.
    - Merges sorted chunks using a heap data structure for efficient smallest element retrieval.
    - Outputs a single sorted file without consuming excessive memory.

##Requirements

    - Python 3.x
    - heapq module (standard library in Python)

##Usage

    ###Sorting a Large File:
        - Adjust chunk_size in the merge_chunks function to balance memory usage and performance.
        - Modify file_path and output_file_path variables to specify input and output file paths.

```file_path = 'large_file.txt'
chunk_size = 10000  # Adjust based on available memory
chunk_files = divide_file(file_path, chunk_size)
merge_chunks(chunk_files, 'sorted_large_file.txt')```

## Example Code Explanation:

    - divide_file(file_path, chunk_size): Divides large_file.txt into smaller sorted chunks.
    - merge_chunks(chunk_files, output_file_path): Merges sorted chunks into sorted_large_file.txt.

## Documentation

[Documentation](https://docs.google.com/document/d/1wZddZ418nOD14muzE3fcBhtixE04GlIWMOrsRRXUAAg/edit?usp=sharing)