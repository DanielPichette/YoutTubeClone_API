# Generated by Django 3.1.8 on 2021-05-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20210527_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.TextField(max_length=750, null=True),
        ),
    ]