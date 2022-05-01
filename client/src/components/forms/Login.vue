<template>
<form action="">
    <h3>Login</h3>
    <label for="username">username
        <input type="text" name="username" id="username">
    </label>
    <label for="password">password
        <input type="password" name="password" id="password">
    </label>
    <button>login</button>
</form>
</template>

<script>
    export default{
        name: 'LoginForm'
    }
</script>