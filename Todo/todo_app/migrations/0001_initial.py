# Generated by Django 4.2.10 on 2024-02-27 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('priority', models.IntegerField(default=0)),
                ('date', models.DateField(default='1111-11-11')),
            ],
        ),
    ]