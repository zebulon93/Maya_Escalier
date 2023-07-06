# -*- mode: python ; coding: utf-8 -*- ; python version: 2.7.11

"""

+++++++++++++++++++++++++++++++++++++++++++++++++++++
############### GENERATEUR D'ESCALIER ###############
+++++++++++++++++++++++++++++++++++++++++++++++++++++



DESCRIPTION :
	
	Creer un escalier soit en colimacon soit droit en utilisant la valeur entree par l'utilisateur (nombre de marche ou hauteur).



CLASSES :

    cls_escalier (object) :
		Gestion de la fenetre.

    cls_escalier_generateur (cls_escalier) :
		Gestion de la creation d'un escalier.

	cls_escalier_creation (cls_escalier_generateur) :
		Creation de l'escalier.

		

FONCTIONS :

	cls_escalier (object) :

    	intField_nb_marche_actif (self:objet, _:boolean) :
    		Rendre accessible la saisie pour le nombre de marche lorsque le bouton radio "rb_nb_marche" est actif.
    	intField_nb_marche_inactif (self:objet, _:boolean) :
			Rendre inaccessible la saisie pour le nombre de marche lorsque le bouton radio "rb_nb_marche" est inactif.
    	escalier (self:objet)
			Creer la fenetre.

	cls_escalier_generateur (cls_escalier) :

    	parametres_lancement (self:objet, int_bouton_generer:int, label_fenetre_generateur_escalier:unicode, rb_escal_colimacon:unicode) :
			Recuperer la sasie de l'utilisateur et lancer la generation de l'escalier suivant le bouton clique.
		escalier_generateur (self:objet, int_valeur:int, rb_escal_colimacon:unicode) :
			Generer l'escalier suivant la valeur donnee par l'utilisateur.

	cls_escalier_creation (cls_escalier_generateur) :

		escalier_colimacon (self:objet, string_objet_prefixe:string):
			Mettre en place l'escalier en colimacon.
		escalier_droit (self:objet, string_objet_prefixe:string) :
			Mettre en place l'escalier en colimacon.
		rotation (self:objet) :
			Pivoter chaque element d'escalier pour l'escalier en colimacon.
		translation (self:objet) :
			Translater chaque element d'escalier pour l'escalier droit.



DIVERS :

	__author__ = "Frederic Boule"
	___droit_d_auteur___ = "Tous droits reserves"
	__copyright__ = "Copyright (C) 2023 Frederic Boule. All rights reserved."
	__version__ = "1.0" 

"""





# ######################################################### #
# ======================= LIBRAIRIES ====================== #
# ######################################################### #


from maya import cmds





# ######################################################### #
# ======================== CLASSES ======================== #
# ######################################################### #


