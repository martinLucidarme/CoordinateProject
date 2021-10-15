class CriarTabela():


    def definir_colunas(lista_das_colunas):
        text_opening = open('text_test.txt','w') #file type object
        '''print(text_opening.read()) #opening.read is str type, this str is the text of the whole file'''
        for col in lista_das_colunas:
            text_opening.write(f'{col}'+'   ')

lista_das_colunas = ['Lat', 'Long', 'N', 'P', 'K']
CriarTabela.definir_colunas(lista_das_colunas)


