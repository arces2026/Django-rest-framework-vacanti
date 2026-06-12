from django.contrib import admin
from .models import Libro, Autore
# Register your models here.


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titolo', 'anno', 'genere', 'autore' )


@admin.register(Autore)
class AutoreAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'nazione')

