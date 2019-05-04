# Generated by Django 2.1.7 on 2019-05-04 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_status', models.CharField(choices=[('Death', 'Death'), ('Normal', 'Normal'), ('Lost', 'Lost')], default='Normal', max_length=20)),
                ('dog_name', models.CharField(max_length=50)),
                ('dog_info', models.TextField()),
                ('dog_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('dog_dob', models.DateField(blank=True, null=True)),
                ('dog_age', models.IntegerField(default=0)),
                ('qr_code', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Owner')),
            ],
        ),
    ]