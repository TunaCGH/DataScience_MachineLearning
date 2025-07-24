'''
Pathlib is a module in Python that provides an object-oriented approach to handle filesystem paths. 
The `glob` method in the `pathlib` module allows you to search for files and directories matching a specified pattern.

Unlike the traditional `os` module, `pathlib` provides a more intuitive and readable way to work with paths.

Flow of contents:
1. Create Path object: PurePath, Concrete Path, Join Path slash /
2. Get current working directory and home directory: Path.cwd(), Path.home()
3. Extract path object components: name, suffix, stem, parent, parents, suffix, suffixes, parts, root
4. Checking path properties: exists(), is_file(), is_dir(), is_symlink(), is_absolute(), is_relative_to()
5. Get Absolute Path - Path Resolution: resolve(), absolute()
6. Directory and File operations: mkdir(), rmdir(), touch(), symlink_to(), 
                                  unlink() [remove a file or symlink],
                                  replace() [move and rename a file or directory] 
                                  
'''

from os import symlink
from loguru import logger
 
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------- 1. Create Path object: PurePath, Concrete Path, slash / --------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

################################################
## PurePath - PurePosixPath - PureWindowsPath ##
################################################

# PurePath classes represent a filesystem path without any actual file system operations.
# They are designed for purely computational operations on path strings, such as joining segments, extracting names, or changing extensions.
# They do not allow for any file system operations like reading or writing files, and other methods like .exists() or .is_file()

from pathlib import PurePath, PurePosixPath, PureWindowsPath


# Create a PurePath object using PurePath. It will automatically handle the path separator based on the operating system.
pure_path = PurePath('parent_dir', 'child_dir', 'example.txt') # Works like os.path.join()
print(pure_path) # parent_dir/child_dir/example.txt


# Create a PurePosixPath object for POSIX-style paths (Linux, macOS).
pure_posix_path = PurePosixPath('/home', 'user/documents', 'example.txt')
print(pure_posix_path)  # /home/user/documents/example.txt


# Create a PureWindowsPath object for Windows-style paths.
pure_windows_path = PureWindowsPath('C:\\', 'Users', 'User', 'Documents', 'example.txt')
print(pure_windows_path)  # C:\Users\User\Documents\example.txt


# Trying to perform file system operations on PurePath objects will raise an AttributeError.
try:
    pure_path.exists()
except Exception as e:
    logger.error(e) # | ERROR    | __main__:<module>:4 - 'PurePosixPath' object has no attribute 'exists'

else:
    print(pure_path.exists())


##################################
## Path - PosixPath WindowsPath ##
##################################

# Concrete Path classes represent actual filesystem paths and allow for file system operations.
# They inherit from PurePath and provide methods to interact with the file system, 
# such as reading and writing files, checking existence, and more.

from pathlib import Path, PosixPath, WindowsPath


# Create a Path object using Path. It will automatically handle the path separator based on the operating system.
path = Path('parent_dir', 'child_dir', 'example.txt')  # Works like os.path.join()
print(path)  # parent_dir/child_dir/example.txt


# Create a PosixPath object for POSIX-style paths (Linux, macOS).
posix_path = PosixPath('/home', 'user/documents', 'example.txt')
print(posix_path)  # /home/user/documents/example.txt


# Create a WindowsPath object for Windows-style paths (Raise error since this is Linux).
try:
    windows_path = WindowsPath('C:\\', 'Users', 'User', 'Documents', 'example.txt')
except Exception as e:
    logger.error(e) # | ERROR    | __main__:<module>:4 - cannot instantiate 'WindowsPath' on your system
else:
    print(windows_path)


# Trying to perform file system operations on Path objects will work as expected.
print(posix_path.exists()) # False
# It returns False, instead of raising an error like PurePath.


#####################################
## Using .joinpath() to join paths ##
#####################################

demo_path = Path('dir_1')

# The .joinpath() method allows you to join multiple path components together, similar to using the slash operator (/).
new_path = demo_path.joinpath('dir_2', 'dir_3', 'example.txt') # This does not modifiy the original path object (demo_path)

print(new_path)  # dir_1/dir_2/dir_3/example.txt


################################################
## Using the slash operator (/) to join paths ##
################################################

parent_path = Path('parent_dir')

# Using the slash operator (/) to join paths is a convenient way to create new paths.
child_path = parent_path / 'child_dir' / 'example.txt'

print(child_path)  # parent_dir/child_dir/example.txt)


#-----------------------------------------------------------------------------------------------------------------------#
#------------------------------ 2. Get current working directory and home directory ------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------#

from pathlib import Path

################
## Path.cwd() ##
################

