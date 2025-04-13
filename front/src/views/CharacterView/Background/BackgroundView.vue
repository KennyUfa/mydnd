<template>

    <CardTitle>Предыстория: {{
            background?.name || 'Нет предыстории'
        }}
    </CardTitle>
    <!--  выбор предыстории-->
    <DropdownMenu>
        <DropdownMenuTrigger v-on:click="loadBackgrounds">
            <Button variant="outline">
                {{ background?.name || 'Нет предыстории' }}
            </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent>
            <DropdownMenuLabel>
                {{ background?.name || 'Нет предыстории' }}
            </DropdownMenuLabel>
            <DropdownMenuSeparator/>
            <DropdownMenuItem
                    v-for="bg in background_list"
                    :key="bg.id"
                    @click="changeBackground(bg)">
                {{ bg.name }} <!-- Отображаем имя архетипа -->
            </DropdownMenuItem>
        </DropdownMenuContent>
    </DropdownMenu>
    <CardDescription>{{ background?.description }}</CardDescription>
    <!--  выбор предыстории-->
    <div class="my-3">

        <CardTitle>Слабости -{{
                background?.selected_origins.flaw?.name
            }}
        </CardTitle>

        <DropdownMenu>
            <DropdownMenuTrigger>
                <Button variant="outline">
                    сменить
                </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent class="max-w-[420px] mx-1">
                <DropdownMenuItem
                        v-for="i in background.flaw"
                        :key="i.id"
                        @click="change({'flaw': i})">
                    {{ i.name }}
                </DropdownMenuItem>
            </DropdownMenuContent>
        </DropdownMenu>


        <CardTitle>Привязанности - {{
                background?.selected_origins.bond?.name
            }}
        </CardTitle>
        <DropdownMenu>
            <DropdownMenuTrigger>
                <Button variant="outline">
                    сменить
                </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent class="max-w-[420px] mx-1">
                <DropdownMenuItem
                        v-for="i in background.bond"
                        :key="i.id"
                        @click="change({'bond': i})">
                    {{ i.name }}
                </DropdownMenuItem>
            </DropdownMenuContent>
        </DropdownMenu>

        <CardTitle>Идеалы - {{
                background?.selected_origins.ideal?.name
            }}
        </CardTitle>
        <DropdownMenu>
            <DropdownMenuTrigger>
                <Button variant="outline">
                    сменить
                </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent class="max-w-[420px] mx-1">
                <DropdownMenuItem
                        class="text-wrap"
                        v-for="i in background.ideal"
                        :key="i.id"
                        @click="change({'ideal': i})">
                    {{ i.name }}
                </DropdownMenuItem
                        class>
            </DropdownMenuContent>
        </DropdownMenu>

        <CardTitle>Черта характера - {{
                background?.selected_origins.trait?.name
            }}
        </CardTitle>
        <DropdownMenu>
            <DropdownMenuTrigger>
                <Button variant="outline">
                    сменить
                </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent class="max-w-[420px] mx-1">
                <DropdownMenuItem
                        v-for="i in background.trait"
                        :key="i.id"
                        @click="change({'trait': i})">
                    {{ i.name }}
                </DropdownMenuItem>
            </DropdownMenuContent>
        </DropdownMenu>
    </div>

    <CardHeader v-for="skill_proficiencies in background?.skill_proficiencies"
                :key="skill_proficiencies.id"
                class="p-2">
        <CardTitle>{{ skill_proficiencies.name }}</CardTitle>
        <CardDescription>{{
                skill_proficiencies.skills_proficiency
            }}
        </CardDescription>
    </CardHeader>
    <CardHeader v-for="feature in background?.features" :key="feature.id"
                class="p-2">
        <CardTitle>{{ feature.name }}</CardTitle>
        <CardDescription>{{ feature.description }}</CardDescription>
        <CardTitle>{{
                feature.selected_options?.option_name ||
                ''
            }}
        </CardTitle>
        <DropdownMenu>
            <DropdownMenuTrigger v-if="feature.has_choice">
                <Button variant="outline">
                    {{ feature?.name || 'Выбрать подрасу' }}
                </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent>
                <DropdownMenuItem
                        v-for="options in feature.options"
                        :key="options.id"
                        @click="changeOptions({'feature': feature.id, 'option': options.id})">
                    {{ options.name }} <!-- Отображаем имя архетипа -->
                </DropdownMenuItem>
            </DropdownMenuContent>
        </DropdownMenu>
    </CardHeader>

</template>

<script setup>
import {
    CardDescription,
    CardHeader,
    CardTitle
} from "@/components/ui/card/index.js";
import {useBackground} from "@/stores/BackgroundStore.js";
import {computed} from "vue";
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger
} from "@/components/ui/dropdown-menu/index.js";
import {Button} from "@/components/ui/button/index.js";

const store = useBackground();
const background = computed(() => store.background)
const background_list = computed(() => store.background_list)

const loadBackgrounds = () => {
    store.loadBackgrounds()
}
const changeBackground = (bg) => {
    store.changeBackground(bg)
}
const changeOptions = (options) => {
    store.changeOptions(options)
}
const change = (options) => {
    store.change(options)
}
</script>
<style scoped></style>
