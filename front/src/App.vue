<template>

    <navbar-view></navbar-view>
    <router-view></router-view>
    <Toaster/>
    <DropdownMenu>
        <DropdownMenuTrigger>
            <Button variant="outline">
                Open
            </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent class="w-1 ml-2">
            <DropdownMenuLabel class="bg-green-500 rounded-xl"
                               v-if="rollStatus" @click="roll">Бросить кубы
            </DropdownMenuLabel>
            <DropdownMenuSeparator/>
            <DropdownMenuGroup>
                <DropdownMenuItem>
                    <div @click.stop="d4+=1">D4</div>
                    <DropdownMenuShortcut>{{ d4 }}</DropdownMenuShortcut>
                </DropdownMenuItem>
                <DropdownMenuItem>
                    <div @click.stop="d6+=1">D6</div>
                    <DropdownMenuShortcut>{{ d6 }}</DropdownMenuShortcut>
                </DropdownMenuItem>
                <DropdownMenuItem>
                    <div @click.stop="d8+=1">D8</div>
                    <DropdownMenuShortcut>{{ d8 }}</DropdownMenuShortcut>
                </DropdownMenuItem>
                <DropdownMenuItem>
                    <div @click.stop="d10+=1">D10</div>
                    <DropdownMenuShortcut>{{ d10 }}</DropdownMenuShortcut>
                </DropdownMenuItem>
                <DropdownMenuItem>
                    <div @click.stop="d12+=1">D12</div>
                    <DropdownMenuShortcut>{{ d12 }}</DropdownMenuShortcut>
                </DropdownMenuItem>
                <DropdownMenuItem>
                    <div @click.stop="d20+=1">D20</div>
                    <DropdownMenuShortcut>{{ d20 }}</DropdownMenuShortcut>
                </DropdownMenuItem>
                <DropdownMenuSeparator/>
            </DropdownMenuGroup>
        </DropdownMenuContent>
    </DropdownMenu>
</template>

<script setup>

import NavbarView from "./components/NavbarView.vue";
import Toaster from '@/components/ui/toast/Toaster.vue'

import {Button} from '@/components/ui/button'
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuShortcut,
    DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import {h, ref, watch} from "vue";
import {useCharacterStore} from "@/stores/characterStore.js";
import {toast} from "@/components/ui/toast/index.js";
import RandomContent from "@/views/RandomContent.vue";

const champion = useCharacterStore();

const rollStatus = ref(false);
const d6 = ref(0);
const d4 = ref(0);
const d8 = ref(0);
const d10 = ref(0);
const d12 = ref(0);
const d20 = ref(0);

watch([d4, d6, d8, d10, d12, d20], () => {
        rollStatus.value = true

    }
)


const roll = () => {
    champion.rollDice(d4.value, d6.value, d8.value, d10.value,
        d12.value,
        d20.value).then(result => {
        toast({
            title: "Бросок кубиков!",
            description: h(RandomContent, {
                result: result
            })
        });
        d6.value = 0
        d4.value = 0
        d8.value = 0
        d10.value = 0
        d12.value = 0
        d20.value = 0
        rollStatus.value = false;
    })
}
</script>