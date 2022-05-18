class Gay:
    resist = []
    weak = []
    immune = []


class Lean:
    resist = []
    weak = []
    immune = []


class Racism:
    resist = []
    weak = []
    immune = []


class Weeb:
    resist = []
    weak = []
    immune = []


class Gainz:
    resist = []
    weak = []
    immune = []


class Sex:
    resist = []
    weak = []
    immune = []


class Gamer:
    resist = []
    weak = []
    immune = []


class Furry:
    resist = []
    weak = []
    immune = []


class Virgin:
    resist = []
    weak = []
    immune = []


class Retard:
    resist = []
    weak = []
    immune = []


class Nerd:
    resist = []
    weak = []
    immune = []

def resist(type,list):
    for i in list:
        type.resist.append(i)

def weak(type,list):
    for i in list:
        type.weak.append(i)

def immune(type,list):
    for i in list:
        type.immune.append(i)

#Racism
resist(Racism,[Racism,Gay,Gainz,Sex,Furry,Retard,Nerd])
weak(Racism,[Weeb,Gamer])

#Lean
resist(Lean,[Lean,Weeb,Gamer,Virgin,Retard])
weak(Lean,[Gainz,Sex,Nerd])

#Gay
resist(Gay,[Sex])
weak(Gay,[Racism,Gay,Gamer,Furry, Retard])

#Weeb
resist(Weeb,[Racism,Gay,Nerd])
weak(Weeb,[Gainz,Virgin])
immune(Weeb,[Sex])

#Gainz
resist(Gainz,[Weeb, Gainz, Gamer, Furry])
weak(Gainz,[Racism, Lean,Nerd])
immune(Gainz,[Virgin])

#Sex
resist(Sex,[Racism,Lean,Gamer,Retard,Nerd])
weak(Sex,[Weeb,Gainz,Furry])
immune(Sex,[Virgin])

#Gamer
resist(Gamer,[Gay,Weeb])
weak(Gamer,[Lean,Gainz,Virgin,Nerd])
immune(Gamer,[Sex])

#Furry
resist(Furry,[Sex])
weak(Furry,[Racism,Lean,Weeb,Gainz,Gamer,Furry,Retard])

#Virgin
resist(Virgin,[Weeb,Gainz,Gamer])
weak(Virgin,[Lean,Gay,Sex,Retard])

#Retard
resist(Retard,[Lean,Gainz,Furry,Virgin,Nerd])
weak(Retard,[Sex])

#Nerd
resist(Nerd,[Lean,Gamer,Virgin])
weak(Nerd,[Gainz,Sex,Retard])


