import os

# folder path
dir_path = r'C:\Users\FX505DT\Desktop'
count = 1
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('File count:', count)

### I must add subfolders count
### Show space occupied

def getfilesize (filename):
    return os.stat(filename).st_size
size = getfilesize('C:/Users/FX505DT/Desktop')
print(f'FileSize: {size}')