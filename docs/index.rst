.. automabot documentation master file, created by
   sphinx-quickstart on Thu Jun  8 09:35:26 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to automabot's documentation!
=====================================

.. toctree::
    :maxdepth: 2
    :caption: Contents:

``AutomaBot``
=============

.. image:: https://travis-ci.org/73VW/AutomaBot.svg?branch=master
    :target: https://travis-ci.org/73VW/AutomaBot
    :alt: Build Status

.. image:: https://badge.fury.io/py/automabot.svg
    :target: https://badge.fury.io/py/automabot
    :alt: PyPi Version

.. image:: https://readthedocs.org/projects/automabot/badge/?version=latest
    :target: http://automabot.readthedocs.io/fr/latest/?badge=latest
    :alt: Documentation Status

Par Maël Pedretti [#mp]_ et Dany Chea [#dc]_

Introduction
------------

Création d'un bot sur discord qui va servir de relais entre le client et le serveur, permettant une manipulation simple de fonctions domotiques, tel que le contrôle de l'allumage de lampes à distance.

Ce projet permet de faire une simulation d'acquisition des états des lampes en différents endroits, que l'on pourra observer via une page HTML.
L'tilisateur enverra une commande au bot, qui va transmettre cette commande au serveur, et retransmettra sa réponse à l'utilisateur dans discord.

Si l'état des lampes est changé depuis une autre plateforme que le bot, le bot transmettra une notification dans le channel entré dans les paramètres.



Tutoriel
--------
Installation du bot
^^^^^^^^^^^^^^^^^^^

Pour installer le bot il suffit d'éxecuter la commande suivante

.. code-block:: console

    $ pip install automabot

Lancement du bot
^^^^^^^^^^^^^^^^

Pour lancer le bot, il suffit d'exécuter

.. code-block:: console

    $ automabot

Lors du lancement du bot, celui-ci demandera quelques informations afin de créer son fichier de configuration, si celui-ci n'existe pas déjà au préalable.
S'il s'agit du premier lancement, il faudra indiquer les éléments suivants:

    - le token du bot Discord, que l'on peut récuperer sur `le portail développers de Discord <https://discordapp.com/developers/applications/me>`_
    - le host du server de notifications
    - le port du server de notifications
    - l'id du channel discord sur lequel le bot va transmettre les notifications
    - le préfixe des commandes qui permet d'appeler le bot
    - l'url du serveur sur lequel envoyer les requêtes pour connaître l'état des lampes
    - l'url du serveur sur lequel envoyer les requêtes pour changer l'état des lampes

Liste des commandes
^^^^^^^^^^^^^^^^^^^

Afin de lister les commandes du bot, il faut taper la commande help, précédée par le motif de préfix donnée dans le fichier de configuration.

    - help: affiche le message d'aide qui va lister les commandes
    - light get : permet de voir l'état d'une lumière
    - light set : permet d'allumer ou d'éteindre une lampe
    - sleep : permet de mettre le bot en veille
    - wakeup : permet de réveiller le bot

Les commandes sleep et wakeup ne sont disponibles que pour le propriétaire du channel, ou par Maël Pedretti. [#mp]_

    .. [#mp] <mael.pedretti@he-arc.ch>
    .. [#dc] <dany.chea@he-arc.ch>
