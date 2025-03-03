from django.db import models


class BackgroundSpecification(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class BackgroundModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    specifications = models.ManyToManyField(BackgroundSpecification)

    def __str__(self):
        return self.name


class CustomBackground(models.Model):
    character = models.ForeignKey(
        'Character', on_delete=models.CASCADE,
        related_name='background_specification_custom'
    )
    race_background = models.ForeignKey(
        BackgroundSpecification, on_delete=models.CASCADE,
        related_name='background_specification_custom',
    )
    custom_description = models.TextField(
        verbose_name="Пользовательское описание", blank=True, null=True
    )
    hide_original = models.BooleanField(
        verbose_name="Скрыть оригинальный текст", default=False
    )
