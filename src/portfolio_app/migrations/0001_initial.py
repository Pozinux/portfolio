<<<<<<< HEAD
# Generated by Django 3.1.5 on 2021-01-23 21:23
=======
# Generated by Django 3.1.5 on 2021-01-28 06:58
>>>>>>> 6ccbbb366e6a2a4821c53eea90c1382693402ffd

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='portfolio_app/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
