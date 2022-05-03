<template>
  <main id="main">
    <Home v-if="active.home"/>
    <Profile v-if="active.profile"/>
    <Settings v-if="active.settings"/>
  </main>
</template>

<script>
import Home from './Main/Home.vue'
import Profile from './Main/Profile.vue'
import Settings from './Main/Settings.vue'

export default {
  name: "Main",
  components: {
    Home,
    Profile,
    Settings,
  },
  updated(){
  },
  data() {
    return{
      active: this.$store.state.active.section
    }
  },
};
</script>
