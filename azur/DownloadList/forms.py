from django import forms
from .models import series,films,jeux,logiciels,livres,musiques,ask_film,ask_serie,ask_musique,ask_jeu,ask_logiciel,ask_livre
from django.contrib.auth.models import User
from django.conf import settings

def title_cleaner(form,model):
        titre=form.cleaned_data['titre']
        similaire=model.objects.filter(titre=titre)
        if len(similaire)>0:
            raise forms.ValidationError("Ce titre est déja pris.")
        return titre

def annee_cleaner(form):
        annee = form.cleaned_data["annee"]
        if 1000>annee:
            raise forms.ValidationError("Depuis quand il y a des séries créés en "+str(annee)+"?")
        elif annee>3000:
            raise forms.ValidationError(str(annee)+"? On est pas dans le futur.")
        return annee

def langage_cleaner(form):
        langage = form.cleaned_data["langage"]
        langage_list = langage.replace(" ","").split(",")
        new_langage_list = []
        for abreviation in langage_list:
            if abreviation=='':
                {}
            elif (len(abreviation)>3 or len(abreviation)<2) and abreviation.lower()!="multi":
                print(abreviation)
                raise forms.ValidationError("seuls sont acceptés les abréviations de 2 à 3 lettres (FR,ENG,SPA) ou Multi.")
            else:
                new_langage_list.append(abreviation)

        if new_langage_list==[]:
            raise forms.ValidationError("Entrez des abréviations correctes.")

        langage=new_langage_list[0]
        for i in range(1,len(new_langage_list)):
            langage+=","+new_langage_list[i]

        return(langage)

def sous_titre_cleaner(form):
        soustitre = form.cleaned_data["soustitre"]
        soustitre_list = soustitre.replace(" ","").split(",")
        new_soustitre_list = []
        for abreviation in soustitre_list:
            if abreviation=='':
                {}
            elif (len(abreviation)>3 or len(abreviation)<2) and abreviation.lower()!="multi":
                print(abreviation)
                raise forms.ValidationError("seuls sont acceptés les abréviations de 2 à 3 lettres (FR,ENG,SPA) ou Multi.")
            else:
                new_soustitre_list.append(abreviation)

        if new_soustitre_list==[]:
            raise forms.ValidationError("Entrez des abréviations correctes.")

        soustitre=new_soustitre_list[0]
        for i in range(1,len(new_soustitre_list)):
            soustitre+=","+new_soustitre_list[i]

        return(soustitre)

class Addseries(forms.ModelForm):
    class Meta:
        model = series
        exclude = ('nbTelechargement','datedepot','uploader')

    def __init__(self, *args, **kwargs):
        super(Addseries, self).__init__(*args, **kwargs)
        self.fields['titre'].widget.attrs={'placeholder': 'ex : Altered Carbon S01, Arrow S03'} 
        self.fields['annee'].widget.attrs={'placeholder': 'ex : 2001, 2007, 2000'} 
        self.fields['nbepisodes'].widget.attrs={'placeholder': 'ex : 10'} 
        self.fields['Genre'].widget.attrs={'placeholder': 'ex : horreur, fantasy'} 
        self.fields['plateforme'].widget.attrs={'placeholder': 'ex : Netflix, Amazon premium'} 
        self.fields['qualite'].widget.attrs={'placeholder': 'ex : 720P, 1080P, SD'} 
        self.fields['langage'].widget.attrs={'placeholder': 'ex : FR, ENG, MULTI'} 
        self.fields['soustitre'].widget.attrs={'placeholder': 'ex : FR, ENG, MULTI, Non'}
        self.fields['synopsis'].widget.attrs={'placeholder': 'ex : Eric était un fervant mangeur de Burger King. Malheureusement, il ne s\'attendait pas à se qui allait se passer dans le BK près de chez lui : la sauce mayonnaise allait disparaitre.','rows' : 10} 

    def clean_titre(self):
        return title_cleaner(self,series)

    def clean_annee(self):
        return annee_cleaner(self)

    def clean_langage(self):
        return langage_cleaner(self)

    def clean_soustitre(self):
        return sous_titre_cleaner(self)

    def clean_fichier(self):
    	fichier= self.cleaned_data["fichier"]
    	if fichier._size > settings.MAX_UPLOAD_SIZE_SERIE*1024**3:
    		raise forms.ValidationError("LE fichier est trop grand. Taille maximum :"+str(settings.MAX_UPLOAD_SIZE_SERIE)+"Go")
    	return(fichier)

