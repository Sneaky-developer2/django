# Generated by Django 4.1 on 2022-08-21 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_review_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('down', 'Down Vote'), ('up', 'Up Vote')], max_length=200),
        ),
    ]