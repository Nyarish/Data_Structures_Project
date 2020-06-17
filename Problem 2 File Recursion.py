import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    if suffix == "":
        return []
    if len(os.listdir(path)) == 0:
        return []
    
    path_items = os.listdir(path)
    path_files = [file for file in path_items if ("." + suffix) in file]
    path_folders = [folder for folder in path_items if "." not in folder]
    
    for folder in path_folders:
        path_files.extend(find_files(suffix=suffix, path=path + '/' + folder))
        
    return path_files



# Tests
path_base = os.getcwd() + '/testdir'

# Testcase 1
print(find_files(suffix='c', path=path_base))

# Testscase 2
print(find_files(suffix='h', path=path_base))


# Testcase 3
print(find_files(suffix='gitkeep', path=path_base))


# Testcase 4
print(find_files(suffix='x', path=path_base))



"""OUTPUT
['t1.c', 'b.c', 'a.c', 'a.c']
['t1.h', 'b.h', 'a.h', 'a.h']
['.gitkeep', '.gitkeep']
[]

"""




