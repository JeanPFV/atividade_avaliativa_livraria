# Feito por: Jean Pierre Franz Vieira
#            Lucas Daniel de Oliveira
from astrapy import DataAPIClient
from datetime import datetime, timedelta

client = DataAPIClient("AstraCS:eAOCGJdipSzWtTQvOHkaMFTP:30256094d0945ebb370a24c4d25e192f6ff077a34fd34f5929deae23c51d185f")
db = client.get_database_by_api_endpoint(
  "https://4d617402-22f3-4722-b1f2-2a79c9d483b3-us-east-2.apps.astra.datastax.com"
)


collection_livros = db.get_collection("livros")
collection_usuarios = db.get_collection("usuarios")
collection_emprestimos = db.get_collection("emprestimos")
collection_devolucoes = db.get_collection("devolucoes")

# Função para formatar strings
def format_str(texto):
    # Remove espaços extras e troca os espaços entre as palavras por underline
    return '_'.join(texto.split()).lower()

def livros():
    
    
    def cadastro_livro():
        # Cadastra um novo livro no banco de dados.
        isbn = input("Digite o ISBN do livro: >>> ")
        nome_livro = format_str(input("Digite o nome do livro: >>> "))
        autor_livro = format_str(input("Digite o autor do livro: >>> "))
        genero_livro = format_str(input("Digite o gênero do livro: >>> "))
        quantidade = int(input("Digite quantidade de exemplares: >>> "))

        livro = {
            "ISBN": isbn,
            "nome": nome_livro,
            "autor": autor_livro,
            "genero_livro": genero_livro,
            "quantidade": quantidade
        }

        try:
            collection_livros.insert_one(livro)
            print("Livro criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar livro: {e}")

        menu_livro()

    def vis_livro():
        # Exibe todos os livros no banco.
        try:
            for livro in collection_livros.find():
                print(livro)
        except Exception as e:
            print(f"Erro ao visualizar livros: {e}")

        menu_livro()

    def alte_livro():
        # Atualiza informações de um livro existente.
        nome_livro = format_str(input("Qual o nome do livro que gostaria de atualizar? >>> "))
        select = input("O que gostaria de alterar? \n1. Nome \n2. Autor \n3. Gênero \nEscolha: ")

        if select == "1":
            novo_nome = format_str(input("Qual o novo nome do livro? >>> "))
            try:
                collection_livros.update_one({"nome": nome_livro}, {"$set": {"nome": novo_nome}})
                print("Nome atualizado com sucesso!")
            except Exception as e:
                print(f"Erro ao atualizar o nome: {e}")
        elif select == "2":
            novo_autor = format_str(input("Qual o novo autor? >>> "))
            try:
                collection_livros.update_one({"nome": nome_livro}, {"$set": {"autor": novo_autor}})
                print("Autor atualizado com sucesso!")
            except Exception as e:
                print(f"Erro ao atualizar o autor: {e}")
        elif select == "3":
            novo_genero = format_str(input("Qual o novo gênero? >>> "))
            try:
                collection_livros.update_one({"nome": nome_livro}, {"$set": {"genero_livro": novo_genero}})
                print("Gênero atualizado com sucesso!")
            except Exception as e:
                print(f"Erro ao atualizar o gênero: {e}")
        else:
            print("Opção inválida.")

        menu_livro()

    def delet_livro():
        # Deleta um livro do banco.
        livro_deletar = format_str(input("Qual livro que deseja deletar? >>> "))
        try:
            collection_livros.delete_one({"nome": livro_deletar})
            print("Livro deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar livro: {e}")

        menu_livro()

    def pesquisa_livro():
        # Consulta e exibe o livro.
        escolha = input("Deseja pesquisar por gênero ou por autor?\n1. Gênero \n2. Autor \nEscolha: ")

        if escolha == "1":
            genero = format_str(input("Digite o gênero que deseja buscar >>> "))
            try:
                for livro in collection_livros.find({"genero_livro": genero}):
                    print(livro)
            except Exception as e:
                print(f"Erro ao pesquisar livro: {e}")
        elif escolha == "2":
            autor = format_str(input("Digite o autor que deseja buscar >>> "))
            try:
                for livro in collection_livros.find({"autor": autor}):
                    print(livro)
            except Exception as e:
                print(f"Erro ao pesquisar livro: {e}")

        menu_livro()

    def menu_livro():
        # Menu principal de interação.
        while True:
            tabela = input(
                "Escolha o que gostaria de fazer:"
                "\n1. Adicionar livro"
                "\n2. Visualizar livros disponíveis"
                "\n3. Alterar livro"
                "\n4. Remover livro"
                "\n5. Pesquisar livros"
                "\n6. Sair"
                "\nEscolha: ")
            if tabela == "1":
                cadastro_livro()
            elif tabela == "2":
                vis_livro()
            elif tabela == "3":
                alte_livro()
            elif tabela == "4":
                delet_livro()
            elif tabela == "5":
                pesquisa_livro()
            elif tabela == "6":
                print("Saindo...")
                break
            else:
                print("Opção inválida, por favor digite uma opção válida.")

    menu_livro()

