# Створення файлу TF23_1
with open("TF23_1.txt", "w") as file1:
    file1.write("1010101101\n")
    file1.write("1110010101010\n")
    file1.write("0010011\n")
    file1.write("1001010101110101010\n")

# Читання вмісту TF23_1, заміна 1 на 0
with open("TF23_1.txt", "r") as file1, open("TF23_2.txt", "w") as file2:
    content = file1.read()  # Зчитуємо весь вміст файла
    modified_content = content.replace("1", "x").replace("0", "1").replace("x", "0")  # Заміна символів

    for i in range(0, len(modified_content), 15):
        file2.write(modified_content[i:i + 15] + "\n")

# Читання та друк вмісту TF23_2
with open("TF23_2.txt", "r") as file2:
    for line in file2:
        print(line.strip())
