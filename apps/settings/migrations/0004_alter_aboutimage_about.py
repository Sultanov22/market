# Generated by Django 3.2.7 on 2022-03-31 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_aboutimage_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutimage',
            name='about',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_image', to='settings.about'),
        ),
    ]