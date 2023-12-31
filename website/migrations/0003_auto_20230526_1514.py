# Generated by Django 3.2.6 on 2023-05-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20230526_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='catagory_image',
            new_name='category_image',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='catagory_name',
            new_name='category_name',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_photo',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
