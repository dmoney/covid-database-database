from django.db import models

# Create your models here.

class Field(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100, null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.name

class Scope(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=True)

    def __str__(self):
        return self.name

class Source(models.Model):
    name=models.CharField(max_length=100)
    url=models.URLField()
    description=models.TextField(null=True, blank=True)
    author_name=models.CharField(max_length=100, null=True, blank=True)
    author_url=models.URLField(null=True, blank=True)

    fields=models.ManyToManyField(Field, blank=True)

    using=models.ManyToManyField("self", symmetrical=False, related_name="used_by", blank=True)

    def __str__(self):
        return f"{self.name} (by {self.author_name or 'Unknown'})"
