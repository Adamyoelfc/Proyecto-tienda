# Generated by Django 2.1.3 on 2020-06-16 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20200613_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200)),
                ('descripcion', models.TextField(default='', max_length=300)),
            ],
        ),
    ]