# The Path.cwd() method returns the current working directory as a Path object. (like os.getcwd())
current_working_directory = Path.cwd()
print(current_working_directory) # /home/longdpt/Documents/Academic/DataScience_MachineLearning


#################
## Path.home() ##
#################

# The Path.home() method returns the home directory of the current user as a Path object. (like os.path.expanduser('~'))
home_directory = Path.home()
print(home_directory) # /home/longdpt


#-----------------------------------------------------------------------------------------------------------------------#
#--------------------------------------- 3. Extract path object components ---------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------#

from pathlib import Path

demo_file_path = Path('parent_dir/child_dir/example.txt')
demo_dir_path = Path("/home/longdpt/Documents/Academic/DataScience_MachineLearning/02_Python_class_OOP")


######################
## path_object.name ##
######################

# The path_object.name property returns the final component of the path, which is the file or directory name.

file_name = demo_file_path.name
print(file_name)  # example.txt

dir_name = demo_dir_path.name
print(dir_name)  # 02_Python_class_OOP


######################
## path_object.stem ##
######################

# The path_object.stem property returns the name of the file or directory without its suffix (extension).

file_stem = demo_file_path.stem
print(file_stem)  # example

dir_stem = demo_dir_path.stem
print(dir_stem)  # 02_Python_class_OOP


########################
## path_object.suffix ##
########################

# The path_object.suffix property returns the file extension (suffix) of the file or directory.

file_suffix = demo_file_path.suffix
print(file_suffix)  # .txt

dir_suffix = demo_dir_path.suffix
print(dir_suffix)  # (empty string, since directories don't have a suffix)


##########################
## path_object.suffixes ##
##########################

# The path_object.suffixes property returns a list of all suffixes (extensions) of the file or directory.

file_suffixes = demo_file_path.suffixes
print(file_suffixes)  # ['.txt']

file_suffixes = Path('example.tar.gz').suffixes
print(file_suffixes)  # ['.tar', '.gz'] (multiple suffixes)

dir_suffixes = demo_dir_path.suffixes
print(dir_suffixes)  # [] (empty list, since directories don't have suffixes)


########################
## path_object.parent ##
########################

# The path_object.parent property returns the parent directory of the file or directory.

file_parent = demo_file_path.parent
print(file_parent)  # parent_dir/child_dir
print(file_parent.parent)

dir_parent = demo_dir_path.parent
print(dir_parent)  # /home/longdpt/Documents/Academic/DataScience_MachineLearning
print(dir_parent.parent)  # /home/longdpt/Documents/Academic/


#########################
## path_object.parents ##
#########################

# The path_object.parents property returns a sequence of all parent directories of the file or directory.

file_parents = demo_file_path.parents
print(file_parents)  # <PosixPath.parents>
print(list(file_parents))  # [PosixPath('parent_dir/child_dir'), PosixPath('parent_dir'), PosixPath('.')]

dir_parents = demo_dir_path.parents
print(dir_parents)  # <PosixPath.parents>
print(list(dir_parents))  # [PosixPath('/home/longdpt/Documents/Academic/DataScience_MachineLearning'), PosixPath('/home/longdpt/Documents/Academic'), PosixPath('/home/longdpt/Documents'), PosixPath('/home/longdpt'), PosixPath('/home'), PosixPath('/')]


#######################
## path_object.parts ##
#######################

# The path_object.parts property returns a tuple of all components (parts) of the path.

file_parts = demo_file_path.parts
print(file_parts)  # ('parent_dir', 'child_dir', 'example.txt')

dir_parts = demo_dir_path.parts
print(dir_parts)  # ('/', 'home', 'longdpt', 'Documents', 'Academic', 'DataScience_MachineLearning', '02_Python_class_OOP')


######################
## path_object.root ##
######################

# The path_object.root property returns the root of the path, which is the top-level directory in the file system.

file_root = demo_file_path.root
print(file_root)  # (empty string, since the file path is relative)

dir_root = demo_dir_path.root
print(dir_root)  # / (the root directory of the file system)


#------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------- 4. Checking path properties -----------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#

from pathlib import Path

demo_file_path = Path('parent_dir/child_dir/example.txt')
exist_file_path = Path('Python_Important_packages.txt')

demo_dir_path = Path("parent_dir/child_dir/subchild_dir")
exist_dir_path = Path("/home/longdpt/Documents/Academic/DataScience_MachineLearning/02_Python_class_OOP")


##########################
## path_object.exists() ##
##########################

# The path_object.exists() method checks if the file or directory exists in the file system.

print(demo_file_path.exists())  # False

print(exist_dir_path.exists())  # True


###########################
## path_object.is_file() ##
###########################

# The path_object.is_file() method checks if the path points to a file (not a directory).

