<template>
  <div id="landing">

    <div id="navbar" class="w-full Flex flex-row">
      <button id="btn-about" class="absolute right-64">About</button>
      <button id="btn-signin" class="absolute right-14">Sign in</button>
    </div>

    <div class="Flex flex-row">
      <div id="text" class="absolute inset-y-96 left-32">
        <h1 class="font-regular text-6xl">Financial Go</h1>
        <p id="content">The easiest way to manage your budget.</p>
        <button id="btn-signup">Start saving</button>
      </div>

      <div id="image-div" class="absolute inset-y-28 right-0">
        <img id="image" src="../assets/logo.svg">
      </div>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'Landing'
  }
</script>