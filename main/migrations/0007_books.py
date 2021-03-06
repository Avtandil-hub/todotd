# Generated by Django 3.1.3 on 2021-01-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210124_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=5)),
                ('genre', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
