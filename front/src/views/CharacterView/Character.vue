<template>
  <Toaster position="boottom-right"/>
  <Tabs default-value="inventory">
    <TabsList>
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
      <TabsTrigger value="inventory">
        Инвентарь
      </TabsTrigger>
    </TabsList>
    <TabsContent value="main">
      <skills-view></skills-view>
      <MainInformation></MainInformation>
      <ability-view @callRandomWindow="callRandomWindowMethod"></ability-view>
      <saving-throw-view
        @callRandomWindow="callRandomWindowMethod"></saving-throw-view>
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
    <TabsContent value="inventory">
      <inventory-view></inventory-view>
    </TabsContent>
  </Tabs>
</template>


<script setup>
import {useRouter} from "vue-router";

import MainInformation
  from "@/views/CharacterView/MainInformations/MainInformation.vue";
import ClassInformationView
  from "@/views/CharacterView/ClassInformations/ClassInformationsView.vue";
import SkillsView from "@/views/CharacterView/Skills/SkillsView.vue";
import AbilityView from "@/views/CharacterView/Skills/АbilityView.vue";
import BackgroundView from "@/views/CharacterView/Background/BackgroundView.vue"
import SavingThrowView from "@/views/CharacterView/Skills/SavingThrowView.vue";
import RaceAndOrigin
  from "@/views/CharacterView/RaceAndOrigin/RaceAndOrigin.vue"
import InventoryView from "@/views/CharacterView/Inventory/InventoryView.vue"
import {Toaster} from "@/components/ui/toast";
import {useToast} from "@/components/ui/toast/use-toast";
import {h} from "vue";
import ToastContent from "@/views/CharacterView/Skills/ui/ToastContent.vue";
import {Tabs, TabsContent, TabsList, TabsTrigger} from '@/components/ui/tabs'


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
