# Generated by Django 3.0.5 on 2020-10-29 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
