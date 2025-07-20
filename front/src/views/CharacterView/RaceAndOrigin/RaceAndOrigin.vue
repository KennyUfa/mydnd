<template>
    <Accordion type="single" class="w-full" collapsible
               default-value="One">
        <!-- Блок для расы -->
        <AccordionItem value="One"
                       class="border border-black-400 rounded-2xl">
            <AccordionTrigger class="ml-4">Информация о расе: {{
                    race.name
                }}
            </AccordionTrigger>
            <AccordionContent>
                <CardHeader>
                    <CardTitle>{{ race.name }}</CardTitle>
                    <CardDescription>{{ race.description }}</CardDescription>
                </CardHeader>
                <CardHeader v-for="feature in race.features" :key="feature.id"
                            class="p-2">
                    <CardTitle>{{ feature.name }}</CardTitle>
                    <CardDescription>{{ feature.description }}</CardDescription>
                </CardHeader>
                <CardHeader v-for="backround in race.backgrounds"
                            :key="backround.id"
                            class="p-2">
                    <CardTitle>{{ backround.name }}</CardTitle>
                    <CardDescription>{{
                            backround.description
                        }}
                    </CardDescription>
                </CardHeader>
            </AccordionContent>
        </AccordionItem>

        <!-- Блок для подрасы -->
        <AccordionItem value="subrace-info"
                       class="border border-black-100 rounded-2xl mb-20">
            <AccordionTrigger class="ml-4">Информация о подрасе: {{
                    sub_race?.name || 'Нет подрасы'
                }}
            </AccordionTrigger>
            <!--ВЫБОР ПОДРАСЫ-->
            <DropdownMenu>
                <DropdownMenuTrigger v-on:click="loadSubRace">
                    <Button variant="outline" class="text-slate-900">
                        {{ sub_race?.name || 'Выбрать подрасу' }}
                    </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent>
                    <DropdownMenuLabel>
                        {{ sub_race?.name || 'Выбрать подрасу' }}
                    </DropdownMenuLabel>
                    <DropdownMenuSeparator/>
                    <DropdownMenuItem
                            v-for="sub_race in sub_race_list"
                            :key="sub_race.id"
                            @click="changeSubRace(sub_race)">
                        {{ sub_race.name }} <!-- Отображаем имя архетипа -->
                    </DropdownMenuItem>
                </DropdownMenuContent>
            </DropdownMenu>
            <!--ВЫБОР ПОДРАСЫ-->
            <AccordionContent v-if="sub_race">
                <CardHeader>
                    <CardTitle>{{ sub_race.name }}</CardTitle>
                    <CardDescription>{{
                            sub_race.description
                        }}
                    </CardDescription>
                </CardHeader>
                <CardHeader v-for="feature in sub_race.features"
                            :key="feature.id" class="p-2">
                    <CardTitle>{{ feature.name }}</CardTitle>
                    <CardDescription>{{ feature.description }}</CardDescription>
                </CardHeader>
                <CardHeader v-for="backround in sub_race.backgrounds"
                            :key="backround.id"
                            class="p-2">
                    <CardTitle>{{ backround.name }}</CardTitle>
                    <CardDescription>{{
                            backround.description
                        }}
                    </CardDescription>
                </CardHeader>
            </AccordionContent>
            <AccordionContent v-else>
                <p>Для этой расы нет подрас.</p>
            </AccordionContent>
        </AccordionItem>
    </Accordion>
</template>

<script setup>
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger
} from '@/components/ui/accordion'
import {useRaceStore} from "@/stores/raceStore.js";
import {
    CardDescription,
    CardHeader,
    CardTitle
} from "@/components/ui/card/index.js";
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger
} from "@/components/ui/dropdown-menu/index.js";
import {Button} from "@/components/ui/button/index.js";
import {computed} from "vue";

const store = useRaceStore();
const race = computed(() => store.race);
const sub_race_list = computed(() => store.sub_race_list);
const sub_race = computed(() => store.race.sub_race);

const loadSubRace = () => {
    store.loadSubRace()
}

const changeSubRace = (id) => {
    store.changeSubRace(id).then(() => {
    })
}
</script>