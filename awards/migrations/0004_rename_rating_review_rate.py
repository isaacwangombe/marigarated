# Generated by Django 4.0.2 on 2022-06-09 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_delete_rating_review_project_review_rating_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rating',
            new_name='rate',
        ),
    ]