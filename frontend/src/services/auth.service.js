import api from "./api";
import TokenService from "./token.service";

class AuthService {
  async login(username, password) {
    const response = await api.post("authapp/login/", {
      username,
      password,
    });
    if (response.data.access) {
      TokenService.setUser(response.data);
    }
    return response.data;
  }

  logout() {
    TokenService.removeUser();
  }

  async register({ username, email, password }) {
    return api.post("/auth/signup", {
      username,
      email,
      password,
    });
  }
}

export default new AuthService();
