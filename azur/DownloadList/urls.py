from django.urls import path
from . import views

urlpatterns = [

    #redirection
    path('',views.view_redirection,name="redirect"),

    #listes des fichiers disponibles
    path('series/<int:id_page>', views.view_Series,name='afficher_series'),
    path('films/<int:id_page>', views.view_Films,name='afficher_films'),
    path('logiciels/<int:id_page>', views.view_Logiciels,name='afficher_logiciels'),
    path('jeux/<int:id_page>', views.view_Jeux,name='afficher_jeux'),
    path('livres/<int:id_page>', views.view_Livres,name='afficher_livres'),
    path('musiques/<int:id_page>', views.view_Musiques,name='afficher_musiques'),

    #zone d'ajout de fichiers
    path('addfiles/<int:cible>/<str:nom_recherche>',views.view_addfiles,name="add_files"),

    #connexion
    path('connexion',views.view_connexion,name="connexion"),
    path('inscription',views.view_inscription,name="inscription"),
    path('deconnexion', views.view_deconnexion, name='deconnexion'),

    #accueil
    path('accueil',views.view_accueil,name="accueil"),
    path('accueil/<int:inscription>',views.view_accueil,name="accueil"),

    #telechargements
    path('telechargement_film/<str:titre>/<str:annee>',views.view_telechargement_film,name="telechargement_film"),
    path('telechargement_serie/<str:titre>/<str:annee>',views.view_telechargement_serie,name="telechargement_serie"),
    path('telechargement_jeu/<str:nom>/<str:annee>',views.view_telechargement_jeu,name="telechargement_jeu"),
    path('telechargement_logiciel/<str:nom>/<str:annee>',views.view_telechargement_logiciel,name="telechargement_logiciel"),
    path('telechargement_livre/<str:nom>/<str:auteur>',views.view_telechargement_livre,name="telechargement_livre"),
    path('telechargement_musique/<str:artiste>/<str:titre>',views.view_telechargement_musique,name="telechargement_musique"),

    #Asklist
    path('Demandes',views.view_list_demandes,name="liste_demandes"),
    path('Demander',views.view_demander,name="demander"),
    path('removeSerieDemande/<str:nom>/<str:langage>/<str:soustitre>',views.view_removeSerieDemande,name="remove_serie"),
    path('removeFilmDemande/<str:nom>/<str:langage>/<str:soustitre>',views.view_removeFilmDemande,name="remove_film"),
    path('removeMusiqueDemande/<str:nom>',views.view_removeMusiqueDemande,name="remove_musique"),
    path('removeJeuDemande/<str:nom>',views.view_removeJeuDemande,name="remove_jeu"),
    path('removeLogicielDemande/<str:nom>',views.view_removeLogicielDemande,name="remove_logiciel"),
    path('removeLivreDemande/<str:nom>',views.view_removeLivreDemande,name="remove_livre"),

    #Recherche
    path('RechercheFilm/<str:nom>/<int:id_page>',views.view_recherche_film,name="recherche_film"),
    path('RechercheSerie/<str:nom>/<int:id_page>',views.view_recherche_serie,name="recherche_serie"),
    path('RechercheJeu/<str:nom>/<int:id_page>',views.view_recherche_jeu,name="recherche_jeu"),
    path('RechercheLogiciel/<str:nom>/<int:id_page>',views.view_recherche_logiciel,name="recherche_logiciel"),
    path('RechercheMusique/<str:nom>/<int:id_page>',views.view_recherche_musique,name="recherche_musique"),
    path('RechercheLivre/<str:nom>/<int:id_page>',views.view_recherche_livre,name="recherche_livre"),

    #Suppression fichier
    path('Supprimer_Film/<str:nom>',views.view_supprimerfilm,name="supprimerfilm"),
    path('Supprimer_Serie/<str:nom>',views.view_supprimerserie,name="supprimerserie"),
    path('Supprimer_Jeu/<str:nom>',views.view_supprimerjeu,name="supprimerjeu"),
    path('Supprimer_Logiciel/<str:nom>',views.view_supprimerlogiciel,name="supprimerlogiciel"),
    path('Supprimer_Livre/<str:nom>',views.view_supprimerlivre,name="supprimerlivre"),
    path('Supprimer_Musique/<str:artiste>/<str:titre>',views.view_supprimermusique,name="supprimermusique"),

    #modification fichier
    path('Modifier_Film/<str:nom>',views.view_modifierfilm,name="modifierfilm"),
    path('Modifier_Serie/<str:nom>',views.view_modifierserie,name="modifierserie"),
    path('Modifier_Jeu/<str:nom>',views.view_modifierjeu,name="modifierjeu"),
    path('Modifier_Logiciel/<str:nom>',views.view_modifierlogiciel,name="modifierlogiciel"),
    path('Modifier_Livre/<str:nom>',views.view_modifierlivre,name="modifierlivre"),
    path('Modifier_Musique/<str:artiste>/<str:titre>',views.view_modifiermusique,name="modifiermusique"),
]