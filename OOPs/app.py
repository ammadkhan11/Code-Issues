class Account:
    def __init__(self, balance, account_no):
        self.balance=balance
        self.account_no=account_no
    
    def debit(self, amount):
        self.balance=self.balance-amount
        print("Your Remaining Balance is: ",self.balance)

    def credit(self, amount):
        self.balance=self.balance+amount
        print("Your Remaining Balance is: ",self.balance)

    def balance_print(self):
        print("Your Balance is: ",self.balance)

acc1=Account(20000, 201108)
acc2=Account(300082,2309876)

acc1.debit(1000)
acc2.credit(87000)
acc2.balance_print()



# class Student:
#     def __init__(self, name,marks):
#         self.name=name
#         self.marks=marks

#     def average(self):
#         return statistics.mean(self.marks)
    
# s1=Student("Ammad", [92, 31, 45])
# print("The average marks of",s1.name, "are", s1.average())
