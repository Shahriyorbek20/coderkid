# Generated by Django 5.1.3 on 2024-12-04 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
