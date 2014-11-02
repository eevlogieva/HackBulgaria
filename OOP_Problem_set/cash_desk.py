class CashDesk():
    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, notes):
        for note in notes:
            self.money[note] += notes[note]

    def total(self):
        total = 0
        for note in self.money:
            total += self.money[note] * note
        return total

    def can_withdraw_money(self, amount_of_money):
        money_lst = []
        copy_money = (self.money).copy()
        for note in copy_money:
            while copy_money[note] > 0:
                money_lst.append(note)
                copy_money[note] -= 1
        lst = sorted(money_lst)[::-1]
        for item in lst:
            if item <= amount_of_money:
                amount_of_money -= item
        return amount_of_money == 0
