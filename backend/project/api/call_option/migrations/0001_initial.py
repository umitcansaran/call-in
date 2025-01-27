# Generated by Django 2.2.7 on 2024-12-15 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('volunteer', '0001_initial'),
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('call', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='call_options', to='call.Call', verbose_name='call')),
                ('volunteers', models.ManyToManyField(blank=True, related_name='call_options', to='volunteer.Volunteer', verbose_name='volunteer participating')),
            ],
        ),
    ]
