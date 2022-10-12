# Generated by Django 4.1.2 on 2022-10-12 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='buys',
            field=models.ManyToManyField(related_name='buys', to='main_app.purchased'),
        ),
        migrations.AlterField(
            model_name='purchased',
            name='budget',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='budget', to='main_app.budget'),
        ),
    ]
