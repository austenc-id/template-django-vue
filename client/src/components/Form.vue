<template>
  <LoginForm v-if="active.login"></LoginForm>
  <RegisterForm v-if="active.register"></RegisterForm>
</template>
<script>
import LoginForm from "./forms/Login.vue";
import RegisterForm from "./forms/Register.vue";

export default {
  name: "Form",
  components: {
    LoginForm,
    RegisterForm,
  },
  data() {
    return {
      active: this.$store.state.active.form,
    };
  },
};
</script>
