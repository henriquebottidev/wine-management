# Winy - Sistema de Gestão para Vinícolas

Bem-vindo ao **Winy**, uma solução completa para vinícolas gerenciarem seu portfólio de vinhos, distribuidores e oferecerem recomendações personalizadas para seus clientes. O sistema foi desenvolvido com o objetivo de fornecer uma interface intuitiva e eficiente para os produtores de vinho. Desde o cadastro e consulta de vinhos até a criação de recomendações detalhadas para diferentes ocasiões, **Winy** oferece uma plataforma robusta e personalizada para o gerenciamento de vinícolas.

## Funcionalidades

### 1. Cadastro de Vinhos
Os usuários podem adicionar vinhos ao sistema fornecendo detalhes importantes, como:
- **Nome do vinho**: O nome comercial do vinho.
- **Ano**: O ano de produção.
- **Região**: A região onde o vinho foi produzido.
- **Uva**: A principal variedade de uva utilizada.

Cada vinho é armazenado em uma lista global, permitindo fácil gerenciamento e acesso futuro.

### 2. Remoção de Vinhos
As vinícolas têm a opção de remover vinhos cadastrados no sistema com base no nome. O sistema lista os vinhos cadastrados e remove o item correspondente, proporcionando uma interface prática para a manutenção de um catálogo atualizado.

### 3. Consulta de Vinhos
O sistema permite buscar vinhos com base em diversos parâmetros:
- **Nome**: Encontre vinhos pelo nome completo ou parcial.
- **Ano**: Pesquise vinhos com base no ano de produção.
- **Região**: Localize vinhos com base na região de origem.
- **Uva**: Filtre vinhos por sua variedade de uva.

A busca é flexível, possibilitando encontrar rapidamente o vinho desejado.

### 4. Cadastro de Distribuidores
Além do cadastro de vinhos, o **Winy** permite adicionar distribuidores parceiros ao sistema. As informações de cada distribuidor incluem:
- **Nome**
- **Email**
- **Telefone**
- **CPF**

Isso facilita o controle de fornecedores e parcerias.

### 5. Recomendações de Vinhos
Com base nas preferências dos clientes ou na ocasião, o sistema pode sugerir vinhos adequados. As recomendações são criadas a partir do portfólio disponível e podem ser usadas para guiar clientes em suas escolhas.

## Estrutura do Código

### Variáveis Globais
- `wines`: Lista global onde são armazenados todos os vinhos cadastrados.

### Funções Principais
- `menu()`: Exibe o menu principal e solicita que o usuário selecione uma ação.
- `addWine()`: Adiciona novos vinhos ao sistema.
- `removeWine()`: Remove um vinho específico do sistema com base no nome.
- `findWine()`: Busca vinhos pelo nome, ano, região ou uva.
- `addDistribuitors()`: Adiciona distribuidores parceiros ao sistema.
- `wineRecommendations()`: Cria recomendações de vinhos personalizadas.

### Estrutura do Menu
O sistema opera com um menu principal, permitindo fácil navegação entre as diversas funcionalidades. O menu inclui as opções para adicionar, remover e consultar vinhos, além de cadastrar distribuidores e gerar recomendações.

## Instalação

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/winy-vinicolas.git
   
2. Execute o script: Certifique-se de ter o Python instalado no sistema e execute o arquivo principal:
    python3 winy.py

## Requisitos
Python 3.6 ou superior

## Melhorias Futuras
Este projeto pode ser expandido com várias melhorias, incluindo:

- Implementação de um banco de dados para armazenamento persistente.
- Interface gráfica para maior acessibilidade e usabilidade.
- Integração com APIs externas para recomendações automáticas baseadas em reviews de usuários.

## Contribuições
Sinta-se à vontade para contribuir com sugestões ou melhorias. Envie um pull request ou abra uma issue no GitHub para discutir suas ideias!
