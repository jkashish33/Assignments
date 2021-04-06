file1 = open ("doc.txt", "w")
L = ["Hello I am a file \n","Where you need to return the data string \n","Which is of even length \n"]
file1.writelines(L)
file1.close()
file1 = open("doc.txt", "r+")
text = file1.readlines()
words = []
for line in text:
    words += line.split(" ")
    words.remove("\n")
even_len_string = []
for i in words:
    if len(i) % 2 == 0:
        even_len_string.append(i)
# print(even_len_string)
listToStr = ' '.join([str(elem) for elem in even_len_string])
# print(listToStr)
file1.close()
with open("doc.txt", "a") as document1:
    f = ["Even length string is : \n",listToStr]
    document1.writelines(f)