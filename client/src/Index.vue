<template>
  <Header />
  <Nav />
  <Main />
  <Footer />
</template>

<script>
import Header from "./components/Header";
import Nav from "./components/Nav";
import Main from "./components/Main";
import Footer from "./components/Footer";

export default {
  name: "Index",
  components: {
    Header,
    Nav,
    Main,
    Footer,
  },
  data() {
    return {
      active: this.$store.state.active,
    };
  },
};
</script>

<style>
@import url("./style/style.css");
</style>
