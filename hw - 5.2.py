with open("my_file_5(1-2).txt", 'r', encoding="utf-8") as file_1:
    lines = 0
    words = 0
    for line in file_1:
        new_list = line.split()
        words = len(line.split())
        lines += 1
        print(f"В строке под номером {lines} содержится {words} слова  ")
