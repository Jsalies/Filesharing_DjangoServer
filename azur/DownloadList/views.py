from django.http import HttpResponse
from django.shortcuts import render
from .forms import Addseries, Addfilms, Addmusiques, Addlogiciels, Addjeux, Addlivres, ConnexionForm, InscriptionForm, searchbar, askSerie,askFilm,askJeu,askLogiciel,askMusique,askLivre,modifierfilm,modifierserie,modifierjeu,modifierlogiciel,modifiermusique,modifierlivre
from .models import series,films,livres,jeux,logiciels,musiques,userprofil,ask_film,ask_serie,ask_musique,ask_jeu,ask_logiciel,ask_livre
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q

def view_redirection(request):
	return redirect("accueil")

def view_recherche_film(request,nom,id_page=1):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')


    liste_films=films.objects.filter(titre__contains=nom)
    pagination=Paginator(liste_films,12,orphans=4)
    if 1 > id_page:
        id_page=1
    elif id_page > pagination.num_pages:
        id_page= pagination.num_pages
    # liste des musiques pour la page à afficher
    liste_films=pagination.page(id_page).object_list
    # page actuelle
    currentpage=pagination.page(id_page)

    liste_pagination=[1]
    for i in range(2,pagination.num_pages+1):
        if i in [pagination.num_pages,id_page,id_page+5,
        id_page-10,id_page-20,id_page-1,id_page+5,id_page+10,id_page+20,id_page+1]:
            if i-liste_pagination[-1]>1:
                liste_pagination.append("...")
            liste_pagination.append(i)

    return render(request, 'recherche_films.html', locals())

def view_recherche_serie(request,nom,id_page=1):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    liste_series=series.objects.filter(titre__contains=nom)
    pagination=Paginator(liste_series,12,orphans=4)
    if 1 > id_page:
        id_page=1
    elif id_page > pagination.num_pages:
        id_page= pagination.num_pages
    # liste des musiques pour la page à afficher
    liste_series=pagination.page(id_page).object_list
    # page actuelle
    currentpage=pagination.page(id_page)

    liste_pagination=[1]
    for i in range(2,pagination.num_pages+1):
        if i in [pagination.num_pages,id_page,id_page+5,
        id_page-10,id_page-20,id_page-1,id_page+5,id_page+10,id_page+20,id_page+1]:
            if i-liste_pagination[-1]>1:
                liste_pagination.append("...")
            liste_pagination.append(i)

    return render(request, 'recherche_series.html', locals())

def view_recherche_jeu(request,nom,id_page=1):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    liste_jeux=jeux.objects.filter(nom__contains=nom)
    pagination=Paginator(liste_jeux,12,orphans=4)
    if 1 > id_page:
        id_page=1
    elif id_page > pagination.num_pages:
        id_page= pagination.num_pages
    # liste des musiques pour la page à afficher
    liste_jeux=pagination.page(id_page).object_list
    # page actuelle
    currentpage=pagination.page(id_page)

    liste_pagination=[1]
    for i in range(2,pagination.num_pages+1):
        if i in [pagination.num_pages,id_page,id_page+5,
        id_page-10,id_page-20,id_page-1,id_page+5,id_page+10,id_page+20,id_page+1]:
            if i-liste_pagination[-1]>1:
                liste_pagination.append("...")
            liste_pagination.append(i)

    return render(request, 'recherche_jeux.html', locals())

def view_recherche_logiciel(request,nom,id_page=1):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    liste_logiciels=logiciels.objects.filter(nom__contains=nom)
    pagination=Paginator(liste_logiciels,12,orphans=4)
    if 1 > id_page:
        id_page=1
    elif id_page > pagination.num_pages:
        id_page= pagination.num_pages
    # liste des musiques pour la page à afficher
    liste_logiciels=pagination.page(id_page).object_list
    # page actuelle
    currentpage=pagination.page(id_page)

    liste_pagination=[1]
    for i in range(2,pagination.num_pages+1):
        if i in [pagination.num_pages,id_page,id_page+5,
        id_page-10,id_page-20,id_page-1,id_page+5,id_page+10,id_page+20,id_page+1]:
            if i-liste_pagination[-1]>1:
                liste_pagination.append("...")
            liste_pagination.append(i)

    return render(request, 'recherche_logiciels.html', locals())

def view_recherche_musique(request,nom,id_page=1):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    liste_musiques=musiques.objects.filter(Q(artiste__contains=nom) | Q(titre__contains=nom))
    pagination=Paginator(liste_musiques,12,orphans=4)
    if 1 > id_page:
    	id_page=1
    elif id_page > pagination.num_pages:
    	id_page= pagination.num_pages
    # liste des musiques pour la page à afficher
    liste_musiques=pagination.page(id_page).object_list
    # page actuelle
    currentpage=pagination.page(id_page)

    liste_pagination=[1]
    for i in range(2,pagination.num_pages+1):
        if i in [pagination.num_pages,id_page,id_page+5,
        id_page-10,id_page-20,id_page-1,id_page+5,id_page+10,id_page+20,id_page+1]:
            if i-liste_pagination[-1]>1:
                liste_pagination.append("...")
            liste_pagination.append(i)

    return render(request, 'recherche_musiques.html', locals())

def view_recherche_livre(request,nom,id_page=1):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    liste_livres=livres.objects.filter(nom__contains=nom)
    pagination=Paginator(liste_livres,12,orphans=4)
    if 1 > id_page:
        id_page=1
    elif id_page > pagination.num_pages:
        id_page= pagination.num_pages
    # liste des musiques pour la page à afficher
    liste_livres=pagination.page(id_page).object_list
    # page actuelle
    currentpage=pagination.page(id_page)

    liste_pagination=[1]
    for i in range(2,pagination.num_pages+1):
        if i in [pagination.num_pages,id_page,id_page+5,
        id_page-10,id_page-20,id_page-1,id_page+5,id_page+10,id_page+20,id_page+1]:
            if i-liste_pagination[-1]>1:
                liste_pagination.append("...")
            liste_pagination.append(i)

    return render(request, 'recherche_livres.html', locals())

