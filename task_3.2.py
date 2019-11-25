text = input("Введите текст: ")
text = text.split()
text.sort(key=lambda x:len(x))
print(text)
