# Generated by Django 4.1.1 on 2022-12-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='leftimg',
            field=models.ImageField(upload_to='images1/'),
        ),
        migrations.AlterField(
            model_name='information',
            name='rightimg',
            field=models.ImageField(upload_to='images1/'),
        ),
    ]
