# Generated by Django 2.2.1 on 2019-05-31 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt', models.CharField(max_length=4)),
                ('title', models.CharField(max_length=1000)),
                ('rating', models.CharField(max_length=1000, null=True)),
                ('subText', models.CharField(max_length=1000, null=True)),
                ('link_poster', models.CharField(max_length=1000, null=True)),
                ('linkVideoPoster', models.CharField(max_length=1000, null=True)),
                ('linkVideoTrailer', models.CharField(max_length=1000, null=True)),
                ('Storyline', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
