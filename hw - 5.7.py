import statistics
import json

rev = {}
aver_profit = []
end_file = []
with open(r"C:\Users\Asus\Desktop\text_7.txt", encoding="utf-8") as file_7:
    for line in file_7:
        firma, forma, profit, cost = line.split()
        my_list = line.split()
        pre_rev = int(profit) - int(cost)
        rev[firma] = pre_rev
        if pre_rev > 0:
            aver_profit.append(pre_rev)
    a_p = statistics.mean(aver_profit)
    my_dict = dict(average_profit=a_p)
    end_file = [rev, my_dict]
with open('file_7.json', 'w', encoding="utf-8") as write_js:
    json.dump(end_file, write_js)

    js_str = json.dumps(end_file)
    print(f'В файле с расширением json хранится: \n '
          f' {js_str}')
