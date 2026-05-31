# 📘 Assignment: File Handling and Error Management

## 🎯 Objective

Learn to work with files in Python by reading and writing data, and master error handling techniques to write defensive code that gracefully handles problems when they occur.

## 📝 Tasks

### 🛠️ Reading from a File

#### Description
Write a function called `read_file_lines()` that reads a text file and returns its contents as a list of lines. Your program should handle the case where the file doesn't exist.

#### Requirements
Completed program should:

- Accept a filename as a parameter
- Open and read the file line by line
- Return a list of lines (with newlines stripped)
- Use a try-except block to catch `FileNotFoundError`
- Print an error message if the file is not found
- Example: `read_file_lines("data.txt")` returns `["Hello", "World"]`


### 🛠️ Writing to a File

#### Description
Write a function called `save_to_file()` that takes a list of items and writes them to a file, with each item on a new line.

#### Requirements
Completed program should:

- Accept a filename and a list of items as parameters
- Open the file in write mode
- Write each item as a separate line
- Handle potential errors with a try-except block
- Print a success message if the file was written
- Print an error message if writing failed
- Example: `save_to_file("output.txt", ["Alice", "Bob", "Charlie"])`


### 🛠️ Error Handling with Try-Except

#### Description
Write a function called `safe_divide()` that divides two numbers and handles errors gracefully.

#### Requirements
Completed program should:

- Accept two numbers as parameters
- Return the result of dividing the first by the second
- Use a try-except block to catch `ZeroDivisionError`
- Use a try-except block to catch `TypeError` (for invalid input types)
- Print an appropriate error message for each type of error
- Return `None` if an error occurs
- Example: `safe_divide(10, 2)` returns `5.0`, `safe_divide(10, 0)` prints error and returns `None`


### 🛠️ Processing a CSV File

#### Description
Write a function called `read_csv_data()` that reads a CSV file and returns the data in a structured format. Each row should become a dictionary with column headers as keys.

#### Requirements
Completed program should:

- Accept a CSV filename as a parameter
- Read the first line as headers
- Convert each subsequent line into a dictionary with headers as keys
- Return a list of dictionaries
- Use try-except to handle `FileNotFoundError` and other errors
- Print an error message and return an empty list if the file cannot be read
- Example: Reading a file with headers `name,age,city` creates dictionaries like `{"name": "Alice", "age": "25", "city": "Portland"}`
