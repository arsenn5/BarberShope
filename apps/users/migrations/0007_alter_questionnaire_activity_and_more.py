# Generated by Django 4.2.7 on 2023-11-02 08:38

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_questionnaire_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='activity',
            field=models.CharField(max_length=100, verbose_name='Деятельность'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='area',
            field=models.CharField(max_length=100, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Последняя изминение'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='description',
            field=models.TextField(max_length=400, verbose_name='O себе'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='language',
            field=models.CharField(max_length=100, verbose_name='Язык'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефон номер'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='schedule',
            field=models.TimeField(verbose_name='Начало график работы'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='schedule_end',
            field=models.TimeField(verbose_name='Конец график работы'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='social',
            field=models.URLField(max_length=100, verbose_name='Соц сети'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='work_experience',
            field=models.CharField(max_length=100, verbose_name='Стаж работы'),
        ),
    ]
