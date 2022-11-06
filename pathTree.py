path = "/Users/macbook/desktop/studia_all/DHLOOS"
def tree(path):
    dir_list = os.listdir(os.path.expanduser(path))
    print("Directory: " + path)
    print(dir_list)
    print("------")
    for i in dir_list:
        if os.path.isdir(i):
            i = path + "/" + str(i)
            tree(i)
