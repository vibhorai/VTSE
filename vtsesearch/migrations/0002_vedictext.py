# Generated by Django 4.1 on 2022-10-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtsesearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VedicText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('translation', models.CharField(max_length=5000)),
                ('url', models.CharField(max_length=5000)),
            ],
        ),
    ]
