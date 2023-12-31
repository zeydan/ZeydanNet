# Generated by Django 4.2.1 on 2023-05-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField(max_length=1000)),
                ('ipaddress', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
