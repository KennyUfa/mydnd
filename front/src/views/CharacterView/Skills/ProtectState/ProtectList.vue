<template>
    <div class="col-span-full text-center text-xl italic font-bold tracking-wide">
        <div class="flex items-center justify-between">
            <div class="w-6"></div>
            <div>Спасброски</div>
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
                            Изменение спассбросков
                        </AlertDialogTitle>
                        <AlertDialogDescription>

                            <div class="grid grid-cols-2">
                                <protect-frame
                                        @callRandomWindow="handleCallRandomWindow"
                                        skill-name="Сила"
                                        stat="strength"
                                        skill-value="protect_state_strength"
                                ></protect-frame>
                                <protect-frame
                                        @callRandomWindow="handleCallRandomWindow"
                                        skill-name="Ловкость"
                                        stat="dexterity"
                                        skill-value="protect_state_dexterity"
                                ></protect-frame>
                                <protect-frame
                                        @callRandomWindow="handleCallRandomWindow"
                                        skill-name="Телосложение"
                                        stat="constitution"
                                        skill-value="protect_state_constitution"
                                ></protect-frame>
                                <protect-frame
                                        @callRandomWindow="handleCallRandomWindow"
                                        skill-name="Интеллект"
                                        stat="intelligence"
                                        skill-value="protect_state_intelligence"
                                ></protect-frame>
                                <protect-frame
                                        @callRandomWindow="handleCallRandomWindow"
                                        skill-name="Мудрость"
                                        stat="wisdom"
                                        skill-value="protect_state_wisdom"
                                ></protect-frame>
                                <protect-frame
                                        @callRandomWindow="handleCallRandomWindow"
                                        skill-name="Харизма"
                                        stat="charisma"
                                        skill-value="protect_state_charisma"
                                ></protect-frame>
                            </div>
                        </AlertDialogDescription>
                    </AlertDialogHeader>
                    <AlertDialogFooter>
                        <AlertDialogAction @click="patchProtectSkills">Изменить
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
} from "@/components/ui/alert-dialog/index.js";
import ProtectFrame
    from "@/views/CharacterView/Skills/ProtectState/ProtectFrame.vue";
import {useCharacterStore} from "@/stores/characterStore.js";
const champion = useCharacterStore();


const patchProtectSkills = async () => {
    await champion.patchProtectSkills();
}

</script>
<style scoped>

</style>