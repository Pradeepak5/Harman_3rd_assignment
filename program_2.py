word=str(input("Write  something :"))
word_len=len(word)
print(word_len)

file=open("data.txt","w")
data=file.write(str(word_len))