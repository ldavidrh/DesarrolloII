# Generated by Django 2.2.2 on 2019-06-15 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]