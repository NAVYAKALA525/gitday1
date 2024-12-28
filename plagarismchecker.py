from difflib import SequenceMatcher

with open("1.txt","r",encoding="UTF-8") as file1 , open("2.txt","r",encoding="UTF-8") as file2:
    f1data =file1.read()
    f2data =file2.read()
    percentage = SequenceMatcher(None,f1data,f2data,autojunk=True).ratio()
    print("Similarity of two text files:",round(percentage * 100),"%")