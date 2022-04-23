# Generated by Django 3.2.7 on 2022-03-31 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_alter_aboutimage_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_image', models.ImageField(upload_to='team_image/')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('skype', models.CharField(max_length=255)),
                ('youtube', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
    ]