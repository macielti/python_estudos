idade=12
if idade < 4:
    print("não paga para entrar no parque.")
elif idade < 18:
    print("paga 5 reais para entrar no parque.")
else:
    print("paga 10 reais para entrar no parque.")
# a mensagem do if só será exibida se a idade for menor que 4, ela é maior, logo essa condição é falsa e não será
# executada.
# a mensagem do elif é exibida se o if for falso e se a condição do elif for verdadeira.
# a mensagem do else será executado se o elif resultar em falso.