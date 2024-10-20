# Generated by Django 4.2.16 on 2024-10-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(max_length=20, verbose_name='Название картинки')),
                ('title_img', models.ImageField(upload_to='img/main_page/', verbose_name='Титульная картинка')),
            ],
            options={
                'verbose_name': 'Контент на главной странице',
                'verbose_name_plural': 'Контент на главной странице',
            },
        ),
    ]
