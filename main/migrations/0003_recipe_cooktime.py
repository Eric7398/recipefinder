# Generated by Django 2.2.4 on 2020-11-17 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201116_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooktime',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
    ]