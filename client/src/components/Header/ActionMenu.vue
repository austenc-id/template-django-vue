<template>
  <menu>
    <!-- <li @click="renderForm('login')">login</li>
    <li @click="renderForm('register')">register</li> -->
    <Auth0/>
  </menu>
</template>

<script>
  import Auth0 from './auth0'
export default {
  name: "ActionMenu",
  components: {
    Auth0
  },
  methods: {
    async renderForm(form) {
      console.log(`rendering ${form}`)
      await fetch(`${this.$store.state.url}/user/login`)
        .then((response) => response.json())
        .then((response) => console.log(response))
      this.$store.commit("toggleElement", { group: "form", element: form });
    },
  },
};
</script>
