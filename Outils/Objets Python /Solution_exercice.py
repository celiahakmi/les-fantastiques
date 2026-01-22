class CompteBancaire:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde
    def deposer(self, montant):
        self.solde = self.solde + montant
    def retirer(self, montant): 
        if self.solde >= montant: 
            self.solde = self.solde - montant 
        else: 
            print("Le solde est insuffisant")
    def afficher(self): 
        print(f"Compte de {self.nom} : {self.solde} €")


compte1 = CompteBancaire("Zina", 3000)
compte1.deposer(1000)
compte1.retirer(500)
compte1.afficher()
    



