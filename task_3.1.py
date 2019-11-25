text = [i for i in input("Введите текст: ") if i.isalnum() and not i.isnumeric()]
big = [i for i in text if i.isupper()]
low = [i for i in text if i.islower()]
print("Процент заглавных букв:", 100 / len(text) * len(big))
print("Процент прописных букв:", 100 / len(text) * len(low))
