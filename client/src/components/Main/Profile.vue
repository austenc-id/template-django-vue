<template>
  <main>
    <div v-if="user">
      <li>{{ user.name.first }}'s profile</li>
      <li>username: {{ user.username }}</li>
      <li>role: {{ user.role }}</li>
      <li>joined: {{ user.dates.joined }}</li>
      <li>last login: {{ user.dates.last_login }}</li>
      <li>email: {{ user.contact.email }}</li>
      <button v-if="user.role === 'admin'" @click="renderUserList()">
        view user list
      </button>
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
    async renderUserList() {
      await fetch(`${this.url}/users`)
        .then((response) => response.json())
        .then((data) => console.log(data));
    },
  },
};
</script>
