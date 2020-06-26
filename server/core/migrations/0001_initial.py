# Generated by Django 3.0.7 on 2020-06-26 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('url', models.URLField()),
                ('description', models.TextField()),
                ('author_name', models.TextField()),
                ('author_url', models.URLField()),
            ],
        ),
    ]
