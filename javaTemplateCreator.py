from datetime import date
from sys import argv

filename = ""
filepath = ""
directory = ""
NAME = 'Joshua Merrill'
verbose = False
scanner = False
simulate = False
force = False

if len(argv) == 1:
    filepath = input("Please enter the location of your Java program: ")
else:
    filepath=argv[1]

try:
    if 'v' in argv[2]:
        verbose = True
    if 's' in argv[2]:
        scanner = True
    if 'S' in argv[2]:
        simulate = True
    if 'f' in argv[2]:
        force = True
except IndexError:
    verbose = False
    scanner = False
    simulate = False

filename = filepath.split("/")[-1]
if ".java" in filename:
    filename = filename.split(".")[0]

for folder in filepath.split("/")[:-1]:
    directory += folder + "/"

print(f"File: {directory}{filename}.java")
if not simulate:
    try:
        javaFile = open(f"{directory}/{filename}.java", "w" if force else "x")
    except FileExistsError:
        print(f"Error: the specified file '{filename}.java' already exists.")
        print(f"Use -f to overwrite {filename}.java.0")
        exit()

filecontents = ""
filecontents += f"//name: {NAME}" + "\n"
filecontents += f"//date: {date.today().isoformat()}" + "\n"
filecontents += f"//file: {filename}.java" + "\n\n"
filecontents += "//generated by javaTemplateCreator.py - https://github.com/Aelar64/CS110-JavaTemplateGenerator \n\n\n"


if scanner:
    filecontents += "import java.util.Scanner;\n\n\n"
filecontents += f"public class {filename} {{\n    "
filecontents += r"public static void main(String[] args) {" + "\n        \n"
if scanner:
    filecontents += "        Scanner scanner = new Scanner(System.in);\n        \n"
filecontents += "    }\n"
filecontents += "}\n"

if not simulate:
    javaFile.write(filecontents)
    javaFile.close()

if verbose or simulate:
    print(filecontents)

if not simulate:
    print(f"Successfully wrote to file {directory}{filename}.java")
