from wishlist_scripts.movies.movie import Movie

full = True

while (full):
    mn = Movie()

    print('**********************************************')
    print('')
    print('  Bem Vindo a Sua WhisList(Lista de Desejo)')
    print('')
    print('**********************************************')
    print('')
    print('')
    
    print('*************************************')
    print('1 - Cadastrar um Novo Filme *********')
    print('2 - Ler [Filme/Filmes ***************')
    print('3 - Atualizar Filme *****************')
    print('4 - Deletar Filme *******************')
    print('5 - Sair ****************************')
    print('')
    resp = input('Digite a Operação: ')


    if resp =='1':
        mn.create_movie()
    elif resp =='2':
        mn.read_movie()
    elif resp =='3':
        mn.update_movie()
    elif resp =='4':
        mn.delete_movie()
    else:
        full = False
