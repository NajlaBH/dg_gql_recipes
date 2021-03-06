# Generated by Django 2.2.9 on 2020-01-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20200113_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredient')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
