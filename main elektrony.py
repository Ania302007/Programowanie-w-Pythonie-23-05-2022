import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


def poj_ladunki():
    pojedyńczy_ladunek = []
    for _ in range(10):
        pojedyńczy_ladunek.append(np.random.uniform(low=0, high=10, size=3))
    return pojedyńczy_ladunek


pojedyńczy_ladunek = poj_ladunki()


def ladunek():
    dodatnie = []
    ujemne = []
    for i in pojedyńczy_ladunek:
        znak = i * np.random.choice([-1, 1])
        if znak[0] < 0:
            ujemne.append(i)
        else:
            dodatnie.append(i)
    return ujemne, dodatnie


oba_ladunki = ladunek()
ujemne = oba_ladunki[0]
dodatnie = oba_ladunki[1]


def wspolrzedne():
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
    return x_ujemne, y_ujemne, z_ujemne, x_dodatnie, y_dodatnie, z_dodatnie


wspolrzedne()
x_ujemne = wspolrzedne()[0]
y_ujemne = wspolrzedne()[1]
z_ujemne = wspolrzedne()[2]
x_dodatnie = wspolrzedne()[3]
y_dodatnie = wspolrzedne()[4]
z_dodatnie = wspolrzedne()[5]
dod_spr = [(4, 4, 4)]
uj_spr = [(5, 5, 4)]


def v_ujemnych():
    plaszczyzna_xy_ujemne = np.zeros((100, 100))
    range1 = np.linspace(0, 10, 100)
    l_range1 = list(range1)
    for m in range1:
        for n in range1:
            for l in ujemne:
                r = np.sqrt((l[0] - m) ** 2 + (l[1] - n) ** 2 + l[2] ** 2)
                V = (9 * 10 ** 9) * (-1 / r)
                plaszczyzna_xy_ujemne[l_range1.index(m), l_range1.index(n)] += V
    return plaszczyzna_xy_ujemne


def v_dodatnich():
    plaszczyznaXY_dodatnie = np.zeros((100, 100))
    range1 = np.linspace(0, 10, 100)
    l_range1 = list(range1)
    for m in range1:
        for n in range1:
            for l in dodatnie:
                r = np.sqrt((l[0] - m) ** 2 + (l[1] - n) ** 2 + l[2] ** 2)
                V = (9 * 10 ** 9) * (1 / r)
                plaszczyznaXY_dodatnie[l_range1.index(m), l_range1.index(n)] += V
    return plaszczyznaXY_dodatnie


macierz_ujemna = v_ujemnych()
macierz_dodatnia = v_dodatnich()
macierz_Vc = macierz_dodatnia + macierz_ujemna


fig = plt.figure(figsize=plt.figaspect(2.))
ax = fig.add_subplot(1, 2, 1, projection="3d")
ax.scatter(x_ujemne, y_ujemne, z_ujemne, color="blue")
ax.scatter(x_dodatnie, y_dodatnie, z_dodatnie, color="red")
ax.set_title("Rozmieszczenie ładunków w przestrzeni")
ax = fig.add_subplot(1, 2, 2)
ax.set_aspect('equal', 'box')
ax.set_title("Izolinie potencjału elektrycznego")
X = np.linspace(1, 10, 100)
Y = np.linspace(1, 10, 100)
X, Y = np.meshgrid(X, Y)
izolonia = ax.contourf(X, Y, macierz_Vc, levels=100, cmap="plasma")
cbar = fig.colorbar(izolonia, orientation="horizontal", pad=0.1)
cbar.ax.set_xlabel('potencjał elektryczny')
plt.show()
