# Generated by Django 3.2.3 on 2021-07-23 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0005_auto_20210521_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagetest',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='num1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagetest',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
