# Generated by Django 5.1.6 on 2025-02-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0002_doctor_alter_patients_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Position', models.CharField(max_length=20)),
                ('Phonenumber', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Hiredate', models.DateField()),
            ],
        ),
        migrations.RenameModel(
            old_name='patients',
            new_name='patient',
        ),
    ]
