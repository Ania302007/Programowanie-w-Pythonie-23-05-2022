import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


def poj_ładunki():
    pojedyńczy_ładunek = []
    for _ in range(10):
        pojedyńczy_ładunek.append(np.random.uniform(low=0, high=10, size=3))
    # print(pojedyńczy_ładunek)
    return pojedyńczy_ładunek
pojedyńczy_ładunek=poj_ładunki()

def ładunek():
    dodatnie = []
    ujemne = []
    for i in pojedyńczy_ładunek:
        znak = i * np.random.choice([-1, 1])
        if znak[0] < 0:
            ujemne.append(i)
        else:
            dodatnie.append(i)
    return ujemne, dodatnie

oba_ładunki=ładunek()
ujemne=oba_ładunki[0]
# print(ujemne)
dodatnie=oba_ładunki[1]
# print(dodatnie)

def współrzędne():
    x_dodatnie = []
    y_dodatnie = []
    z_dodatnie = []
    x_ujemne = []
    y_ujemne = []
    z_ujemne = []
    for j in ujemne:
        x_ujemne.append(j[0])
        y_ujemne.append(j[1])
        z_ujemne.append(j[2])
    for k in dodatnie:
        x_dodatnie.append(k[0])
        y_dodatnie.append(k[1])
        z_dodatnie.append(k[2])
    return x_ujemne, y_ujemne, z_ujemne,x_dodatnie, y_dodatnie, z_dodatnie

współrzędne()
x_ujemne=współrzędne()[0]
y_ujemne=współrzędne()[1]
z_ujemne=współrzędne()[2]
x_dodatnie=współrzędne()[3]
y_dodatnie=współrzędne()[4]
z_dodatnie=współrzędne()[5]
# print(x_ujemne)
# print(y_ujemne)
# print(z_ujemne)
# print(x_dodatnie)
# print(y_dodatnie)
# print(z_dodatnie)
#
#
def v_ujemnych():
    płaszczyznaXY_ujemne=np.zeros((10, 10))
    for m in range(0,10):
        for n in range(0,10):
            for l in ujemne:
                r=np.sqrt((l[0]-m)**2+(l[1]-n)**2+l[2]**2)
                V=(9*10**9)*(-1/r)
                płaszczyznaXY_ujemne[m, n] +=V
    return płaszczyznaXY_ujemne
def v_dodatnich():
    płaszczyznaXY_dodatnie=np.zeros((10,10))
    for m in range(0,10):
        for n in range(0,10):
            for l in dodatnie:
                r=np.sqrt((l[0]-m)**2+(l[1]-n)**2+l[2]**2)
                V=(9*10**9)*(1/r)
                płaszczyznaXY_dodatnie[m, n] +=V
    return płaszczyznaXY_dodatnie
macierz_ujemna=v_ujemnych()
macierz_dodatnia=v_dodatnich()
macierz_Vc=macierz_dodatnia+macierz_ujemna
# print(macierz_Vc)
# print(macierz_Vc.shape)

fig = plt.figure(figsize=plt.figaspect(2.))
fig.suptitle('Rozmieszczenie ładunków w przestrzeni i izolinie potencjału elektrycznego')
ax = fig.add_subplot(2, 1, 1,projection="3d")
ax.scatter(x_ujemne,y_ujemne,z_ujemne,color="blue")
ax.scatter(x_dodatnie,y_dodatnie,z_dodatnie,color="red")
ax = fig.add_subplot(2, 1, 2)
X=np.linspace(1,10,10)
Y=np.linspace(1,10,10)
X,Y=np.meshgrid(X,Y)
izolonia=ax.contourf(X,Y,macierz_Vc,levels=50,extent=[0,20,0,20],cmap="plasma")
# izolinia=ax.imshow(macierz_Vc,extent=[0,20,0,20],cmap="plasma")
plt.show()