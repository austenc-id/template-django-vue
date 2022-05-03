<template>
  <button @click="toggleUserColor()">use favorite color</button>
</template>

<script>
export default {
  name: "Settings",
  methods: {
    toggleUserColor(){
      this.$store.commit('toggleUserColor')
    }
  }
};
</script>
