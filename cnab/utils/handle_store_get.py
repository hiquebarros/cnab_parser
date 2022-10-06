from cnab.models import Transaction

def getTransactions(name):
    queryset = Transaction.objects.filter(name=name)
    return queryset

def getBalance(name):
    balance = 0
    result = Transaction.objects.filter(name=name)
    for transaction in result:
        if transaction.type == 2 or transaction.type == 3 or transaction.type == 9:
            balance -= int(float(transaction.value))
        else:        
            balance += int(float(transaction.value))

    return balance