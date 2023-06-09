# Generated by Django 4.1.2 on 2023-06-21 22:44

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenC', models.ImageField(null=True, upload_to='Carrusel')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Figuras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenP', models.ImageField(null=True, upload_to='Posters')),
                ('imagenF', models.ImageField(null=True, upload_to='Figuras')),
                ('nombreF', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombreF')),
                ('precioF', models.IntegerField()),
                ('anime', models.CharField(max_length=100)),
                ('tamano', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('envio', models.CharField(max_length=15)),
                ('activo', models.BooleanField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='figura.categoria')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='figura.material')),
            ],
        ),
    ]
