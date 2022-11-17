# Generated by Django 4.1.2 on 2022-11-17 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='recipe_pages.image'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='link',
            field=models.SlugField(blank=True, null=True),
        ),
    ]