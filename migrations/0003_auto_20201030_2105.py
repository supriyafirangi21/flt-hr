# Generated by Django 3.0.5 on 2020-10-30 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20201029_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_periods',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activity_periods',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_info', serialize=False, to='apis.Activity_user'),
        ),
        migrations.AlterField(
            model_name='activity_periods',
            name='start_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activity_user',
            name='id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='activity_user',
            name='real_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='activity_user',
            name='tz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]