from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import SET_NULL
from django.conf import settings
import os
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

def _delete_file(path):
    # Deletes file from filesystem.
    if os.path.isfile(path):
        os.remove(path)

class series(models.Model):
    """Permet de structurer notre base de données"""
    titre = models.CharField(max_length=50, verbose_name="titre")
    annee = models.IntegerField(verbose_name="année de production")
    nbepisodes = models.IntegerField( verbose_name="nombre d'épisodes")
    Genre = models.CharField(max_length=100, verbose_name="Genre")
    plateforme = models.CharField(max_length=20, verbose_name="Entreprise de production")
    qualite = models.CharField(max_length=10, verbose_name="Qualité")
    langage = models.CharField(max_length=20, verbose_name="Langage")
    soustitre = models.CharField(max_length=20, verbose_name="Language sous-titres")
    nbTelechargement = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="series/images/", verbose_name="Jaquette/ Image")
    synopsis = models.TextField(null=False, verbose_name="Synopsis")
    fichier = models.FileField(upload_to="series/fichiers/",verbose_name="Fichier ( max : "+str(settings.MAX_UPLOAD_SIZE_SERIE)+"Go )")
    datedepot = models.DateTimeField(default=timezone.now,
                                     verbose_name="Date de mise en ligne")
    uploader = models.ForeignKey(User,on_delete=SET_NULL,null=True)

    class Meta:
        """Permet de donner un nom et un ordre de base à notre bdd"""
        verbose_name = "series"
        ordering = ['titre']

    def __str__(self):
        """Permet de parametrer les détails des entrées de
		la table qui sont vues dans la page d'administration"""
        return self.titre+" | "+str(self.annee)+" | "+self.Genre+" | "+self.plateforme


class films(models.Model):
    """Permet de structurer notre base de données"""
    titre = models.CharField(max_length=50, verbose_name="titre")
    annee = models.IntegerField(verbose_name="année")
    Genre = models.CharField(max_length=100,verbose_name="Genre")
    realisateur = models.CharField(max_length=40,verbose_name="réalisateur")
    qualite = models.CharField(max_length=10,verbose_name="qualité")
    langage = models.CharField(max_length=20,verbose_name="Langage")
    soustitre = models.CharField(max_length=20,verbose_name="Langage sous-titres")
    nbTelechargement = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="films/images/")
    synopsis = models.TextField(null=False,verbose_name="Synopsis")
    fichier = models.FileField(upload_to="films/fichiers/",verbose_name="Fichier ( max : "+str(settings.MAX_UPLOAD_SIZE_FILM)+"Go )")
    datedepot = models.DateTimeField(default=timezone.now,
                                     verbose_name="Date de mise en ligne")
    uploader = models.ForeignKey(User,on_delete=SET_NULL,null=True)

    class Meta:
        """Permet de donner un nom et un ordre de base à notre bdd"""
        verbose_name = "films"
        ordering = ['titre']

    def __str__(self):
        """Permet de parametrer les détails des entrées de
		la table qui sont vues dans la page d'administration"""
        return self.titre+" | "+str(self.annee)+" | "+self.Genre+" | "+self.realisateur



class musiques(models.Model):
    """Permet de structurer notre base de données"""
    artiste = models.CharField(max_length=50,verbose_name="Artiste")
    titre = models.CharField(max_length=50,verbose_name="Titre album")
    annee = models.IntegerField(verbose_name="Année")
    Genre = models.CharField(max_length=100,verbose_name="Genre")
    qualite = models.CharField(max_length=10,verbose_name="Qualité")
    nbTelechargement = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="musiques/images/")
    synopsis = models.TextField(null=False,verbose_name="Présentation")
    tracklist = models.TextField(null=False,verbose_name="Liste des pistes audios")
    fichier = models.FileField(upload_to="musiques/fichiers/",verbose_name="Fichier ( max : "+str(settings.MAX_UPLOAD_SIZE_MUSIQUE)+"Go )")
    datedepot = models.DateTimeField(default=timezone.now,
                                     verbose_name="Date de mise en ligne")
    uploader = models.ForeignKey(User,on_delete=SET_NULL,null=True)

    class Meta:
        """Permet de donner un nom et un ordre de base à notre bdd"""
        verbose_name = "musiques"
        ordering = ['artiste', 'titre']

    def __str__(self):
        """Permet de parametrer les détails des entrées de
		la table qui sont vues dans la page d'administration"""
        return self.artiste+" | "+self.titre+" | "+str(self.annee)+" | "+self.Genre

@receiver(models.signals.post_delete, sender=musiques)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.fichier:
        if os.path.isfile(instance.fichier.path):
            os.remove(instance.fichier.path)
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)

