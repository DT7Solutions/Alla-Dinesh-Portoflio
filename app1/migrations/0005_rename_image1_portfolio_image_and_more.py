# Generated by Django 5.0 on 2023-12-20 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_portfolio_alter_about_discription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='image1',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='image6',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