def get_disk_size():
    #remplacer cette partie avec le bon code

    return 230.12,430.71

#accueil du site
def view_accueil(request, inscription=10):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    freespace,totalspace=get_disk_size()
    usedspace = round(totalspace - freespace,2)
    used_percent = 100-int(freespace/totalspace*100)
    return render(request, 'accueil.html',locals())

# list des fichiers disponibles
def view_Series(request, id_page=1, order="alpha"):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    liste_series=series.objects.all()
    pagination=Paginator(liste_series,12,orphans=4)
    if 1 > id_page:
        id_page=1
    elif id_page > pagination.num_pages:
        id_page= pagination.num_pages
    # liste des musiques pour la page à afficher
    liste_series=pagination.page(id_page).object_list
    # page actuelle
    currentpage=pagination.page(id_page)

    liste_pagination=[1]
    for i in range(2,pagination.num_pages+1):
        if i in [pagination.num_pages,id_page,id_page+5,
        id_page-10,id_page-20,id_page-1,id_page+5,id_page+10,id_page+20,id_page+1]:
            if i-liste_pagination[-1]>1:
                liste_pagination.append("...")
            liste_pagination.append(i)

    return render(request, 'series.html', locals())

def view_Films(request, id_page=1, order="alpha"):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    liste_films=films.objects.all()
    pagination=Paginator(liste_films,12,orphans=4)
    if 1 > id_page:
        id_page=1
    elif id_page > pagination.num_pages:
        id_page= pagination.num_pages
    # liste des musiques pour la page à afficher
    liste_films=pagination.page(id_page).object_list
    # page actuelle
    currentpage=pagination.page(id_page)

    liste_pagination=[1]
    for i in range(2,pagination.num_pages+1):
        if i in [pagination.num_pages,id_page,id_page+5,
        id_page-10,id_page-20,id_page-1,id_page+5,id_page+10,id_page+20,id_page+1]:
            if i-liste_pagination[-1]>1:
                liste_pagination.append("...")
            liste_pagination.append(i)

    return render(request, 'films.html', locals())

def view_Musiques(request, id_page=1, order="alpha"):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')


    liste_musiques=musiques.objects.all()
    pagination=Paginator(liste_musiques,12,orphans=4)
    if 1 > id_page:
    	id_page=1
    elif id_page > pagination.num_pages:
    	id_page= pagination.num_pages
    # liste des musiques pour la page à afficher
    liste_musiques=pagination.page(id_page).object_list
    # page actuelle
    currentpage=pagination.page(id_page)

    liste_pagination=[1]
    for i in range(2,pagination.num_pages+1):
        if i in [pagination.num_pages,id_page,id_page+5,
        id_page-10,id_page-20,id_page-1,id_page+5,id_page+10,id_page+20,id_page+1]:
            if i-liste_pagination[-1]>1:
                liste_pagination.append("...")
            liste_pagination.append(i)

    return render(request, 'musiques.html', locals())

def view_Logiciels(request, id_page=1, order="alpha"):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')


    liste_logiciels=logiciels.objects.all()
    pagination=Paginator(liste_logiciels,12,orphans=4)
    if 1 > id_page:
        id_page=1
    elif id_page > pagination.num_pages:
        id_page= pagination.num_pages
    # liste des musiques pour la page à afficher
    liste_logiciels=pagination.page(id_page).object_list
    # page actuelle
    currentpage=pagination.page(id_page)

    liste_pagination=[1]
    for i in range(2,pagination.num_pages+1):
        if i in [pagination.num_pages,id_page,id_page+5,
        id_page-10,id_page-20,id_page-1,id_page+5,id_page+10,id_page+20,id_page+1]:
            if i-liste_pagination[-1]>1:
                liste_pagination.append("...")
            liste_pagination.append(i)

    return render(request, 'logiciels.html', locals())

def view_Jeux(request, id_page=1, order="alpha"):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')


    liste_jeux=jeux.objects.all()
    pagination=Paginator(liste_jeux,12,orphans=4)
    if 1 > id_page:
        id_page=1
    elif id_page > pagination.num_pages:
        id_page= pagination.num_pages
    # liste des musiques pour la page à afficher
    liste_jeux=pagination.page(id_page).object_list
    # page actuelle
    currentpage=pagination.page(id_page)

    liste_pagination=[1]
    for i in range(2,pagination.num_pages+1):
        if i in [pagination.num_pages,id_page,id_page+5,
        id_page-10,id_page-20,id_page-1,id_page+5,id_page+10,id_page+20,id_page+1]:
            if i-liste_pagination[-1]>1:
                liste_pagination.append("...")
            liste_pagination.append(i)

    return render(request, 'jeux.html', locals())

def view_Livres(request, id_page=1, order="alpha"):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    liste_livres=livres.objects.all()
    pagination=Paginator(liste_livres,12,orphans=4)
    if 1 > id_page:
        id_page=1
    elif id_page > pagination.num_pages:
        id_page= pagination.num_pages
    # liste des musiques pour la page à afficher
    liste_livres=pagination.page(id_page).object_list
    # page actuelle
    currentpage=pagination.page(id_page)

    liste_pagination=[1]
    for i in range(2,pagination.num_pages+1):
        if i in [pagination.num_pages,id_page,id_page+5,
        id_page-10,id_page-20,id_page-1,id_page+5,id_page+10,id_page+20,id_page+1]:
            if i-liste_pagination[-1]>1:
                liste_pagination.append("...")
            liste_pagination.append(i)

    return render(request, 'livres.html', locals())



