# Generated by Django 2.2.6 on 2019-11-05 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('cake_ID', models.AutoField(primary_key=True, serialize=False)),
                ('cake_Name', models.CharField(max_length=100)),
                ('date_made', models.DateField(auto_now=True)),
                ('descr', models.CharField(max_length=500)),
                ('cake_customer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('ingredient_id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient_name', models.CharField(max_length=200)),
                ('price_paid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_gram', models.DecimalField(decimal_places=5, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commnent_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('rating', models.IntegerField(default=5)),
                ('cake_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakes.Cake')),
            ],
        ),
    ]
