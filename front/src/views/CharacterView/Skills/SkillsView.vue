<template>
    <div class="relative my-6">
        <change-skills></change-skills>
        <div class="grid grid-cols-6 gap-4">
            <BaseSkill
                    skill-name="СИЛ"
                    v-model:skill-value="skills.strength"

            ></BaseSkill>
            <BaseSkill
                    skill-name="ЛВК"
                    v-model:skill-value="skills.dexterity"

            ></BaseSkill>
            <BaseSkill
                    skill-name="ТСЛ"
                    v-model:skill-value="skills.constitution"

            ></BaseSkill>
            <BaseSkill
                    skill-name="ИНТ"
                    v-model:skill-value="skills.intelligence"

            ></BaseSkill>
            <BaseSkill
                    skill-name="МДР"
                    v-model:skill-value="skills.wisdom"
            ></BaseSkill>
            <BaseSkill
                    skill-name="ХАР"
                    v-model:skill-value="skills.charisma"
            ></BaseSkill>
        </div>
    </div>
</template>

<script setup>
import {useCharacterStore} from "@/stores/characterStore";
import BaseSkill
    from "@/views/CharacterView/MainInformations/ChangeSkills/BaseSkill.vue";
import ChangeSkills
    from "@/views/CharacterView/MainInformations/ChangeSkills/ChangeSkills.vue";

const champion = useCharacterStore();
const skills = champion.character.skills


</script>

<style scoped>
</style>
