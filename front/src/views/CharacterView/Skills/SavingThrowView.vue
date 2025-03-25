<template>
    <div
            class="grid grid-cols-3 gap-1 bg-white text-slate-900 border-2 border-red-600 rounded-lg p-4">
        <protect-list></protect-list>
        <protect-state
                @callRandomWindow="handleCallRandomWindow"
                skill-name="СИЛ"
                stat="strength"
                skill-value="protect_state_strength"
        ></protect-state>
        <protect-state
                @callRandomWindow="handleCallRandomWindow"
                skill-name="ЛВК"
                stat="dexterity"
                skill-value="protect_state_dexterity"
        ></protect-state>
        <protect-state
                @callRandomWindow="handleCallRandomWindow"
                skill-name="ТСЛ"
                stat="constitution"
                skill-value="protect_state_constitution"
        ></protect-state>
        <protect-state
                @callRandomWindow="handleCallRandomWindow"
                skill-name="ИНТ"
                stat="intelligence"
                skill-value="protect_state_intelligence"
        ></protect-state>
        <protect-state
                @callRandomWindow="handleCallRandomWindow"
                skill-name="МДР"
                stat="wisdom"
                skill-value="protect_state_wisdom"
        ></protect-state>
        <protect-state
                @callRandomWindow="handleCallRandomWindow"
                skill-name="ХАР"
                stat="charisma"
                skill-value="protect_state_charisma"
        ></protect-state>
    </div>
</template>

<script setup>
import ProtectState from "@/views/CharacterView/Skills/ui/ProtectState.vue";
import {useCharacterStore} from "@/stores/characterStore";
import ProtectList
    from "@/views/CharacterView/Skills/ProtectState/ProtectList.vue";


const emit = defineEmits(["callRandomWindow"]);
const champion = useCharacterStore();



const handleCallRandomWindow = (data) => {
    emit("callRandomWindow", data);
};
</script>

<style scoped>

</style>
