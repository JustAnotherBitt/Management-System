# Generated by Django 5.1.6 on 2025-02-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telephone', models.CharField(blank=True, max_length=255, null=True)),
                ('complaint', models.CharField(choices=[('ADHD', 'ADHD'), ('D', 'Depression'), ('A', 'Anxiety'), ('GAD', 'Generalized anxiety disorder')], default='ADHD', max_length=4)),
                ('photo', models.ImageField(upload_to='photos')),
                ('payment_on_day', models.BooleanField(default=True)),
            ],
        ),
    ]
