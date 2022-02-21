from create_coordinates import Coord_Clean

class CriarTabela:


    def definir_colunas(self,lista_das_colunas):
        '''
        Give a name to every column: each str of the list will be the header of
        the column
        :param lista_das_colunas: list of str, each str is the name of a column
        :return: write in a text file the name of the column
        '''

        text_opening = open('text_test.txt', 'w') #file type object
        #print(text_opening.read()) #opening.read is str type, this str is the text of the whole file
        for col in lista_das_colunas:
            text_opening.write(f'{col}'+'   ')
        text_opening.write('\n')

tableau = CriarTabela()
coord_clean= Coord_Clean()

print('Xinit')
#Xinit = float(input())
Xinit = 40

print('Yinit')
#Yinit = float(input())
Yinit = 5

print('Xfinal')
#Xfinal = float(input())
Xfinal = 60

print('Yfinal')
#Yfinal = float(input())
Yfinal = -15

print('pace')
#pace = float(input())
pace = 2

dbl_string_coord = coord_clean.extract_coord(coord_clean.calc_coord(Xinit,Yinit,Xfinal,Yfinal,pace))
lista_das_colunas = ['Lat', 'Long', 'N', 'P', 'K','Micro', 'pH', 'CTC','V%']

tableau.definir_colunas(lista_das_colunas)
tableau.definir_colunas(dbl_string_coord)

