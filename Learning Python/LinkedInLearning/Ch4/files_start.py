#
# Read and write files using the built-in Python file methods
#

def main():  
    # Open a file for writing and create it if it doesn't exist
    #f = open("textfile2.txt", "w+")
    
    # Open the file for appending text to the end
    f = open("textfile2.txt", "r")
    
    # write some lines of data to the file
    #for i in range(10):
        #f.write("These are the appended lines " + str(i) + "\r\n")
    
    # close the file when done
    #f.close()
    
    # Open the file back up and read the contents
    #===========================================================================
    # if f.mode == 'r':
    #     contents = f.read()
    #     print(contents)
    #===========================================================================
    
    #read the contents of the file line by line
    if f.mode == 'r':
        fl = f.readlines()
        
    for x in fl:
        print(x)
    
if __name__ == "__main__":
    main()
