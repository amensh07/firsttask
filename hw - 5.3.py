import statistics

with open(r"C:\Users\Asus\Desktop\text_3.txt", encoding="utf-8") as file_3:
    salary_list = []
    for line in file_3:
        name, salary = line.split()
        salary = float(salary)
        salary_list.append(salary)
        if salary < 20000:
            print(name)
    print(statistics.mean(salary_list))
