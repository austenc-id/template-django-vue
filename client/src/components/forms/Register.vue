<template>
  <form action="">
    <h3>Register</h3>
    <label for="username"
      >username
      <input type="text" name="username" id="username" />
    </label>
    <label for="password"
      >password
      <input type="password" name="password" id="password" />
    </label>
    <label for="confirm-password"
    >confirm password
    <input type="password" name="confirm-password" id="confirm-password" />
  </label>
    <button>register</button>
  </form>
</template>

<script>
export default {
  name: "RegisterForm",
};
</script>
