<template>
    <AlertDialog>
        <AlertDialogTrigger as-child>
            <button class="absolute -right-3 -pt3 space-y-2 -top-5">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none"
                     viewBox="0 0 24 24" stroke-width="1.5"
                     stroke="currentColor" class="size-6">
                    <path stroke-linecap="round" stroke-linejoin="round"
                          d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125"/>
                </svg>
            </button>
        </AlertDialogTrigger>
        <AlertDialogContent class="max-w-96">
            <AlertDialogHeader>
                <AlertDialogTitle class="font-bold uppercase italic">Изменение
                    основных
                    характеристик
                </AlertDialogTitle>
                <AlertDialogDescription>
                    <div class="grid grid-cols-2 gap-3">
                        <SkillButton
                                skill-name="СИЛ"
                                v-model:skill-value="skills.strength"
                        ></SkillButton>
                        <SkillButton
                                skill-name="ЛВК"
                                v-model:skill-value="skills.dexterity"
                        ></SkillButton>
                        <SkillButton
                                skill-name="ТСЛ"
                                v-model:skill-value="skills.constitution"
                        ></SkillButton>
                        <SkillButton
                                skill-name="ИНТ"
                                v-model:skill-value="skills.intelligence"
                        ></SkillButton>
                        <SkillButton
                                skill-name="МДР"
                                v-model:skill-value="skills.wisdom"
                        ></SkillButton>
                        <SkillButton
                                skill-name="ХАР"
                                v-model:skill-value="skills.charisma"
                        ></SkillButton>
                    </div>
                </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
                <AlertDialogAction @click="postSkills">Изменить
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
    </AlertDialog>
</template>
<script setup>
import {useCharacterStore} from "@/stores/characterStore";
import {
    AlertDialog,
    AlertDialogAction,
    AlertDialogContent,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogTitle,
    AlertDialogTrigger,
} from '@/components/ui/alert-dialog'
import {Button} from '@/components/ui/button'
import SkillButton from "@/views/CharacterView/Skills/ui/SkillButton.vue";

const champion = useCharacterStore();
const skills = champion.character.skills

const store = useCharacterStore();
const postSkills = () => {
    store.postSkills();
}
</script>
<style scoped>

</style>