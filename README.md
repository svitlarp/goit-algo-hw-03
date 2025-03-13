# goit-algo-hw-03



## Recursion
 
### 1. Write a Python program that recursively copies files in a source directory, moves them to a new directory, and sorts them into subdirectories named based on the file extension.
- <strong>Parsing arguments: </strong>
    - The script should accept two command line arguments: the path to the source directory and the path to the destination directory (by default, if the destination folder is not passed, it should be named dist).

- <strong>Recursively reading directories: </strong>
    - A function should be written that takes the path to a directory as an argument.
    - The function should iterate over all the elements in the directory.
    - If the element is a directory, the function should call itself recursively for that directory.
    - If the element is a file, it should be available for copying.
- <strong>Copying files: </strong> 
    - For each type of file, a new path should be created in the source directory, using the file extension for the subdirectory name. The file with the corresponding type should be copied to the corresponding subdirectory.
- <strong>Exception handling: </strong>
    - The code must properly handle exceptions, such as file or directory access errors.

### 2. Write a Python program that generates a Koch snowflake fractal using recursion, allowing the user to specify the desired recursion level.
![401491322-1b3a6dd7-9515-4a89-a682-c1ba79856eef](https://github.com/user-attachments/assets/f1d6b9bc-f914-4b5b-8d3f-973d7abd45b9)



### 3. Towers of Hanoi
![Example-of-Hanoi-Tower-with-3-disks](https://github.com/user-attachments/assets/b28ed311-a853-40da-9137-9f45bc9ca95f)
