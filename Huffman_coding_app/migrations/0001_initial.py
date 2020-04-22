# Generated by Django 3.0.4 on 2020-04-12 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=100)),
                ('message', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]