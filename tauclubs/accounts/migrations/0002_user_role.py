# Generated by Django 3.2.10 on 2022-12-01 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('U', 'User'), ('A', 'Admin'), ('CM', 'Club Manager'), ('M', 'Member')], default='U', max_length=2),
        ),
    ]
