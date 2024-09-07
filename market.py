# Função para adicionar vinhos
wines = []
dist_list = []

# Exibir o menu principal
def menu():
    print(" =========================================================")
    print(" ****** Bem Vindo Ao Sistema De Vinhos Winy **************")
    print(" =========================================================")
    print("Escolha uma opção:\n [1]- Adicionar Vinhos\n [2]- Remover Vinhos\n [3]- Consultar Vinhos\n [4]- Adicionar distribuidores\n [5]- Consultar Distribuidores\n [6]- Recomendações de vinho\n [7]- Sair")

# Função para adicionar vinhos
def addWine():
    global wines
    active = True

    while active:
        print(" =========================================================")
        print("Para voltar digite 'voltar' ---- Para cadastrar vinhos é só digitar")

        wine_entry = {}

        nome = input("Digite o nome do vinho: ")

        if nome.lower() == "voltar":
            active = False 
            break

        ano = input('Digite o ano do vinho: ')
        regiao = input('Digite a região do vinho: ')
        uva = input('Digite o nome da uva: ')

        wine_entry['Nome'] = nome.title()
        wine_entry['Ano'] = ano 
        wine_entry['Região'] = regiao.title()
        wine_entry['Uva'] = uva.title()

        wines.append(wine_entry)
        print(wines)
    
    return wines

def findWine():
    global wines

    found = False

    print("Para voltar digite 'voltar' ---- Para cadastrar vinhos é só digitar")

    key = input('Encontre um vinho pelo Nome, Ano, Região ou Uva: ')

    for wine in wines:
        if(key in wine['Nome'] or
           key in wine['Ano'] or 
           key in wine['Região'] or 
           key in wine['Uva']):
            print(' ========= Encontrado =========')
            print(f"Vinho: {wine["Nome"]}")
            print(f"Ano: {wine["Ano"]}")
            print(f"Região: {wine["Região"]}")
            print(f"Uva: {wine["Uva"]}")
            print('------')
            found = True 
        
        if not found:
            print("Nenhum Vinho Encontrado") 

def removeWine():
    global wines

    print(wines)
    key = input('Remova um vinho pelo Nome: ')

    removed = False 

    for wine in wines:
        if(key in wine['Nome']):
            wines.remove(wine)
            print(" ============================")
            print(f"{wine['Nome']} Foi Removido!")
            print(" ============================")
            removed = True 
            break

        if not removed:
            print('No wine to be removed.')

def wineRecommendations():

    global wines

    wine_recommendations = [
    {
        'Evento': 'Jantar de família',
        'Comida': 'Carne com massa',
        'Recomendação de Vinho': wines[0]
    },
    {
        'Evento': 'Jantar romântico',
        'Comida': 'Massa com molho branco',
        'Recomendação de Vinho': wines[0]
    },
    {
        'Evento': 'Jantar de negócios',
        'Comida': 'Filé mignon ao molho de pimenta',
        'Recomendação de Vinho': wines[0]
    },
    ]

    found = False 

    print(" =========== BEM VINDO: Recomendações de Vinho =================")
    user_event = input("==== Qual é a ocasião?: ")
    user_food = input("==== Qual é o estilo gastrônomico?: ")

    for recommendations in wine_recommendations:
        if(user_event in recommendations['Evento'] or
           user_food in recommendations['Comida']):
            print(f"\nMelhor Vinho: {recommendations['Recomendação de Vinho']}")
            found = True 
        
    if not found:
        print("There is no wine recommendations")

def addDistribuitors():
    global dist_list 
    dist = {}

    print

    dist_name = input("Digite 'voltar' para ir ao menu -----\nOu continue digitando o nome do distribuidor\n: ")

    if dist_name.lower() == 'voltar':
        return

    # nome, cpf , telefone

    dist_cpf = input('Digite o cpf do fornecedor: ')
    dist_tel = input('Digite o telefone do fornecedor: ')

    dist['Nome'] = dist_name.title()
    dist['Cpf'] = dist_cpf
    dist['Tel'] = dist_tel

    dist_list.append(dist)
    print(dist_list)

def findDistribuitors():
    global dist_list
    print(dist_list)


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
                findDistribuitors()

            case '6':
                wineRecommendations()
            
            case '7': 
                print('Saindo do Sistema!')
                online = False
            
            case _:
                print('Opção Inválida: Tente novamente!')

#Executar programa
main()


        
