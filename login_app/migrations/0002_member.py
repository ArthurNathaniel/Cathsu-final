# Generated by Django 4.1.7 on 2023-05-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('contact_number', models.PositiveIntegerField()),
                ('house_number', models.CharField(max_length=255)),
                ('hometown', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('profile_image', models.ImageField(upload_to='profile_images')),
                ('previous_school', models.CharField(max_length=255)),
                ('current_school', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('level', models.CharField(max_length=255)),
                ('field', models.CharField(max_length=255)),
                ('date_of_joining', models.DateField()),
                ('status', models.CharField(choices=[('Active', 'Active Member'), ('Affiliate', 'Affiliate Member'), ('Patron', 'Patron/Patronessess')], max_length=255)),
            ],
        ),
    ]
