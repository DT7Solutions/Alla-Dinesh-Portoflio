# Generated by Django 4.0.3 on 2023-12-20 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
