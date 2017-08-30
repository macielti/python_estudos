list_user_ban=["Lucinauro", "Jorel", "Irineu"]
user="Bruno"
if user not in list_user_ban:
    print("você já pode enviar sua resposta agora")
#o not vai negar o resultado da verificação do in. Sem o not o resultado seria falso e o print não seria executado.
#com o not negamos o resultado falso. A negação de falso resulta em verdade, logo o if é executado;