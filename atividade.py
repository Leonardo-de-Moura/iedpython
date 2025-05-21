dados = []

while True:
	nome= input("digite seu nome")
	idade= input("digite sua idade")
	carro= input("digite seu carro")

	pessoa= { 
			"id": len(dados) + 1,
			"nome": nome,
			"idade": idade,
			"endereco": carro}
	dados.append(pessoa)
	print("pessoa adicionada a lista")
	print("lista atual:", dados)
	print()