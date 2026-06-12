from django.db import models

# Create your models here.
class Autore(models.Model):
    nome = models.CharField(max_length=100)
    nazione = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = "Autori"  # Plurale italiano


class Libro(models.Model):
    titolo = models.CharField(max_length=250)
    anno = models.IntegerField()
    genere = models.CharField(max_length=60)
    autore = models.ForeignKey(Autore, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titolo}"

    class Meta:
        verbose_name_plural = "Libri"  # Plurale italiano


