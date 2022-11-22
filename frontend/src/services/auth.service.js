import api from "./api";
import TokenService from "./token.service";

class AuthService {
  login( username, password ) {
    return api
      .post("api/token/", {
        username,
        password
      })
      .then((response) => {
        if (response.data.access) {
          TokenService.setUser(response.data);
        }
        return response.data;
      });
  }

  logout() {
    TokenService.removeUser();
  }

  register({ username, email, password }) {
    return api.post("/auth/signup", {
      username,
      email,
      password
    });
  }
}

export default new AuthService();
