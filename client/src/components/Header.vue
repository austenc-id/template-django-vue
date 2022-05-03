<template>
    <header>
      <div id="row-1">
        <h1>Atlas Electronica</h1>
      </div>
      <div id="row-2">
        <h2>subtitle</h2>
        <Auth0/>
      </div>
    </header>
</template>

<script>
import Auth0 from "./auth0";
export default {
  name: "Header",
  components: {
    Auth0,
  },
};
</script>