class logiciels(models.Model):
    """Permet de structurer notre base de données"""
    nom = models.CharField(max_length=50,verbose_name="Nom")
    version = models.CharField(max_length=20, verbose_name="Version logiciel")
    annee = models.IntegerField(verbose_name="Année de sortie")
    license = models.CharField(max_length=20,verbose_name="License")
    langage = models.CharField(max_length=20,verbose_name="Langage")
    nbTelechargement = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="logiciels/images/")
    presentation = models.TextField(null=False,verbose_name="Présentation")
    crack = models.TextField(null=True,verbose_name="Méthode de crackage")
    fichier = models.FileField(upload_to="logiciels/fichiers/",verbose_name="Fichier ( max : "+str(settings.MAX_UPLOAD_SIZE_LOGICIEL)+"Go )")
    datedepot = models.DateTimeField(default=timezone.now,
                                     verbose_name="Date de mise en ligne")
    uploader = models.ForeignKey(User,on_delete=SET_NULL,null=True)

    class Meta:
        """Permet de donner un nom et un ordre de base à notre bdd"""
        verbose_name = "logiciels"
        ordering = ['nom', 'version']

    def __str__(self):
        """Permet de parametrer les détails des entrées de
		la table qui sont vues dans la page d'administration"""
        return self.nom+" | "+self.version+" | "+self.license+" | "+self.langage

class jeux(models.Model):
    """Permet de structurer notre base de données"""
    nom = models.CharField(max_length=50,verbose_name="Nom")
    version = models.CharField(max_length=20,verbose_name="Version")
    annee = models.IntegerField(verbose_name="Année de sortie")
    edition = models.CharField(max_length=20, verbose_name="entreprise")
    langage = models.CharField(max_length=20,verbose_name="Langage")
    nbTelechargement = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="jeux/images/")
    presentation = models.TextField(null=False,verbose_name="Présentation")
    crack = models.TextField(null=True,verbose_name="Méthode de crackage")
    fichier = models.FileField(upload_to="jeux/fichiers/",verbose_name="Fichier ( max : "+str(settings.MAX_UPLOAD_SIZE_JEU)+"Go )")
    datedepot = models.DateTimeField(default=timezone.now,
                                     verbose_name="Date de mise en ligne")
    uploader = models.ForeignKey(User,on_delete=SET_NULL,null=True)

    class Meta:
        """Permet de donner un nom et un ordre de base à notre bdd"""
        verbose_name = "jeux"
        ordering = ['nom', 'version']

    def __str__(self):
        """Permet de parametrer les détails des entrées de
		la table qui sont vues dans la page d'administration"""
        return self.nom+" | "+self.version+" | "+str(self.annee)+" | "+self.langage

class livres(models.Model):
    """Permet de structurer notre base de données"""
    nom = models.CharField(max_length=50,verbose_name="Titre")
    auteur = models.CharField(max_length=50,verbose_name="Auteur")
    annee = models.IntegerField(verbose_name="Année de sortie")
    langage = models.CharField(max_length=20,verbose_name="Langage")
    Genre = models.CharField(max_length=100,verbose_name="Genre")
    nbTelechargement = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="livres/images/")
    resume = models.TextField(null=False,verbose_name="Résumé")
    fichier = models.FileField(upload_to="livres/fichiers/",verbose_name="Fichier ( max : "+str(settings.MAX_UPLOAD_SIZE_LIVRE)+"Go )")
    datedepot = models.DateTimeField(default=timezone.now,
                                     verbose_name="Date de mise en ligne")
    uploader = models.ForeignKey(User,on_delete=SET_NULL,null=True)

    class Meta:
        """Permet de donner un nom et un ordre de base à notre bdd"""
        verbose_name = "livres"
        ordering = ['nom', 'auteur']

    def __str__(self):
        """Permet de parametrer les détails des entrées de
		la table qui sont vues dans la page d'administration"""
        return self.nom+" | "+self.auteur+" | "+str(self.annee)+" | "+self.Genre

@receiver(models.signals.post_delete, sender=films)
@receiver(models.signals.post_delete, sender=jeux)
@receiver(models.signals.post_delete, sender=musiques)
@receiver(models.signals.post_delete, sender=logiciels)
@receiver(models.signals.post_delete, sender=series)
@receiver(models.signals.post_delete, sender=livres)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.fichier:
        if os.path.isfile(instance.fichier.path):
            os.remove(instance.fichier.path)
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


