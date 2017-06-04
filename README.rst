``AutomaBot``
=============
.. image:: https://travis-ci.org/73VW/AutomaBot.svg?branch=master
    :target: https://travis-ci.org/73VW/AutomaBot

Par Maël Pedretti [#mp]_ et Dany Chea [#dc]_

(
introduction
tutoriel
api reference
developer documentation
)

Introduction
------------

Création d'un bot sur discord qui va servir de relais entre le client et le serveur, permettant une manipulation simple de fonctions domotiques, tel que le contrôle de l'allumage de lampe à distance.

Ce projet permet de faire une simulation d'acquisition des états des lampes en différents endroits, que l'on pourra observer via une page HTML.
Utilisateur enverra une commande au bot, qui va transmettre cette commande au serveur, et retransmettra sa réponse à l'utilisateur dans discord.



Tutoriel
--------
Lancement du bot
^^^^^^^^^^^^^^^^

Pour lancer le bot, il suffit d'exécuter le fichier  `__main__.py <automabot/__main__.py>`_ .

Lors du lancement du bot, celui-ci demandera quelques informations afin de créer son fichier de configuration, si celui-ci n'existe pas déjà au préalable.
Si il s'agit du premier lancement, il faudra indiquer les éléments suivants:

- le token du bot Discord, que l'on peut récuperer sur Discord ()
- le host
- le port
- l'id du channel discord sur lequel le bot va répondre
- le préfixe des commandes qui permet d'appeler le bot
- l'url du serveur sur lequel envoyer les requêtes GET
- l'url du serveur sur lequel envoyer les requêtes POST

Liste des commandes
^^^^^^^^^^^^^^^^^^^

Afin de lister les commandes du bot, il faut taper la commande help, précédée par le motif de préfix donnée dans le fichier de configuration.

- help: affiche le message d'aide qui va lister les commandes
- light get : permet de voir l'état d'une lumière
- light set : permet d'allumer ou d'éteindre une lampe
- sleep : permet de mettre le bot en veille
- wakeup : permet de réveiller le bot

Les commandes sleep et wakeup ne sont disponible que par le propriétaire du channel, ou par Maël Pedretti. [#mp]_





.. [#mp] <mael.pedretti@he-arc.ch>
.. [#dc] <dany.chea@he-arc.ch>