def view_addfiles(request,cible=0,nom_recherche=""):
	#Si l'utilisateur n'est pas connecté, il n'a pas le droit d'Uploader
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
    	user= request.user

    #Pour se souvenir du formulaire sur lequel on travaillait
    formulaire=1

	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else :
        recherche=searchbar(prefix='search')

    #Si l'utilisateur envoie un film
    if request.method == 'POST' and 'film' in request.POST:
        addfilm=Addfilms(request.POST,request.FILES, prefix='film')
        if addfilm.is_valid():
            titre = addfilm.cleaned_data['titre']
            annee = addfilm.cleaned_data['annee']
            Genre = addfilm.cleaned_data['Genre']
            realisateur = addfilm.cleaned_data['realisateur']
            qualite = addfilm.cleaned_data['qualite']
            langage = addfilm.cleaned_data['langage']
            soustitre = addfilm.cleaned_data['soustitre']
            photo = addfilm.cleaned_data['photo']
            synopsis = addfilm.cleaned_data['synopsis']
            fichier = addfilm.cleaned_data['fichier']
            films(titre=titre,annee=annee,Genre=Genre,realisateur=realisateur,qualite=qualite,langage=langage,soustitre=soustitre,photo=photo,synopsis=synopsis,fichier=fichier,uploader=user).save()
            if cible==1 and nom_recherche!="":
                anciennes_demandes=ask_film.objects.filter(nom__iexact=nom_recherche)
                for i in range(0,len(anciennes_demandes)):
                    anciennes_demandes[i].delete()
            return redirect(view_accueil, inscription=3)
        else:
            formulaire=1
    else :
        if cible==1:
            addfilm=Addfilms(prefix='film',initial={'titre':nom_recherche})
            formulaire=1
        else:
            addfilm=Addfilms(prefix='film')

    #Si l'utilisateur envoie une serie
    if request.method == 'POST' and 'serie' in request.POST:
        addserie=Addseries(request.POST,request.FILES, prefix='serie')
        if addserie.is_valid():
            titre = addserie.cleaned_data['titre']
            annee = addserie.cleaned_data['annee']
            nbepisodes = addserie.cleaned_data['nbepisodes']
            Genre = addserie.cleaned_data['Genre']
            plateforme = addserie.cleaned_data['plateforme']
            qualite = addserie.cleaned_data['qualite']
            langage = addserie.cleaned_data['langage']
            soustitre = addserie.cleaned_data['soustitre']
            photo = addserie.cleaned_data['photo']
            synopsis = addserie.cleaned_data['synopsis']
            fichier = addserie.cleaned_data['fichier']
            series(titre=titre,annee=annee,nbepisodes=nbepisodes,Genre=Genre,plateforme=plateforme,qualite=qualite,langage=langage,soustitre=soustitre,photo=photo,synopsis=synopsis,fichier=fichier,uploader=user).save()
            if cible==2 and nom_recherche!="":
                anciennes_demandes=ask_serie.objects.filter(nom__iexact=nom_recherche)
                for i in range(0,len(anciennes_demandes)):
                    anciennes_demandes[i].delete()
            return redirect(view_accueil, inscription=3)
        else:
            formulaire=2
    else : 
        if cible==2:
            addserie=Addseries(prefix='serie',initial={'titre':nom_recherche})
            formulaire=2
        else:
        	addserie=Addseries(prefix='serie')

    #Si l'utilisateur envoie un jeu
    if request.method == 'POST' and 'jeu' in request.POST:
        addjeu=Addjeux(request.POST,request.FILES, prefix='jeu')
        if addjeu.is_valid():
            nom = addjeu.cleaned_data['nom']
            version = addjeu.cleaned_data['version']
            annee = addjeu.cleaned_data['annee']
            edition = addjeu.cleaned_data['edition']
            langage = addjeu.cleaned_data['langage']
            photo = addjeu.cleaned_data['photo']
            presentation = addjeu.cleaned_data['presentation']
            crack = addjeu.cleaned_data['crack']
            fichier = addjeu.cleaned_data['fichier']
            jeux(nom=nom,version=version,annee=annee,edition=edition,langage=langage,photo=photo,presentation=presentation,crack=crack,fichier=fichier,uploader=user).save()
            if cible==3 and nom_recherche!="":
                anciennes_demandes=ask_jeu.objects.filter(nom__iexact=nom_recherche)
                for i in range(0,len(anciennes_demandes)):
                    anciennes_demandes[i].delete()
            return redirect(view_accueil, inscription=3)
        else:
            formulaire=3
    else : 
        if cible==3:
        	addjeu=Addjeux(prefix='jeu',initial={'nom':nom_recherche})
        	formulaire=3
        else:
        	addjeu=Addjeux(prefix='jeu')

    #Si l'utilisateur envoie un logiciel
    if request.method == 'POST' and 'logiciel' in request.POST:
        addlogiciel=Addlogiciels(request.POST,request.FILES, prefix='logiciel')
        if addlogiciel.is_valid():
            nom = addlogiciel.cleaned_data['nom']
            version = addlogiciel.cleaned_data['version']
            annee = addlogiciel.cleaned_data['annee']
            license = addlogiciel.cleaned_data['license']
            langage = addlogiciel.cleaned_data['langage']
            photo = addlogiciel.cleaned_data['photo']
            presentation = addlogiciel.cleaned_data['presentation']
            crack = addlogiciel.cleaned_data['crack']
            fichier = addlogiciel.cleaned_data['fichier']
            logiciels(nom=nom,version=version,annee=annee,license=license,langage=langage,photo=photo,presentation=presentation,crack=crack,fichier=fichier,uploader=user).save()
            if cible==4 and nom_recherche!="":
                anciennes_demandes=ask_logiciel.objects.filter(nom__iexact=nom_recherche)
                for i in range(0,len(anciennes_demandes)):
                    anciennes_demandes[i].delete()
            return redirect(view_accueil, inscription=3)
        else:
            formulaire=4
    else : 
        if cible==4:
        	addlogiciel=Addlogiciels(prefix='logiciel',initial={'nom':nom_recherche})
        	formulaire=4
        else:
        	addlogiciel=Addlogiciels(prefix='logiciel')

    #Si l'utilisateur envoie un serie
    if request.method == 'POST' and 'livre' in request.POST:
        addlivre=Addlivres(request.POST,request.FILES, prefix='livre')
        if addlivre.is_valid():
            nom = addlivre.cleaned_data['nom']
            auteur = addlivre.cleaned_data['auteur']
            annee = addlivre.cleaned_data['annee']
            langage = addlivre.cleaned_data['langage']
            Genre = addlivre.cleaned_data['Genre']
            photo = addlivre.cleaned_data['photo']
            resume = addlivre.cleaned_data['resume']
            fichier = addlivre.cleaned_data['fichier']
            livres(nom=nom,auteur=auteur,annee=annee,Genre=Genre,langage=langage,photo=photo,resume=resume,fichier=fichier,uploader=user).save()
            if cible==5 and nom_recherche!="":
                anciennes_demandes=ask_livre.objects.filter(nom__iexact=nom_recherche)
                for i in range(0,len(anciennes_demandes)):
                    anciennes_demandes[i].delete()
            return redirect(view_accueil, inscription=3)
        else:
            formulaire=5
    else :
        if cible==5:
        	addlivre=Addlivres(prefix='livre',initial={'nom':nom_recherche})
        	formulaire=5
        else:
        	addlivre=Addlivres(prefix='livre')


    #Si l'utilisateur envoie de la musique
    if request.method == 'POST' and 'musique' in request.POST:
        addmusique=Addmusiques(request.POST,request.FILES, prefix='musique')
        if addmusique.is_valid():
            artiste = addmusique.cleaned_data['artiste']
            titre = addmusique.cleaned_data['titre']
            annee = addmusique.cleaned_data['annee']
            Genre = addmusique.cleaned_data['Genre']
            qualite = addmusique.cleaned_data['qualite']
            photo = addmusique.cleaned_data['photo']
            synopsis = addmusique.cleaned_data['synopsis']
            tracklist = addmusique.cleaned_data['tracklist']
            fichier = addmusique.cleaned_data['fichier']
            musiques(artiste=artiste,titre=titre,annee=annee,Genre=Genre,qualite=qualite,photo=photo,synopsis=synopsis,tracklist=tracklist,fichier=fichier,uploader=user).save()
            if cible==6 and nom_recherche!="":
                anciennes_demandes=ask_musique.objects.filter(nom__iexact=nom_recherche)
                for i in range(0,len(anciennes_demandes)):
                    anciennes_demandes[i].delete()
            return redirect(view_accueil, inscription=3)
        else:
            formulaire=6
    else :
        if cible==6:
        	addmusique=Addmusiques(prefix='musique',initial={'titre':nom_recherche})
        	formulaire=6
        else:
        	addmusique=Addmusiques(prefix='musique')

    return render(request, 'menuAjout.html',locals())



