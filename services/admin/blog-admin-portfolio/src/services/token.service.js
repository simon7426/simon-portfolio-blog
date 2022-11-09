import { useAuthStore } from "../store/useAuthStore";

class TokenService {
  setUser(access_token) {
    const store = useAuthStore();
    const user = {
      access_token: access_token,
    };
    localStorage.setItem("user", JSON.stringify(user));
    store.setToken(access_token);
  }
  getUser() {
    return JSON.parse(localStorage.getItem("user"));
  }
  getAccessToken() {
    const { access_token } = useAuthStore();
    return access_token;
  }
  getLocalAccessToken() {
    return this.getUser()?.access_token;
  }
  removeUser() {
    const store = useAuthStore();
    store.removeToken();
    localStorage.removeItem("user");
  }
}

export default new TokenService();
