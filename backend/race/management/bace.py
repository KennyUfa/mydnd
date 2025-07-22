from race.models import SmallFeaturesRace, RaceBackground, Race

def half_elf():
    race,_ = Race.objects.get_or_create(
        name="",
        description="""""",
    )

    small_features_data = [
        {"name": "", "description": ""},
        {"name": "", "description": ""},
    ]

    for feature in small_features_data:
        x,_ = SmallFeaturesRace.objects.get_or_create(**feature)
        race.features.add(x)

    features_data = [
        {"name": "", "description": """"""},
        {"name": "", "description": """"""},
        {"name": "", "description": """"""},
        {"name": "", "description": """"""},
    ]

    for feature in features_data:
        x, _ = RaceBackground.objects.get_or_create(**feature)
        race.background.add(x)


    # _______
    # sub, _ = race.sub_race.get_or_create(
    #     name="",
    # )
    # sub.description = """"""
    # sub.save()
    #
    # small_features_data = [
    #     {"name": "", "description": ""},
    # ]
    #
    # for feature in small_features_data:
    #     x,_ = SmallFeaturesRace.objects.get_or_create(**feature)
    #     sub.features.add(x)
    #
    #
