export default {
  setUser(user) {
    localStorage.setItem('user', JSON.stringify(user));
  },

  removeUser() {
    localStorage.removeItem('user');
  },

  getToken() {
    const user = JSON.parse(localStorage.getItem('user'));
    return user?.accessToken || null;
  },
};