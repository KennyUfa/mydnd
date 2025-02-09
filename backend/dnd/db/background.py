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

    def get_background(self, obj):
        if not obj.background:
            return {"message": "No background assigned"}

        race_data = {
            "id": obj.background.id,
            "name": obj.background.name,
            "description": obj.background.description,
            "specifications": self.get_specification_with_custom(obj),

        }
        return race_data

    def get_specification_with_custom(self, obj):
        custom_specifications = CustomBackground.objects.filter(character=obj)
        custom_map = {custom.race_background_id: custom for custom in
                      custom_specifications}
        specification = obj.background.specifications.all()

        result = []

        for specific in specification:
            data = {
                "id": specific.id,
                "name": specific.name,
                "description": specific.description,

            }
            custom = custom_map.get(specific.id)

            if custom:
                specific.description = custom.custom_description
                specific.hide_original = custom.hide_original
                data["custom"] = {
                    "id": custom.id,
                    "custom_description": custom.custom_description,
                    "hide_original": custom.hide_original,
                }
            result.append(data)
        return result


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
