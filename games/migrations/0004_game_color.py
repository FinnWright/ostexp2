# Generated by Django 4.0.4 on 2022-06-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_game_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='color',
            field=models.CharField(default='#00076f', max_length=10),
            preserve_default=False,
        ),
    ]
