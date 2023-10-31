

if __name__ == '__main__':
    arq_contatos = 'contatos.txt'

    while True:
        print('Digite uma das opções a seguir:\n\n4) Para adicionar um novo contato.\n3) Para apresentar todos os contatos.\n2) Para deletar um contato.\n1) Para editar um contato existente.\n0) Para encerrar o programa.')
        resposta = int(input('Digite a opção: '))

        if resposta == 4:
            adicionar_contato(arq_contatos)
            print('O contato foi adicionado com sucesso!')
        
        elif resposta == 3:
            apresentar_contatos(arq_contatos)
        
        elif resposta == 2:
            deletar_contato(arq_contatos)
            print('O contato foi deletado com sucesso!')
        
        elif resposta == 1:
            editar_contato(arq_contatos)
            print('O contato foi alterado com sucesso!')
        
        elif resposta == 0:
            print('Espero te ver de novo ;)')
            break

        else:
            print('Digite uma das opções correspondentes!')
