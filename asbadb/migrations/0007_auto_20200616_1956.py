# Generated by Django 3.0.7 on 2020-06-16 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asbadb', '0006_remove_userprofile_profilepic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.RenameField(
            model_name='credentials',
            old_name='Username',
            new_name='username',
        ),
    ]