print(demo_file_path.is_file())  # False (since the file does not exist)

print(exist_file_path.is_file())  # True

print(exist_dir_path.is_file())  # False (since it's a directory)


##########################
## path_object.is_dir() ##
##########################

# The path_object.is_dir() method checks if the path points to a directory (not a file).

print(demo_dir_path.is_dir())  # False (since the directory does not exist)

print(exist_dir_path.is_dir())  # True

print(exist_file_path.is_dir())  # False (since it's a file)


##############################
## path_object.is_symlink() ##
##############################

demo_symlink_path = Path('parent_dir/child_dir/symlink_fake')
exist_symlink_path = Path('/home/longdpt/lmstudio/lmstudio_exe')

# The path_object.is_symlink() method checks if the path is a symbolic link.
# Note: This will return False if the path does not exist.

print(demo_symlink_path.is_symlink())  # False (since the symlink does not exist)

print(exist_symlink_path.is_symlink())  # True

print(exist_file_path.is_symlink())  # False (since it's a file)


###############################
## path_object.is_absolute() ##
###############################

# The path_object.is_absolute() method checks if the path is an absolute path (starts from the root directory).

print(exist_file_path.is_absolute())  # False (since it's a relative path)

print(exist_dir_path.is_absolute())  # True (since it's an absolute path)


##################################
## path_object.is_relative_to() ##
##################################

# The path_object.is_relative_to() method checks if the path is relative to another path.

print(demo_file_path.is_relative_to('parent_dir'))  # True (since it's relative to 'parent_dir')

print(exist_dir_path.is_relative_to('/home/longdpt/Documents/Academic/'))  # True (since it's relative to the specified path)

print(demo_dir_path.is_relative_to('/home/longdpt/'))  # False (since it's not relative to the specified path)


#------------------------------------------------------------------------------------------------------------------------#
#------------------------------------- 5. Get Absolute Path - Path Resolution -------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#

from pathlib import Path

demo_relative_path_1 = Path("02_Python_class_OOP")
demo_relative_path_2 = Path("DataScience_MachineLearning/02_Python_class_OOP")

symlink_path = Path('/home/longdpt/lmstudio/lmstudio_exe')


###########################
## path_object.resolve() ##
###########################

# The path_object.resolve() method returns the absolute path of the file or directory, 
# It also resolves any symbolic links and relative paths.
''' Note: If the path does not exist, it will raise a FileNotFoundError.'''


absolute_path = demo_relative_path_1.resolve()
print(absolute_path)  
# /home/longdpt/Documents/Academic/DataScience_MachineLearning/02_Python_class_OOP

absolute_path_alternative = demo_relative_path_2.resolve()
print(absolute_path_alternative)
# /home/longdpt/Documents/Academic/DataScience_MachineLearning/DataScience_MachineLearning/02_Python_class_OOP
''' 
>> Note: there is a duplication of the path => this is because the path is relative to the current working directory,
>> and the current working directory is already inside the 'DataScience_MachineLearning' directory.
'''

absolute_symlink_path = symlink_path.resolve()
print(absolute_symlink_path)
# /home/longdpt/lmstudio/LM-Studio-0.3.17-11-x64.AppImage
# (The actual path of the symlink target is resolved)


############################
## path_object.absolute() ##
############################

# The path_object.absolute() method returns the absolute path of the file or directory,
# but it does not resolve symbolic links or relative paths.

absolute_path_alternative = demo_relative_path_1.absolute()
print(absolute_path_alternative)
# /home/longdpt/Documents/Academic/DataScience_MachineLearning/02_Python_class_OOP

absolute_symlink_path = symlink_path.absolute()
print(absolute_symlink_path)
# /home/longdpt/lmstudio/lmstudio_exe

'''
############################################################################################################
## NOTE: they get the absolute path from the current working directory, not the real actual absolute path ##
############################################################################################################
'''

relative_symlink_path = Path('lmstudio_exe')

print(relative_symlink_path.resolve())  # /home/longdpt/Documents/Academic/DataScience_MachineLearning/lmstudio_exe
print(relative_symlink_path.absolute())  # /home/longdpt/Documents/Academic/DataScience_MachineLearning/lmstudio_exe

'''
>> Note: the absolute path is not the actual absolute path of the symlink target, 
>> but rather the absolute path from the current working directory to the symlink itself.
'''

#------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------- 6. Directory and File operations ----------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#

from pathlib import Path

######################################
## mkdir() - Create a new directory ##
######################################

# mkdir() basic use
data_dir = Path('./data')
data_dir.mkdir(exist_ok = True)  # Create 'data' directory (at existed parent dir) like os.mkdir()
                                 # Don't fail if exists


