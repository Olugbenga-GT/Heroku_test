# Generated by Django 3.1.7 on 2021-04-22 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=14)),
                ('image', models.ImageField(upload_to='gallery/User/')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
