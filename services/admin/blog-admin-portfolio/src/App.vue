<script setup>
import NavBar from "./components/NavBar.vue";
</script>
<template>
  <div class="h-screen bg-cream-white">
    <NavBar />
    <router-view />
  </div>
</template>
<style lang="scss">
.bg-cream-white {
  background: $primary;
}
.bg-secondary {
  background: $secondary;
}
</style>
