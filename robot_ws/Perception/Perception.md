1.1 Présentation des données
**Quelle est la forme du tableau? À quoi corresponde ces dimensions ?**
R : C'est un tablau à 3 dimensions. La dimension 1 (imag.shape[0]) correction aux colonnes de l'image, la dimension 2 (imag.shape[1]) aux lignes et dimension 3 (imag.shape[2]) au pixel, c'est à dire les intensités de valeurs RGB de chaque pixel de l'image


**Observez les valeurs minimales et maximales du tableau. Sont elles les même pour toutes les images ?**
R : Non, elles ne sont pas les mêmes pour les valeurs max


**Quel est le type des données enregistrées dans le tableau numpy? Pourquoi est-ce le cas? Ce type de donnée est il adapté aux réseaux de neurones ?**
R : Le type de données est du UINT8. Parce-que les valeurs de pixels sont entre 0 et 255. Oui elles sont adaptés


**De manière générale, trouvez vous que la face des cubes est semblable aux images du dataset mnist que nous allons devoir utiliser pour l'apprentissage ?**
R : Non car couleurs inversées sur Datset mnist



1.2 Segmentation de l'image
**----------**
**Pouvez vous penser à plusieurs manière de transformer une image en RGB en une image en niveaux de gris ?**
R : Oui. Pour convertir une image RGB en niveau de gris il faut remplacer, pour chaque pixel les trois valeurs RGB par une seule valeur représentant la luminosité. Cette valeur est : Luminosity = 0.21 × R + 0.72 × G + 0.07 × B


**Y a t il une différence à utiliser une méthode en particulier ?**
R : Non


**Quelle est la taille de l'image maintenant ?**
R : C'est une matrice 2D de taille 480x640


**Quels sont les valeurs maximales et minimales ?**
R : 6.39 et 166.77


**Quel est le type de donnée ? Est il le même ou a t il changé ?**
R : Non, le type de donnée est différent


**Quel est maintenant le type des données de l'image ?**
R : float64


**Observez ces différentes images. Les cubes sont ils entièrement classifiés comme tels ?** 
R : oui elles le sont.


**Qu'en est il des écritures se trouvant sur les faces ?**
R : nettement plus visible


**La segmentation vous semble elle satisfaisante par rapport au problême ?**
R : Oui, car on peut poursuivre le traitement avec les images résultants


**Observez attentivement les images issues de l'opération de seuillage. Voyez vous des zones qui pourraient être séparées alors qu'elles ne couvrent pas un cube entier ?**
R : Aucune zone détecté


**Quelle est la signification de ces opérations? Détaillez. ?**
R : Supression de trou noir et zone blanche en vue de rendre plus visible les contours


**En quoi pensez vous que ces opérations puissent améliorer notre segmentation ?**
R : Pour mieux visualiser les contours


**OQuelle est l'utilité du paramètre de voisinage? Comment pensez vous pouvoir le régler ?**
R : C'est élément de décision qui permet l'ajout ou la suppression d'un pixel sur la couleur majoritaire de ces voisins 


**Quelle implémentations vous semble la plus rapide entre les deux ?**
R : Skimage est implémenté en python, ce qui implique une baisse de performance comparé à Spicy oû la performance est élevée

**Comment avez vous réglé le paramètre de voisinage? Quelle valeur avez vous choisi ?**
R :Suivant le rendu des tests

**Quelle valeur avez vous choisi ?**
-> nous avons choisie 3,3


**Les défauts de l'image binaire ont ils disparu ?**
R : Oui


**La segmentation vous semble t elle satisfaisante ?**
R : Oui


**Quelles méthodes avez vous utilisé pour nettoyer la forme?**
-> Le "convex_hull_object" qui calcule l'image convexe de la coque des objets individuels dans une image binaire




1.3 Recherche des contours
**-----**
**Quelles stratégie avez vous adopté pour extraire les coins ?**
R : 1- Determination des contours de l'objet
    2- Determination du centre du carrré
    3- Determination des 4 points les plus éloignés de ce centre


