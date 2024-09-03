# class Invoice:
#     def __init__(self, number):
#         self._number = number
#         self._items = []

#     def add_items(self, item):
#         self._items.append(item)

# def total(self):
#     t = 0
#     for item in self._items:
#         t += item.total()
#     return t

# class FeeItem:
#     def __init__(self, rate, amount, description):
#         self._rate = rate
#         self._amount = amount
#         self._description = description

#     def total(self):
#         return self._rate * self._amount


# class ExpensesItem:
#     def __init__(self, amount, description):
#         self._amount = amount
#         self._description = description

#     def total(self):
#         return self._amount


# invoice = Invoice('A32345')
# fee =   FeeItem(100, 1.5, 'phone conversation')
# expense = ExpensesItem(200, 'Copies')

# print(invoice)
# print(fee.total())
# print(expense.total())

# invoice.add_items(fee)
# invoice.add_items(expense)
# print(invoice.total())   

# use_triple = """ multi
# \\line
# string"""
# print(use_triple)

# import random

# print(random.choice([30, 40, 50, 60, 70, 80], 4))

# y = 7
# z = 7

# print(y,z)

def numbers(x):
    return 10 * x

print(numbers(5))
print(numbers(5))
print(numbers(5))