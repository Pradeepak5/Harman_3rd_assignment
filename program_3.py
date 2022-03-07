def palindromefun(word):
    return word[::-1]


a=str(input("Type Something :"))
result=palindromefun(a)
print(result)

if a==result:
    print("It is palindrome")
else:
    print("It is not a palindrome")
