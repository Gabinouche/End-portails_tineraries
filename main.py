# Gabriel Leblanc AKA Gabinouche 06/26/2021
# Ce code permet de calculer la distance entre tout les portails connus et votre position afin de trouver le plus proche.
# le scirpt peut prendre un peu de temps à s'éxecuter sur l'IDE en ligne

#import des bibliothéques
from tkinter import *#bibliothéque interface
from matplotlib import pylab#bibliothéque pour le tracé graphique
from math import sqrt

portail_x = [0, -633, 1160, -653, -576, -224, -294, -1022, -3928, -4093, 4600, 630, 1672, -544, -2650]  #coordonnée x de tout les portails trouvés

portail_y = [0, 855, 24, -927, -1214, -1856, -1498, 336, 816, 702, 602, -839, -2174, -2793, -2790]  #coordonnée y de tout les portails trouvés

couleur = "#215D1F"#définition d'une variable pour la couleur

#création des liste de tri
portail_total_distance = []
nouv_portail_total_distance = []

#fenetre
window = Tk()

#parametres de la fenetre
window.title("Portal Searcher")
window.geometry("720x480")
window.minsize(480,360)
window.config(background=couleur)
window.iconbitmap('Eye_of_Ender-1.ico')

#première frame
frame = Frame(window, bg=couleur)

#creation sous-boite(2nd frame
frame_droite = Frame(frame,bg=couleur)

#création d'un texte
titre = Label(frame_droite,text='Entrez vos coordonnées ici:',font=('Helvetica',20),bg=couleur,fg='white')
titre.pack()

#définition des valeurs des variables réponse
phrase_rep1=StringVar()
phrase_rep2=StringVar()

#ajouter la touche entrée comme bouton
#window.bind('<Return>')

#bloc d'instruction pour les calcules
def recup():

  repxj = (entry_x.get())#aquisition des valeurs entrée dans l'interface
  repyj = (entry_y.get())#aquisition des valeurs entrée dans l'interface
  xj = int(repxj)#on attribut les valeurs à une nouvelle variable
  yj = int(repyj)#on attribut les valeurs à une nouvelle variable
  print(repxj,repyj)#on affiche les nouvelles variables
  v=0
  while v < len(portail_x):  # tant que v n'est pas égale aux nombre de valeurs dans la liste le programme se répète
      p1 = sqrt((xj - portail_x[v]) ** 2 + (yj - portail_y[v]) ** 2)#calcule de distance entre deux points avec la formule(qui se note -> \sqrt{(x_{b}-x_{a})²+(y_{b}-y_{a})²}=\overrightarrow{AB} <-)

      v=v+1

      portail_total_distance.append(p1)  # les distances sont misent dans une nouvelle liste


  nouv_portail_total_distance = portail_total_distance[:]#définition d'une nouvelle liste
  nouv_portail_total_distance.sort(reverse=False)#classement des valeurs de la nouvelle liste dans l'ordre croissant
  coor = portail_total_distance.index(nouv_portail_total_distance[0])#définition de l'indice pour trouver la plus petite distance dans la liste triée
  # affichage de la réponse
  phrase_rep1.set(f'Le portail le plus proche de toi est à {nouv_portail_total_distance[0]} blocks de ta position')
  # affichage de la réponse
  phrase_rep2.set(f'Le portail se trouve aux coodonnées X {portail_x[coor]} et Y {portail_y[coor]}')

  portail_total_distance.clear()
  nouv_portail_total_distance.clear()


    #définition des paramétres pour l'affichage
  x = [xj, portail_x[coor]]
  y = [yj, portail_y[coor]]
  px = [portail_x[:]]
  py = [portail_y[:]]

  pylab.plot(xj,yj,"yo") #affiche un point au coordonnées du joueur en jaune
  pylab.plot(x, y,"m-", linewidth=2) #trace le trajet entre le joueur et le portail le plus proche en magenta
  pylab.plot(px,py,"bo") #affiche un point à tout les portails connus en bleu
  pylab.plot(0,0,"go") #affiche un point vert au portail de l'ile du Dragon
  pylab.show()
pylab.grid() #affiche un cadriage
# création image
width = 300
height = 300
image = PhotoImage(file="boussole.png").zoom(18).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg=couleur,bd=0,highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0,column=1,sticky=W)
#ajout d'un bouton
bouton1 = Button(frame,text = "Trouver un portail" , font = ("Courrirer" ,25), bg="white", fg =couleur,command=recup)
bouton1.grid(row=1,column=1,sticky=W)
#création d'une entrée (coordonnée x du joueur)
entry_x = Entry(frame_droite,font=("Helvetica",20),bg='white',fg="#AA1BAB")
entry_x.pack(pady=25)
#création d'une entrée (coordonnée y du joueur)
entry_y = Entry(frame_droite,font=("Helvetica",20),bg='white',fg="#AA1BAB")
entry_y.pack(pady=5)



#création d'un texte
rep_distance = Label(frame_droite,textvariable=phrase_rep1,font=('Helvetica',20),wraplength=400, justify="center",bg=couleur,fg='white')
rep_distance.pack(pady=5)
#création d'un texte


repcoord = Label(frame_droite,textvariable=phrase_rep2,font=('Helvetica',20),wraplength=400, justify="center",bg=couleur,fg='white')
repcoord.pack(pady=10)

#xj.insert(0,portail_x[coor])
#yj.insert(0,portail_y[coor])

#afficher les frame
frame.pack(expand=YES)
frame_droite.grid(row=0,column=2,sticky=E)

#afficher la fenetre
window.mainloop()