class cls_escalier (object):
	'''

	-> Gestion de la fenetre :

	def intField_nb_marche_actif (self:objet, _:boolean): rendre accessible la saisie pour le nombre de marche lorsque le bouton radio "rb_nb_marche" est actif
	return : none

	def intField_nb_marche_inactif (self:objet, _:boolean) : rendre inaccessible la saisie pour le nombre de marche lorsque le bouton radio "rb_nb_marche" est inactif
	return : none

	def escalier (self:objet) : creer la fenetre
	return : none

	'''


	def __init__ (self):


		# elements pour affichage et gestion de la fenetre :
		self.label_fenetre_generateur_escalier		= "Generateur d'escalier en colimacon"
		self.int_fenetre_position_haut				= 430
		self.int_fenetre_position_gauche			= 700
		self.string_vide							= ""
		self.string_saut_ligne						= "\n"
		self.label_type_escalier					= "Type d'escalier :"
		self.label_rb_escal_colimacon				= "Escalier en colimacon"
		self.label_rb_escal_droit					= "Escalier droit"
		self.label_choix_parametre					= "Choix du parametre :"
		self.label_rb_nb_marche						= "Nombre de marche :"
		self.label_rb_hauteur						= "Hauteur (15 min) :"
		self.label_intField_nb_marche				= "IntField_nb_marche"
		self.label_intField_hauteur					= "IntField_hauteur"
		self.label_bouton_generer_et_fermer			= "Generer et fermer"
		self.label_bouton_generer					= "Generer"
		self.label_bouton_fermer					= "Fermer"
		self.int_bouton_generer_et_fermer			= 1
		self.int_bouton_generer						= 0

	
	def intField_nb_marche_actif (self, _):
		'''

		-> Rendre accessible la saisie pour le nombre de marche lorsque le bouton radio "rb_nb_marche" est actif :

		param self : instance actuelle
		type : objet

		param _ : etat dans lequel le bouton radio "rb_nb_marche" est (non utilise)
		type _ : boolean

		return : none

		'''

		
		cmds.intField (self.label_intField_nb_marche, edit=True, enable=True)
		cmds.intField (self.label_intField_hauteur, edit=True, enable=False)


	def intField_nb_marche_inactif (self, _):
		'''

		-> Rendre inaccessible la saisie pour le nombre de marche lorsque le bouton radio "rb_nb_marche" est inactif :

		param self : instance actuelle
		type : objet

		param _ : etat dans lequel le bouton radio "rb_nb_marche" est (non utilise)
		type _ : boolean

		return : none

		'''


		cmds.intField (self.label_intField_nb_marche, edit=True, enable=False)
		cmds.intField (self.label_intField_hauteur, edit=True, enable=True)


	def escalier (self):
		'''

		-> Creer la fenetre

		param self : instance actuelle
		type : objet

		return : none

		'''
		

		# ============================== #
		# - - VERIFICATIONS / SET-UP - - #
		# ============================== #
		

		# Fermer la fenetre si elle existe deja :
		if cmds.window (self.label_fenetre_generateur_escalier, query=True, exists=True):
			cmds.deleteUI (self.label_fenetre_generateur_escalier, window=True)
			cmds.windowPref (self.label_fenetre_generateur_escalier, remove=True)
			'''plus besoin pour la taille car je l'ai bloqué mais le faire pour la position, pour recentrer la fenetre'''
			'''WindowPref ne fonctionne pas'''

			# Supprimer la taille de la fenetre precedente :
			if cmds.windowPref (self.label_fenetre_generateur_escalier, query=True, exists=True):
				cmds.windowPref (self.label_fenetre_generateur_escalier, remove=True)
		
		# Creer et initialiser la fenetre :
		self.label_fenetre_generateur_escalier = cmds.window (self.label_fenetre_generateur_escalier, title=self.label_fenetre_generateur_escalier, topEdge=self.int_fenetre_position_haut, leftEdge=self.int_fenetre_position_gauche, sizeable=False)
		

		# ============================ #
		# - - ORGANISATION INTERNE - - #
		# ============================ #


		# Creer un layout, parent (zone pour y ajouter des elements) :
		cmds.columnLayout ()

		cmds.text (label=self.string_saut_ligne)

		# Creer un layout ajustable de quatre colonnes, (premier) enfant de "columnLayout" :
		cmds.rowColumnLayout (numberOfColumns=4, columnWidth=[(1,75), (2,150), (3,90), (4,75)], rowSpacing=[(1,10)])

		# - - - - - - - - - - - - - - - - - - - - - #
		#     BOUTONS RADIO ET ZONES DE SAISIE     #
		# - - - - - - - - - - - - - - - - - - - - - #

		# Remplir la cellule (ligne 1, colonne 1) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# Remplir la cellule (ligne 1, colonne 2) de "rowColumnLayout" :
		cmds.text (label=self.label_type_escalier, align="left")

		# Remplir la cellule (ligne 1, colonne 3) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# Remplir la cellule (ligne 1, colonne 4) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# ------------------------------------------------------------ #

		# Creer une collection de radio bouton qui contiendra automatiquement les boutons radio du choix de l'escalier voulu :
		rc_choix_escalier = cmds.radioCollection ()

		# Remplir la cellule (ligne 2, colonne 1) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# Remplir la cellule (ligne 2, colonne 2) de "rowColumnLayout" :
		# Creer le bouton radio "rb_escal_colimacon" qui permettra la creation d'un escalier en colimacon :
		rb_escal_colimacon = cmds.radioButton (label=self.label_rb_escal_colimacon)

		# Remplir la cellule (ligne 2, colonne 3) de "rowColumnLayout" :
		# Creer le bouton radio "rb_escal_droit" qui permettra la creation d'un escalier droit :
		rb_escal_droit = cmds.radioButton (label=self.label_rb_escal_droit)

		# Remplir la cellule (ligne 2, colonne 4) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		cmds.radioCollection (rc_choix_escalier, edit=True, select=rb_escal_colimacon)
		
		# ------------------------------------------------------------ #

		# Remplir la cellule (ligne 3, colonne 1) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# Remplir la cellule (ligne 3, colonne 2) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# Remplir la cellule (ligne 3, colonne 3) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# Remplir la cellule (ligne 3, colonne 4) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# ------------------------------------------------------------ #

		# Remplir la cellule (ligne 4, colonne 1) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# Remplir la cellule (ligne 4, colonne 2) de "rowColumnLayout" :
		cmds.text (label=self.label_choix_parametre, align="left")

		# Remplir la cellule (ligne 4, colonne 3) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# Remplir la cellule (ligne 4, colonne 4) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# ------------------------------------------------------------ #

		# Creer une collection de radio bouton qui contiendra automatiquement les boutons radio du choix du parametre utilise pour la creation :
		rc_choix_parametre = cmds.radioCollection ()

		# Remplir la cellule (ligne 5, colonne 1) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# Remplir la cellule suivante (ligne 5, colonne 2) de "rowColumnLayout" :
		# Creer le bouton radio "rb_nb_marche" qui gerera l'accessibilite des zones de saisies :
		rb_nb_marche = cmds.radioButton (label=self.label_rb_nb_marche, onCommand=self.intField_nb_marche_actif, offCommand=self.intField_nb_marche_inactif)

		# Remplir la cellule suivante (ligne 5, colonne 3) de "rowColumnLayout" :
		cmds.intField (self.label_intField_nb_marche)

		# Remplir la cellule suivante (ligne 5, colonne 4) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# ------------------------------------------------------------ #

		# Remplir la cellule suivante (ligne 6, colonne 1) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		# Remplir la cellule suivante (ligne 6, colonne 2) de "rowColumnLayout" :
		rb_hauteur = cmds.radioButton (label=self.label_rb_hauteur)

		# Remplir la cellule suivante (ligne 6, colonne 3) de "rowColumnLayout" :
		cmds.intField (self.label_intField_hauteur)

		# Remplir la cellule suivante (ligne 6, colonne 4) de "rowColumnLayout" :
		cmds.text (label=self.string_vide)

		cmds.radioCollection (rc_choix_parametre, edit=True, select=rb_nb_marche)
		
		# - - - - - - - - - #
		#      BOUTONS     #
		# - - - - - - - - - #

		# Sortir du layout enfant "rowColumnLayout" pour revenir a son parent "columnLayout" :
		cmds.setParent ("..")

		cmds.text (label=self.string_saut_ligne + self.string_saut_ligne)
		
		# Creer un layout a trois colonnes, second enfant de "columnLayout" :
		cmds.rowLayout (numberOfColumns=3, columnAlign3=["center","center","center"])

		cmds.button (self.label_bouton_generer_et_fermer,	width=130, command=lambda bouton_generer_et_fermer: cls_escalier_generateur().parametres_lancement(self.int_bouton_generer_et_fermer, self.label_fenetre_generateur_escalier, rb_escal_colimacon))
		
		cmds.button (self.label_bouton_generer,				width=130, command=lambda bouton_generer: cls_escalier_generateur().parametres_lancement(self.int_bouton_generer, self.label_fenetre_generateur_escalier, rb_escal_colimacon))

		cmds.button (self.label_bouton_fermer,				width=130, command=lambda bouton_fermer: cmds.deleteUI (self.label_fenetre_generateur_escalier))


		# =========================== #
		# --- RENDU DE LA FENETRE --- #
		# =========================== #


		cmds.showWindow (self.label_fenetre_generateur_escalier)





