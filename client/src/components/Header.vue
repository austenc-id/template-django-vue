<template>
    <header>
      <div id="row-1">
        <h1>Atlas Electronica</h1>
      </div>
      <div id="row-2">
        <h2>subtitle</h2>
        <ActionMenu />
      </div>
    </header>
</template>

<script>
import ActionMenu from "./Header/ActionMenu.vue";
export default {
  name: "Header",
  components: {
    ActionMenu,
  },
};
</script>
