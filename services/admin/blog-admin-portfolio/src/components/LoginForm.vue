<script setup>
import { ref } from "vue";
import SyncLoader from "vue-spinner/src/SyncLoader.vue";
import authService from "../services/auth.service";
import { useRouter } from "vue-router";
import { useReCaptcha } from "vue-recaptcha-v3";

const loadercolor = ref("#dcdde1");
const isLoading = ref(false);
const username = ref("");
const password = ref("");

const router = useRouter();
const { executeRecaptcha, recaptchaLoaded } = useReCaptcha();

async function handleSubmit() {
  const inp_username = username.value.trim();
  const inp_password = password.value.trim();
  if (inp_password.length !== 0 && inp_username.length !== 0) {
    isLoading.value = true;
    await recaptchaLoaded();
    const token = await executeRecaptcha("login");
    const user = {
      username: inp_username,
      password: inp_password,
      token: token,
    };
    await authService
      .login(user)
      .then(() => {
        router.push({ name: "DashboardPage" });
      })
      .catch(() => {
        isLoading.value = false;
        username.value = "";
        password.value = "";
      });
  } else {
    username.value = "";
    password.value = "";
  }
}
</script>

<template>
  <div class="container flex flex-wrap mx-auto">
    <div class="container grid px-6 py-12 h-full place-items-center">
      <div
        class="flex justify-center items-center flex-wrap h-full g-6 text-gray-800"
      >
        <div class="md:w-8/12 lg:w-6/12 mb-12 md:mb-0">
          <img
            src="../assets/img/programmer.svg"
            class="w-full"
            alt="Phone image"
          />
        </div>
        <div class="p-20 md:w-8/12 lg:w-5/12 lg:ml-20">
          <form>
            <!-- Email input -->
            <div class="mb-6">
              <input
                v-model="username"
                type="text"
                class="form-control block w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                placeholder="Username"
              />
            </div>

            <!-- Password input -->
            <div class="mb-6">
              <input
                v-model="password"
                type="password"
                class="form-control block w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                placeholder="Password"
              />
            </div>

            <!-- Submit button -->
            <button
              @click="handleSubmit"
              type="button"
              class="inline-block px-7 py-3 button-background button-text font-medium text-sm leading-snug uppercase rounded shadow-md grey-button-bg transition duration-150 ease-in-out w-full"
              data-mdb-ripple="true"
              data-mdb-ripple-color="light"
            >
              <SyncLoader :loading="isLoading" :color="loadercolor" />
              <p v-if="!isLoading">Sign in</p>
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">
.button-background {
  background-color: $secondary;
}
.button-text {
  color: $nav;
}
.grey-button-bg:hover {
  background-color: $secondarylight;
}
</style>