**Relancez le script pour faire défiler quelques images dont les coins ont étédétectés. Comment marche votre algorithme ?**
R : 1- Traitement de l'image (greyscale, thresholding, binarisation...)
    2- Détermination des contours possible et stockage dans un tableau
    3- Analyse du tableau et recupération des 4 contours les plus éloignés du centre.



1.4 Extraction des vignettes
**Qu'est ce qu'une transformation projective ?**
R : Une transformations projective est une des transformations en géométrie projective. Elle s'obtient comme composée d'un nombre fini de projections centrales. Elle décrit ce qui arrive aux positions observées de différents objets quand l'œil de l'observateur change de place.


**Sur quelles hypothèses est basé l'algorithme d'extraction de vignettes ?**
R : 1- Différence de couleur 
    2- Reconnaisance de forme


**Dans les données d'essais dont nous disposons, arrive-t-il que ces hypothèses soient brisées ?**
R : Oui. C'est le cas de dualité cubique ou la reconnaissance considére la forme comme une unique entité.


**Pouvez vous penser à des situations dans laquelle notre robot pourrait se trouver, qui briseraient également ces hypothèses ?**
R : N/D





3.1 Chargement des données
**-------------**

**Que contiennent les variables x_train et y_train?** 
R : Forme, type, valeur_min et valeur_min de l'image


**Pourquoi la fonction load_data renvoie-t-elle également les variables x_test et y_test?**
R : Afin de verifier l'exactitude entre test precedent et resultat courant


**Quelles sont les formes respectives de x_train et y_train?**
R : x_train est une forme à trois dimensions (30596, 28, 28)
    y_train est une forme à trois dimension ()


**Pouvez vous expliquer à quoi correspondent chacune des dimensions de ces deux tableaux?**
R : Nombre de d'echantillons, longueur et largeur de l'image


**Quelles sont les valeurs minimales et maximales de ces deux tableaux? De quel type sont les données ? Expliquez.**
R : min : 0, max: 255 
    min : 0 , max: 4
    Les données sont de type uint8 et cela represente les couleurs





3.2 Pré-visualisation des données brutes
**-----------------**

**Quelle sont les valeurs des pixels blancs (représentés en jaune) et des pixels noirs?**
R : Les pixels blancs ont une valeur proche de 255 et les pixels noirs une valeur proche de 0


**Observez bien les données et leurs labels. Toutes les images sont elles simples à classifier correctement?** 
R : Non


**Feriez vous des erreurs en les classifiant?**
R : Non




3.3 Préparation des données
**--------------------**

**Quelle est la forme de `x_train` maintenant**
R : (30596, 28 , 28 , 1)

**Quelles sont les valeurs min et max ?**
R : min is -0.423428208415
    max is 2.81233257579


**Est ce que cela convient bien à notre pré-requis?**
R : Non ecart type invalide


**Le type de donnée devrait avoir changé? Quel est il? Sur quel type de donnée pensez vous qu'un réseau de neurone travaille?**
R : C'est du float64. Sur des données de type float


**Qu'est ce qu'un one-hot-encoding? En quoi est ce différent des données dont nous disposons actuellement?**
R : C'est un encode qui permet de représenter des états en utilisant pour chacun, une valeur dont la représentation binaire n'a qu'un chiffre. 
Parce-que nous representons un echantillon avec pour chaucun un element du tableau qui represente le one-hot.


**Observez la fonction `load_data`. A quoi sert la variable globale `CLASSES`?**
R : Permet de comparer nos données a la variables "CLASSES", si nous avons un element est vrai, alors il est enregistré,
Cela permet de detemriner et de selectionner le chiffre auquel correspond l'image.


**Quelle est la forme de `y_train` maintenant ?**
R : float32

**Quelles sont les valeurs min et max ? Est ce que cela convient bien à notre pré-requis?**
R : min is 0.0
    max is 1.0
Oui, correspond
