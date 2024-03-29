# Generated by Django 4.0 on 2022-02-09 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=30)),
                ('hero', models.CharField(max_length=30)),
                ('herohin', models.CharField(max_length=30)),
                ('released_date', models.DateField()),
                ('genre', models.CharField(max_length=30)),
                ('language', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='showApp.movie')),
            ],
        ),
    ]
