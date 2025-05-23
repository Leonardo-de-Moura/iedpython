dados = []
dadostransporte= []

while True:
	ask= input("quer adicionar? [S/N]")
	if ask=="S":
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
	else: 
		break

ask= input("tem transporte?[S/N]")
if ask== "N":
	nome= input("digite seu nome")
	idade= input("digite sua idade")
	pessoa= { 
	"id": len(dadostransporte) + 1,
		"nome": nome,
		"idade": idade,
		"endereco": carro}
	dadostransporte.append(pessoa)
	print("pessoa adicionada a lista")
	print("lista atual:", dadostransporte)
	print()
else:
	print("ja que tem transporte, nao e necessario adicona-lo a lista")