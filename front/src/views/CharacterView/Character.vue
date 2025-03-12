<template>
  <Toaster position="boottom-right"/>
  <button @click="callRandomWindow">Показать уведомление</button>

  <Tabs default-value="class-information" class="">
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
  </Tabs>

  <!-- Tab panes -->
  <!--    <div class="tab-content">tab-content-->
  <!--      <div class="tab-pane fade" id="inventory" role="tabpanel">-->
  <!--        <inventory-view></inventory-view>-->
  <!--      </div>-->
  <!--      <div class="tab-pane fade" id="spells" role="tabpanel">-->
  <!--        <spell-view></spell-view>-->
  <!--      </div>-->
  <!--      <div class="tab-pane fade show active" id="main" role="tabpanel">-->

  <!--      </div>-->
  <!--    </div>-->
  <!--  </div>-->
  <!--                  <div class="tab-pane fade" id="prehistory" role="tabpanel">-->
  <!--                    <background-view></background-view>-->
  <!--                  </div>-->
  <!--  <div class="tab-pane fade" id="class-information"-->
  <!--       role="tabpanel">-->

  <!--  </div>-->
  <!--                  <div class="tab-pane fade" id="outher" role="tabpanel">-->
  <!--                    <proficiencie-and-languages></proficiencie-and-languages>-->
  <!--                  </div>-->
  <!--    </div>-->
  <!--  </div>-->
</template>


<script setup>
import {useRouter} from "vue-router";

import MainInformation
  from "@/views/CharacterView/MainInformations/MainInformation.vue";
import ClassInformationView
  from "@/views/CharacterView/ClassInformations/ClassInformationsView.vue";
import SkillsView from "@/views/CharacterView/Skills/SkillsView.vue";
import AbilityView from "@/views/CharacterView/Skills/АbilityView.vue";
import SavingThrowView from "@/views/CharacterView/Skills/SavingThrowView.vue";
import RaceAndOrigin from "@/views/CharacterView/RaceAndOrigin/RaceAndOrigin.vue"
import {Toaster} from "@/components/ui/toast";
import {useToast} from "@/components/ui/toast/use-toast";
import {h} from "vue";
import ToastContent from "@/views/CharacterView/Skills/ui/ToastContent.vue";

import {Button} from '@/components/ui/button'
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
