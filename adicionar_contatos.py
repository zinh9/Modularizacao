def adicionar_contato(arq_contatos):
    lista_contatos = []

    while True:
        nome = input('Digite o nome do contato (digite "sair" para encerrar): ')

        if nome == 'sair':
            break

        endereco = input('Digite o endereço do contato: ')
        numero = int(input('Digite o número do contato (com DDD): '))

        contato = {
            'Nome': nome,
            'Endereço': endereco,
            'Número': numero
        }

        lista_contatos.append(contato)

        with open(arq_contatos, 'w') as arquivo:
            for contato in lista_contatos:
                for chave, valor in contato.items():
                    arquivo.write(f'{chave}: {valor}')
        
        resposta = input('Deseja adicionar outro número ao contato: ')

        if resposta == 'sim':
            numero = int(input('Digite o número do contato: '))
            with open(arq_contatos, 'a') as arquivo:
