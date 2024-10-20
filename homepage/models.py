from django.db import models

from tinymce.models import HTMLField


class MainPageContent(models.Model):
    img_name = models.CharField(
        max_length=20,
        verbose_name='Название картинки'
    )
    title_img = models.ImageField(
        upload_to = 'img/main_page/',
        verbose_name='Титульная картинка',
    )
    description = HTMLField(
        default = 'Немного о себе'
    )
    work_img = models.ImageField(
        upload_to= 'img/main_page/',
        default='',
        verbose_name='Картинка с работой',
    )

    class Meta:
        verbose_name = 'Контент на главной странице'
        verbose_name_plural = 'Контент на главной странице'

    def __str__(self):
        return self.img_name
