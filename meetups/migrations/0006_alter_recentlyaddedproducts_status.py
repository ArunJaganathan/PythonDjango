# Generated by Django 4.2.1 on 2023-05-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_recentlyaddedproducts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentlyaddedproducts',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Active'), ('2', 'In Active'), ('3', 'Draft')], max_length=2, null=True),
        ),
    ]