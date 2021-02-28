# Generated by Django 3.1.7 on 2021-02-23 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentsite', '0002_auto_20210222_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(choices=[('Vd', 'Video'), ('Ebook', 'Ebook'), ('Audio', 'Audio')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
