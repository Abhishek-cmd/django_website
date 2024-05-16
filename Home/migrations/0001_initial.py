# Generated by Django 5.0.6 on 2024-05-16 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('mobile_no', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('created_on', models.DateField()),
            ],
        ),
    ]
