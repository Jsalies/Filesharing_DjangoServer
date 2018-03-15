from django.contrib import admin
from .models import series,films,livres,jeux,logiciels,musiques,userprofil,ask_film,ask_serie,ask_musique,ask_jeu,ask_logiciel,ask_livre

# Register your models here.
admin.site.register(series)
admin.site.register(films)
admin.site.register(livres)
admin.site.register(jeux)
admin.site.register(logiciels)
admin.site.register(musiques)
admin.site.register(userprofil)
admin.site.register(ask_film)
admin.site.register(ask_serie)
admin.site.register(ask_musique)
admin.site.register(ask_jeu)
admin.site.register(ask_logiciel)
admin.site.register(ask_livre)