def view_connexion(request):
    if request.user.is_authenticated:
        return redirect("accueil")

    form = ConnexionForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
        if user:  # Si l'objet renvoyé n'est pas None
            login(request, user)  # nous connectons l'utilisateur
            return redirect(view_accueil, inscription=2)
        else: # sinon une erreur sera affichée
            error = True

    return render(request, 'connexion.html', locals())

def view_deconnexion(request):
    logout(request)
    return redirect(reverse(view_accueil))

def view_inscription(request):
    if request.user.is_authenticated:
        return redirect("accueil")

    form = InscriptionForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data["user"]
        mail = form.cleaned_data["mail"]
        annee = form.cleaned_data["annee"]
        password = form.cleaned_data["password"]
        password2 = form.cleaned_data["password2"]
        #On crée l'utilisateur
        newUser = User.objects.create_user(username,mail,password)
        userprofil(user=newUser,annee=annee).save()
        return redirect(view_accueil, inscription=1)

    return render(request, 'inscription.html', locals())

def view_telechargement_serie(request,titre,annee):
    cible=series.objects.get(titre=titre,annee=annee)
    cible.nbTelechargement+=1
    cible.save()

    return redirect(cible.fichier.url)

def view_telechargement_film(request,titre,annee):
    cible=films.objects.get(titre=titre,annee=annee)
    cible.nbTelechargement+=1
    cible.save()

    return redirect(cible.fichier.url)

def view_telechargement_jeu(request,nom,annee):
    cible=jeux.objects.get(nom=nom,annee=annee)
    cible.nbTelechargement+=1
    cible.save()

    return redirect(cible.fichier.url)

def view_telechargement_logiciel(request,nom,annee):
    cible=logiciels.objects.get(nom=nom,annee=annee)
    cible.nbTelechargement+=1
    cible.save()

    return redirect(cible.fichier.url)

def view_telechargement_livre(request,nom,auteur):
    cible=livres.objects.get(nom=nom,auteur=auteur)
    cible.nbTelechargement+=1
    cible.save()

    return redirect(cible.fichier.url)

def view_telechargement_musique(request,artiste,titre):
    cible=musiques.objects.get(artiste=artiste,titre=titre)
    cible.nbTelechargement+=1
    cible.save()

    return redirect(cible.fichier.url)


# Regarder les demandes

def view_list_demandes(request):
	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    liste_films=ask_film.objects.all().order_by('-datedepot')
    liste_series=ask_serie.objects.all().order_by('-datedepot')
    liste_musiques=ask_musique.objects.all().order_by('-datedepot')
    liste_jeux=ask_jeu.objects.all().order_by('-datedepot')
    liste_logiciels=ask_logiciel.objects.all().order_by('-datedepot')
    liste_livres=ask_livre.objects.all().order_by('-datedepot')

    return render(request, 'liste_demandes.html',locals())



#Faire des demandes

