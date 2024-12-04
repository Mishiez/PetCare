# Generated by Django 4.2 on 2024-12-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petcareapp', '0002_alter_user_yob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
