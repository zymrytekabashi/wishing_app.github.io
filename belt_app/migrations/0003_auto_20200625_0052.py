# Generated by Django 2.2 on 2020-06-24 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0002_auto_20200625_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_wishes', to='belt_app.User'),
        ),
        migrations.DeleteModel(
            name='Granted',
        ),
    ]
