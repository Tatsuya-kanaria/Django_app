# Generated by Django 3.2.4 on 2021-09-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=200)),
                ('gender', models.BooleanField()),
                ('age', models.IntegerField(default=0)),
                ('birthday', models.DateField()),
            ],
        ),
    ]
