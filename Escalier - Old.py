""" +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ """
""" ############### GENERATION D'UN ESCALIER EN COLIMACON ############### """
""" +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ """





# ######################################################### #
# ======================= LIBRAIRIES ====================== #
# ######################################################### #


from maya import cmds





# ######################################################### #
# ======================== VARIABLES ====================== #
# ######################################################### #


# Dimensions des objets 3D :
# Ne pas les changer car la generation ne s'adapte pas.
colonne_rayon			= 13
colonne_hauteur			= 15
fixation_rayon			= 5
fixation_hauteur		= 16
marche_hauteur			= 15
marche_profondeur		= 35
marche_largeur			= 120
garde_corps_1_rayon		= 1
garde_corps_1_hauteur	= 45
garde_corps_2_rayon		= 1
garde_corps_2_hauteur	= 66

# Noms pour les objets 3D :
escal				= "escal"
element				= "element"
elmt				= "elmt"
colonne				= "colonne"
fixation			= "fixation"
marche				= "marche"
garde_corps_1		= "garde_corps_1"
garde_corps_2		= "garde_corps_2"

# Noms des elements de la fenetre et sa gestion :
fenetre_generateur_d_escalier_titre		= "Generateur d'escalier en colimacon"
fenetre_position_haut					= 430
fenetre_position_gauche					= 700
rb_nb_marche_label						= "Le nombre de marche : "
rb_hauteur_label						= "La hauteur : "
intField_nb_marche						= "nb_marche"
intField_hauteur						= "hauteur"
boutton_generer_et_fermer_label			= "Generer et fermer"
boutton_generer_label					= "Generer"
boutton_fermer_label					= "Fermer"
boutton_generer_et_fermer_valeur		= 1
boutton_generer_valeur					= 0


fenetre_generateur_escalier = 			"fenetre"





# ######################################################### #
# ======================= PROCEDURES ====================== #
# ######################################################### #


def intField_nb_marche_actif (*args):
	'''
	-> Rendre accessible la saisie pour le nombre de marche lorsque le boutton radio "rb_nb_marche" est actif :
	param *args : etat dans lequel le boutton radio "rb_nb_marche" est (non utilise).
	type *args : boolean
	'''

	
	cmds.intField (intField_nb_marche, edit=True, enable=True)
	cmds.intField (intField_hauteur, edit=True, enable=False)


def intField_nb_marche_inactif (*args):
	'''
	-> Rendre inaccessible la saisie pour le nombre de marche lorsque le boutton radio "rb_nb_marche" est inactif :
	param *args : etat dans lequel le boutton radio "rb_nb_marche" est (non utilise).
	type *args : boolean
	'''


	cmds.intField (intField_nb_marche, edit=True, enable=False)
	cmds.intField (intField_hauteur, edit=True, enable=True)


def lancement_generation (bouton_clique):
	'''
	-> Recuperer la sasie de l'utilisateur et generer l'escalier suivant le bouton clique :
	param bouton_clique : chiffre utilise pour identifier le boutton clique.
	type bouton_clique : int
	'''


	# Recuperer la "valeur" insere suivant la case active :
	if (cmds.intField (intField_nb_marche, query=True, enable=True) == True):
		valeur = cmds.intField (intField_nb_marche, query=True, value=1)

	else:
		valeur = cmds.intField (intField_hauteur, query=True, value=1)
		# Arrondir a l'entier inferieur :
		valeur = valeur/marche_hauteur


	# Agir suivant si "Generer" ou "Generer et fermer" est clique :
	if ((bouton_clique == boutton_generer_valeur) and (valeur > 0)):
		generation_escalier (valeur)

	elif ((bouton_clique == boutton_generer_et_fermer_valeur) and (valeur > 0)):
		generation_escalier (valeur)
		cmds.deleteUI (fenetre_generateur_escalier, window=True)

	else:
		cmds.confirmDialog (title="Mauvaise valeur !", message="Vous avez entre une valeur non correcte.", button=["Ok"], dismissString="Ok")


