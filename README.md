# Build Tags

## Usage
usage: build_tags.py [-h] -f FILE -t TAG [-v] {add,remove} ...

### positional arguments:
  *{add,remove}* 

### optional arguments:

| Argument | Description |
| -------- | ----------: |
| -h, --help | show help message and exit |
| -f, --file FILE | file to edit |
| -t, --tag TAG | the tag to operate on |
| -v, --verbose | enable debug statements |

## Sample Usage

Imagine a file titled **example.txt** containing:  
*This is a line*

### Add text
After calling the following line:

`python build_tags.py -f example.txt -t OROV add --text "Hello world/nHow are you"`

**example.txt** would contain:

*This is a line*  
*OROV_START*  
*Hello world*  
*How are you*  
*OROV_END*

### Remove text
Now, let's say we use the above **example.txt** and apend the line:  
*This is another line*  

**example.txt** would contain:

*This is a line*  
*OROV_START*  
*Hello world*  
*How are you*  
*OROV_END*  
*This is another line*

To remove the code block, call:

`python build_tags.py -f example.txt -t OROV remove`

**example.txt** would now contain:  

*This is a line*  
*This is another line*
