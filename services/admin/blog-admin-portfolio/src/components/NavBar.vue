<script setup>
import { ref, computed } from "vue";
import authService from "../services/auth.service";
import { useRouter } from "vue-router";

import { useAuthStore } from "../store/useAuthStore";
import tokenService from "../services/token.service";

const isHidden = ref(true);

async function toggleNav() {
  isHidden.value = !isHidden.value;
}

const router = useRouter();
const store = useAuthStore();

const isLoggedIn = computed(() => {
  if (store.isLoggedIn === false && tokenService.getLocalAccessToken()) {
    store.setToken(tokenService.getLocalAccessToken());
  }
  return store.isLoggedIn;
});

function logoutClick() {
  authService.logout();
  router.push({ name: "LoginPage" });
}
</script>

<template>
  <nav class="nav-background border-gray-200 px-2 sm:px-4 py-1">
    <div class="container flex flex-wrap justify-between items-center mx-auto">
      <router-link to="/">
        <span
          class="self-center text-xl nav-text font-semibold whitespace-nowrap dark:text-white"
        >
          Blog Admin Panel
        </span>
      </router-link>
      <button
        data-collapse-toggle="navbar-default"
        type="button"
        @click="toggleNav"
        class="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
        aria-controls="navbar-default"
        aria-expanded="false"
      >
        <span class="sr-only">Open main menu</span>
        <svg
          class="w-6 h-6"
          aria-hidden="true"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
            clip-rule="evenodd"
          ></path>
        </svg>
      </button>
      <div
        class="w-full md:block md:w-auto"
        :class="{ hidden: isHidden }"
        id="navbar-default"
      >
        <ul
          class="flex flex-col p-2 mt-4 rounded-lg border border-gray-100 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 dark:border-gray-700"
        >
          <li v-if="!isLoggedIn">
            <router-link to="/login">
              <div
                class="py-2 pr-4 pl-3 nav-text rounded grey-button-bg"
                aria-current="page"
              >
                Login
              </div>
            </router-link>
          </li>
          <li v-if="isLoggedIn">
            <div class="flex flex-col md:flex-row">
              <router-link to="/">
                <div
                  class="py-2 pr-4 pl-3 nav-text rounded grey-button-bg"
                  aria-current="page"
                >
                  Dashboard
                </div>
              </router-link>
              <router-link to="/blogs">
                <div
                  class="py-2 pr-4 pl-3 nav-text rounded grey-button-bg"
                  aria-current="page"
                >
                  Blogs
                </div>
              </router-link>
              <router-link to="/login">
                <div
                  @click="logoutClick"
                  class="py-2 pr-4 pl-3 nav-text rounded grey-button-bg"
                >
                  Logout
                </div>
              </router-link>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<style scoped lang="scss">
.grey-button-bg:hover {
  background-color: $primary;
  color: $navhover;
}
.nav-background {
  background-color: $secondary;
}
.nav-text {
  color: $nav;
}
</style>
