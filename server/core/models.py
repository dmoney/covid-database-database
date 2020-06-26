from django.db import models

# Create your models here.

class Field(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name

class Scope(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name

class Source(models.Model):
    name=models.CharField(max_length=100)
    url=models.URLField()
    description=models.TextField()
    author_name=models.CharField(max_length=100)
    author_url=models.URLField()

    fields=models.ManyToManyField(Field)

    using=models.ManyToManyField("self", symmetrical=False, related_name="used_by")

    def __str__(self):
        return f"{self.name} (by {self.author_name or 'Unknown'})"
