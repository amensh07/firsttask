hours = {}
with open(r"C:\Users\Asus\Desktop\text_6.txt", encoding="utf-8") as file_6:
    for line in file_6:
        new_line = line.replace('-', '0')
        new_line = new_line.replace('(пр)', '')
        new_line = new_line.replace('(л)', '')
        new_line = new_line.replace('(лаб)', '')
        sub, lec, prac, lab = new_line.split()
        print(new_line.split())
        hours[sub] = int(lec) + int(prac) + int(lab)
print(f'Общее количество часов по предмету - \n {hours}')
