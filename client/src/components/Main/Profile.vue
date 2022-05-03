<template>
    <div class="profile-header">
      <img :src="user.avatar" :alt="user.nickname">
      <div class="user-identification">
        <h3>{{ user.name }}</h3>
        <li>{{user.contact.email}}</li>
        <li>joined: {{user.joined}}</li>
      </div>
    <span>admin</span>
  </div>
    <p class="user-bio">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae tempore non at. Exercitationem dignissimos odio quae earum obcaecati quidem laborum facere qui delectus ad!
    </p>
</template>

<script>
export default {
  name: "Profile",
  data() {
    return {
      url: this.$store.state.url,
      user: this.$store.state.active.user,
      color: false,
    };
  },
  methods: {

  },
};
</script>
