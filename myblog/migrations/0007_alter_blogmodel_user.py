# Generated by Django 4.0.4 on 2022-05-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_alter_blogmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
