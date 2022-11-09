<script setup>
import GridLoader from "vue-spinner/src/GridLoader.vue";
const loadercolor = "#40739e";
</script>

<template>
  <div class="flex flex-col items-center justify-center px-6 py-12 h-4/5">
    <GridLoader :color="loadercolor" />
  </div>
</template>
