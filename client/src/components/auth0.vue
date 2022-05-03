<template>
  <menu>
    <li v-if="!authenticated" @click="login()">Log In/Register</li>
    <li v-if="authenticated" @click="logout()">Log Out</li>
  </menu>
</template>

<script>
import AuthService from "../auth";
import axios from "axios";
const API_URL = "https://atlaspatrons.us.auth0.com";

const auth = new AuthService();

export default {
  name: "auth0",
  components: {},
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
  updated() {
    this.getUserInfo();
  },
  methods: {
    login() {
      auth.login();
    },
    logout() {
      auth.logout();
      this.$store.state.active.user = false
      window.location.reload();

    },
    getUserInfo() {
      if (this.authenticated) {
        let heading = "https://atlaselectronica";
        let data = auth.getUserProfile();
        let profile = {
          avatar: data.picture,
          name: data.name,
          joined: this.dateFromString(data[`${heading}/joined`]),
          color: data[`${heading}/color`],
          contact: {
            email: data[`${heading}/email`],
            phone: data[`${heading}/phone`],
          },
          login: {
            country: data[`${heading}/country`],
            timezone: data[`${heading}/timezone`],
          },
        };
        this.$store.state.active.user = profile;
        this.$store.commit("toggleUserColor");
      }
    },
    dateFromString(str) {
      let date = new Date(str);

      return date.toDateString();
    },
  },
};
</script>