class Addfilms(forms.ModelForm):
    class Meta:
        model = films
        exclude = ('nbTelechargement','datedepot','uploader')

    def __init__(self, *args, **kwargs):
        super(Addfilms, self).__init__(*args, **kwargs)
        self.fields['titre'].widget.attrs={'placeholder': 'ex : Interstellar, Le loup de Wall Street'} 
        self.fields['annee'].widget.attrs={'placeholder': 'ex : 2001, 2007, 2000'} 
        self.fields['realisateur'].widget.attrs={'placeholder': 'ex : Quentin Tarantino, Steven Spielberg'}
        self.fields['Genre'].widget.attrs={'placeholder': 'ex : horreur, fantasy'} 
        self.fields['qualite'].widget.attrs={'placeholder': 'ex : 720P, 1080P, SD'} 
        self.fields['langage'].widget.attrs={'placeholder': 'ex : FR, ENG, MULTI'} 
        self.fields['soustitre'].widget.attrs={'placeholder': 'ex : FR, ENG, MULTI, Non'}
        self.fields['synopsis'].widget.attrs={'placeholder': 'ex : Bernard était un kangourou heureux dans sa vie jusqu\'au jour ou il réalisa qu\'il était adopté. Il décida alors de partir à la recherche de ses parents au pôle sud.','rows' : 10} 

    def clean_titre(self):
        return title_cleaner(self,films)

    def clean_annee(self):
        return annee_cleaner(self)

    def clean_langage(self):
        return langage_cleaner(self)

    def clean_soustitre(self):
        return sous_titre_cleaner(self)

    def clean_fichier(self):
    	fichier= self.cleaned_data["fichier"]
    	if fichier._size > settings.MAX_UPLOAD_SIZE_FILM*1024**3:
    		raise forms.ValidationError("LE fichier est trop grand. Taille maximum :"+str(settings.MAX_UPLOAD_SIZE_FILM)+"Go")
    	return(fichier)

class Addmusiques(forms.ModelForm):
    class Meta:
        model = musiques
        exclude = ('nbTelechargement','datedepot','uploader')

    def __init__(self, *args, **kwargs):
        super(Addmusiques, self).__init__(*args, **kwargs)
        self.fields['artiste'].widget.attrs={'placeholder': 'ex : Booba, Mozart, Metallica, 50 cents'} 
        self.fields['titre'].widget.attrs={'placeholder': 'ex : Master of puppets, Stairway to Heaven'} 
        self.fields['annee'].widget.attrs={'placeholder': 'ex : 2001, 2007, 2000'} 
        self.fields['Genre'].widget.attrs={'placeholder': 'ex : Metal, Rap, Classique, Techno'}
        self.fields['qualite'].widget.attrs={'placeholder': 'ex : 320kbps/s, flac (lossless)'} 
        self.fields['tracklist'].widget.attrs={'placeholder': 'ex : \n1/ 1:30min Stairway to heaven \n2/ 5:28min back in black \n3/ 5:10min Feel good \n4/ 4:12min Eyes of the tiger','rows' : 10} 
        self.fields['synopsis'].widget.attrs={'placeholder': 'ex : LittlePoney est un groupe nord coréen complêtement inconnu du grand public qui a besoin de vendre des CDs à travers le monde pour prouver la grandeur de leur Pays.','rows' : 10} 

    def clean_titre(self):
    	artiste=self.cleaned_data['artiste']
    	titre=self.cleaned_data['titre']
    	similaire=musiques.objects.filter(artiste=artiste,titre=titre)
    	if len(similaire)>0:
    		raise forms.ValidationError("La combinaison artiste/titre existe déja.")
    	return titre

    def clean_annee(self):
        return annee_cleaner(self)

    def clean_fichier(self):
    	fichier= self.cleaned_data["fichier"]
    	if fichier._size > settings.MAX_UPLOAD_SIZE_MUSIQUE*1024**3:
    		raise forms.ValidationError("LE fichier est trop grand. Taille maximum :"+str(settings.MAX_UPLOAD_SIZE_MUSIQUE)+"Go")
    	return(fichier)

