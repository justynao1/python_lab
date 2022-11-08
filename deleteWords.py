# usuwanie słów

def deleteWords():
    file1 = "/Users/macbook/downloads/text_files/france/London.txt"
    file2 = "/Users/macbook/downloads/text_files/france/empty_file.txt"
    deleteList = ["and", "or", "is"]
    fin = open(file1)
    fout = open(file2, "w+")
    for i in fin:
        for j in deleteList:
            i = i.replace(j, "")
        fout.write(i)
    fin.close()
    fout.close()


deleteWords()
