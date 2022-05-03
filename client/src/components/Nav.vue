<template>
  <nav>
    <homeIcon @click="renderSection('home')" />
    <profileIcon @click="renderSection('profile')" />
    <settingsIcon @click="renderSection('settings')" />
  </nav>
</template>

<script>
import homeIcon from "./Main/icons/home";
import profileIcon from "./Main/icons/profile";
import settingsIcon from "./Main/icons/settings";
export default {
  name: "Nav",
  components: {
    homeIcon,
    profileIcon,
    settingsIcon,
  },
  methods: {
    renderSection(section) {
      this.$store.commit("toggleElement", {
        group: "section",
        element: section,
      });
    },
  },
};
</script>
