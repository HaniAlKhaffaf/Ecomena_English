# Generated by Django 4.0.6 on 2022-07-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco', '0012_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.TextField()),
            ],
        ),
    ]
