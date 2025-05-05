##### Classes #####
# %%
class Chien:
    pass 

##### Objects(Instances) #####
# %%
mon_chien = Chien()
type(mon_chien) # <class '__main__.Chien'>
# %%


###### Attributes ######
# %%
class Chien:
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race
# %%
mon_chein = Chien("Pipo", "Labrador")
print(mon_chein.nom) # Pipo
print(mon_chein.race) # Labrador

##### Methods ######
# %%
class Chien:
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race
    def aboyer(self):
        print(f"{self.nom} aboie  !")

# %%
rex = Chien("Rex", "Berger Allemand")
print(rex.aboyer()) # Rex aboie !
# %%