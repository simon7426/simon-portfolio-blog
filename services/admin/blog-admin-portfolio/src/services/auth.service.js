import api from "./api";
import tokenService from "./token.service";

class AuthService {
  async login({ username, password, token }) {
    return api
      .post(
        "/auth/login",
        {
          username,
          password,
        },
        {
          headers: {
            "X-Recaptcha-Key": token,
          },
        }
      )
      .then((response) => {
        if (response.data?.access_token) {
          tokenService.setUser(response.data.access_token);
        }
        return response.data;
      });
  }
  isLoggedIn() {
    return tokenService.getUser() !== null;
  }
  logout() {
    tokenService.removeUser();
  }
}

export default new AuthService();
