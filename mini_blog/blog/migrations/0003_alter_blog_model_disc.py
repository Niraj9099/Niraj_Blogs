# Generated by Django 4.1.7 on 2023-03-31 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contactform_alter_blog_model_disc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_model',
            name='disc',
            field=models.FloatField(max_length=1000),
        ),
    ]