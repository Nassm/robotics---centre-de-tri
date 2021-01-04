#2 Comprendre la représentation d'un robot ROS

#2.1 Comprendre le descripteur URDF#
**Que représentent les rectangles ?** 
R : Ce sont les accroches, ici structures imprimées

**Que représentent les bulles ?**
R : Ce sont les jointures, ici les cervomoteurs

**Que représentent les flèches et surtout les valeurs `xyz` et `rpy` associées ?**
R : "XYZ", c'est le degré de liberté, ici base_link-m1 varie en z
"RPY", c'est la rotation autour des axes fixes (roll, pitch, yaw)


#2.2 Comprendre les E/S du contrôleur#
#Topics du robot
**Quel est son nom ?**
R : /joint_states

**Quel est le type de message qu'il transmet ?**
R : sensor_msgs/joinState

**A quelle fréquence (en Hertz) est-ce qu'il met à jour l'état des joints ?**
R: 30Hz
 

#Services du robot
**Quel est son nom ?** 
R : /set_compliant

**Quel est le type de service qu'il transmet ?** 
R : Un service de type : std_srvs/SetBool 


**Quels sont les champs de la requête de ce service ?**
R : un champ data qui est de type boolean

**Quels sont les champs de la réponse de ce service ?**
R : success de type boolean et message de type string


**Appelez ce service pour activer et désactiver le mode compliant et essayer de faire bouger votre robot à la main à chaque fois. Que déduisez-vous de la signification du mode compliant ?** 
R : à #true#, les moteurs ramolissent et sont manipulable à la main. Quand compliance est #is_disable#, les moteurs retrouvent leurs état normal, solide et non manipulable à la main.




#3. Cinématique, et planification avec MoveIt dans RViz
#3.2 Planification#
**Que désigne le robot gris parfois mobile mais lent ?**
R : C'est la position actuelle du robot

**Que désigne le robot orange (fixe) ?**
R : C'est la position cible


**Que désigne le robot gris qui répète infiniment un mouvement rapide ?**
R : C'est le mouvement prévue pour atteindre la position destination

**Dans RViz, activer l'affichage du modèle de collision dans `Displays`, `Scene Robot`, `Show Robot Collision`, quelle est la forme de ce modèle utilisé par OMPL pour simplifier le calcul des collisions ?**
R : N/A


#3.3 Planning groups#
**Quelle est la différence entre ces 2 groupes ?**
R : Le premier permet de manipuler la pince et le bras, le seocnd seulement le bras

**Quel est le groupe pour lequel le goal est le plus facilement manipulable et pourquoi ?** 
R : Arm_and_finger car l'ensemble des moteurs peut être diriger


**Déduisez-en une proposition sur ce que désigne un planning group.**
R : Un planning peut-être considéré comme un ensemble de composant du robot que l'on voudrait diriger simultanément.


##3.4 Transformations `tf`#
**Comment est nommé le repère de base ?** 
R : Base_link

**Comment sont nommés les deux effecteurs finaux possibles ?**
R : fixed_tip et moving_tip
