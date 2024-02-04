from contact import Contact

class ContactManager:
    def __init__(self) -> None:
        pass

    def start_manager(self):
        print("Iniciando o ContactManager")
        while True:
            print("\n|-------------------------------------------------|")
            print("\nEscolha uma opção:")
            print("1 - Adicionar contato")
            print("2 - Listar contatos")
            print("3 - Listar contatos favoritos")
            print("4 - Remover contato")
            print("5 - Editar contato")
            print("6 - Sair")
            choice = input("Escolha: ")

            if choice == '1':
                name = input("Digite o nome do contato: ")
                telephone = input("Digite o telefone do contato: ")
                email = input("Digite o email do contato: ")
                favorite = input("Digite se o contato é favorito (True/False): ")
                try:
                    contact = Contact(name,telephone,email,favorite)
                    print("\nContato criado com sucesso")
                except:
                    print("Erro ao criar contato")
            elif choice == '2':
                print("\nListando todos os contatos")
                Contact.get_all_contacts()
            elif choice == '3':
                print("\nListando contatos favoritos")
                Contact.get_all_favorite_contacts()
            elif choice=='4':
                email = input("\nIndique o email do contato que deseja deletar: ")
                Contact.delete_contact(email)
            elif choice == '5':
                print("Indique o email do contato que você gostaria de editar:")
                email = input("Email: ")
                print("Indique qual dado você gostaria de editar:")
                print("1 - Nome")
                print("2 - Telefone")
                print("3 - Email")
                print("4 - Favorito")
                choice = input("Escolha: ")
                if choice == '1':
                    name = input("Digite o novo nome: ")
                    Contact.update_name(email,name)
                elif choice == '2':
                    telephone = input("Digite o novo telefone: ")
                    Contact.update_telephone(email,telephone)
                elif choice == '3':
                    new_email = input("Digite o novo email: ")
                    Contact.update_email(email,new_email)
                elif choice == '4':
                    favorite = input("Digite se o contato é favorito (True/False): ")
                    Contact.update_favorite(email,favorite)
                
            
manager = ContactManager()
manager.start_manager()
