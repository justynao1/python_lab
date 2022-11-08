# usuwanie słów
"""
def deleteWords():
    # text = r'/Users/macbook/downloads/text_files/italy/Amber.txt'
    with open('/Users/macbook/downloads/text_files/italy/Amidah.txt', 'r') as file:
        new_text = '/Users/macbook/downloads/text_files/italy/Amidah.txt'.replace('is', "")
        file.write(new_text)
        print(new_text)
"""

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
