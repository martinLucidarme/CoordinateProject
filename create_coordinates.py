class Coord_Clean:

    def calc_coord(self,Xinit,Yinit,Xfinal,Yfinal,pace):
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
            Xatual = Xinit
            Yatual= Yinit
            listacoordX = [Xinit]
            while Xatual < Xfinal:
                Xatual += pace
                listacoordX += [Xatual]
            listacoordY = [Yinit]
            while Yatual < Yfinal:
                Yatual += pace
                listacoordY += [Yatual]
            return [listacoordX,listacoordY]

    def extract_coord(self, dbllistX_Y):

    print('Xinit= initial coordinate of longitude / Yinit initial coordinate oflatitude' )
    print('Xfinal= final coordinate of longitude / Yfinal final coordinate oflatitude')
    print('pace= number of degrees between coord numbers')
    print('Xinit')
    Xinit = float(input())
    print('Yinit')
    Yinit = float(input())
    print('Xfinal')
    Xfinal = float(input())
    print('Yfinal')
    Yfinal = float(input())
    print('pace')
    pace = float(input())
    calc_coord(Xinit,Yinit,Xfinal,Yfinal,pace)
    print(calc_coord(Xinit,Yinit,Xfinal,Yfinal,pace))