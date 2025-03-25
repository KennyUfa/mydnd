<template>
    <!--    описание класса -->
    <div class="bg-white text-slate-900 border-2 border-red-600 rounded-lg p-4">
        <div class="font-bold uppercase text-xl italic">{{
                champion_class.name
            }}
        </div>
        <div class="">{{
                champion_class.description
            }}
        </div>
    </div>

    <DropdownMenu>
        <DropdownMenuTrigger v-on:click="loadArchetypes">
            <Button variant="outline">
                {{ 'Выбрать' }}
            </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent>
            <DropdownMenuItem
                    v-for="arch in archetype_list"
                    :key="arch.id"
                    @click="changeArchetype(arch)">
                {{ arch.name }}
            </DropdownMenuItem>
        </DropdownMenuContent>
    </DropdownMenu>

    <!--описание архетипа-->
    <div class="bg-white text-slate-900 border-2 border-red-600 rounded-lg p-4">
        <div class="font-bold uppercase text-xl italic"
             v-if="archetype">{{
                archetype.name
            }}
        </div>
        <div class="" v-if="archetype">
            <p class="">{{
                    archetype.description
                }}</p>
        </div>
    </div>

    <!-- Описание способностей -->
    <div v-if="store.allAbilities.length > 0" class="">
        <h3 class="font-bold text-center uppercase py-3">
            Описание способностей</h3>
        <div
                v-for="ability in store.allAbilities"
                :key="ability.name"
                :id="`ability-${ability.name.toLowerCase().replace(/\s+/g, '-')}`"
        >


            <div class="bg-white border-2 border-red-600 rounded-lg p-4 mb-3 relative">
                <DropdownMenu>
                    <DropdownMenuTrigger
                            class="absolute right-1.5 top-0.5 mt-2">
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg"
                                 viewBox="0 0 24 24"
                                 fill="currentColor" class="size-6">
                                <path fill-rule="evenodd"
                                      d="M11.078 2.25c-.917 0-1.699.663-1.85 1.567L9.05 4.889c-.02.12-.115.26-.297.348a7.493 7.493 0 0 0-.986.57c-.166.115-.334.126-.45.083L6.3 5.508a1.875 1.875 0 0 0-2.282.819l-.922 1.597a1.875 1.875 0 0 0 .432 2.385l.84.692c.095.078.17.229.154.43a7.598 7.598 0 0 0 0 1.139c.015.2-.059.352-.153.43l-.841.692a1.875 1.875 0 0 0-.432 2.385l.922 1.597a1.875 1.875 0 0 0 2.282.818l1.019-.382c.115-.043.283-.031.45.082.312.214.641.405.985.57.182.088.277.228.297.35l.178 1.071c.151.904.933 1.567 1.85 1.567h1.844c.916 0 1.699-.663 1.85-1.567l.178-1.072c.02-.12.114-.26.297-.349.344-.165.673-.356.985-.57.167-.114.335-.125.45-.082l1.02.382a1.875 1.875 0 0 0 2.28-.819l.923-1.597a1.875 1.875 0 0 0-.432-2.385l-.84-.692c-.095-.078-.17-.229-.154-.43a7.614 7.614 0 0 0 0-1.139c-.016-.2.059-.352.153-.43l.84-.692c.708-.582.891-1.59.433-2.385l-.922-1.597a1.875 1.875 0 0 0-2.282-.818l-1.02.382c-.114.043-.282.031-.449-.083a7.49 7.49 0 0 0-.985-.57c-.183-.087-.277-.227-.297-.348l-.179-1.072a1.875 1.875 0 0 0-1.85-1.567h-1.843ZM12 15.75a3.75 3.75 0 1 0 0-7.5 3.75 3.75 0 0 0 0 7.5Z"
                                      clip-rule="evenodd"/>
                            </svg>
                        </div>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent class="w-56">
                        <DropdownMenuLabel class="text-center">Настройки
                            отображения
                        </DropdownMenuLabel>
                        <DropdownMenuSeparator/>
                        <DropdownMenuGroup>
                            <DropdownMenuItem>
                                <div class="flex items-center space-x-2">
                                    <Switch class="ml-5"
                                            v-model="ability.custom_description.hide_original"
                                            @click="updateHideOriginal(ability)"
                                            id="original"/>
                                    <label for="original">Отображение
                                        оригинала</label>
                                </div>
                            </DropdownMenuItem>
                            <DropdownMenuItem>
                                <div class="flex items-center space-x-2">
                                    <Switch class="ml-5"
                                            v-model="ability.custom_description.hide_custom"
                                            @click="updateHideCustomAbility(ability)"
                                            id="custom"/>
                                    <label for="custom">Пользовательское
                                        описание</label>
                                </div>
                            </DropdownMenuItem>
                        </DropdownMenuGroup>
                    </DropdownMenuContent>
                </DropdownMenu>


                <strong>{{ ability.name }}</strong>
                <!-- Оригинальное описание -->
                <div v-if="!ability.custom_description?.hide_original">
                    {{ ability.description }}
                </div>

                <!-- Кастомное описание -->
                <div v-if="!ability.custom_description?.hide_custom">
                    <div v-if="!ability.custom_description?.isEditing">
                        {{
                            ability.custom_description.custom_description
                        }}
                    </div>
                    <textarea
                            v-else
                            v-model="ability.custom_description.custom_description"
                            rows="4"
                            class="w-full border rounded p-2"
                    ></textarea>
                    <div class="inline-block"
                         v-if="!ability.custom_description?.hide_custom">
                        <button class="btn" @click="toggleEdit(ability)">
                            <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    width="16"
                                    height="16"
                                    fill="currentColor"
                                    class="bi bi-pencil"
                                    viewBox="0 0 16 16"
                            >
                                <path
                                        d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325"
                                />
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!--    информация по уровням-->
    <Accordion type="single" collapsible v-for="(levelData, index) in
    allLevelsWithAbilities" :key="index"
               class="bg-white border-2 border-red-600 rounded-lg px-2">
        <AccordionItem value=index class="card">
            <AccordionTrigger><strong>Уровень:</strong> {{ levelData.level }}
            </AccordionTrigger>
            <AccordionContent>
                <div class="card-row">
                    <strong>Бонус мастерства:</strong>
                    +{{ levelData.proficiency_bonus }}
                </div>
                <div class="card-row">
                    <strong>Способности:</strong>
                    <ul>
                        <li v-for="ability in levelData.abilities"
                            :key="ability.name">
                            <a :href="`#ability-${ability.name.toLowerCase().replace(/\s+/g, '-')}`">
                                {{ ability.name }}
                            </a>
                        </li>
                    </ul>
                </div>
                <div class="card-row"
                     v-for="(specificColumn, colIndex) in champion_class.specific_columns"
                     :key="'specific-column-value-' + colIndex">
                    <strong>{{ specificColumn.name }}:</strong>
                    {{ specificColumn.value[index] }}
                </div>
                <div class="card-row"
                     v-if="archetype?.specific_columns?.length > 0"
                     v-for="(specificColumn, colIndex) in archetype.specific_columns"
                     :key="'specific-column-value-' + colIndex">
                    <strong>{{ specificColumn.name }}:</strong>
                    {{ specificColumn.value[index] }}
                </div>
                <div class="card-row" v-if="archetype?.spell_slots?.length > 0"
                     v-for="(i,j) in archetype.spell_slots[0].slots">
                    <strong>Ячейки заклинаний {{ j }}:</strong> {{ i[index] }}
                </div>
                <div class="card-row"
                     v-if="champion_class?.spell_slots?.length > 0"
                     v-for="(i,j) in (champion_class.spell_slots[0].slots)">
                    <strong>Ячейки заклинаний {{ j }}:</strong> {{ i[index] }}
                </div>
            </AccordionContent>
        </AccordionItem>
    </Accordion>
