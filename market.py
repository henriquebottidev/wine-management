# Exibir o menu principal
def menu():
    print(" =========================================================")
    print(" ****** Bem Vindo Ao Sistema De Vinhos Winy **************")
    print(" =========================================================")
    print("Escolha uma opção:\n [1]- Adicionar Vinhos\n [2]- Remover Vinhos\n [3]- Consultar Vinhos\n [4]- Adicionar distribuidores\n [5]- Recomendações de vinho\n [6]- Sair")

# Função para adicionar vinhos
def addWine():

# Função para remover vinhos
def removeWine():

# Função para encontrar vinhos
def findWine():

# Função para adicionar distribuidores de vinho
def addDistribuitors():

# Função para recomendação de vinhos 
def wineRecommendations():

# Função principal que controla o sistema
def main():
    online = True

    while online:
        menu() # Exibe o menu, invocando a função. 
        user = input('Digite um número: ')

        match user:
            case '1':
                addWine()

            case '2':
                removeWine()
            
            case '3':
                findWine()

            case '4': 
                addDistribuitors()

            case '5':
                wineRecommendations()
            
            case '6': 
                print('Saindo do Sistema!')
                online = False
            
            case _:
                print('Opção Inválida: Tente novamente!')

#Executar programa
main()


        
