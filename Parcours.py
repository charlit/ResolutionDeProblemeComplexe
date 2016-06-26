ParcoursProfondeur = []

ListeSommets = ['A','B','C','D']
ListeSommetsMarques = []
File = []
Graphe1 = [[0,1,1,0],
          [1,0,1,1],
          [1,1,0,1],
          [0,1,1,0]]

def Ajouter(Element):
    File.append(Element)

def Retirer():
    Element = File[0]
    del File[0]
    return Element 


def EstMarque(Sommet):
    for i in range(0,len(ListeSommetsMarques)):
        if(ListeSommetsMarques[i][0]==Sommet and ListeSommetsMarques[i][1] != ''):
            return True
    return False

def Marquer(Sommet):
    for i in range(0,len(ListeSommetsMarques)):
        if(ListeSommetsMarques[i][0]==Sommet):
            ListeSommetsMarques[i][1]='*'
            return
    ListeSommetsMarques.append([Sommet,'*'])

def ParcourirLargeur(Graphe):
    ParcoursLargeur = []
    
    if(len(File)==0):
        Ajouter(ListeSommets[0])
        Marquer(ListeSommets[0])
        
    for i in range(0,len(Graphe)):
        ParcoursLargeur.append([])
        for j in range(0,len(Graphe)):
            ParcoursLargeur[i].append(0)

    while(len(File)>0):
        Element = Retirer()
        nElement = 0
        for i in range(0,len(ListeSommets)):
            if(ListeSommets[i]==Element):
                nElement = i
        for i in range(0,len(Graphe)):
            if(Graphe[nElement][i]!=0 and EstMarque(ListeSommets[i])==False):
                Ajouter(ListeSommets[i])
                Marquer(ListeSommets[i])
                ParcoursLargeur[nElement][i]=Graphe[nElement][i]
                ParcoursLargeur[i][nElement]=Graphe[nElement][i]
    return ParcoursLargeur

def ParcourirProfondeur(Graphe):
    ParcoursProfondeur = []
    
    if(len(File)==0):
        Ajouter(ListeSommets[0])
        Marquer(ListeSommets[0])
        
    for i in range(0,len(Graphe)):
        ParcoursProfondeur.append([])
        for j in range(0,len(Graphe)):
            ParcoursProfondeur[i].append(0)
            
    while(len(File)>0):
        Element = Retirer()
        nElement = 0
        first = True
        for i in range(0,len(ListeSommets)):
            if(ListeSommets[i]==Element):
                nElement = i
        for i in range(0,len(Graphe)):
            if(Graphe[nElement][i]!=0 and EstMarque(ListeSommets[i])==False):
                Ajouter(ListeSommets[i])
                if first:
                    first=False
                    Marquer(ListeSommets[i])
                    ParcoursProfondeur[nElement][i]=Graphe[nElement][i]
                    ParcoursProfondeur[i][nElement]=Graphe[nElement][i]
    return ParcoursProfondeur


print(ParcourirLargeur(Graphe1))
