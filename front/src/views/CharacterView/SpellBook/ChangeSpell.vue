<template>
    <Sheet>
        <SheetTrigger as-child>
            <Button variant="outline">
                Добавить заклинание
            </Button>
        </SheetTrigger>
        <SheetContent class="overflow-y-auto w-full sm:max-w-3xl">
            <SheetHeader>
                <SheetTitle>Книга заклинаний</SheetTitle>
                <SheetDescription v-if="!class_list">
                    <Badge>Загрузка классов</Badge>
                </SheetDescription>
                <SheetDescription v-else>
                    <Badge v-for="cls in class_list"
                           @click="addSearchClass(cls.id)"
                           :class="getClassColor(cls.id)">
                        <span>{{ cls.name }}</span>
                    </Badge>
                </SheetDescription>

                <SheetDescription v-if="archetype_list.length>0">
                    <Badge v-for="cls in archetype_list"
                           @click="addSearchArchetype(cls.id)"
                           :class="getArchetypeColor(cls.id)">
                        <span>{{ cls.name }}</span>
                    </Badge>
                </SheetDescription>
                <div class="grid gap-4 py-4">
                    <div class="grid grid-cols-4 items-center gap-4">
                        <Label for="name" class="text-right">
                            поиск
                        </Label>
                        <input id="name"
                               class="col-span-3 border-4"/>
                    </div>
                </div>
                <Button type="submit"
                        @click="spell_book.searchSpells">
                    Найти
                </Button>
            </SheetHeader>

            <SheetFooter>
                <div class="">
                    <!-- Перебираем уровни -->
                    <div v-for="(spells, level) in spells" :key="level"
                         class="">
                        <!-- Заголовок уровня -->
                        <SheetTitle>Уровень {{ level }}</SheetTitle>

                        <!-- Список заклинаний -->
                        <div class="">
                            <SheetDescription v-for="spell in spells"
                                              :key="spell.id">
                                <div class="border-2 rounded-md flex justify-between">
                                    <div>{{
                                            spell.name
                                        }}
                                    </div>
                                    <Badge @click="addSpell(spell)"
                                            class="border-2 rounded-md w-30 h-30">+
                                    </Badge>
                                </div>

                            </SheetDescription>
                        </div>
                    </div>
                </div>
            </SheetFooter>
        </SheetContent>
    </Sheet>
</template>
<script setup>

import {
    Sheet,
    SheetContent,
    SheetDescription,
    SheetFooter,
    SheetHeader,
    SheetTitle,
    SheetTrigger
} from "@/components/ui/sheet/index.js";
import {Button} from "@/components/ui/button/index.js";
import Label from "@/components/ui/label/Label.vue";
import {Badge} from "@/components/ui/badge/index.js";
import {computed} from "vue";
import {useCreateCharacter} from "@/stores/create.character.js";
import {useSpellBook} from "@/stores/SpellBookStore.js";

const create_character = useCreateCharacter();
const spell_book = useSpellBook();


const class_list = computed(() => create_character.class_list);
const spells = computed(() => spell_book.spells);
const archetype_list = computed(() => spell_book.archetype_list);

const props = defineProps({
    level_slots: Number
});

function addSearchClass(id) {
    const index = spell_book.sortByClass.indexOf(id);
    if (index === -1) {
        spell_book.sortByClass.push(id); // Добавляем ID в список
    } else {
        spell_book.sortByClass.splice(index, 1); // Удаляем ID из списка
    }
    spell_book.getArchetypeList();
}

function getArchetypeColor(id) {
    return {
        'bg-lime-600': !spell_book.sortByArchetype.includes(id), // Зелёный цвет по умолчанию
        'bg-cyan-600': spell_book.sortByArchetype.includes(id)   // Цвет при выборе
    };
}

function addSearchArchetype(id) {
    const index = spell_book.sortByArchetype.indexOf(id);
    if (index === -1) {
        spell_book.sortByArchetype.push(id); // Добавляем ID в список
    } else {
        spell_book.sortByArchetype.splice(index, 1); // Удаляем ID из списка
    }
}

function getClassColor(id) {
    return {
        'bg-lime-600': !spell_book.sortByClass.includes(id), // Зелёный цвет по умолчанию
        'bg-cyan-600': spell_book.sortByClass.includes(id)   // Цвет при выборе
    };
}

function addSpell(spell) {
    spell_book.addSpell(spell, props.level_slots);
}

</script>