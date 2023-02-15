import os

file_name = '\\' + 'username' '.txt'
#Where the files will be stores, this will change ignore this
os.chdir('.\\')
file_path_finder = os.getcwd()
location = file_path_finder + "\\users" + file_name

print(location)