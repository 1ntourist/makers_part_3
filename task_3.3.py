text = input("Введите цифры через пробел: ").split()
shift = int(input("Введите сдвиг: "))
chast1 = text[ : shift]
chast2 = text[shift : ]
fin = chast2 + chast1
super_fin = []
for i in fin:
    super_fin.append(int(i))
print("до сдвига: ", list(map(lambda x: int(x), text)))
print("после сдвига: ", super_fin)
