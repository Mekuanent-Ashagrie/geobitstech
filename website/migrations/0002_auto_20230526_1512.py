# Generated by Django 3.2.6 on 2023-05-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_free',
            new_name='course_fee',
        ),
        migrations.AlterField(
            model_name='category',
            name='catagory_image',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
