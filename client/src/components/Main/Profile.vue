<template>
  <main>
    <div>
      <img :src="user.picture" :alt="user.nickname">
      <li>{{ user.nickname }}'s profile</li>
      <li>email: {{ user.name }}</li>
    </div>
  </main>
</template>

<script>
export default {
  name: "Profile",
  data() {
    return {
      url: this.$store.state.url,
      user: this.$store.state.active.user,
    };
  },
  methods: {
  },
};
</script>
