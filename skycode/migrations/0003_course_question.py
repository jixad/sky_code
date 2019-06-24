# Generated by Django 2.2.2 on 2019-06-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skycode', '0002_auto_20190623_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('teacher', models.CharField(max_length=50)),
                ('start', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='course/')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('question', models.TextField(max_length=200)),
            ],
        ),
    ]
