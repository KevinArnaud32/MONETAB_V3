from models.couleurs import *
from datetime import datetime
from base import bd
from models.personne import Personne
from Eleve.ICrudEleve import ICRUDEleve

class Eleve(Personne, ICRUDEleve):
    """
        Classe représentant un élève, héritant de la classe Personne et de la classe ICRUDEleve.
    """
    __eleves = []

    # Initialise un nouvel élève avec ses informations personnelles
    def __init__(self, dateNaissance, ville, prenom, nom, telephone, classe, matricule):
        super().__init__(dateNaissance, ville, prenom, nom, telephone)
        self.__classe = classe
        self.__matricule = matricule

    # Retourne une représentation sous forme de chaîne de l'élève
    def __str__(self):
        return f"Eleve n° {self.get_id} : {self.get_nom} {self.get_prenom}, née le {self.get_date_naissance} à {self.ville}, classe: {self.__classe}, matricule: {self.__matricule}, téléphone: {self.telephone}"

    # Retourne le matricule de l'élève.
    @property 
    def get_matricule(self):
        return self.__matricule
    
    @property 
    def get_classe(self):
        return self.__classe

    def set_classe(self, classe):
        self.__classe = classe            

    def set_matricule(self, matricule):
        self.__matricule = matricule

    # Implémentation des méthodes CRUD
    # Ajouter un élève
    def ajouter(self):
        """Ajoute un nouvel elève à la base de données."""
    
        nouvel_eleve = cls()
        
        connection = bd.create_connection()
        if connection and connection.is_connected():
            try:
                curseur = connection.cursor()

                query = "INSERT INTO utilisateurs (pseudo, mot_de_passe, date_creation) VALUES (%s, %s, NOW())"
                curseur.execute(query, ())
                
                connection.commit()
                nouvel_eleve.__id = curseur.lastrowid  # Récupérer l'ID de l'utilisateur créé
                return f"{vert}Compte créé avec succès !!\n-->Pseudo : {pseudo}{reset}"
            except Exception as e:
                print(f"{rouge}Erreur lors de la création du compte: {e}{reset}")
            finally:
                curseur.close()
                connection.close()
        return f"{rouge}Échec de la connexion à la base de données.{reset}"

    # modifier un élève
    def modifier(eleve):
        for index, eleve_existe in enumerate(Eleve.__eleves):
            if eleve_existe.id == eleve.id:
                Eleve.__eleves[index] = eleve
                return True
        return False

    # supprimer un élève 
    def supprimer(identifiant):
        for index, eleve in enumerate(Eleve.__eleves):
            if eleve.matricule == identifiant:
                del Eleve.__eleves[index]
                return True
        return False

    # Obtenir les élèves
    def obtenirEleve():
        return [str(eleve) for eleve in Eleve.__eleves]


    # Obtenir un élève par son id
    def obtenir(identifiant):
        for eleve in Eleve.__eleves:
            if eleve.matricule == identifiant:
                return eleve
        return None