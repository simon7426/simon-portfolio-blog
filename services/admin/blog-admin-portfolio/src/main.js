import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { VueReCaptcha } from "vue-recaptcha-v3";
import "./assets/main.css";
import { createPinia } from "pinia";

const app = createApp(App);
const store = createPinia();

app.use(store);
app.use(router);
app.use(VueReCaptcha, {
  siteKey: "6LfMGXQiAAAAAEcbzOTl9G9m21hGPUXjloZ9sUzS",
});

app.mount("#app");
