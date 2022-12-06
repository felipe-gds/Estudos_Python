### Operador tenário

login = True
msg = "Logado" if login else "não logado"
print(msg)

saque = 2000
autorizar_saque = (saque <= 10000)
msg2 = "Saque autorizado" if autorizar_saque else "Saldo insuficiente"
print(msg2)