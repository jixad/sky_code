# Generated by Django 2.2.2 on 2019-07-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skycode', '0005_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answered',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
