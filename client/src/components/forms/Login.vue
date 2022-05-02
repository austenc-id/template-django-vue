<template>
  <form action="" onsubmit="event.preventDefault()" id="login-form">
    <h3>Login</h3>
    <label for="username"
      >username
      <input type="text" name="username" id="username" />
    </label>
    <label for="password"
      >password
      <input type="password" name="password" id="password" />
    </label>
    <button @click="submitLogin()">login</button>
  </form>
</template>

<script>
export default {
  name: "LoginForm",
  data() {
    return {
      url: this.$store.state.url,
    };
  },
  methods: {
    async submitLogin() {
      const data = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value,
      };
      await fetch(`${this.url}/user/login/`, {
        method: "POST",
        headers: {
          "X-csrftoken": this.$store.state.csrftoken,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
        .then((response) => response.json())
        .then((response) => {
          alert(response.message);
          return response;
        })
        .then((response) => {
          this.$store.commit("setActiveUser", { user: response.user });
          if (response.status === 202) {
            this.$store.commit("toggleElement", {
              group: "form",
              element: "login",
            });
            this.$store.commit("toggleElement", {
              group: "section",
              element: "profile",
            });
          }
        });
    },
  },
};
</script>
