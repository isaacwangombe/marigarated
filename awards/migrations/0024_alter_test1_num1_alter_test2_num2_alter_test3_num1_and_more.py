# Generated by Django 4.0.2 on 2022-07-09 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0023_test1_test2_test3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test1',
            name='num1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='test2',
            name='num2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='test3',
            name='num1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='test3',
            name='num2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]