class bank:
    def __init__(self,name,acctno):
        self.name=name
        self.acctno=acctno
    def display(self):
        print("account details")
        print("---------")
        print("account holder name is:",self.name)
        print("accountnumber is:",self.acctno)
        print()
    def deposit(self,deposit):
        self.dp=deposit
        self.balance=self.dp+self.balance
        print("deposited sucessfully")
        print()
    def withdraw(self,w):
        if w<self.balance:
            self.balance-w
            print("amount is withdrawed")
        else:
            print("not enough amount")
    def balance(self):
        return self.balance



