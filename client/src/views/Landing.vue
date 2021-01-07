<template>
  <div id="landing">
    <div id="navbar" class="w-full Flex flex-row right">
      <button id="btn-about">About</button>
      <button id="btn-signin">Sign in</button>
    </div>
    <div id="text" class="Flex flex-col justify-center h-full">
      <h1 class="font-regular text-6xl">Financial Go</h1>
      <p id="content">The easiest way to manage your budget.</p>
      <button id="btn-signup">Start saving</button>
    </div>
    <div id="image">
      <img src="../assets/logo.svg">
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Landing'
  }
</script>