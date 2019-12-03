# Generated by Django 2.2.4 on 2019-12-03 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='award_amount',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='enrollment_requisite',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='geographic_requisite',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='major_requisite',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='scholarship_link',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='scholarship_name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
