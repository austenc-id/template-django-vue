<template>
    <li v-if="!authenticated" @click="login()">Log In</li>
    <svg v-if="authenticated" @click="renderSection('profile')" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
      <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
      <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
    </svg>
    <li v-if="authenticated" @click="logout()">Log Out</li>
</template>

<script>
import AuthService from "../../auth/AuthService";
import axios from "axios";

const API_URL = "https://atlaspatrons.us.auth0.com";

const auth = new AuthService();

export default {
  name: "auth0",
  data() {
    auth.handleAuthentication();
    this.authenticated = false;

    auth.authNotifier.on("authChange", (authState) => {
      this.authenticated = authState.authenticated;
    });
    return {
      authenticated: false,
      message: "",
    };
  },
  updated(){
    this.getUserInfo()
  },
  methods: {
    login() {
      auth.login();
    },
    logout() {
      auth.logout();
    },
    getUserInfo() {
      const url = `${API_URL}/userinfo`;
      return axios
        .get(url, {
          headers: { Authorization: `Bearer ${auth.getAuthToken()}` },
        })
        .then((response) => {
          console.log(response.data);
          this.$store.state.active.user = response.data
          this.message = response.data || "";
        });
    },
    renderSection(section){
        console.log(`rendering ${section}`)
        console.log(this.$store.state.active.user)
        this.$store.commit("toggleElement", { group: "section", element: section });
      }
  },
};
</script>
