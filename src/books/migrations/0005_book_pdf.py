# Generated by Django 2.2 on 2021-06-21 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210621_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='book_pdf'),
        ),
    ]
