# Generated by Django 2.2.4 on 2019-12-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholar', '0004_auto_20191203_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholar',
            name='award_amount',
            field=models.CharField(default='$0', max_length=100),
        ),
    ]
