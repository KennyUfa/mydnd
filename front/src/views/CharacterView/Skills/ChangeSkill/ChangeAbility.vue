<template>
    <div class="col-span-full text-center text-xl italic font-bold tracking-wide">
        <div class="flex items-center justify-between">
            <div class="w-6"></div>
            <div>Навыки</div>
            <AlertDialog>
                <AlertDialogTrigger as-child>
                    <button class="">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none"
                             viewBox="0 0 24 24" stroke-width="1.5"
                             stroke="currentColor" class="size-6">
                            <path stroke-linecap="round"
                                  stroke-linejoin="round"
                                  d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125"/>
                        </svg>
                    </button>
                </AlertDialogTrigger>
                <AlertDialogContent class="max-w-96 px-2 overflow-y: auto">
                    <AlertDialogHeader>
                        <AlertDialogTitle
                                class="font-bold uppercase italic">
                            Изменение навыков
                        </AlertDialogTitle>
                        <AlertDialogDescription>

                            <div class="grid grid-cols-2">
                                <change-ability-frame

                                        skill-name="Атлетика"
                                        stat="strength"
                                        skill-value="athletics"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Акробатика"
                                        stat="dexterity"
                                        skill-value="acrobatics"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Ловкость рук"
                                        stat="dexterity"
                                        skill-value="sleight_of_hand"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Скрытность"
                                        stat="dexterity"
                                        skill-value="stealth"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Магия"
                                        stat="intelligence"
                                        skill-value="arcana"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="История"
                                        stat="intelligence"
                                        skill-value="history"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Анализ"
                                        stat="intelligence"
                                        skill-value="investigation"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Природа"
                                        stat="intelligence"
                                        skill-value="nature"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Религия"
                                        stat="intelligence"
                                        skill-value="religion"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Уход за животными"
                                        stat="wisdom"
                                        skill-value="animal_handling"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Проницательность"
                                        stat="wisdom"
                                        skill-value="insight"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Медицина"
                                        stat="wisdom"
                                        skill-value="medicine"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Внимательность"
                                        stat="wisdom"
                                        skill-value="perception"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Выживание"
                                        stat="wisdom"
                                        skill-value="survival"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Обман"
                                        stat="charisma"
                                        skill-value="deception"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Запугивание"
                                        stat="charisma"
                                        skill-value="intimidation"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Выступление"
                                        stat="charisma"
                                        skill-value="performance"

                                ></change-ability-frame>
                                <change-ability-frame

                                        skill-name="Убеждение"
                                        stat="charisma"
                                        skill-value="persuasion"
                                ></change-ability-frame>
                            </div>
                        </AlertDialogDescription>
                    </AlertDialogHeader>
                    <AlertDialogFooter>
                        <AlertDialogAction class="mb-20"
                                           @click="patchAbilitySkills">Изменить
                        </AlertDialogAction>
                    </AlertDialogFooter>
                </AlertDialogContent>
            </AlertDialog>

        </div>
    </div>
</template>
<script setup>
import {
    AlertDialog,
    AlertDialogAction,
    AlertDialogContent,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogTitle,
    AlertDialogTrigger
} from "@/components/ui/alert-dialog";
import {useCharacterStore} from "@/stores/characterStore.js";
import ChangeAbilityFrame
    from "@/views/CharacterView/Skills/ChangeSkill/ChangeAbilityFrame.vue";

const champion = useCharacterStore();

const patchAbilitySkills = () => {
    champion.patchAbilityState();
}
</script>

<style scoped>

</style>