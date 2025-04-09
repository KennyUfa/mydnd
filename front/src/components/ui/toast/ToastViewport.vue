<script setup>
import { cn } from '@/lib/utils';
import { ToastViewport } from 'reka-ui';
import { computed } from 'vue';

const props = defineProps({
  hotkey: { type: Array, required: false },
  label: { type: [String, Function], required: false },
  asChild: { type: Boolean, required: false },
  as: { type: null, required: false },
  class: { type: null, required: false },
});

const delegatedProps = computed(() => {
  const { class: _, ...delegated } = props;

  return delegated;
});
</script>

<template>
  <ToastViewport
    v-bind="delegatedProps"
    :class="
      cn(
        'fixed bottom-0 right-0 z-[100] flex max-h-screen flex-col-reverse p-4 sm:top-auto sm:flex-col max-w-90',
        props.class,
      )
    "
  />
</template>
