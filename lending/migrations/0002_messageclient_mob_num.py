# Generated by Django 4.1.4 on 2022-12-14 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageclient',
            name='mob_num',
            field=models.CharField(default=800000000, max_length=20),
            preserve_default=False,
        ),
    ]
