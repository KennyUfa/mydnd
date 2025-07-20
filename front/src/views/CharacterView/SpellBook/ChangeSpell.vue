<template>
    <Sheet>
        <SheetTrigger as-child>
            <Button variant="outline" class="text-black">
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
                <div class="relative">
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


                                    <Dialog>
                                        <DialogTrigger class="spell-block"
                                                       as-child>
                                            <Button variant="outline "
                                                    class="text-balance"
                                                    @click="getSpellDetails(spell)">
                                                {{ spell.name }}
                                            </Button>
                                        </DialogTrigger>
                                        <DialogContent class="overflow-y-auto max-h-[80vh]">
                                            <DialogHeader
                                                    v-if="spell_details" class="">
                                                <DialogTitle>
                                                    {{ spell_details.name }} -
                                                    Уровень:
                                                    {{
                                                        spell_details.level
                                                    }}
                                                </DialogTitle>
                                                <DialogDescription>
                                                    <div>{{
                                                            spell_details.class_actor
                                                        }}
                                                    </div>
                                                    <div>{{
                                                            spell_details.archetype
                                                        }}
                                                    </div>
                                                    <div>{{
                                                            spell_details.school
                                                        }}
                                                    </div>
                                                    <div>{{
                                                            spell_details.timing
                                                        }}
                                                    </div>
                                                    <div>{{
                                                            spell_details.instruction
                                                        }}
                                                    </div>
                                                </DialogDescription>
                                            </DialogHeader>
                                        </DialogContent>
                                    </Dialog>
                                    <Badge @click="addSpell(spell)"
                                           class="border-2 rounded-md w-30 h-30">
                                        +
                                    </Badge>
                                </div>
                            </SheetDescription>
                        </div>
                    </div>
                    <SheetClose as-child class="fixed bottom-0 right-0">
                        <Button type="submit">
                            Закрыть окно
                        </Button>
                    </SheetClose>
                </div>

            </SheetFooter>
        </SheetContent>
    </Sheet>
</template>
<script setup>

import {
    Sheet,
    SheetClose,
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
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogTrigger
} from "@/components/ui/dialog/index.js";

const create_character = useCreateCharacter();
const spell_book = useSpellBook();


const class_list = computed(() => create_character.class_list);
const spells = computed(() => spell_book.spells);
const archetype_list = computed(() => spell_book.archetype_list);
const spell_details = computed(() => spell_book.spell_details);
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
    console.log(spell_book.sortByClass.values())
}

function getArchetypeColor(id) {
    return {
        'bg-lime-600': !spell_book.sortByArchetype.includes(id), // Зелёный цвет по умолчанию
        'bg-cyan-600': spell_book.sortByArchetype.includes(id)   // Цвет при выборе
    };
}

function getSpellDetails(spell) {
    spell_book.getSpellDetails(spell.id)
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