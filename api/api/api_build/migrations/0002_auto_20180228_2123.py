# Generated by Django 2.0.2 on 2018-02-28 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_build', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='appliances',
        ),
        migrations.DeleteModel(
            name='dailyusage',
        ),
        migrations.DeleteModel(
            name='energyusage',
        ),
        migrations.DeleteModel(
            name='hvacusage',
        ),
        migrations.DeleteModel(
            name='rooms',
        ),
        migrations.DeleteModel(
            name='sensors',
        ),
        migrations.DeleteModel(
            name='waterusage',
        ),
        migrations.DeleteModel(
            name='weather',
        ),
    ]
