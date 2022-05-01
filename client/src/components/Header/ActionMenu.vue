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
    renderForm(form) {
      console.log(`rendering ${form}`)

      this.$store.commit("toggleElement", { group: "form", element: form });
    },
  },
};
</script>
