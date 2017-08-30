pessoas=["jailson", "jamelão", "guina"]
for peeplo in pessoas:
	print(peeplo.title()+", estude python")
print(peeplo.title()+", ótimo conselho")
#isso ocorre por que o python usa a identação para saber o que está dentro do for,
#como o segundo está fora, então ele não será repetido assim como o primeiro print, exibindo apenas o ultimo valor armazenado na variavel peeplo.

