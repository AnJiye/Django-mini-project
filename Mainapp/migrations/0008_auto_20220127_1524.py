# Generated by Django 2.2.5 on 2022-01-27 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0007_total_like_board_total_scrap'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.DeleteModel(
            name='Like_Board',
        ),
        migrations.DeleteModel(
            name='Photo_Board',
        ),
        migrations.DeleteModel(
            name='QnA_Board',
        ),
        migrations.DeleteModel(
            name='Scrap',
        ),
    ]
