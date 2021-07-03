# Reading and writing files

## Check current directory
Path.cwd()

## Using the / Operator to Join Paths
Path('spam') / 'bacon' / 'eggs'

Python evaluates the / operator from left to right and evaluates to a Path object, so either the first or second leftmost value must be a Path object for the entire expression to evaluate to a Path object. Here’s how the / operator and a Path object evaluate to the final Path object.

## Change directory
 os.chdir('C:/ThisFolderDoesNotExist')

## Home directory
Path.home()

## Parts of the path
The parts of a file path include the following:

- The anchor, which is the root folder of the filesystem
On Windows, the drive, which is the single letter that often denotes a physical hard drive or other storage device
- The parent, which is the folder that contains the file
- The name of the file, made up of the stem (or base name) and the suffix (or extension)

> p = Path('C:\\Users\\khoi.nguyena\\Desktop\\test_folder\\hello.txt')
> path.anchor() -- Geting the drive name


