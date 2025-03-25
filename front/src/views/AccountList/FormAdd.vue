<template>
    <div class="border-2 border-black rounded-md p-3">
        <Input
                type="text"
                v-model="name_champion"
                placeholder="Имя персонажа"
                class="border-4 border-black h-300 mb-3"
        />
        <div class="flex flex-row gap-2">
            <div class="mb-4 flex-1">
                <DropdownMenu>
                    <Button variant="destructive"
                            class="w-full flex justify-center"
                            as-child>
                        <DropdownMenuTrigger
                                class="font-bold italic leading-[0.8] ">
                            {{ champion_class.name || "Выбери класс" }}
                        </DropdownMenuTrigger>
                    </Button>
                    <DropdownMenuContent>
                        <DropdownMenuItem v-if="!class_list">Загрузка...
                        </DropdownMenuItem>
                        <DropdownMenuItem
                                v-for="class_info in class_list"
                                :key="class_info.id"
                                @click="change_class(class_info)"
                        >
                            {{ class_info.name }}
                        </DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
            </div>

            <!-- Выбор расы -->
            <div class="mb-4  flex-1">
                <DropdownMenu>
                    <Button variant="destructive"
                            class="w-full flex justify-center"
                            as-child>
                        <DropdownMenuTrigger>
                            {{ race.name || "Выбери расу" }}
                        </DropdownMenuTrigger>
                    </Button>
                    <DropdownMenuContent>
                        <DropdownMenuItem v-if="!race_list">Загрузка...
                        </DropdownMenuItem>
                        <DropdownMenuItem
                                v-for="race_info in race_list"
                                :key="race_info.id"
                                @click="change_race(race_info)"
                        >
                            {{ race_info.name }}
                        </DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
            </div>

            <!-- Выбор уровня -->
            <div class="mb-4 flex-1">
                <DropdownMenu>
                    <Button variant="destructive"
                            class="w-full flex justify-center"
                            as-child>
                        <DropdownMenuTrigger>
                            Уровень - {{ level }}
                        </DropdownMenuTrigger>
                    </Button>
                    <DropdownMenuContent>
                        <DropdownMenuItem
                                v-for="n in 20"
                                :key="n"
                                @click="change_level(n)"
                        >
                            {{ n }}
                        </DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
            </div>
        </div>

        <!-- Кнопка создания персонажа -->
        <Button variant="default" class="w-full" @click="createChampion">
            Создать нового чемпиона
        </Button>
    </div>

</template>

<script setup>
import {computed, onMounted, ref} from 'vue';
import {useCreateCharacter} from '@/stores/create.character.js';
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import {Input} from '@/components/ui/input';
import {Button} from '@/components/ui/button';

// Инициализация хранилища
const create_character = useCreateCharacter();

// Реактивные переменные
const name_champion = ref('');
const champion_class = ref({});
const race = ref({});
const level = ref(1);

// Вычисляемые свойства
const class_list = computed(() => create_character.class_list);
const race_list = computed(() => create_character.race_list);

// Методы для изменения состояния
const change_class = (selected) => {
    champion_class.value = selected;
};

const change_race = (selected) => {
    race.value = selected;
};

const change_level = (selected) => {
    level.value = selected;
};

// Метод для создания персонажа
const createChampion = async () => {
    const data = {
        name_champion: name_champion.value,
        champion_class: champion_class.value,
        race: race.value,
        level: level.value,
    };
    try {
        await create_character.createCharacter(data);
        // После успешного создания можно очистить форму или перенаправить пользователя
    } catch (error) {
        console.error('Ошибка создания:', error);
    }
};

// Загрузка данных при монтировании
onMounted(() => {
    create_character.fetchClassList();
    create_character.fetchRaceList();
});
</script>

<style scoped></style>
