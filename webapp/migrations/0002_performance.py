# Generated by Django 3.1.3 on 2021-12-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algo', models.CharField(max_length=30)),
                ('acc', models.CharField(max_length=30)),
                ('prec', models.CharField(max_length=30)),
                ('recall', models.CharField(max_length=30)),
                ('f1', models.CharField(max_length=30)),
            ],
        ),
    ]