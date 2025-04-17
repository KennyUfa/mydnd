<template>

    <Tabs default-value="main">
        <TabsList class="grid grid-cols-3">
            <TabsTrigger value="main">
                Главная
            </TabsTrigger>
            <TabsTrigger value="class-information">
                Класс и уровень
            </TabsTrigger>
            <TabsTrigger value="race-information">
                Раса
            </TabsTrigger>
            <TabsTrigger value="background">
                Предыстория
            </TabsTrigger>
            <TabsTrigger value="item_list">
                База предметов
            </TabsTrigger>
            <TabsTrigger value="inventory">
                Инвентарь
            </TabsTrigger>
            <TabsTrigger value="spell-book">
                Книга заклинаний
            </TabsTrigger>
        </TabsList>
        <TabsContent value="main">

            <MainInformation></MainInformation>
            <hit-view></hit-view>
            <inform></inform>

            <saving-throw-view
                    @callRandomWindow="callRandomWindowMethod"></saving-throw-view>
            <ability-view
                    @callRandomWindow="callRandomWindowMethod"></ability-view>
        </TabsContent>
        <TabsContent value="class-information">
            <class-information-view></class-information-view>
        </TabsContent>
        <TabsContent value="race-information">
            <race-and-origin></race-and-origin>
        </TabsContent>
        <TabsContent value="background">
            <background-view></background-view>
        </TabsContent>
        <TabsContent value="item_list">
            <ItemsView></ItemsView>
        </TabsContent>
        <TabsContent value="inventory">
            <inventory-view></inventory-view>
        </TabsContent>
        <TabsContent value="spell-book">
            <spell-book-view></spell-book-view>
        </TabsContent>
    </Tabs>
    <!--кубы-->
    <DropdownMenu>
        <DropdownMenuTrigger>
            <Button variant="outline"
                    class="fixed bottom-0 w-16 h-16 rounded-lg mb-2">
                <img src="@/assets/152068.svg" alt="Куб" class="w-10 h-10">
            </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent class="relative w-1 ml-2">
            <DropdownMenuLabel class="bg-green-500 rounded-xl"
                               v-if="rollStatus" @click="roll">Бросить кубы
            </DropdownMenuLabel>
            <DropdownMenuSeparator/>
            <DropdownMenuGroup>
                <DropdownMenuItem>
                    <div @click.stop="d4+=1" class="w-full">D4</div>
                    <DropdownMenuShortcut>{{ d4 }}</DropdownMenuShortcut>
                </DropdownMenuItem>
                <DropdownMenuItem>
                    <div @click.stop="d6+=1" class="w-full">D6</div>
                    <DropdownMenuShortcut>{{ d6 }}</DropdownMenuShortcut>
                </DropdownMenuItem>
                <DropdownMenuItem>
                    <div @click.stop="d8+=1" class="w-full">D8</div>
                    <DropdownMenuShortcut>{{ d8 }}</DropdownMenuShortcut>
                </DropdownMenuItem>
                <DropdownMenuItem>
                    <div @click.stop="d10+=1" class="w-full">D10</div>
                    <DropdownMenuShortcut>{{ d10 }}</DropdownMenuShortcut>
                </DropdownMenuItem>
                <DropdownMenuItem>
                    <div @click.stop="d12+=1" class="w-full">D12</div>
                    <DropdownMenuShortcut>{{ d12 }}</DropdownMenuShortcut>
                </DropdownMenuItem>
                <DropdownMenuItem>
                    <div @click.stop="d20+=1" class="w-full">D20</div>
                    <DropdownMenuShortcut>{{ d20 }}</DropdownMenuShortcut>
                </DropdownMenuItem>
                <DropdownMenuSeparator/>
            </DropdownMenuGroup>
        </DropdownMenuContent>
    </DropdownMenu>
</template>


<script setup>
import {useRouter} from "vue-router";
import MainInformation
    from "@/views/CharacterView/MainInformations/MainInformation.vue";
import ClassInformationView
    from "@/views/CharacterView/ClassInformations/ClassInformationsView.vue";
import AbilityView from "@/views/CharacterView/Skills/АbilityView.vue";
import BackgroundView from "@/views/CharacterView/Background/BackgroundView.vue"
import SavingThrowView from "@/views/CharacterView/Skills/SavingThrowView.vue";
import RaceAndOrigin
    from "@/views/CharacterView/RaceAndOrigin/RaceAndOrigin.vue"
import ItemsView from "@/views/CharacterView/Inventory/ItemsView.vue"
import {useToast} from "@/components/ui/toast/use-toast";
import {h, ref, watch} from "vue";
import ToastContent from "@/views/ToastContent.vue";
import {Tabs, TabsContent, TabsList, TabsTrigger} from '@/components/ui/tabs'
import InventoryView from "@/views/CharacterView/Inventory/InventoryView.vue";
import SpellBookView from "@/views/CharacterView/SpellBook/SpellBookView.vue";
import Inform from "@/views/CharacterView/CharacterInfo/Inform.vue";
import HitView from "@/views/CharacterView/HitView/HitVue.vue";
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuShortcut,
    DropdownMenuTrigger
} from "@/components/ui/dropdown-menu/index.js";
import {Button} from "@/components/ui/button/index.js";
import {useCharacterStore} from "@/stores/characterStore.js";
import RandomContent from "@/views/RandomContent.vue";

const router = useRouter();
const {toast} = useToast();


// Метод для показа тоста
const callRandomWindowMethod = (responseData) => {
    toast({
        class: "",
        title: "Бросок кубиков!",
        description: h(ToastContent, {data: responseData}),

    });

};

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