def generation_escalier (valeur):
	'''
	-> Generer l'escalier suivant la valeur donnee par l'utilisateur :
	param valeur : donnee que l'utilisateur renseigne.
	type valeur : int
	'''


	# Nom pour un groupe "escalier" : 
	escalier = "escalier_1"

	# Creer un groupe parent vide "escalier" :
	cmds.group (empty=True, name=escalier)
	
	# Recuperer le chiffre actuel d'iteration d' "escalier" par le nom actuel du groupe parent (utilisation de l'iteration automatique de Maya) :
	escalier = (cmds.ls (selection=True))[0]
	
	# Recuperer le chiffre actuel d'iteration d' "escalier" :
	escalier_nb = escalier[9]

	# Initialiser les variables du premier "escal_"escalier_nb"_element"
	escal_elmt_posY = 0
	escal_elmt_rotation = 0
	
	for i in range (valeur):
		objet_nom_prefixe = escal + "_" + escalier_nb + "_" + elmt + "_" + str(i+1) + "_"

		# Objet "colonne" :
		cmds.polyCylinder (axis=[0,1,0], radius=colonne_rayon, height=colonne_hauteur, subdivisionsZ=1, createUVs=3, constructionHistory=1, name=objet_nom_prefixe + colonne)
		cmds.move (0, 7.5, 0)

		# Objet "fixation" :
		cmds.polyCylinder (axis=[0,0,1], radius=fixation_rayon, height=fixation_hauteur, createUVs=3, constructionHistory=1, name=objet_nom_prefixe + fixation)
		cmds.move (2, 7, -18)

		# Objet "marche" :
		cmds.polyCube (axis=[0,1,0], width=marche_profondeur, height=marche_hauteur, depth=marche_largeur, createUVs=4, constructionHistory=1, name=objet_nom_prefixe + marche)
		cmds.move (0, 7.5, -89)
		cmds.select(objet_nom_prefixe + marche + "|" + ".e[8]")
		cmds.move (-29.60973, 0, 6.564316, relative=True)
		cmds.select(objet_nom_prefixe + marche + "|" + ".e[5]")
		cmds.move (-10.044058, 0, 4.6923, relative=True)
		cmds.select(objet_nom_prefixe + marche + "|" + ".e[4]")
		cmds.move (13.984512, 0 , 3.818729, relative=True)

		# Objet "garde_corps_1" :
		cmds.polyCylinder (axis=[0,1,0], radius=garde_corps_1_rayon, height=garde_corps_1_hauteur, createUVs=3, constructionHistory=1, name=objet_nom_prefixe + garde_corps_1)
		cmds.move (15, 35.5, -146.5)

		# Objet "garde_corps_2" :
		cmds.polyCylinder (axis=[1,0,0], radius=garde_corps_2_rayon, height=garde_corps_2_hauteur, createUVs=3, constructionHistory=1, name=objet_nom_prefixe + garde_corps_2)
		cmds.move (-16.5, 65.5, -142.85)
		cmds.rotate (0.8, 6.476, -13.623)

		# Grouper les objets pour former un groupe "escal_"escalier_nb"_element" et le placer dans le groupe parent "escalier" :
		cmds.group (objet_nom_prefixe + colonne,
					objet_nom_prefixe + fixation,
					objet_nom_prefixe + marche,
					objet_nom_prefixe + garde_corps_1,
					objet_nom_prefixe + garde_corps_2,
					name=escal + "_" + escalier_nb + "_" + element + "_" + str(i+1),
					parent=escalier)
		
		# Recuperer la position en y du bas de l'objet "colonne" :
		colonne_posY_bas = cmds.getAttr (escalier + "|" + (cmds.ls (selection=True))[0] + "|" + objet_nom_prefixe + colonne + ".boundingBoxMin")
		
		# Deplacer le point de pivot de "escal_"escalier_nb"_element" au centre bas de l'objet "colonne"
		cmds.xform (rotatePivot		=(colonne_posY_bas[0][0]+(26/2), colonne_posY_bas[0][1], colonne_posY_bas[0][2]+(26/2)),
					scalePivot		=(colonne_posY_bas[0][0]+(26/2), colonne_posY_bas[0][1], colonne_posY_bas[0][2]+(26/2)))
		
		# Positioner chaque "escal_"escalier_nb"_element"
		cmds.rotate (0, escal_elmt_rotation, 0, relative=True)
		escal_elmt_rotation += 25
		cmds.move (0, escal_elmt_posY, 0, relative=True)
		escal_elmt_posY += 15
	
	# Deplacer le point de pivot du groupe "escalier" au meme endroit que celui de la premiere colonne :
	#cmds.select (escalier)
	#cmds.xform (rotatePivot		=(colonne_posY_bas[0][0]+(26/2), colonne_posY_bas[0][1], colonne_posY_bas[0][2]+(26/2)),
				#scalePivot		=(colonne_posY_bas[0][0]+(26/2), colonne_posY_bas[0][1], colonne_posY_bas[0][2]+(26/2)))

	



	'''
	# adapter escalier en donnant des valeurs ?
	# faire des classes
	# onglets pour escalier droit
	# souci avec si la fenetre existe deja
	'''





