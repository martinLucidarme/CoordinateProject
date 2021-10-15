class CriarTabela:

    def __init__(self):
        self.arquivo =0

    def definir_colunas(self,lista_das_colunas):
        text_opening = open('text_test.txt','w') #file type object
        '''print(text_opening.read()) #opening.read is str type, this str is the text of the whole file'''
        for col in lista_das_colunas:
            text_opening.write(f'{col}'+'   ')

tableau = CriarTabela()
lista_das_colunas = ['Lat', 'Long', 'N', 'P', 'K','Micro', 'pH', 'CTC','V%']
tableau.definir_colunas(lista_das_colunas)


