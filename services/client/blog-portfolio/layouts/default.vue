<script>
import NavBar from '../components/NavBar.vue'
export default {
  components: { NavBar },

  async mounted() {
    try {
      await this.$recaptcha.init()
    } catch (e) {
      // console.log(e);
    }
  },
}
</script>

<template>
  <div
    class="flex flex-col min-h-screen max-w-screen mx-auto px-3 divide-y divide-gray-300"
  >
    <NavBar />
    <main class="flex-grow py-10">
      <Nuxt />
    </main>
    <footer class="text-center py-5 text-gray-500 text-sm">
      <p>© 2022–{{ $moment().format('YYYY') }} Simon Islam</p>
    </footer>
  </div>
</template>

<style lang="postcss" scoped>
.nav-link {
  @apply text-green-700 hover:text-green-800 underline;
}
</style>