def view_demander(request):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    #on recupere la liste de nos demandes
    liste_films=ask_film.objects.filter(demandeur=user).order_by('-datedepot')
    liste_series=ask_serie.objects.filter(demandeur=user).order_by('-datedepot')
    liste_musiques=ask_musique.objects.filter(demandeur=user).order_by('-datedepot')
    liste_jeux=ask_jeu.objects.filter(demandeur=user).order_by('-datedepot')
    liste_logiciels=ask_logiciel.objects.filter(demandeur=user).order_by('-datedepot')
    liste_livres=ask_livre.objects.filter(demandeur=user).order_by('-datedepot')
    
    #Si l'utilisateur envoie un demande pour un film
    if request.method == 'POST' and 'film' in request.POST:
        askfilm=askFilm(request.POST, prefix='film')

        if askfilm.is_valid() and liste_films.count()<2:
            nom = askfilm.cleaned_data['nom']
            langage = askfilm.cleaned_data['langage']
            soustitre = askfilm.cleaned_data['soustitre']
            ask_film(nom=nom,langage=langage,soustitre=soustitre,demandeur=user).save()
            askfilm=askFilm(prefix='film')

            liste_tempo=ask_film.objects.order_by('datedepot')

            print(liste_tempo.count())
            if liste_tempo.count()>30:
                difference=liste_tempo.count()-30
                print(range(0,difference))
                for i in range(0,difference):
                    print(i)
                    liste_tempo[i].delete()

            liste_films=ask_film.objects.filter(demandeur=user).order_by('-datedepot')
    else :
        askfilm=askFilm(prefix='film')

    #Si l'utilisateur envoie un demande pour un serie
    if request.method == 'POST' and 'serie' in request.POST:
        askserie=askSerie(request.POST, prefix='serie')

        if askserie.is_valid() and liste_series.count()<2:
            nom = askserie.cleaned_data['nom']
            langage = askserie.cleaned_data['langage']
            soustitre = askserie.cleaned_data['soustitre']
            ask_serie(nom=nom,langage=langage,soustitre=soustitre,demandeur=user).save()
            askserie=askSerie(prefix='serie')

            liste_tempo=ask_serie.objects.order_by('datedepot')

            print(liste_tempo.count())
            if liste_tempo.count()>30:
                difference=liste_tempo.count()-30
                print(range(0,difference))
                for i in range(0,difference):
                    print(i)
                    liste_tempo[i].delete()

            liste_series=ask_serie.objects.filter(demandeur=user).order_by('-datedepot')
    else :
        askserie=askSerie(prefix='serie')

    #Si l'utilisateur envoie un demande pour un jeu
    if request.method == 'POST' and 'jeu' in request.POST:
        askjeu=askJeu(request.POST, prefix='jeu')

        if askjeu.is_valid() and liste_jeux.count()<2:
            nom = askjeu.cleaned_data['nom']
            ask_jeu(nom=nom,demandeur=user).save()
            askjeu=askJeu(prefix='jeu')

            liste_tempo=ask_jeu.objects.order_by('datedepot')

            print(liste_tempo.count())
            if liste_tempo.count()>30:
                difference=liste_tempo.count()-30
                print(range(0,difference))
                for i in range(0,difference):
                    print(i)
                    liste_tempo[i].delete()

            liste_jeux=ask_jeu.objects.filter(demandeur=user).order_by('-datedepot')
    else :
        askjeu=askJeu(prefix='jeu')

    #Si l'utilisateur envoie un demande pour un logiciel
    if request.method == 'POST' and 'logiciel' in request.POST:
        asklogiciel=askLogiciel(request.POST, prefix='logiciel')

        if asklogiciel.is_valid() and liste_logiciels.count()<2:
            nom = asklogiciel.cleaned_data['nom']
            ask_logiciel(nom=nom,demandeur=user).save()
            asklogiciel=askLogiciel(prefix='logiciel')

            liste_tempo=ask_logiciel.objects.order_by('datedepot')

            print(liste_tempo.count())
            if liste_tempo.count()>30:
                difference=liste_tempo.count()-30
                print(range(0,difference))
                for i in range(0,difference):
                    print(i)
                    liste_tempo[i].delete()

            liste_logiciels=ask_logiciel.objects.filter(demandeur=user).order_by('-datedepot')
    else :
        asklogiciel=askLogiciel(prefix='logiciel')

    #Si l'utilisateur envoie un demande pour un musique
    if request.method == 'POST' and 'musique' in request.POST:
        askmusique=askMusique(request.POST, prefix='musique')

        if askmusique.is_valid() and liste_musiques.count()<2:
            nom = askmusique.cleaned_data['nom']
            ask_musique(nom=nom,demandeur=user).save()
            askmusique=askMusique(prefix='musique')

            liste_tempo=ask_musique.objects.order_by('datedepot')

            print(liste_tempo.count())
            if liste_tempo.count()>30:
                difference=liste_tempo.count()-30
                print(range(0,difference))
                for i in range(0,difference):
                    print(i)
                    liste_tempo[i].delete()

            liste_musiques=ask_musique.objects.filter(demandeur=user).order_by('-datedepot')
    else :
        askmusique=askMusique(prefix='musique')

    #Si l'utilisateur envoie un demande pour un livre
    if request.method == 'POST' and 'livre' in request.POST:
        asklivre=askLivre(request.POST, prefix='livre')

        if asklivre.is_valid() and liste_livres.count()<2:
            nom = asklivre.cleaned_data['nom']
            ask_livre(nom=nom,demandeur=user).save()
            asklivre=askLivre(prefix='livre')

            liste_tempo=ask_livre.objects.order_by('datedepot')

            print(liste_tempo.count())
            if liste_tempo.count()>30:
                difference=liste_tempo.count()-30
                print(range(0,difference))
                for i in range(0,difference):
                    print(i)
                    liste_tempo[i].delete()

            liste_livres=ask_livre.objects.filter(demandeur=user).order_by('-datedepot')
    else :
        asklivre=askLivre(prefix='livre')

    qtt_film=liste_films.count()
    qtt_serie=liste_series.count()
    qtt_musique=liste_musiques.count()
    qtt_jeu=liste_jeux.count()
    qtt_logiciel=liste_logiciels.count()
    qtt_livre=liste_livres.count()

    return render(request, 'demander.html',locals())


def view_removeSerieDemande(request,nom,langage,soustitre):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

    cible=ask_serie.objects.filter(nom=nom,langage=langage,soustitre=soustitre,demandeur=user)
    if len(cible)==0:
        return redirect('demander')
    else:
        cible[0].delete()
        return redirect('demander')

def view_removeFilmDemande(request,nom,langage,soustitre):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

    cible=ask_film.objects.filter(nom=nom,langage=langage,soustitre=soustitre,demandeur=user)
    if len(cible)==0:
        return redirect('demander')
    else:
        cible[0].delete()
        return redirect('demander')

