import axios from "axios";
import tokenService from "./token.service";
import authService from "./auth.service";
import router from "../router";
const instance = axios.create({
  baseURL: "http://admin.hello.world/api/v1/admin",
  headers: {
    "Content-Type": "applications/json",
  },
});

instance.interceptors.request.use(
  (config) => {
    const access_token = tokenService.getAccessToken();
    if (access_token !== null) {
      config.headers["Authorization"] = "Bearer " + access_token;
    }
    config.headers["Content-Type"] = "application/json";
    return config;
  },
  (error) => {
    console.log(error);
  }
);

instance.interceptors.response.use(
  (config) => {
    return config;
  },
  (err) => {
    if (err.response.status == 401) {
      authService.logout();
      router.push({ name: "LoginPage" });
    }
    return err;
  }
);

export default instance;
