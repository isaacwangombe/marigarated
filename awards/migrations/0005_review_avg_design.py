# Generated by Django 4.0.2 on 2022-06-15 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0004_review_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='avg_design',
            field=models.IntegerField(default=0),
        ),
    ]