class cls_escalier_generateur (cls_escalier):
	'''

	-> Gestion de la creation d'un escalier :

	def parametres_lancement (self:objet, int_bouton_generer:int, label_fenetre_generateur_escalier:unicode, rb_escal_colimacon:unicode) : recuperer la saisie de l'utilisateur et lancer la generation de l'escalier suivant le bouton clique
	return : none

	def escalier_generateur (self:objet, int_valeur:int, rb_escal_colimacon:unicode) : generer l'escalier suivant la valeur donnee par l'utilisateur
	return : none

	'''


	def __init__ (self):


		super (cls_escalier_generateur, self).__init__ ()
		
		# Noms pour les objets 3D :
		self.string_escal					= "escal"
		self.string_element					= "element"
		self.string_elmt					= "elmt"
		self.string_colonne					= "colonne"
		self.string_fixation				= "fixation"
		self.string_marche					= "marche"
		self.string_garde_corps_1			= "garde_corps_1"
		self.string_garde_corps_2			= "garde_corps_2"
		
		# Nom pour un groupe "escalier" :
		self.string_escalier				= "escalier_1"
		
		# Dimensions des objets 3D :
		''' Ne pas les changer car la generation ne s'adapte pas '''
		self.int_marche_hauteur				= 15


		'''deplacer posX et rotation la ou ils sont vraiment utilises ?'''
		# Initialiser les attributs du premier "escal_"int_escalier_nb"_element"
		self.int_escal_elmt_posY			= 0
		self.int_escal_elmt_posX			= 0
		self.int_escal_elmt_rotation		= 0


	def parametres_lancement (self, int_bouton_generer, label_fenetre_generateur_escalier, rb_escal_colimacon):
		'''
		-> Recuperer la sasie de l'utilisateur et lancer la generation de l'escalier suivant le bouton clique :

		param self : instance actuelle
		type : objet

		param int_bouton_generer : chiffre utilise pour identifier le bouton clique
		type int_bouton_generer : int

		param label_fenetre_generateur_escalier : fenetre du programme
		type label_fenetre_generateur_escalier : unicode

		param rb_escal_colimacon : bouton radio permettant de decider quel escalier est cree 
		type rb_escal_colimacon : unicode

		return : none

		'''


		# Recuperer la "valeur" insere suivant la case active :
		if (cmds.intField (self.label_intField_nb_marche, query=True, enable=True) == True):
			int_valeur = cmds.intField (self.label_intField_nb_marche, query=True, value=1)

		else:
			int_valeur = cmds.intField (self.label_intField_hauteur, query=True, value=1)
			# Arrondir a l'entier inferieur :
			int_valeur = int_valeur/self.int_marche_hauteur

		# Agir suivant si "Generer" ou "Generer et fermer" est clique :
		if ((int_bouton_generer == self.int_bouton_generer) and (int_valeur > 0)):
			self.escalier_generateur (int_valeur, rb_escal_colimacon)

		elif ((int_bouton_generer == self.int_bouton_generer_et_fermer) and (int_valeur > 0)):
			self.escalier_generateur (int_valeur, rb_escal_colimacon)
			cmds.deleteUI (label_fenetre_generateur_escalier)
			'''+ remove windowPref ?'''
		else:
			cmds.confirmDialog (title="Valeur erronee !", message="Vous avez entre une valeur non correcte.", button=["Ok"], dismissString="Ok")	


	def escalier_generateur (self, int_valeur, rb_escal_colimacon):
		'''
		-> Generer l'escalier suivant la valeur donnee par l'utilisateur :

		param self : instance actuelle
		type : objet

		param int_valeur : donnee que l'utilisateur renseigne
		type int_valeur : int

		param rb_escal_colimacon : bouton radio permettant de decider quel escalier est cree 
		type rb_escal_colimacon : unicode

		return : none

		'''


		# Creer un groupe parent vide "escalier" :
		cmds.group (empty=True, name=self.string_escalier)
		
		# Recuperer le chiffre actuel d'iteration d' "escalier" par le nom actuel du groupe parent (utilisation de l'iteration automatique de Maya) :
		self.string_escalier = (cmds.ls (selection=True))[0]
		
		# Recuperer le chiffre actuel d'iteration d' "escalier" :
		int_escalier_nb = self.string_escalier [9]

		dict_switcher = {
				0:	cls_escalier_creation ().rotation,
				1:	cls_escalier_creation ().translation
			}

		for i in range (int_valeur):

			# ============================== #
			# --- CREATION DES OBJETS 3D --- #
			# ============================== #

			#debut de nom des objets
			string_objet_prefixe = self.string_escal + "_" + int_escalier_nb + "_" + self.string_elmt + "_" + str (i+1) + "_"
			'''pas moyen de faire  un appel à la def ou est cree rb_escal_colimacon pour l'appeller plutot que de le transmettre dans tous les appels de fonctions? 
			 PLUS deplacer la condition avant la boucle puis juste utiliser int_switcher'''
			if (cmds.radioButton (rb_escal_colimacon, query=True, select=True)):
				cls_escalier_creation ().escalier_colimacon (string_objet_prefixe)
				int_switcher = 0
			else:
				cls_escalier_creation ().escalier_droit (string_objet_prefixe)
				int_switcher = 1

			# Grouper les objets pour former un groupe "escal_"int_escalier_nb"_element" et le placer dans le groupe parent "escalier" :
			cmds.group (string_objet_prefixe + self.string_colonne,
						string_objet_prefixe + self.string_fixation,
						string_objet_prefixe + self.string_marche,
						string_objet_prefixe + self.string_garde_corps_1,
						string_objet_prefixe + self.string_garde_corps_2,
						name=self.string_escal + "_" + int_escalier_nb + "_" + self.string_element + "_" + str (i+1),
						parent=self.string_escalier)
			
			# Recuperer la position en y du bas de l'objet "colonne" :
			list_colonne_posY_bas = cmds.getAttr ((cmds.ls (selection=True)) [0] + "|" + string_objet_prefixe + self.string_colonne + ".boundingBoxMin")
			
			# Deplacer le point de pivot de "escal_"int_escalier_nb"_element" au centre bas de l'objet "colonne"
			cmds.xform (rotatePivot	= (list_colonne_posY_bas [0][0]+(26/2), list_colonne_posY_bas [0][1], list_colonne_posY_bas [0][2]+(26/2)),
						scalePivot	= (list_colonne_posY_bas [0][0]+(26/2), list_colonne_posY_bas [0][1], list_colonne_posY_bas [0][2]+(26/2)))


			# ============================== #
			# --- CREATION DE L'ESCALIER --- #
			# ============================== #

			
			# Lancer la fonction adequate suivant la version de l'escalier concerne
			dict_switcher.get (int_switcher, "empty") ()

			# Placer la marche
			cmds.move (0, self.int_escal_elmt_posY, 0, relative=True)
			self.int_escal_elmt_posY += self.int_marche_hauteur

		# Selection de l'ensemble de l'escalier genere
		cmds.select (self.string_escalier)





