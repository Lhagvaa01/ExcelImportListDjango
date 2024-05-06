# Generated by Django 4.1.7 on 2024-05-06 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TCUSERICON', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('TCUSERNAME', models.CharField(help_text='Хэрэглэгчийн нэр', max_length=100)),
                ('TCPHONE', models.IntegerField(blank=True, help_text='Нууц үг', null=True)),
                ('TCPASSWORD', models.CharField(help_text='Нууц үг', max_length=100)),
                ('TCEMAIL', models.CharField(help_text='Имэйл хаяг', max_length=100, unique=True)),
                ('otp', models.IntegerField(blank=True, editable=False, help_text='OTP CODE', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VoicherPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Нэр', max_length=255)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TCITEMCODE', models.CharField(help_text='Dotood kod', max_length=100)),
                ('TCNAME', models.CharField(help_text='Ner', max_length=100)),
                ('TCGROUP', models.CharField(help_text='Tasag', max_length=100)),
                ('TCSALEPRICE', models.IntegerField(blank=True, help_text='Sale Price', null=True)),
                ('TCBARCODE', models.IntegerField(blank=True, help_text='Barcode', null=True)),
                ('TCVOUCHERPRICEPk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExcelImport.voicherprice')),
            ],
        ),
    ]