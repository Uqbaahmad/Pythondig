import os

if not os.path.exists('data analysis'):
    os.mkdir("data analysis")

print("The current location")
print(os.getcwd())    


print("The current directory content")
content = os.listdir()
print(content)

if os.path.isdir('data analysis'):                            # (isdir) directory means folder
    print('data analysis is a directory')

if os.path.isfile('set.ipynb'):
    print('set.ipynb is a file')

print('size of file', os.path.getsize('list.ipynb')/(1024 * 1024), 'MB')    