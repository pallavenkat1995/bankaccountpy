class Account:
    def __init__(self, balance):
        if balance<0:
            self.balance=0.0
            print("intial balance was invalid")
        else:
            self.balance=balance
    def credit(self,camt):
        if camt<=0:
            print("camt can not be negative")
            return False
        else:
            self.balance=self.balance+camt
            return False
    def debit(self,damt):
        if damt>self.balance:
            print("deblit amount exceeded account balane")
            return False
        else:
            self.balance=self.balance-damt
            return True
    def getbalance(self):
        return self.balance
class SavingsAccount(Account):
    def __init__(self,balance,roi):
        super().__init__(balance)
        self.roi=roi
    def CalculateInterest(self):
        inter=(self.balance*self.roi)
        return inter
class CheckingAccount(Account):
    def __init__(self,balance,tf):
        super().__init__(balance)
        self.tf=tf
    def credit(self,camt):
        status=super().credit(camt)
        if status:
            self.balance=self.balance-self.tf
    def debit(self,damt):
        status=super().debit(damt)
        if status:
            self.balance=self.balance-self.tf
class CurrentAccount(Account):
    def __init__(self,balance,od):
        super().__init__(balance)
        self.od=od
    def debit(self,damt):
        if self.balance>damt:
            self.balance=self.balance-damt
        else:
            tw=self.balance+self.od
            if tw>=damt:
                self.balance=self.balance-damt
            else:
                print("over draft limit is exceeded")
ac1=Account(10000.00)
ac1.credit(5000)
ac1.debit(7000.00)
print(ac1.getbalance())
ac2=Account(-10000.00)
ac2.credit(5000.00)
ac2.debit(13000)
print(ac2.getbalance())
sa1=SavingsAccount(100000.00,12)
sa1.credit(70000)
sa1.debit(20000.00)
print(sa1.getbalance())
print(sa1.CalculateInterest())
ca1=CheckingAccount(100000.00,25.00)
ca1.credit(70000.00)
ca1.debit(20000)
print(ca1.getbalance())
cu1=CurrentAccount(100000.00,25000.00)
cu1.credit(75000.00)
print(cu1.getbalance())
cu1.debit(190000.00)
print(cu1.getbalance())