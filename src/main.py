from datetime import datetime
from customer import Customer
from account import Account
from transaction import Transaction
from transfer import Transfer

bob = Customer("BOB", "232.453.233-10")
nubank = Account("Nubank", "43434", bob)
nubank.deposit(1000, 'Saldo Inicial')

mary = Customer("MARY", "434.343.232-10")
inter = Account("Inter", "34434", mary)
inter.deposit(2000, 'Saldo Inicial')

inter.withdraw(1200.50, "Aluguel apto")

nubank.transfer("Curso Ingles prof Mary", inter, 200.50)
nubank.withdraw(122.32, "Pagando conta de Luz")

print(f"O saldo de {bob.name} na conta {nubank.name} é de {nubank.balance:.2f}")
print(f"O saldo de {mary.name} na conta {inter.name} é de {inter.balance:.2f}")
