<template>
    <Toaster position="boottom-right"/>
    <Tabs default-value="main">
        <TabsList class="grid grid-cols-4">
            <TabsTrigger value="main">
                Главная
            </TabsTrigger>
            <TabsTrigger value="class-information">
                Информация по классу
            </TabsTrigger>
            <TabsTrigger value="race-information">
                Расы и происхождения
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
            <TabsTrigger value="test">
                тест
            </TabsTrigger>
        </TabsList>
        <TabsContent value="main">

            <MainInformation></MainInformation>
            <saving-throw-view
                    @callRandomWindow="callRandomWindowMethod"></saving-throw-view>
            <ability-view
                    @callRandomWindow="callRandomWindowMethod"></ability-view>

            <!--        <div class="wrapper">-->
            <!--          <div class="container">-->
            <!--            <possession-bonus></possession-bonus>-->
            <!--            <passive-perception></passive-perception>-->
            <!--            <inspiration-frame></inspiration-frame>-->
            <!--            <protection-class-view></protection-class-view>-->
            <!--            <initiative-view></initiative-view>-->
            <!--            <speed-view></speed-view>-->
            <!--          </div>-->
            <!--        </div>-->
            <!--        <hit-vue></hit-vue>-->
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
        <TabsContent value="test">
            <test></test>
        </TabsContent>
    </Tabs>
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
import {Toaster} from "@/components/ui/toast";
import {useToast} from "@/components/ui/toast/use-toast";
import {h} from "vue";
import ToastContent from "@/views/CharacterView/Skills/ui/ToastContent.vue";
import {Tabs, TabsContent, TabsList, TabsTrigger} from '@/components/ui/tabs'
import InventoryView from "@/views/CharacterView/Inventory/InventoryView.vue";
import SpellBookView from "@/views/CharacterView/SpellBook/SpellBookView.vue";
import Test from "@/views/CharacterView/test.vue";

const router = useRouter();
const {toast} = useToast();


// Метод для показа тоста
const callRandomWindowMethod = (responseData) => {
    toast({
        title: "Бросок кубиков!",
        description: h(ToastContent, {data: responseData}), // Используем компонент
        variant: "default",
        position: "bottom-left",
    });
};

</script>
