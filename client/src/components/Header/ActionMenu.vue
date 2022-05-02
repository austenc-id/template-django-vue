<template>
  <menu>
    <li @click="renderForm('login')">login</li>
    <li @click="renderForm('register')">register</li>
  </menu>
</template>

<script>
export default {
  name: "ActionMenu",
  components: {},
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
