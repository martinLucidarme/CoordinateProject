class Ideia2_coordinates:
    def calc_coord(self, Xinit,Xfinal,Yinit, Yfinal, pace):
        '''
        A function that creates a list of coordinates in EPSG: WGS-84
        :param Xinit: initial x coordinate of longitude
        :param Yinit: initial y coordinate of latitude
        :param pace: number of degrees between 2 points
        :param Xfinal: final x coordinate of longitude
        :param Yfinal: final y coordinate of latitude

        :return: a list of X and Y coordinates between X,Yinit and X,Yfinal

        Example:
        Xinit = 40
        Yinit = 50
        Xfinal = 50
        Yfinal = 60
        pace = 2
        calc_coord(Xinit,Yinit,Xfinal,Yfinal,pace)
        [40, 42, 44, 46, 48, 50, 50, 52, 54, 56, 58, 60]
        '''
        Xatual = min(Xinit, Xfinal)
        Yatual = min(Yinit, Yfinal)
        listacoordX = [min(Xinit, Xfinal)]
        while Xatual < max(Xinit, Xfinal):
            Xatual += pace
            listacoordX += [Xatual]
        listacoordY = [min(Yinit, Yfinal)]
        while Yatual < max(Yinit, Yfinal):
            Yatual += pace
            listacoordY += [Yatual]
        return [listacoordX, listacoordY]

    def string_coord(self,list_of_list):
        strcord = ''
        n = len(list_of_list[0])
        j=0
        for x in range(n):
            while j< len(list_of_list):
                strcord+= f'{list_of_list[j][x]}'+'    '
                j+=1
            j=0
            strcord += '\n'
        return strcord



ideia2= Ideia2_coordinates()
Xinit= -13.595
Xfinal= -13.600
Yinit =-55.800
Yfinal=-55.805
pace = 0.0010
list_x_y = ideia2.calc_coord(Xinit,Xfinal,Yinit, Yfinal, pace)+ideia2.calc_coord(20,30,5, 15, 1)+ideia2.calc_coord(30,40,18, 28, 1)
print(list_x_y)
column_ok = ideia2.string_coord(list_x_y)
print(column_ok)
header = 'Lat   Long    N   P   K   MO'+'\n'
text_opening = open('text_test.txt','w')
text_opening.write(header+column_ok)