# mkdir() with joinpath()
Path('/home/longdpt/Documents/Academic/DataScience_MachineLearning/').joinpath('new_dir').mkdir(exist_ok=True)
# Add "new_dir" to the path with .joinpath() method
# Then use .mkdir() to create the directory at the specified path


# mkdir() with parents=True like os.makedirs()
data_dir_with_parents = Path('./data/subdir')
data_dir_with_parents.mkdir(parents=True, exist_ok=True) # Don't fail if exists, and create all parent


# Create a structured directory
project_structure = [
    'project/data/raw',
    'project/data/processed', 
    'project/data/external',
    'project/models/trained',
    'project/models/checkpoints',
    'project/notebooks/exploratory',
    'project/notebooks/modeling',
    'project/results/figures',
    'project/results/metrics'
]

for path_str in project_structure:
    Path(path_str).mkdir(parents=True, exist_ok=True)


'''
WRONG USAGE: 
   Path.cwd().mkdir('new_dir')
   >>> Create nothing
'''


#########################################
## rmdir() - Remove an empty directory ##
#########################################

project_path = Path('./project')

# Remove an empty directory (./project/data/raw) [RECOMMENDED]
Path(project_path / 'data').joinpath('raw').rmdir()

# Remove an empty directory (./project/data/raw) [NOT RECOMMENDED]
Path(project_path / 'data' / 'raw').rmdir()

project_path.rmdir() # Raise error


############################################
## shutil.rmtree() - Remove non-empty dir ##
############################################

# To remove a non-empty dir with all its contents, use shutil.rmtree()

import shutil
shutil.rmtree(project_path)


#######################################################
## touch() - Create new file in a specific directory ##
#######################################################

path_cwd = Path.cwd()
print(path_cwd)  # /home/longdpt/Documents/Academic/DataScience_MachineLearning

# Create a new file in the current working directory
path_cwd.joinpath('demo_file.txt').touch(exist_ok=True)  # Add "demo_file.txt" to the path_cwd
                                                         # then use .touch() to create the file

'''
WRONG USAGE: 
    path_cwd.touch('demo_file.txt')
    >>> Create nothing
'''

#####################################################
## symlink_to() - Create a symbolic link to a file ##
#####################################################

# symlink_to() creates a symbolic link to a file or directory.


# Create a symbolic link to the demo_file.txt
symlink_target = Path('demo_file.txt')
symlink_path = Path('demo_symlink.txt')

symlink_path.symlink_to(symlink_target, target_is_directory=False)  # Create a symlink to the file
print(symlink_path.is_symlink())  # True


# Create a symbolic link to a directory
dir_symlink_target = Path('data/raw')
dir_symlink_path = Path('data_raw_symlink')

dir_symlink_path.symlink_to(dir_symlink_target, target_is_directory=True)  # Create a symlink to the directory
print(dir_symlink_path.is_symlink())  # True


'''
NOTE: even if the target file or directory does not exist,
the symlink will still be created, but it will be broken (pointing to a non-existent target).
'''


#######################################
## unlink() - REMOVE FILE or SYMLINK ##
#######################################

# unlink() removes a file or a symbolic link. (like os.remove())


# Remove a file
Path.cwd().joinpath('demo_file.txt').unlink(missing_ok=True)  # Remove the file if it exists
                                                              # Don't raise an error if the file does not exist


# Remove a symbolic link to a file
symlink_path = Path('./demo_symlink.txt')
symlink_path.unlink(missing_ok=True)  # Remove the symlink if it exists
                                      # Don't raise an error if the symlink does not exist


# Remove a symbolic link to a directory
dir_symlink_path = Path('./data_raw_symlink')
dir_symlink_path.unlink(missing_ok=True)  # Remove the symlink if it exists
                                          # Don't raise an error if the symlink does not exist


#####################################################
## replace() - MOVE and RENAME a file or directory ##
#####################################################

#--------------------------
## Rename with replace()
#--------------------------

Path.cwd().joinpath('demo_file.txt').touch(exist_ok=True)  # Create a file to rename
Path.cwd().joinpath('demo_dir').mkdir(exist_ok=True)  # Create a directory to rename

# Rename a file
Path('./demo_file.txt').replace('renamed_file.txt')  # Rename the file to 'renamed_file.txt'
Path.cwd().joinpath('demo_file.txt').replace('renamed_file.txt')  # Rename the file to 'renamed_file.txt' using joinpath()

# Rename a directory
Path('./demo_dir').replace('renamed_dir')  # Rename the directory to 'renamed_dir'
Path.cwd().joinpath('demo_dir').replace('renamed_dir')  # Rename the directory to 'renamed_dir' using joinpath()

