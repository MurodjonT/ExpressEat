# Generated by Django 4.0.5 on 2022-08-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_food', '0003_alter_mahsulotlar_mahsulot_narxi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=150, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
