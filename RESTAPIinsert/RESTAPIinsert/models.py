from django.db import models

class Booksmodel(models.Model):
    BookName=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)
    Genre=models.CharField(max_length=50)
    PublishedYear=models.IntegerField()
    class Meta:
        db_table="booksdata"