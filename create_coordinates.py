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
            Xatual = min(Xinit,Xfinal)
            Yatual= min(Yinit,Yfinal)
            listacoordX = [min(Xinit,Xfinal)]
            while Xatual < max(Xinit,Xfinal):
                Xatual += pace
                listacoordX += [Xatual]
            listacoordY = [min(Yinit,Yfinal)]
            while Yatual < max(Yinit,Yfinal):
                Yatual += pace
                listacoordY += [Yatual]
            return [listacoordX,listacoordY]

    def extract_coord(self, dbllistX_Y):
        Xlist = dbllistX_Y[0]
        Ylist = dbllistX_Y[1]
        strX= ''
        strY = ''
        for x in Xlist:
            strX += str(x)+'\n'
        for y in Ylist:
            strY += str(y) + '\n'
        return strX, strY
coord_clean = Coord_Clean()
print('Xinit= initial coordinate of longitude / Yinit initial coordinate oflatitude' )
print('Xfinal= final coordinate of longitude / Yfinal final coordinate oflatitude')
print('pace= number of degrees between coord numbers')

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

calculated_coord = coord_clean.calc_coord(Xinit,Yinit,Xfinal,Yfinal,pace)
print(calculated_coord)
print(coord_clean.extract_coord(calculated_coord))
