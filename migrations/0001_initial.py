# Generated by Django 2.1.1 on 2018-10-12 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retype_username', models.CharField(max_length=250)),
                ('retype_email', models.EmailField(max_length=254)),
                ('Phone_no', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('Date_of_Birth', models.DateField(blank=True, null=True)),
                ('Female_or_Male', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Help_and_Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=10)),
                ('comments_on_PG', models.TextField()),
                ('comments_on_website', models.TextField()),
                ('satisfied', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostelSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Check_in', models.CharField(max_length=250)),
                ('Check_out', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Landdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retype_username', models.CharField(max_length=250)),
                ('retype_email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('Hostel_name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=500)),
                ('Female_or_Male', models.CharField(max_length=50)),
                ('Mess', models.CharField(default='', max_length=50)),
                ('Pictures', models.CharField(max_length=1000)),
                ('Rent', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PG_selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='help_and_support',
            name='PG_selection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pg.PG_selection'),
        ),
        migrations.AddField(
            model_name='custdetails',
            name='Designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pg.Designation'),
        ),
    ]