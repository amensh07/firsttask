words = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
my_new_text = open("my_new_text.txt", 'w', encoding="utf-8")
with open(r"C:\Users\Asus\Desktop\text_4.txt", encoding="utf-8") as file_4:
    text = file_4.read()
    for line in text.split("\n"):
        key, value = line.split(' -')
        for i in words.keys():
            if key == i:
                text = text.replace(key, words.get(i))
    my_new_text.write(text)
    my_new_text.close()
my_new_text_to_read = open("my_new_text.txt", 'r', encoding="utf-8")
print(my_new_text_to_read.read())
