# Generated by Django 3.1.8 on 2021-05-06 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_hero_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='hero_photo',
            field=models.ImageField(blank=True, help_text='Image of me to be displayed in the hero.', upload_to=''),
        ),
    ]