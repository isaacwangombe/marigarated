# Generated by Django 4.0.2 on 2022-06-15 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0015_alter_profile_picture_alter_projects_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content_rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='design_rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='user_experience_rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
    ]
