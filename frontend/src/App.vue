<template>
  <div class="container-fluid">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },}

    // data() {
    //   return {
    //     data_champion: {
    //       champion_class: 'default',
    //       re_history: 'default',
    //       race: 'default',
    //       world_outlook: 'default',
    //       account: 'default',
    //       experience: 'default',
    //       lvl: 1,
    //     },
    //   }
    // },

    /*  methods: {
        async getInfo() {
          const token = localStorage.getItem('Bearer');

          const res = await fetch('http://127.0.0.1:8000/dnd/character/', {
            method: 'GET',
            headers: {
              'Content-type': 'application/json',
              'Authorization': `Bearer ${token}`, // notice the Bearer before your token
            }
          }).catch(err => {
            return console.log(err);
          });
          if (res.status === 401) {
            await this.refreshToken()
          } else if (res.status === 200) {
            this.data_champion = await res.json()
          }
          return false
        },


        async refreshToken() {
          const res = await fetch("http://127.0.0.1:8000/api/token/refresh/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body:
                JSON.stringify({
                  'refresh': localStorage.getItem('refresh'),
                }),
          }).catch(err => {
            localStorage.clear();
            console.log(err);
            return false;
          });
          if (res.status === 200) {
            let response;
            response = res.json()
                .then(response => localStorage.setItem('Bearer', response.access));
            return true
          }
        },
      },*/
  }
</script>