def view_removeMusiqueDemande(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

    cible=ask_musique.objects.filter(nom=nom,demandeur=user)
    
    if len(cible)==0:
        return redirect('demander')
    else:
        cible[0].delete()
        return redirect('demander')

def view_removeJeuDemande(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

    cible=ask_jeu.objects.filter(nom=nom,demandeur=user)
    
    if len(cible)==0:
        return redirect('demander')
    else:
        cible[0].delete()
        return redirect('demander')

def view_removeLogicielDemande(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

    cible=ask_logiciel.objects.filter(nom=nom,demandeur=user)
    
    if len(cible)==0:
        return redirect('demander')
    else:
        cible[0].delete()
        return redirect('demander')

def view_removeLivreDemande(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

    cible=ask_livre.objects.filter(nom=nom,demandeur=user)
    
    if len(cible)==0:
        return redirect('demander')
    else:
        cible[0].delete()
        return redirect('demander')







def view_supprimerfilm(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

    cible=films.objects.filter(titre=nom)
    if len(cible)==0:
        return redirect("accueil")
    else:
        cible=cible[0]
        if request.user==cible.uploader or request.user.is_superuser:
            cible.delete()
            return redirect("accueil",inscription=4)
        else:
            return redirect("accueil",inscription=6)

def view_supprimerserie(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

    cible=series.objects.filter(titre=nom)
    if len(cible)==0:
        return redirect("accueil")
    else:
        cible=cible[0]
        if request.user==cible.uploader or request.user.is_superuser:
            cible.delete()
            return redirect("accueil",inscription=4)
        else:
            return redirect("accueil",inscription=6)

def view_supprimerjeu(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

    cible=jeux.objects.filter(nom=nom)
    if len(cible)==0:
        return redirect("accueil")
    else:
        cible=cible[0]
        if request.user==cible.uploader or request.user.is_superuser:
            cible.delete()
            return redirect("accueil",inscription=4)
        else:
            return redirect("accueil",inscription=6)

def view_supprimerlogiciel(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

    cible=logiciels.objects.filter(nom=nom)
    if len(cible)==0:
        return redirect("accueil")
    else:
        cible=cible[0]
        if request.user==cible.uploader or request.user.is_superuser:
            cible.delete()
            return redirect("accueil",inscription=4)
        else:
            return redirect("accueil",inscription=6)

def view_supprimermusique(request,artiste,titre):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

    cible=musiques.objects.filter(artiste=artiste,titre=titre)
    if len(cible)==0:
        return redirect("accueil")
    else:
        cible=cible[0]
        if request.user==cible.uploader or request.user.is_superuser:
            cible.delete()
            return redirect("accueil",inscription=4)
        else:
            return redirect("accueil",inscription=6)

def view_supprimerlivre(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

    cible=livres.objects.filter(nom=nom)
    if len(cible)==0:
        return redirect("accueil")
    else:
        cible=cible[0]
        if request.user==cible.uploader or request.user.is_superuser:
            cible.delete()
            return redirect("accueil",inscription=4)
        else:
            return redirect("accueil",inscription=6)









#Modification fichier
def view_modifierfilm(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')
        
    cible=films.objects.filter(titre=nom)
    if len(cible)==0:
    	return redirect("accueil",inscription=6)
    else:
        cible=cible[0]
        if cible.uploader != request.user and not request.user.is_superuser:
        	return redirect("accueil", inscription=7)
        #Si l'utilisateur envoie un demande pour un logiciel
        if request.method == 'POST' and 'modifierfilm' in request.POST:
	        film_a_modifier=modifierfilm(request.POST,request.FILES, prefix='modifierfilm')
	        if film_a_modifier.is_valid():
	            titre = film_a_modifier.cleaned_data['titre']

	            already_exist = films.objects.filter(titre=titre)
	            if len(already_exist)!=0 and already_exist[0]!=cible:
	            	error=1
	            	film_a_modifier=modifierfilm(prefix='modifierfilm',initial={'titre': cible.titre,'annee': cible.annee,'Genre': cible.Genre,'realisateur': cible.realisateur,'qualite': cible.qualite,'langage': cible.langage,'soustitre': cible.soustitre,'synopsis': cible.synopsis})
	            	return render(request, 'modifier_film.html',locals())

	            cible.titre = titre
	            cible.annee = film_a_modifier.cleaned_data['annee']
	            cible.Genre = film_a_modifier.cleaned_data['Genre']
	            cible.realisateur = film_a_modifier.cleaned_data['realisateur']
	            cible.qualite = film_a_modifier.cleaned_data['qualite']
	            cible.langage = film_a_modifier.cleaned_data['langage']
	            cible.soustitre = film_a_modifier.cleaned_data['soustitre']
	            cible.synopsis = film_a_modifier.cleaned_data['synopsis']
	            photo = film_a_modifier.cleaned_data['photo']
	            fichier = film_a_modifier.cleaned_data['fichier']
	            if photo != None:
	            	cible.photo = photo
	            if fichier != None:
	            	cible.fichier = fichier
	            cible.save()
	            return redirect("accueil",inscription=5)
        else:
	        film_a_modifier=modifierfilm(prefix='modifierfilm',initial={'titre': cible.titre,'annee': cible.annee,'Genre': cible.Genre,'realisateur': cible.realisateur,'qualite': cible.qualite,'langage': cible.langage,'soustitre': cible.soustitre,'synopsis': cible.synopsis})

    return render(request, 'modifier_film.html',locals())

def view_modifierserie(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    cible=series.objects.filter(titre=nom)
    if len(cible)==0:
    	return redirect("accueil",inscription=6)
    else:
        cible=cible[0]
        if cible.uploader != request.user and not request.user.is_superuser:
        	return redirect("accueil", inscription=7)
        #Si l'utilisateur envoie un demande pour un logiciel
        if request.method == 'POST' and 'modifierserie' in request.POST:
	        serie_a_modifier=modifierserie(request.POST,request.FILES, prefix='modifierserie')
	        if serie_a_modifier.is_valid():
	            titre = serie_a_modifier.cleaned_data['titre']

	            already_exist = series.objects.filter(titre=titre)
	            if len(already_exist)!=0 and already_exist[0]!=cible:
	            	error=1
	            	serie_a_modifier=modifierserie(prefix='modifierserie',initial={'titre': cible.titre,'annee': cible.annee,'nbepisodes':cible.nbepisodes,'Genre': cible.Genre,'plateforme': cible.plateforme,'qualite': cible.qualite,'langage': cible.langage,'soustitre': cible.soustitre,'synopsis': cible.synopsis})
	            	return render(request, 'modifier_serie.html',locals())

	            cible.titre = titre
	            cible.annee = serie_a_modifier.cleaned_data['annee']
	            cible.nbepisodes = serie_a_modifier.cleaned_data['nbepisodes']
	            cible.Genre = serie_a_modifier.cleaned_data['Genre']
	            cible.plateforme = serie_a_modifier.cleaned_data['plateforme']
	            cible.qualite = serie_a_modifier.cleaned_data['qualite']
	            cible.langage = serie_a_modifier.cleaned_data['langage']
	            cible.soustitre = serie_a_modifier.cleaned_data['soustitre']
	            cible.synopsis = serie_a_modifier.cleaned_data['synopsis']
	            photo = serie_a_modifier.cleaned_data['photo']
	            fichier = serie_a_modifier.cleaned_data['fichier']
	            if photo != None:
	            	cible.photo = photo
	            if fichier != None:
	            	cible.fichier = fichier
	            cible.save()
	            return redirect("accueil",inscription=5)
        else:
	        serie_a_modifier=modifierserie(prefix='modifierserie',initial={'titre': cible.titre,'annee': cible.annee,'nbepisodes':cible.nbepisodes,'Genre': cible.Genre,'plateforme': cible.plateforme,'qualite': cible.qualite,'langage': cible.langage,'soustitre': cible.soustitre,'synopsis': cible.synopsis})

    return render(request, 'modifier_serie.html',locals())

def view_modifierjeu(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    cible=jeux.objects.filter(nom=nom)
    if len(cible)==0:
    	return redirect("accueil",inscription=6)
    else:
        cible=cible[0]
        if cible.uploader != request.user and not request.user.is_superuser:
        	return redirect("accueil", inscription=7)
        #Si l'utilisateur envoie un demande pour un logiciel
        if request.method == 'POST' and 'modifierjeu' in request.POST:
	        jeu_a_modifier=modifierjeu(request.POST,request.FILES, prefix='modifierjeu')
	        if jeu_a_modifier.is_valid():
	            nom = jeu_a_modifier.cleaned_data['nom']

	            already_exist = jeux.objects.filter(nom=nom)
	            if len(already_exist)!=0 and already_exist[0]!=cible:
	            	error=1
	            	jeu_a_modifier=modifierjeu(prefix='modifierjeu',initial={'nom': cible.nom,'version': cible.version,'annee': cible.annee,'edition': cible.edition,'langage': cible.langage,'presentation': cible.presentation,'crack': cible.crack})
	            	return render(request, 'modifier_jeu.html',locals())

	            cible.nom = nom
	            cible.version = jeu_a_modifier.cleaned_data['version']
	            cible.annee = jeu_a_modifier.cleaned_data['annee']
	            cible.edition = jeu_a_modifier.cleaned_data['edition']
	            cible.langage = jeu_a_modifier.cleaned_data['langage']
	            cible.presentation = jeu_a_modifier.cleaned_data['presentation']
	            cible.crack = jeu_a_modifier.cleaned_data['crack']
	            photo = jeu_a_modifier.cleaned_data['photo']
	            fichier = jeu_a_modifier.cleaned_data['fichier']
	            if photo != None:
	            	cible.photo = photo
	            if fichier != None:
	            	cible.fichier = fichier
	            cible.save()
	            return redirect("accueil",inscription=5)
        else:
	        jeu_a_modifier=modifierjeu(prefix='modifierjeu',initial={'nom': cible.nom,'version': cible.version,'annee': cible.annee,'edition': cible.edition,'langage': cible.langage,'presentation': cible.presentation,'crack': cible.crack})

    return render(request, 'modifier_jeu.html',locals())

def view_modifierlogiciel(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    cible=logiciels.objects.filter(nom=nom)
    if len(cible)==0:
    	return redirect("accueil",inscription=6)
    else:
        cible=cible[0]
        if cible.uploader != request.user and not request.user.is_superuser:
        	return redirect("accueil", inscription=7)
        #Si l'utilisateur envoie un demande pour un logiciel
        if request.method == 'POST' and 'modifierlogiciel' in request.POST:
	        logiciel_a_modifier=modifierlogiciel(request.POST,request.FILES, prefix='modifierlogiciel')
	        if logiciel_a_modifier.is_valid():
	            nom = logiciel_a_modifier.cleaned_data['nom']

	            already_exist = logiciels.objects.filter(nom=nom)
	            if len(already_exist)!=0 and already_exist[0]!=cible:
	            	error=1
	            	logiciel_a_modifier=modifierlogiciel(prefix='modifierlogiciel',initial={'nom': cible.nom,'version': cible.version,'annee': cible.annee,'license': cible.license,'langage': cible.langage,'presentation': cible.presentation,'crack': cible.crack})
	            	return render(request, 'modifier_logiciel.html',locals())

	            cible.nom = nom
	            cible.version = logiciel_a_modifier.cleaned_data['version']
	            cible.annee = logiciel_a_modifier.cleaned_data['annee']
	            cible.license = logiciel_a_modifier.cleaned_data['license']
	            cible.langage = logiciel_a_modifier.cleaned_data['langage']
	            cible.presentation = logiciel_a_modifier.cleaned_data['presentation']
	            cible.crack = logiciel_a_modifier.cleaned_data['crack']
	            photo = logiciel_a_modifier.cleaned_data['photo']
	            fichier = logiciel_a_modifier.cleaned_data['fichier']
	            if photo != None:
	            	cible.photo = photo
	            if fichier != None:
	            	cible.fichier = fichier
	            cible.save()
	            return redirect("accueil",inscription=5)
        else:
	        logiciel_a_modifier=modifierlogiciel(prefix='modifierlogiciel',initial={'nom': cible.nom,'version': cible.version,'annee': cible.annee,'license': cible.license,'langage': cible.langage,'presentation': cible.presentation,'crack': cible.crack})

    return render(request, 'modifier_logiciel.html',locals())

def view_modifierlivre(request,nom):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    cible=livres.objects.filter(nom=nom)
    if len(cible)==0:
    	return redirect("accueil",inscription=6)
    else:
        cible=cible[0]
        if cible.uploader != request.user and not request.user.is_superuser:
        	return redirect("accueil", inscription=7)
        #Si l'utilisateur envoie un demande pour un logiciel
        if request.method == 'POST' and 'modifierlivre' in request.POST:
	        livre_a_modifier=modifierlivre(request.POST,request.FILES, prefix='modifierlivre')
	        if livre_a_modifier.is_valid():
	            nom = livre_a_modifier.cleaned_data['nom']

	            already_exist = livres.objects.filter(nom=nom)
	            if len(already_exist)!=0 and already_exist[0]!=cible:
	            	error=1
	            	livre_a_modifier=modifierlivre(prefix='modifierlivre',initial={'nom': cible.nom,'auteur': cible.auteur,'annee': cible.annee,'langage': cible.langage,'Genre': cible.Genre,'resume': cible.resume})
	            	return render(request, 'modifier_livre.html',locals())

	            cible.nom = nom
	            cible.auteur = livre_a_modifier.cleaned_data['auteur']
	            cible.annee = livre_a_modifier.cleaned_data['annee']
	            cible.langage = livre_a_modifier.cleaned_data['langage']
	            cible.Genre = livre_a_modifier.cleaned_data['Genre']
	            cible.resume = livre_a_modifier.cleaned_data['resume']
	            photo = livre_a_modifier.cleaned_data['photo']
	            fichier = livre_a_modifier.cleaned_data['fichier']
	            if photo != None:
	            	cible.photo = photo
	            if fichier != None:
	            	cible.fichier = fichier
	            cible.save()
	            return redirect("accueil",inscription=5)
        else:
	        livre_a_modifier=modifierlivre(prefix='modifierlivre',initial={'nom': cible.nom,'auteur': cible.auteur,'annee': cible.annee,'langage': cible.langage,'Genre': cible.Genre,'resume': cible.resume})

    return render(request, 'modifier_livre.html',locals())

def view_modifiermusique(request,artiste,titre):
    #Si l'utilisateur n'est pas connecté, il n'a pas le droit de faire de demandes
    if not request.user.is_authenticated:
        return redirect("connexion")
    else:
        user= request.user

	#Si l'utilisateur envoie une recherche
    if request.method == 'POST' and 'search' in request.POST:
        recherche=searchbar(request.POST, prefix='search')
        if recherche.is_valid():
            motclef=recherche.cleaned_data['motclef']
            categorie=recherche.cleaned_data['categorie']
            if categorie=="films":
                return redirect("recherche_film",nom=motclef,id_page=1)
            elif categorie=="séries":
                return redirect("recherche_serie",nom=motclef,id_page=1)
            elif categorie=="jeux":
                return redirect("recherche_jeu",nom=motclef,id_page=1)
            elif categorie=="logiciels":
                return redirect("recherche_logiciel",nom=motclef,id_page=1)
            elif categorie=="musiques":
                return redirect("recherche_musique",nom=motclef,id_page=1)
            elif categorie=="livres":
                return redirect("recherche_livre",nom=motclef,id_page=1)
            return redirect(view_accueil)
    else : 
        recherche=searchbar(prefix='search')

    cible=musiques.objects.filter(artiste=artiste,titre=titre)
    if len(cible)==0:
    	return redirect("accueil",inscription=6)
    else:
        cible=cible[0]
        if cible.uploader != request.user and not request.user.is_superuser:
        	return redirect("accueil", inscription=7)
        #Si l'utilisateur envoie un demande pour un logiciel
        if request.method == 'POST' and 'modifiermusique' in request.POST:
	        musique_a_modifier=modifiermusique(request.POST,request.FILES, prefix='modifiermusique')
	        if musique_a_modifier.is_valid():
	            artiste = musique_a_modifier.cleaned_data['artiste']
	            titre = musique_a_modifier.cleaned_data['titre']

	            already_exist = musiques.objects.filter(artiste=artiste,titre=titre)
	            if len(already_exist)!=0 and already_exist[0]!=cible:
	            	error=1
	            	musique_a_modifier=modifiermusique(prefix='modifiermusique',initial={'artiste': cible.artiste,'titre': cible.titre,'annee': cible.annee,'Genre': cible.Genre,'qualite': cible.qualite,'synopsis': cible.synopsis,'tracklist': cible.tracklist,'synopsis': cible.synopsis})
	            	return render(request, 'modifier_musique.html',locals())

	            cible.artiste = artiste
	            cible.titre = titre
	            cible.annee = musique_a_modifier.cleaned_data['annee']
	            cible.Genre = musique_a_modifier.cleaned_data['Genre']
	            cible.qualite = musique_a_modifier.cleaned_data['qualite']
	            cible.synopsis = musique_a_modifier.cleaned_data['synopsis']
	            cible.tracklist = musique_a_modifier.cleaned_data['tracklist']
	            photo = musique_a_modifier.cleaned_data['photo']
	            fichier = musique_a_modifier.cleaned_data['fichier']
	            if photo != None:
	            	cible.photo = photo
	            if fichier != None:
	            	cible.fichier = fichier
	            cible.save()
	            return redirect("accueil",inscription=5)
        else:
	        musique_a_modifier=modifiermusique(prefix='modifiermusique',initial={'artiste': cible.artiste,'titre': cible.titre,'annee': cible.annee,'Genre': cible.Genre,'qualite': cible.qualite,'synopsis': cible.synopsis,'tracklist': cible.tracklist,'synopsis': cible.synopsis})

    return render(request, 'modifier_musique.html',locals())