# ######################################################### #
# ========================= FENETRE ======================= #
# ######################################################### #


# ============================== #
# - - VERIFICATIONS / SET-UP - - #
# ============================== #


# Fermer la fenetre si elle existe deja :
if cmds.window (fenetre_generateur_escalier, exists=True):
	cmds.deleteUI (fenetre_generateur_escalier, window=True)
	
	# Supprimer la taille de la fenetre precedente :
	if cmds.windowPref (fenetre_generateur_escalier, exists=True):
		cmds.windowPref (fenetre_generateur_escalier, remove=True)

# Creation et initialisation de la fenetre :
fenetre_generateur_escalier = cmds.window (title=fenetre_generateur_d_escalier_titre, topEdge=fenetre_position_haut, leftEdge=fenetre_position_gauche, sizeable=False)


# ============================ #
# - - ORGANISATION INTERNE - - #
# ============================ #


# Creer un layout, parent (zone pour y ajouter des elements) :
cmds.columnLayout ()

cmds.text (label="\n")

# Creer un layout ajustable de quatre colonnes, (premier) enfant de "columnLayout" :
cmds.rowColumnLayout (numberOfColumns=4, columnWidth=[(1,75), (2,150), (3,90), (4,75)], rowSpacing=[(1,10)])

# - - - - - - - - - - - - - - - - - - - - - #
#     BOUTTONS RADIO ET ZONES DE SAISIE     #
# - - - - - - - - - - - - - - - - - - - - - #

# Creer une collection de radio bouton qui contiendra les radio bouttons automatiquement :
radio_button_choix = cmds.radioCollection ()

# Remplir la premiere cellule (ligne 1, colonne 1) de "rowColumnLayout" :
cmds.text (label="")

# Remplir la cellule suivante (ligne 1, colonne 2) de "rowColumnLayout" :
# Creer le boutton radio "rb_nb_marche" qui gerera l'accessibilite des zones de saisies :
rb_nb_marche = cmds.radioButton (label=rb_nb_marche_label, onCommand=intField_nb_marche_actif, offCommand=intField_nb_marche_inactif)

# Remplir la cellule suivante (ligne 1, colonne 3) de "rowColumnLayout" :
cmds.intField (intField_nb_marche)

# Remplir la cellule suivante (ligne 1, colonne 4) de "rowColumnLayout" :
cmds.text (label="")

# Remplir la cellule suivante (ligne 2, colonne 1) de "rowColumnLayout" :
cmds.text (label="")

# Remplir la cellule suivante (ligne 2, colonne 2) de "rowColumnLayout" :
rb_hauteur = cmds.radioButton (label=rb_hauteur_label)

# Remplir la cellule suivante (ligne 2, colonne 3) de "rowColumnLayout" :
cmds.intField (intField_hauteur)

# Remplir la cellule suivante (ligne 2, colonne 4) de "rowColumnLayout" :
cmds.text (label="")

cmds.radioCollection (radio_button_choix, edit=True, select=rb_nb_marche)

# - - - - - - - - - #
#      BOUTTONS     #
# - - - - - - - - - #

# Sortir du layout enfant "rowColumnLayout" pour revenir a son parent "columnLayout" :
cmds.setParent ("..")

cmds.text (label="\n\n")

# Creer un layout a trois colonnes, second enfant de "columnLayout" :
cmds.rowLayout (numberOfColumns=3, columnAlign3=["center","center","center"])

cmds.button (boutton_generer_et_fermer_label, 	width=130, command="lancement_generation (boutton_generer_et_fermer_valeur)")

cmds.button (boutton_generer_label, 			width=130, command="lancement_generation (boutton_generer_valeur)")

cmds.button (boutton_fermer_label, 				width=130, command="cmds.deleteUI (fenetre_generateur_escalier)")


# =========================== #
# --- RENDU DE LA FENETRE --- #
# =========================== #


cmds.showWindow (fenetre_generateur_escalier)