@receiver(models.signals.pre_save, sender=films)
@receiver(models.signals.pre_save, sender=jeux)
@receiver(models.signals.pre_save, sender=musiques)
@receiver(models.signals.pre_save, sender=logiciels)
@receiver(models.signals.pre_save, sender=series)
@receiver(models.signals.pre_save, sender=livres)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_photo = sender.objects.get(pk=instance.pk).photo
        old_file = sender.objects.get(pk=instance.pk).fichier
    except sender.DoesNotExist:
        return False

    new_file = instance.fichier
    new_photo = instance.photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

    if not old_photo == new_photo:
        if os.path.isfile(old_photo.path):
            os.remove(old_photo.path)

class userprofil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
	annee = models.TextField(null=False, choices=(('1A', '1ère année'),
	                                              ('2A', '2ème année'),
	                                              ('3A', '3ème année')), default='1A', )
	def __str__(self):
	    return "Profil de {0}".format(self.user.username)


# ASK LIST
class ask_serie(models.Model):
	nom = models.CharField(max_length=50,verbose_name="serie demandé")
	langage = models.CharField(max_length=50,verbose_name="langage")
	soustitre = models.CharField(max_length=50,verbose_name="sous-titre")
	demandeur =models.ForeignKey(User,on_delete=SET_NULL,null=True)
	datedepot = models.DateTimeField(default=timezone.now,
	                                 verbose_name="Date de mise en ligne")

	def __str__(self):
		"""Permet de parametrer les détails des entrées de
		la table qui sont vues dans la page d'administration"""
		if self.demandeur==None:
			return self.nom+" | "+self.langage+" | "+self.soustitre+" | None"
		return self.nom+" | "+self.langage+" | "+self.soustitre+" | "+self.demandeur.username

class ask_film(models.Model):
	nom = models.CharField(max_length=50,verbose_name="film demandé")
	langage = models.CharField(max_length=50,verbose_name="langage")
	soustitre = models.CharField(max_length=50,verbose_name="sous-titre")
	demandeur =models.ForeignKey(User,on_delete=SET_NULL,null=True)
	datedepot = models.DateTimeField(default=timezone.now,
	                                 verbose_name="Date de mise en ligne")

	def __str__(self):
		"""Permet de parametrer les détails des entrées de
		la table qui sont vues dans la page d'administration"""
		if self.demandeur==None:
			return self.nom+" | "+self.langage+" | "+self.soustitre+" | None"
		return self.nom+" | "+self.langage+" | "+self.soustitre+" | "+self.demandeur.username

class ask_jeu(models.Model):
	nom = models.CharField(max_length=50,verbose_name="jeu demandé.")
	demandeur =models.ForeignKey(User,on_delete=SET_NULL,null=True)
	datedepot = models.DateTimeField(default=timezone.now,
	                                 verbose_name="Date de mise en ligne")

	def __str__(self):
		"""Permet de parametrer les détails des entrées de
		la table qui sont vues dans la page d'administration"""
		if self.demandeur==None:
			return self.nom+" | None"
		return self.nom+" | "+self.demandeur.username

class ask_logiciel(models.Model):
	nom = models.CharField(max_length=50,verbose_name="logiciel demandé.")
	demandeur =models.ForeignKey(User,on_delete=SET_NULL,null=True)
	datedepot = models.DateTimeField(default=timezone.now,
	                                 verbose_name="Date de mise en ligne")

	def __str__(self):
		"""Permet de parametrer les détails des entrées de
		la table qui sont vues dans la page d'administration"""
		if self.demandeur==None:
			return self.nom+" | None"
		return self.nom+" | "+self.demandeur.username

class ask_livre(models.Model):
	nom = models.CharField(max_length=50,verbose_name="livre demandé.")
	demandeur =models.ForeignKey(User,on_delete=SET_NULL,null=True)
	datedepot = models.DateTimeField(default=timezone.now,
	                                 verbose_name="Date de mise en ligne")

	def __str__(self):
		"""Permet de parametrer les détails des entrées de
		la table qui sont vues dans la page d'administration"""
		if self.demandeur==None:
			return self.nom+" | None"
		return self.nom+" | "+self.demandeur.username

class ask_musique(models.Model):
	nom = models.CharField(max_length=50,verbose_name="musique demandée.")
	demandeur =models.ForeignKey(User,on_delete=SET_NULL,null=True)
	datedepot = models.DateTimeField(default=timezone.now,
	                                 verbose_name="Date de mise en ligne")

	def __str__(self):
		"""Permet de parametrer les détails des entrées de
		la table qui sont vues dans la page d'administration"""
		if self.demandeur==None:
			return self.nom+" | None"
		return self.nom+" | "+self.demandeur.username