print('Привет, спортсмен! Напиши со скольких километров ты стартуешь')
start = float(input())
print('Это хорошее начало!Теперь напиши сколько км твоя конечная цель')
goal = float(input())
goal_days = 1
while goal > start:
    start = start + 0.1*start
    goal_days += 1
print(f'Вы достигните желаемого километража через {goal_days} дней')