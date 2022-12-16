# Generated by Django 4.1.2 on 2022-12-07 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_pages', '0004_alter_recipe_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='measurement',
        ),
        migrations.RemoveField(
            model_name='recipe_ingredient',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='recipe_ingredient',
            name='measurement',
        ),
        migrations.AddField(
            model_name='recipe',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='Measurement',
        ),
        migrations.DeleteModel(
            name='Recipe_Ingredient',
        ),
    ]
