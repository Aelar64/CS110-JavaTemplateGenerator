# CS110-JavaTemplateGenerator
Holds the template creator that I made for CS110 at CWU. Generates a blank Java program with the appropriate header.  

By default, the program will only create a new file, so it won't overwrite anything that's already there (use `-f` to make it overwrite).  

## Usage

`python javaTemplateCreator.py [file] [-vfsS]`  

#### Flags:
`-v`: Verbose. Outputs the generated file to the command line.  
`-f`: Force. Overwrite the file if it already exists.  
`-s`: Scanner. Imports `java.util.Scanner`, and declares a `Scanner` object called `scanner` using `System.in`.  
`-S`: Simulate. Doesn't write to a file, only outputs to the command line.
