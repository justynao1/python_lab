import os
def counter():
    directoryPath = r'/Users/macbook/desktop/studia_all'
    count = 0
    for path in os.listdir(directoryPath):
        if os.path.isfile(os.path.join(directoryPath, path)):
            count += 1
    print("The number of file is: ", count)