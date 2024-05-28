## Bibliotecas
import random

## Listas 
# Nomes
names = ["John",
         "Emily", 
         "Michael",
         "Sophia",
         "David"
         ]

# E-mails
emails = ["John@email.com",
         "Emily@email.com", 
         "Michael@email.com",
         "Sophia@email.com",
         "David@email.com"
         ]

# Telefones
phone_numbers = ["+1 555-123-4567", 
                 "+1 555-987-6543",
                 "+1 555-456-7890",
                 "+1 555-234-5678",
                 "+1 555-876-5432"
                 ]

# Cidades
cities = ["São Bernanrdo do Campo",
          "Rio Preto", "Salvador",
          "Brasília",
          "Fortaleza"
          ]

# Estados
states = ["São Paulo",
          "Rio de Janeiro",
          "Minas Gerais",
          "Bahia",
          "Paraná"
          ]

## Menu
def menu():
    print('BEM-VINDO AO GERADOR DE DADOS')
    print('-' * 75)
    print('Escolha uma ou mais opções separado por vírgula.')
    print('-' * 75)
    print('[1] - Nome')
    print('[2] - E-mail')
    print('[3] - Telefone')
    print('[4] - Cidade')
    print('[5] - Estado')
    print('[SAIR] - Para Finalizar')
    

## Gerar dados aleatórios
def generate_random_data(choices):
    """
    Generates random data based on the specified data types.
    
    Args:
        choices (list): A list of strings representing the desired data types.
                           Valid options are: "name", "email", "phone", "city", "state".
    
    Returns:
        list: A list of randomly generated data based on the specified data types.
    """
    random_data = []
    
    for choice in choices:
        if choice == 1:
            random_data.append(random.choice(names))
        elif choice == 2:
            random_data.append(random.choice(emails))
        elif choice == 3:
            random_data.append(random.choice(phone_numbers))
        elif choice == 4:
            random_data.append(random.choice(cities))
        elif choice == 5:
            random_data.append(random.choice(states))
        else:
            random_data.append("Seleção inválida, tente novamente.")
    
    return random_data

## Salvar lista em um arquivo.txt
def save_to_file(data):
    with open('random_data.txt', 'a') as file:
        for item in data:
            file.write(str(item) + '\n')

## Programa
if __name__ == "__main__":
    while True:
        menu()
        user_input = input("Digite uma ou mais opções (separado por vígulas): ")
        print('-' * 75)

        if user_input.upper() == 'SAIR':
            print("Finalizando o programa.")
            break

        try:
            user_choices = [int(choice) for choice in user_input.split(',')]
            random_data = generate_random_data(user_choices)
            

            save_option = input("Você deseja salvar esta informação em um arquivo? (s/n)").lower()
            if save_option == 's':
                save_to_file(random_data)
                print("Salvo no arquivo: 'random_data.txt'")
            
            print(random_data)

        except ValueError:
            print("Entrada inválida. Por favor insira um número ou \"Sair\".")