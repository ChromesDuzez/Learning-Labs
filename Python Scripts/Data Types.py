name = "Zach Wilson"
wealth = 120.25
numBankAccounts = 2
married = False

if(married):
    numBankAccounts = numBankAccounts / 2
    print(numBankAccounts)
elif((wealth > 100) and not(married)):
    print("Get Some Bitches")
else:
    print("Get Some Dinero " + name)

