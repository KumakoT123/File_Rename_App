#program
#!/usr/bin/env python
import os 
  
# Function to rename multiple files 
def main(): 

	print("Hello, input your folder directory and desired name separated by a space\n")

	print("Before you continue, make sure the files you wish to rename are all in a single folder without any other unnecessary files\n")

	print("To simplify the process, place this script where the desired folder can be found\n")

	print("E.g. MyFileDirectory MyFileName\n")

	dir, name = input("Your folder directory and desired file name: ").split()


	i = 0
      
	for filename in os.listdir(dir): 
		src = dir + "/" + filename
		dst = name + str(i) + "." + filename.split(".", 2)[1]
		dst = dir + "/" + dst
			
		# rename() function will 
		# rename all the files 
		os.rename(src, dst) 
		i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
	# Calling main() function 
	main()
