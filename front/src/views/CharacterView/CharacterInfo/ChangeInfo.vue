<template>
    <AlertDialog>
        <AlertDialogTrigger as-child>
            <button class="absolute right-1 top-2">
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
                <AlertDialogTitle
                        class="font-bold uppercase italic">Измененить показатели
                </AlertDialogTitle>
                <AlertDialogDescription>
                    <possession-bonus></possession-bonus>
                    <inspiration-frame></inspiration-frame>
                    <protection-class-view></protection-class-view>
                    <speed-view></speed-view>
                </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
                <AlertDialogAction @click="">Изменить
                </AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
    </AlertDialog>
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
import {Button} from "@/components/ui/button/index.js";
import PossessionBonus
    from "@/views/CharacterView/CharacterInfo/ChangeView/PossessionBonus.vue";
import InspirationFrame
    from "@/views/CharacterView/CharacterInfo/ChangeView/InspirationFrame.vue";
import ProtectionClassView
    from
        "@/views/CharacterView/CharacterInfo/ChangeView/ProtectionClassView.vue";
import SpeedView from
        "@/views/CharacterView/CharacterInfo/ChangeView/SpeedView.vue";
</script>

<style scoped>

</style>