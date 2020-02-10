# Generated by Django 2.1.7 on 2019-04-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nustartup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(default='insert')),
                ('logo', models.ImageField(blank=True, default='default.jpg', upload_to='events')),
                ('url', models.CharField(max_length=255)),
            ],
        ),
    ]