</template>


<script setup>
import {computed} from "vue";
import {useClassInformationStore} from "@/stores/classStore.js";
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import {Button} from '@/components/ui/button';
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger
} from '@/components/ui/accordion'
import {Switch} from "@/components/ui/switch";

const store = useClassInformationStore();
const champion_class = computed(() => store.class_info);
const archetype = computed(() => store.archetype);
const archetype_list = computed(() => store.archetype_list);

const updateHideOriginal = (ability) => {
    store.updateHideOriginal(ability)

}

const updateHideCustomAbility = (ability) => {
    store.updateHideCustomAbility(ability)
}


const toggleEdit = (ability) => {
    if (ability.custom_description.isEditing) {
        // Если уже в режиме редактирования, отправляем данные на сервер
        updateCustomDescription(ability);
        ability.custom_description.isEditing = false;
    } else {
        // Включаем режим редактирования
        ability.custom_description.isEditing = true;
    }
};


const updateCustomDescription = async (ability) => {
    try {
        // Отправляем данные на сервер
        await store.updateCustomDescriptionOnServer(ability.custom_description);
        // Выключаем режим редактирования
        ability.isEditing = false;
    } catch (error) {
        console.error("Ошибка при обновлении описания:", error);
    }
};

const allLevelsWithAbilities = computed(() => {


    const levelsMap = new Map();

    // Добавляем уровни из основного класса
    if (champion_class.value.levels) {
        champion_class.value.levels.forEach(level => {
            levelsMap.set(level.level, {
                ...level,
                abilities: [...(level.abilities || [])], // Копируем способности
            });
        });
    }

    // Добавляем уровни из архетипа
    if (archetype.value?.levels) {
        archetype.value.levels.forEach(level => {
            if (levelsMap.has(level.level)) {
                // Если уровень уже существует, добавляем способности из архетипа
                const existingLevel = levelsMap.get(level.level);
                existingLevel.abilities.push(...(level.abilities || []));
            } else {
                // Если уровня нет, создаем новую запись
                levelsMap.set(level.level, {
                    ...level,
                    abilities: [...(level.abilities || [])],
                });
            }
        });
    }

    // Преобразуем Map обратно в массив и сортируем по уровню
    return Array.from(levelsMap.values()).sort((a, b) => a.level - b.level);
});

const loadArchetypes = () => {
    store.loadArchetypes()
}
const changeArchetype = (id) => {
    store.changeArchetype(id)
}
</script>
<style>


</style>