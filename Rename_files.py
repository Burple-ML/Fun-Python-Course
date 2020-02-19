import os 
def rename_files():
    # open the files in python
    file_names=os.listdir(r"/Users/raghav/Desktop/Udacity course/prank")
    print(file_names)
    saved_path=os.getcwd()
    print("*************this is the current working directory of the program************"+saved_path)
    
    # use the function to rename these files
    transition_table=str.maketrans("0123456789", "          ", "0123456789")
    os.chdir("/Users/raghav/Desktop/Udacity course/prank")
    for file_name in file_names:
        os.rename(file_name, file_name.translate(transition_table))
    os.chdir(saved_path)
    print("**************this is the current working directory of the program***************"+saved_path)
        
rename_files()
