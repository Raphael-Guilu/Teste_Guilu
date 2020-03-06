import requests,json,time,os

class Movie:

    def __init__(self):
        pass

    def operacao(self):
        print('')
        print('*********************')
        resp = input('Digite a Operação: ')
        print('*********************')
        print('')

        return resp

    def create_movie(self):
        key = '49f1a182'
        movie_name = input('Digite o filme a ser buscado: ').lower()
        url = f'http://www.omdbapi.com/?apikey={key}&t={movie_name}'
        
        response = requests.get(url).json()

        print(json.dumps(response,indent=4))
        print('')
        print('')
        print(f'Titulo: {response["Title"]}')
        print(f'Ano: {response["Year"]}')
        print(f'Lançamento: {response["Released"]}')
        print(f'Tempo: {response["Runtime"]}')
        print(f'Genero: {response["Genre"]}')
        print(f'Linguagem Primaria: {response["Language"]}')
        print(f'Pais: {response["Country"]}')
        time.sleep(2)
        print('')
        print('')
        print('Este é o filme desejado para Salvar:\n 1 - Sim \n 2 - Não')
        resp = self.operacao()
        
        movie_new = {
            'Titulo':f'{response["Title"]}',
            'Ano':f'{response["Year"]}',
            'Lancamento': f'{response["Released"]}',
            'Tempo': f'{response["Runtime"]}',
            'Genero': f'{response["Genre"]}',
            'Linguagem' : f'{response["Language"]}',
            'Pais': f'{response["Country"]}',
            'Status': f'Pendente'
        }

        if resp == '1':

            flag = True
            try:
                charge_movie =[]

                with open('movies.json') as file_json_movie:
                    charge_movie = json.load(file_json_movie)
                    for movie in charge_movie:
                        if movie['Titulo'] == response['Title']:
                            print('Filme existente !!!')
                            flag = False
                if flag:
                    charge_movie.append(movie_new)

                with open('movies.json','w') as file:
                    json.dump(charge_movie, file, indent=4)

            except FileNotFoundError:
                with open('movies.json', 'w') as file:
                    movie_new = [movie_new]
                    json.dump(movie_new, file, indent=4)    
            print('Filme Salvado com Sucesso na Sua Lista de Desejo !!!') 

        else:
            print('Voltando ao menu principal.')
    
    def read_movie(self):
        movie_name = input('Digite o Nome do Livro: ').lower()
        if os.path.isfile('movies.json'):
            with open('movies.json','r') as file_json_movie:
                charge_movie = json.load(file_json_movie)
                for movie in charge_movie:
                    if str(movie['Titulo']).lower() == movie_name:
                        print(movie)   
                   
        else:
            print('Arquivo Não Existente')

    def update_movie(self):
        movie_name = input('Digite o Titulo a Ser Atualizado: ').lower()
        print('')
        print('**************************')
        print('')
        print('1 - Pendente')
        print('2 - Proximo da Lista')
        print('3 - Assistido')
        print('4 - Assistir Mais Tarde')
        print('')
        print('**************************')

        resp = self.operacao()
        read_movie = []
        new_movies = []
        try:
            with open('movies.json','r') as file_json:
                read_movie =json.load(file_json)
                for movies in read_movie:
                    if str(movies['Titulo']).lower() == movie_name:
                        if resp == '1':
                            movies['Status'] = 'Pendente'
                        elif resp == '2':
                            movies['Status'] = 'Proximo da Lista'
                        elif resp == '3':
                            movies['Status'] = 'Assistido'
                        elif resp == '4':
                            movies['Status'] = 'Assistir Mais Tarde'
                        
                        new_movies.append(movies)
                    else:
                        new_movies.append(movies)

            with open('movies.json','w') as file_json_update:
                json.dump(new_movies,file_json_update,indent=4)
                print('Livro Atualizado Com Sucesso !!!')
        except Exception as e:
            print(e)

    def delete_movie(self):

        remove_movie = input('Filme a ser Deletado: ').lower()
        movies_read =[]
        movies_new_arq =[]
        try:
            with open('movies.json','r') as file_json:
                movies_read = json.load(file_json)
                for movie in movies_read:
                    if str(movie['Titulo']).lower() != remove_movie:
                        movies_new_arq.append(movie)
                    else:
                        pass
            
            with open('movies.json','w') as file_json_movie:
                json.dump(movies_new_arq,file_json_movie,indent=4)

        except Exception as e:
            print(e)

if __name__ == "__main__":
    mov = Movie()
    mov.read_movie()
