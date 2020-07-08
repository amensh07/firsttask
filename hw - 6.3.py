class Worker:
    def metod(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Possition(Worker):

    def get_full_name(self):
        return ' '.join([self.name, self.surname, self.position])

    def get_total_income(self):
        total_profit = self._income.get('wage') + self._income.get('bonus')
        return f'Ее зарплата + бонусы : {total_profit}'


result = Possition()
result.metod('Настя', 'Меньшова', 'Студент', 100, 10)
print(result.get_full_name())
print(result.get_total_income())
