# Generated by Django 4.0.6 on 2022-07-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco', '0014_rename_user_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='subject',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=158),
        ),
    ]