def usuarios():
    
    
    def cadastro_usuario():
        # Cadastra um novo usuário no banco de dados.Nome
        nome_usuario = format_str(input("Digite o nome do usuário: >>> "))
        email_usuario = input("Digite o e-mail do funcionário: >>> ")
        documento_usuario = input("Digite o CPF ou RG do usuário: >>> ")
        datanascimento_usuario = input("Digite a data de nascimento do usuário: ",)

        usuario = {
            "nome": nome_usuario,
            "email": email_usuario,
            "documento": documento_usuario,
            "data_de_nascimento": datanascimento_usuario,
            }

        # Mensagem de sucesso ou erro ao criar usuário.
        try:
            collection_usuarios.insert_one(usuario)
            print("Usuário criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            
        menu_usuario()

    def visu_usuario():
        # Exibe todos os usuarios no banco.
        try:
            for usuario in collection_usuarios.find():
                print(usuario)
        except Exception as e:
            print(f"Erro ao visualizar usuarios: {e}")
            
        menu_usuario()

    def alte_usuario():
        # Atualiza informações de uma música existente na coleção musicas.
        nome_usuario = format_str(input("Qual o nome do usuário que gostaria de atualizar? >>> "))
        select = input("O que gostaria de alterar? \n1. nome \n2. E-mail \n3. documento: \n4. Data de nascimento\nEscolha: ")

        if select == "1":
            novo_nome = input("Qual o novo nome do usuário? >>> ")
            try:
                collection_usuarios.update_one({"nome": nome_usuario}, {"$set": {"nome": novo_nome}})
                print("Nome atualizado com sucesso!")
            except Exception as e:
                print(f"Erro ao atualizar o nome: {e}")
        elif select == "2":
            novo_email= input("Qual o novo email? >>> ")
            try:
                collection_usuarios.update_one({"nome": nome_usuario}, {"$set": {"email": novo_email}})
                print("Email atualizado com sucesso!")
            except Exception as e:
                print(f"Erro ao atualizar o email: {e}")
        elif select == "3":
            novo_documento= input("Qual o novo documento? >>> ")
            try:
                collection_usuarios.update_one({"nome": nome_usuario}, {"$set": {"email": novo_documento}})
                print("Documento atualizado com sucesso!")
            except Exception as e:
                print(f"Erro ao atualizar o documento: {e}")
        elif select == "4":
            nova_data= input("Qual a nova data de nascimento? >>> ")
            try:
                collection_usuarios.update_one({"nome": nome_usuario}, {"$set": {"email": nova_data}})
                print("Data de nascimento atualizado com sucesso!")
            except Exception as e:
                print(f"Erro ao atualizar a data de nascimento: {e}")
        else:
            print("Opção inválida.")
            
        menu_usuario()

    def deleta_usuario():
        # Deleta um usuário do banco.
        usuario_deletar = format_str(input("Qual usuário deseja deletar? >>> "))
        try:
            collection_usuarios.delete_one({"nome": usuario_deletar})
            print("Usuário deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            
        menu_usuario()

    def pesquisa_usuario():
        # Consulta e exibe o usuário.
        nome = format_str(input("Digite o nome do usuário que deseja buscar >>> "))
        try:
            for usuario in collection_usuarios.find({"nome": nome}):
                print(usuario)
        except Exception as e:
            print(f"Erro ao pesquisar usuário: {e}")
        
        menu_usuario()


    def menu_usuario():
        # Menu principal de interação.
        while True:
            tabela = input(
                "Escolha o que gostaria de fazer com a tabela:"
                "\n1. Adicionar usuário"
                "\n2. Visualizar usuário"
                "\n3. Alterar usuário"
                "\n4. Remover usuário"
                "\n5.Pesquisa de usuario"
                "\n6.Sair"
                "\nEscolha: ")
            if tabela == "1":
                cadastro_usuario()
            elif tabela == "2":
                visu_usuario()
            elif tabela == "3":
                alte_usuario()
            elif tabela == "4":
                deleta_usuario()
            elif tabela =="5":
                pesquisa_usuario()
            elif tabela == "6":
                print("Saindo...")
                break
            else:
                print("Opção inválida, por favor digite uma opção válida.")

    # Executa a função principal
    menu_usuario()

def emprestimo_livro():
    # Verificar se há exemplares disponíveis do livro
    livro_escolhido = input("Digite o nome do livro que deseja emprestar: >>> ")
    livro = collection_livros.find_one({"nome": livro_escolhido})
    if livro and livro["quantidade"] > 0:
        # Registrar o empréstimo, associando o livro ao usuário
        usuario_escolhido = input("Digite o nome do usuário que deseja emprestar o livro: >>> ")
        usuario = collection_usuarios.find_one({"nome": usuario_escolhido})
        if usuario:
            emprestimo = {
                "livro": livro_escolhido,
                "usuario": usuario_escolhido,
                "data_emprestimo": datetime.now(),
                "data_devolucao_prevista": (datetime.now() + timedelta(days=14))  # 14 dias para devolução
            }
            # Atualizar a quantidade de exemplares disponíveis
            collection_livros.update_one({"nome": livro_escolhido}, {"$inc": {"quantidade": -1}})
            # Registrar a data do empréstimo e a data prevista de devolução
            collection_emprestimos.insert_one(emprestimo)
            print("Empréstimo realizado com sucesso!")
        else:
            print("Usuário não encontrado.")
    else:
        print("Livro não encontrado ou não há exemplares disponíveis.")
        
    menu()

def devolucao_livro():
    # Verificar se o empréstimo existe
    livro_escolhido = input("Digite o nome do livro que deseja devolver: >>> ")
    usuario_escolhido = input("Digite o nome do usuário: >>>")
    emprestimo = collection_emprestimos.find_one(
        {"livro": livro_escolhido,
         "usuario": usuario_escolhido})
    
    if emprestimo:
        # Atualizar a quantidade de exemplares disponíveis do livro
        collection_livros.update_one({"nome": livro_escolhido}, {"$inc": {"quantidade": 1}})
        # Registrar a data de devolução
        devolucao = {
            "livro": livro_escolhido,
            "data_devolucao": datetime.now()
        }
        collection_devolucoes.insert_one(devolucao)
        # Remover o empréstimo
        collection_emprestimos.delete_one({"livro": livro_escolhido})
        print("Devolução realizada com sucesso!")
    else:
        print("Empréstimo não encontrado no usuário.")
        
    menu()

def relatorio(): 
    
    def livro_disponivel():
        try:
            # Filtrar apenas os livros com quantidade maior que 0
            livros_em_estoque = collection_livros.find({"quantidade": {"$gt": 0}})

            for livro in livros_em_estoque:
                print(livro)
        except Exception as e:
            print(f"Erro ao visualizar livros: {e}")
            
        menu_emprestimos()

    def emprestimo_usuario():
        usuario = input("Qual o usuário que gostaria de consultar? ")
        for emprestimo in collection_emprestimos.find({"usuario": usuario}):
            print(emprestimo)
            
        menu_emprestimos()
            
    def vencido():
        try:            
            # Encontrar todos os empréstimos onde a data de devolução prevista é menor que a data atual
            emprestimos_atrasados = collection_emprestimos.find({"data_devolucao_prevista": {"$lt": datetime.now()}})
            emprestimos_atrasados_list = list(emprestimos_atrasados)
            if len(emprestimos_atrasados_list) > 0:
                print("Empréstimos atrasados:")
                for emprestimo in emprestimos_atrasados_list:
                    print(emprestimo)
            else:
                print("Não há empréstimos atrasados.")
        
        except Exception as e:
            print(f"Erro ao verificar empréstimos atrasados: {e}")
            
        menu_emprestimos()
    
    
    def relatorio_emprestimos_data():
        try:
            # Input para as datas de início e fim
            data_inicio_str = input("Digite o início do período que deseja consultar por dia, mês e ano (DD/MM/AAAA): ")
            data_fim_str = input("Digite o fim do período que deseja consultar por dia, mês e ano (DD/MM/AAAA): ")

            # Converte as strings de data de início e fim para datetime
            data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y")
            data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y")

            # Converte as datas para o formato desejado {"$date": <timestamp>}
            data_inicio_formatada = {"$date": int(data_inicio.timestamp() * 1000)}
            data_fim_formatada = {"$date": int(data_fim.timestamp() * 1000)}

            # Encontrar todos os empréstimos realizados entre as duas datas
            emprestimos_periodo = collection_emprestimos.find({
                "data_emprestimo": {
                    "$gte": data_inicio_formatada,  # Maior ou igual à data de início
                    "$lte": data_fim_formatada  # Menor ou igual à data de fim
                }
            })

            emprestimos_periodo_list = list(emprestimos_periodo)

            if len(emprestimos_periodo_list) > 0:
                print("Relatório de Empréstimos:")
                for emprestimo in emprestimos_periodo_list:
                    print(emprestimo)
            else:
                print("Não há empréstimos realizados nesse período.")

        except Exception as e:
            print(f"Erro ao gerar relatório de empréstimos: {e}")
        
        menu_emprestimos()
            
    def menu_emprestimos():
        # Menu principal de interação.
        while True:
            tabela = input(
                "Escolha o que gostaria de fazer :"
                "\n1. Verificar os livros disponíveis para emprestimo"
                "\n2. Verificar o que um usuário está devendo de livro"
                "\n3. Verificar quais emprestimos estão vencidos"
                "\n4. Verificar todos os emprestimos relaizados por um período"
                "\n5. Sair"
                "\nEscolha: ")
            if tabela == "1":
                livro_disponivel()
            elif tabela == "2":
                emprestimo_usuario()
            elif tabela == "3":
                vencido()
            elif tabela == "4":
                relatorio_emprestimos_data()
            elif tabela == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida, por favor digite uma opção válida.")

    menu_emprestimos()
        
        
def menu():
    while True:
        print("\nMenu de Seleção:")
        print("1. Empréstimo")
        print("2. Devolução")
        print("3. Livros")
        print("4. Usuários")
        print("5. Relatório de emprestimo")
        print("6. Sair")

        escolha = input("Escolha uma opção (1-6): ")

        if escolha == '1':
            emprestimo_livro()
        elif escolha == '2':
            devolucao_livro()
        elif escolha == '3':
            livros()
        elif escolha == '4':
            usuarios()
        elif escolha == '5':
            relatorio()  
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executar o menu
menu()