class cls_escalier_creation (cls_escalier_generateur):
	'''

	-> Creation de l'escalier :
		
	def escalier_colimacon (self:objet, string_objet_prefixe:string) : mettre en place l'escalier en colimacon
	return : none

	def escalier_droit (self:objet, string_objet_prefixe:string) : mettre en place l'escalier droit
	return : none

	def rotation (self:objet): pivoter chaque element d'escalier pour l'escalier en colimacon
	return : none
		
	def translation (self:objet): translater chaque element d'escalier pour l'escalier droit
	return : none

	'''


	def __init__ (self):


		super (cls_escalier_creation, self).__init__ ()


		# Dimensions des objets 3D :
		''' Ne pas les changer car la generation ne s'adapte pas '''
		self.int_colonne_rayon				= 13
		self.int_colonne_hauteur			= 15
		self.int_fixation_rayon				= 5
		self.int_fixation_hauteur			= 16
		self.int_marche_profondeur			= 35
		self.int_marche_largeur				= 120
		self.int_garde_corps_1_rayon		= 1
		self.int_garde_corps_1_hauteur		= 45
		self.int_garde_corps_2_rayon		= 1
		self.int_garde_corps_2_hauteur		= 66


	def escalier_colimacon (self, string_objet_prefixe):
		'''

		-> Mettre en place l'escalier en colimacon :

		param self : instance actuelle
		type : objet
		
		string_objet_prefixe : debut de nom des objets
		type : string

		return : none

		'''


		# Objet "colonne" :
		cmds.polyCylinder (axis=[0,1,0], radius=self.int_colonne_rayon, height=self.int_colonne_hauteur, subdivisionsZ=1, createUVs=3, constructionHistory=1, name=string_objet_prefixe + self.string_colonne)
		cmds.move (0, 7.5, 0)
		
		# Objet "fixation" :
		cmds.polyCylinder (axis=[0,0,1], radius=self.int_fixation_rayon, height=self.int_fixation_hauteur, createUVs=3, constructionHistory=1, name=string_objet_prefixe + self.string_fixation)
		cmds.move (2, 7, -18)

		# Objet "marche" :
		cmds.polyCube (axis=[0,1,0], width=self.int_marche_profondeur, height=self.int_marche_hauteur, depth=self.int_marche_largeur, createUVs=4, constructionHistory=1, name=string_objet_prefixe + self.string_marche)
		cmds.move (0, 7.5, -89)
		cmds.select(string_objet_prefixe + self.string_marche + "|" + ".e[8]")
		cmds.move (-29.60973, 0, 6.564316, relative=True)
		cmds.select(string_objet_prefixe + self.string_marche + "|" + ".e[5]")
		cmds.move (-10.044058, 0, 4.6923, relative=True)
		cmds.select(string_objet_prefixe + self.string_marche + "|" + ".e[4]")
		cmds.move (13.984512, 0 , 3.818729, relative=True)

		# Objet "garde_corps_1" :
		cmds.polyCylinder (axis=[0,1,0], radius=self.int_garde_corps_1_rayon, height=self.int_garde_corps_1_hauteur, createUVs=3, constructionHistory=1, name=string_objet_prefixe + self.string_garde_corps_1)
		cmds.move (15, 35.5, -146.5)

		# Objet "garde_corps_2" :
		cmds.polyCylinder (axis=[1,0,0], radius=self.int_garde_corps_2_rayon, height=self.int_garde_corps_2_hauteur, createUVs=3, constructionHistory=1, name=string_objet_prefixe + self.string_garde_corps_2)
		cmds.move (-16.5, 65.5, -142.85)
		cmds.rotate (0.8, 6.476, -13.623)


	def escalier_droit (self, string_objet_prefixe):
		'''

		-> Mettre en place l'escalier en colimacon :

		param self : instance actuelle
		type : objet
		
		string_objet_prefixe : debut de nom des objets
		type : string

		return : none

		'''


		# Objet "colonne" :
		cmds.polyCylinder (axis=[0,1,0], radius=self.int_colonne_rayon, height=self.int_colonne_hauteur + 23.1, subdivisionsZ=1, createUVs=3, constructionHistory=1, name=string_objet_prefixe + self.string_colonne)
		cmds.move (0, 7.5, 0)
		cmds.rotate (0, 0, 66.8)

		# Objet "fixation" :
		cmds.polyCylinder (axis=[0,0,1], radius=self.int_fixation_rayon, height=self.int_fixation_hauteur, createUVs=3, constructionHistory=1, name=string_objet_prefixe + self.string_fixation)
		cmds.move (2, 7, -18)
		
		# Objet "marche" :
		cmds.polyCube (axis=[0,1,0], width=self.int_marche_profondeur, height=self.int_marche_hauteur, depth=self.int_marche_largeur, createUVs=4, constructionHistory=1, name=string_objet_prefixe + self.string_marche)
		cmds.move (0, 7.5, -89)

		# Objet "garde_corps_1" :
		cmds.polyCylinder (axis=[0,1,0], radius=self.int_garde_corps_1_rayon, height=self.int_garde_corps_1_hauteur, createUVs=3, constructionHistory=1, name=string_objet_prefixe + self.string_garde_corps_1)
		cmds.move (15, 35.5, -146.5)

		# Objet "garde_corps_2" :
		cmds.polyCylinder (axis=[1,0,0], radius=self.int_garde_corps_2_rayon, height=self.int_garde_corps_2_hauteur - 27.8, createUVs=3, constructionHistory=1, name=string_objet_prefixe + self.string_garde_corps_2)
		cmds.move (-2.253, 65.517, -146.497)
		cmds.rotate (0.742, 0.102, -23.204)


	def rotation (self):
		'''

		-> Pivoter chaque element d'escalier pour l'escalier en colimacon

		param self : instance actuelle
		type : objet
		
		return : none

		'''


		cmds.rotate (0, self.int_escal_elmt_rotation, 0, relative=True)
		self.int_escal_elmt_rotation += 25


	def translation (self):
		'''

		-> Translater chaque element d'escalier pour l'escalier droit

		param self : instance actuelle
		type : objet
		
		return : none

		'''


		cmds.move (self.int_escal_elmt_posX, 0, 0, relative=True)
		self.int_escal_elmt_posX -= 35





# ######################################################### #
# ======================= LANCEMENT ======================= #
# ######################################################### #


cls_escalier().escalier()


'''
# adapter escalier en donnant des valeurs ?
# souci avec si la fenetre existe deja -> verif marche pas car window1, window2 ... donc jamais le meme nom pour la verif
#ma fenetre est recree a chaque fois car c'est une nouvelle instance a chaque fois que je cree
# freeze et delete history de tous les objets ?
#exceptions : try : except
#probleme iteration maya groupe escalier arriver a 10
'''