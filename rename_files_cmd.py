#
#!/usr/bin/env python
import os 

print("Hello, input your folder directory and desired name separated by a space")
print("Before you type anything, make sure the files you wish to rename are all in a single folder without any other unnecessary files")
print("E.g. /Documents Text")

dir, name = input("Your folder directory and file name:").split()
  
# Function to rename multiple files 
def main(): 
    i = 0
      
    for filename in os.listdir("xyz"): 
        dst ="Hostel" + str(i) + ".jpg"
        src ='xyz'+ filename
        dst ='xyz'+ dst
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 