class Addlogiciels(forms.ModelForm):
    class Meta:
        model = logiciels
        exclude = ('nbTelechargement','datedepot','uploader')

    def __init__(self, *args, **kwargs):
        super(Addlogiciels, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs={'placeholder': 'ex : Guitar Pro, Photo Shop, Matlab'} 
        self.fields['version'].widget.attrs={'placeholder': 'ex : v2.0.0.7, HD0.70'} 
        self.fields['annee'].widget.attrs={'placeholder': 'ex : 2001, 2007, 2000'} 
        self.fields['license'].widget.attrs={'placeholder': 'ex : OpenSource, payant, license libre'}
        self.fields['langage'].widget.attrs={'placeholder': 'ex : FR, ENG, MULTI'}
        self.fields['crack'].widget.attrs={'placeholder': 'ex : Pas de crack\nEtapes de crakage\nReadMe disponible dans le fichier','rows' : 10}
        self.fields['presentation'].widget.attrs={'placeholder': 'ex : Même generator est un logiciel de conception de mèmes assisté par ordinateur permettant de publier des images troll sur DarkMèmeSE.','rows' : 10}

    def clean_nom(self):
    	nom=self.cleaned_data['nom']
    	similaire=logiciels.objects.filter(nom=nom)
    	if len(similaire)>0:
    		raise forms.ValidationError("Ce nom est déja pris.")
    	return nom

    def clean_annee(self):
        return annee_cleaner(self)

    def clean_langage(self):
        return langage_cleaner(self)

    def clean_fichier(self):
    	fichier= self.cleaned_data["fichier"]
    	if fichier._size > settings.MAX_UPLOAD_SIZE_LOGICIEL*1024**3:
    		raise forms.ValidationError("LE fichier est trop grand. Taille maximum :"+str(settings.MAX_UPLOAD_SIZE_LOGICIEL)+"Go")
    	return(fichier)

class Addjeux(forms.ModelForm):
    class Meta:
        model = jeux
        exclude = ('nbTelechargement','datedepot','uploader')

    def __init__(self, *args, **kwargs):
        super(Addjeux, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs={'placeholder': 'ex : Starcraft 2, Warcraft, Skyrim'} 
        self.fields['version'].widget.attrs={'placeholder': 'ex : v2.0.0.7, HD0.70'} 
        self.fields['annee'].widget.attrs={'placeholder': 'ex : 2001, 2007, 2000'} 
        self.fields['edition'].widget.attrs={'placeholder': 'ex : Blizzard, Riot Games'}
        self.fields['langage'].widget.attrs={'placeholder': 'ex : FR, ENG, MULTI'}
        self.fields['presentation'].widget.attrs={'placeholder': 'ex : Skyrim est un jeu de plateforme ou vous devez contrôler des poneys fous afin de vous frayer un chemin dans la campagne sauvage de Savoie.', 'rows' : 10}        
        self.fields['crack'].widget.attrs={'placeholder': 'ex : Pas de crack\nOU Etapes de crakage\nOU ReadMe disponible dans le fichier','rows' : 10}

    def clean_nom(self):
    	nom=self.cleaned_data['nom']
    	similaire=jeux.objects.filter(nom=nom)
    	if len(similaire)>0:
    		raise forms.ValidationError("Ce nom est déja pris.")
    	return nom

    def clean_annee(self):
        return annee_cleaner(self)

    def clean_langage(self):
        return langage_cleaner(self)

    def clean_fichier(self):
    	fichier= self.cleaned_data["fichier"]
    	if fichier._size > settings.MAX_UPLOAD_SIZE_JEU*1024**3:
    		raise forms.ValidationError("LE fichier est trop grand. Taille maximum :"+str(settings.MAX_UPLOAD_SIZE_JEU)+"Go")
    	return(fichier)

class Addlivres(forms.ModelForm):
    class Meta:
        model = livres
        exclude = ('nbTelechargement','datedepot','uploader')

    def __init__(self, *args, **kwargs):
        super(Addlivres, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs={'placeholder': 'ex : Harry potter et la chambre des secrets'} 
        self.fields['auteur'].widget.attrs={'placeholder': 'ex : J.K Rowling'} 
        self.fields['annee'].widget.attrs={'placeholder': 'ex : 2001, 2007, 2000'} 
        self.fields['langage'].widget.attrs={'placeholder': 'ex : FR, ENG, SPA'}
        self.fields['resume'].widget.attrs={'placeholder': 'ex : Thomas était un caniche sauvage jusqu\'au jour ou sa vie bascula après avoir rencontré un arbre cogneur.', 'rows' : 10}
        self.fields['Genre'].widget.attrs={'placeholder': 'ex : fantastique, horreur'}

    def clean_nom(self):
    	nom=self.cleaned_data['nom']
    	similaire=livres.objects.filter(nom=nom)
    	if len(similaire)>0:
    		raise forms.ValidationError("Ce nom est déja pris.")
    	return nom

    def clean_annee(self):
        return annee_cleaner(self)

    def clean_fichier(self):
    	fichier= self.cleaned_data["fichier"]
    	if fichier._size > settings.MAX_UPLOAD_SIZE_LIVRE*1024**3:
    		raise forms.ValidationError("LE fichier est trop grand. Taille maximum :"+str(settings.MAX_UPLOAD_SIZE_LIVRE)+"Go")
    	return(fichier)

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=15)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, max_length=15)

class InscriptionForm(forms.Form):
    user = forms.CharField(label="Nom d'utilisateur", max_length=15)
    mail = forms.EmailField(label="Adresse e-mail", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, max_length=15)
    password2 = forms.CharField(label="Confirmation", widget=forms.PasswordInput, max_length=15)
    annee = forms.ChoiceField(choices=(('1A','1ère année'),
                                      ('2A','2ème année'),
                                      ('3A','3ème année')))
    
    def clean_user(self):
        user = self.cleaned_data["user"]
        if len(user)<6:
            raise forms.ValidationError("Le nom d'utilisateur doit comporter au moins 6 caractères")
        if len(User.objects.filter(username=user))!=0:
            raise forms.ValidationError("Nom d'utilisateur déja existant")
        return user

    def clean_password2(self):
        password = self.cleaned_data["password"]
        if len(password)<6:
            raise forms.ValidationError("Le mot de passe doit comporter au moins 6 caractères")        
        password2 = self.cleaned_data["password2"]
        if password!=password2:
            raise forms.ValidationError("Les deux mots de passe diffèrent")
        return password2

class searchbar(forms.Form):
    motclef=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder': 'Search...','style':'background :#ededef url("/static/image/search.png") no-repeat;background-size: auto 90%;'}))
    categorie=forms.ChoiceField(choices=(('films', 'films'),
                                                  ('séries', 'séries'),
                                                  ('jeux', 'jeux'),
                                                  ('logiciels', 'logiciels'),
                                                  ('livres', 'livres'),
                                                  ('musiques', 'musiques')))

class askSerie(forms.ModelForm):
    class Meta:
        model = ask_serie
        exclude = ('demandeur','datedepot')

    def __init__(self, *args, **kwargs):
        super(askSerie, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs={'placeholder': 'Fichier demandé'} 
        self.fields['langage'].widget.attrs={'placeholder': 'langage'} 
        self.fields['soustitre'].widget.attrs={'placeholder': 'sous-titre'} 
 
class askFilm(forms.ModelForm):
    class Meta:
        model = ask_film
        exclude = ('demandeur','datedepot')

    def __init__(self, *args, **kwargs):
        super(askFilm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs={'placeholder': 'Fichier demandé'} 
        self.fields['langage'].widget.attrs={'placeholder': 'langage'} 
        self.fields['soustitre'].widget.attrs={'placeholder': 'sous-titre'} 
 
class askJeu(forms.ModelForm):
    class Meta:
        model = ask_jeu
        exclude = ('demandeur','datedepot')

    def __init__(self, *args, **kwargs):
        super(askJeu, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs={'placeholder': 'Fichier demandé'} 

class askLogiciel(forms.ModelForm):
    class Meta:
        model = ask_logiciel
        exclude = ('demandeur','datedepot')

    def __init__(self, *args, **kwargs):
        super(askLogiciel, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs={'placeholder': 'Fichier demandé'} 

class askLivre(forms.ModelForm):
    class Meta:
        model = ask_livre
        exclude = ('demandeur','datedepot')

    def __init__(self, *args, **kwargs):
        super(askLivre, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs={'placeholder': 'Fichier demandé'} 

class askMusique(forms.ModelForm):
    class Meta:
        model = ask_musique
        exclude = ('demandeur','datedepot')

    def __init__(self, *args, **kwargs):
        super(askMusique, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs={'placeholder': 'Fichier demandé'}





























#modification de fichiers
class modifierfilm(forms.ModelForm):
    fichier=forms.FileField(required=False,label="Fichier (non obligatoire)")
    photo=forms.ImageField(required=False,label="Photo (non obligatoire)")

    class Meta:
        model = films
        exclude = ('nbTelechargement','datedepot','uploader','fichier','photo')

    def __init__(self, *args, **kwargs):
        super(modifierfilm, self).__init__(*args, **kwargs)
        self.fields['titre'].widget.attrs={'placeholder': 'ex : Interstellar, Le loup de Wall Street'} 
        self.fields['annee'].widget.attrs={'placeholder': 'ex : 2001, 2007, 2000'} 
        self.fields['realisateur'].widget.attrs={'placeholder': 'ex : Quentin Tarantino, Steven Spielberg'}
        self.fields['Genre'].widget.attrs={'placeholder': 'ex : horreur, fantasy'} 
        self.fields['qualite'].widget.attrs={'placeholder': 'ex : 720P, 1080P, SD'} 
        self.fields['langage'].widget.attrs={'placeholder': 'ex : FR, ENG, MULTI'} 
        self.fields['soustitre'].widget.attrs={'placeholder': 'ex : FR, ENG, MULTI, Non'}
        self.fields['synopsis'].widget.attrs={'placeholder': 'ex : Bernard était un kangourou heureux dans sa vie jusqu\'au jour ou il réalisa qu\'il était adopté. Il décida alors de partir à la recherche de ses parents au pôle sud.','rows' : 10} 

    def clean_annee(self):
        return annee_cleaner(self)

    def clean_langage(self):
        return langage_cleaner(self)

    def clean_soustitre(self):
        return sous_titre_cleaner(self)

    def clean_fichier(self):
        fichier= self.cleaned_data["fichier"]
        if fichier==None:
            return fichier
        if fichier._size > settings.MAX_UPLOAD_SIZE_SERIE*1024**3:
            raise forms.ValidationError("LE fichier est trop grand. Taille maximum :"+str(settings.MAX_UPLOAD_SIZE_SERIE)+"Go")
        return(fichier)

class modifierserie(forms.ModelForm):
    fichier=forms.FileField(required=False,label="Fichier (non obligatoire)")
    photo=forms.ImageField(required=False,label="Photo (non obligatoire)")

    class Meta:
        model = series
        exclude = ('nbTelechargement','datedepot','uploader','fichier','photo')

    def __init__(self, *args, **kwargs):
        super(modifierserie, self).__init__(*args, **kwargs)
        self.fields['titre'].widget.attrs={'placeholder': 'ex : Altered Carbon S01, Arrow S03'} 
        self.fields['annee'].widget.attrs={'placeholder': 'ex : 2001, 2007, 2000'} 
        self.fields['nbepisodes'].widget.attrs={'placeholder': 'ex : 10'} 
        self.fields['Genre'].widget.attrs={'placeholder': 'ex : horreur, fantasy'} 
        self.fields['plateforme'].widget.attrs={'placeholder': 'ex : Netflix, Amazon premium'} 
        self.fields['qualite'].widget.attrs={'placeholder': 'ex : 720P, 1080P, SD'} 
        self.fields['langage'].widget.attrs={'placeholder': 'ex : FR, ENG, MULTI'} 
        self.fields['soustitre'].widget.attrs={'placeholder': 'ex : FR, ENG, MULTI, Non'}
        self.fields['synopsis'].widget.attrs={'placeholder': 'ex : Eric était un fervant mangeur de Burger King. Malheureusement, il ne s\'attendait pas à se qui allait se passer dans le BK près de chez lui : la sauce mayonnaise allait disparaitre.','rows' : 10} 

    def clean_annee(self):
        return annee_cleaner(self)

    def clean_langage(self):
        return langage_cleaner(self)

    def clean_soustitre(self):
        return sous_titre_cleaner(self)

    def clean_fichier(self):
        fichier= self.cleaned_data["fichier"]
        if fichier==None:
            return fichier
        if fichier._size > settings.MAX_UPLOAD_SIZE_SERIE*1024**3:
            raise forms.ValidationError("LE fichier est trop grand. Taille maximum :"+str(settings.MAX_UPLOAD_SIZE_SERIE)+"Go")
        return(fichier)


class modifiermusique(forms.ModelForm):
    fichier=forms.FileField(required=False,label="Fichier (non obligatoire)")
    photo=forms.ImageField(required=False,label="Photo (non obligatoire)")

    class Meta:
        model = musiques
        exclude = ('nbTelechargement','datedepot','uploader','fichier','photo')

    def __init__(self, *args, **kwargs):
        super(modifiermusique, self).__init__(*args, **kwargs)
        self.fields['artiste'].widget.attrs={'placeholder': 'ex : Booba, Mozart, Metallica, 50 cents'} 
        self.fields['titre'].widget.attrs={'placeholder': 'ex : Master of puppets, Stairway to Heaven'} 
        self.fields['annee'].widget.attrs={'placeholder': 'ex : 2001, 2007, 2000'} 
        self.fields['Genre'].widget.attrs={'placeholder': 'ex : Metal, Rap, Classique, Techno'}
        self.fields['qualite'].widget.attrs={'placeholder': 'ex : 320kbps/s, flac (lossless)'} 
        self.fields['tracklist'].widget.attrs={'placeholder': 'ex : \n1/ 1:30min Stairway to heaven \n2/ 5:28min back in black \n3/ 5:10min Feel good \n4/ 4:12min Eyes of the tiger','rows' : 10} 
        self.fields['synopsis'].widget.attrs={'placeholder': 'ex : LittlePoney est un groupe nord coréen complêtement inconnu du grand public qui a besoin de vendre des CDs à travers le monde pour prouver la grandeur de leur Pays.','rows' : 10} 

    def clean_annee(self):
        return annee_cleaner(self)

    def clean_fichier(self):
        fichier= self.cleaned_data["fichier"]
        if fichier==None:
            return fichier
        if fichier._size > settings.MAX_UPLOAD_SIZE_MUSIQUE*1024**3:
            raise forms.ValidationError("LE fichier est trop grand. Taille maximum :"+str(settings.MAX_UPLOAD_SIZE_MUSIQUE)+"Go")
        return(fichier)

class modifierlogiciel(forms.ModelForm):
    fichier=forms.FileField(required=False,label="Fichier (non obligatoire)")
    photo=forms.ImageField(required=False,label="Photo (non obligatoire)")

    class Meta:
        model = logiciels
        exclude = ('nbTelechargement','datedepot','uploader','fichier','photo')

    def __init__(self, *args, **kwargs):
        super(modifierlogiciel, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs={'placeholder': 'ex : Guitar Pro, Photo Shop, Matlab'} 
        self.fields['version'].widget.attrs={'placeholder': 'ex : v2.0.0.7, HD0.70'} 
        self.fields['annee'].widget.attrs={'placeholder': 'ex : 2001, 2007, 2000'} 
        self.fields['license'].widget.attrs={'placeholder': 'ex : OpenSource, payant, license libre'}
        self.fields['langage'].widget.attrs={'placeholder': 'ex : FR, ENG, MULTI'}
        self.fields['crack'].widget.attrs={'placeholder': 'ex : Pas de crack\nEtapes de crakage\nReadMe disponible dans le fichier','rows' : 10}
        self.fields['presentation'].widget.attrs={'placeholder': 'ex : Même generator est un logiciel de conception de mèmes assisté par ordinateur permettant de publier des images troll sur DarkMèmeSE.','rows' : 10}

    def clean_annee(self):
        return annee_cleaner(self)

    def clean_langage(self):
        return langage_cleaner(self)

    def clean_fichier(self):
        fichier= self.cleaned_data["fichier"]
        if fichier==None:
            return fichier
        if fichier._size > settings.MAX_UPLOAD_SIZE_LOGICIEL*1024**3:
            raise forms.ValidationError("LE fichier est trop grand. Taille maximum :"+str(settings.MAX_UPLOAD_SIZE_LOGICIEL)+"Go")
        return(fichier)

class modifierjeu(forms.ModelForm):
    fichier=forms.FileField(required=False,label="Fichier (non obligatoire)")
    photo=forms.ImageField(required=False,label="Photo (non obligatoire)")

    class Meta:
        model = jeux
        exclude = ('nbTelechargement','datedepot','uploader','fichier','photo')

    def __init__(self, *args, **kwargs):
        super(modifierjeu, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs={'placeholder': 'ex : Starcraft 2, Warcraft, Skyrim'} 
        self.fields['version'].widget.attrs={'placeholder': 'ex : v2.0.0.7, HD0.70'} 
        self.fields['annee'].widget.attrs={'placeholder': 'ex : 2001, 2007, 2000'} 
        self.fields['edition'].widget.attrs={'placeholder': 'ex : Blizzard, Riot Games'}
        self.fields['langage'].widget.attrs={'placeholder': 'ex : FR, ENG, MULTI'}
        self.fields['presentation'].widget.attrs={'placeholder': 'ex : Skyrim est un jeu de plateforme ou vous devez contrôler des poneys fous afin de vous frayer un chemin dans la campagne sauvage de Savoie.', 'rows' : 10}        
        self.fields['crack'].widget.attrs={'placeholder': 'ex : Pas de crack\nOU Etapes de crakage\nOU ReadMe disponible dans le fichier','rows' : 10}

    def clean_annee(self):
        return annee_cleaner(self)

    def clean_langage(self):
        return langage_cleaner(self)

    def clean_fichier(self):
        fichier= self.cleaned_data["fichier"]
        if fichier==None:
            return fichier
        if fichier._size > settings.MAX_UPLOAD_SIZE_JEU*1024**3:
            raise forms.ValidationError("LE fichier est trop grand. Taille maximum :"+str(settings.MAX_UPLOAD_SIZE_JEU)+"Go")
        return(fichier)

class modifierlivre(forms.ModelForm):
    fichier=forms.FileField(required=False,label="Fichier (non obligatoire)")
    photo=forms.ImageField(required=False,label="Photo (non obligatoire)")

    class Meta:
        model = livres
        exclude = ('nbTelechargement','datedepot','uploader','fichier','photo')

    def __init__(self, *args, **kwargs):
        super(modifierlivre, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs={'placeholder': 'ex : Harry potter et la chambre des secrets'} 
        self.fields['auteur'].widget.attrs={'placeholder': 'ex : J.K Rowling'} 
        self.fields['annee'].widget.attrs={'placeholder': 'ex : 2001, 2007, 2000'} 
        self.fields['langage'].widget.attrs={'placeholder': 'ex : FR, ENG, SPA'}
        self.fields['resume'].widget.attrs={'placeholder': 'ex : Thomas était un caniche sauvage jusqu\'au jour ou sa vie bascula après avoir rencontré un arbre cogneur.', 'rows' : 10}
        self.fields['Genre'].widget.attrs={'placeholder': 'ex : fantastique, horreur'}

    def clean_annee(self):
        return annee_cleaner(self)

    def clean_fichier(self):
        fichier= self.cleaned_data["fichier"]
        if fichier==None:
            return fichier
        if fichier._size > settings.MAX_UPLOAD_SIZE_LIVRE*1024**3:
            raise forms.ValidationError("LE fichier est trop grand. Taille maximum :"+str(settings.MAX_UPLOAD_SIZE_LIVRE)+"Go")
        return(fichier)