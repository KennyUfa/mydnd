<template>
    <header class="bg-white shadow-md flex justify-between items-center">

        <!-- Логотип -->
        <div class=" text-xl font-bold text-gray-800 space-x-6 items-center ">
            <router-link class="text-lg font-bold p-2"
                         to="/">DnD Лист
            </router-link>
        </div>
        <div v-if="authStore.user"
             class="items-center space-x-6">
                    <span class="text-sm text-muted-foreground">Hello {{
                            authStore.user.name
                        }}</span>

        </div>
        <div v-else class="items-center space-x-4">
            <router-link to="/">
                <Button variant="outline">Log In</Button>
            </router-link>
            <router-link to="/signup">
                <Button>Sign Up</Button>
            </router-link>
        </div>

        <Menubar>
            <MenubarMenu value="file">
                <MenubarTrigger
                        class="py-2 p-1 space-y-1 flex-col outline-none select-none font-semibold leading-none rounded text-grass11 text-xs flex items-center justify-between gap-[2px] data-[highlighted]:bg-green4 data-[state=open]:bg-green4"
                >
                         <span
                                 v-for="(line, index) in 3"
                                 :key="index"
                                 class="block w-6 h-0.5 bg-gray-700 transition duration-300 ease-in-out"
                         ></span>
                </MenubarTrigger>
                <MenubarContent
                        class="min-w-[220px] outline-none bg-white rounded-lg p-[5px] border shadow-sm [animation-duration:_400ms] [animation-timing-function:_cubic-bezier(0.16,_1,_0.3,_1)] will-change-[transform,opacity]"
                        align="start"
                        :side-offset="5"
                        :align-offset="-3"
                >
                    <MenubarItem>
                        <router-link
                                class="px-4 text-gray-700 text-2xl transition duration-300 ease-in-out whitespace-nowrap"
                                to="/"
                        >
                            Home
                        </router-link>
                    </MenubarItem>
                    <MenubarSeparator/>
                    <MenubarItem>
                        <router-link
                                class="px-4 text-gray-700 text-2xl transition duration-300 ease-in-out whitespace-nowrap"
                                to="/character"
                        >
                            Текущий персонаж
                        </router-link>
                    </MenubarItem>
                    <MenubarSeparator/>
                    <MenubarItem>
                        <router-link
                                class="px-4 text-gray-700 text-2xl transition duration-300 ease-in-out whitespace-nowrap"
                                to="/characters"
                        >
                            Лист персонажей
                        </router-link>
                    </MenubarItem>
                    <MenubarItem>
                        <Button variant="destructive" @click="logout"
                                v-if="authStore.user">
                            Logout
                        </Button>
                    </MenubarItem>
                </MenubarContent>
            </MenubarMenu>
        </Menubar>
    </header>
</template>
<script setup>
import {useAuthStore} from '@/stores/authStore';
import {useRouter} from 'vue-router';
import {Button} from '@/components/ui/button';
import {ref} from "vue";
import {
    Menubar,
    MenubarContent,
    MenubarItem,
    MenubarMenu,
    MenubarSeparator,
    MenubarTrigger
} from '@/components/ui/menubar';

const authStore = useAuthStore();
const router = useRouter();

const logout = () => {
    authStore.logout();
    router.push({path: '/'});
};

const isMenuOpen = ref(false);


function toggleMenu() {
    isMenuOpen.value = !isMenuOpen.value;
    console.log('isMenuOpen:', isMenuOpen.value);
}
</script>