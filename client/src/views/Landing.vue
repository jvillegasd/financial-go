<template>
  <div id="landing">

    <div id="navbar" class="w-full Flex flex-row">
      <BorderlessButton
        title="About"
        :width=174
        :height=44.45
        :fontSize=19
        :marginTop=32
        class="absolute right-64"
      ></BorderlessButton>
      <BorderedButton
        title="Sign in"
        :width=174
        :height=44.45
        :fontSize=19
        :marginTop=32
        class="absolute right-14"
      ></BorderedButton>
    </div>

    <div class="Flex flex-row relative ">
      <div id="text" class="absolute inset-y-96 left-32">
        <h1 class="font-regular text-6xl">Financial Go</h1>
        <p id="content">The easiest way to manage your budget.</p>
        <BlueButton
          title="Start saving"
          :width=233
          :height=44.45
          :fontSize=19
          :marginTop=30
        ></BlueButton>
      </div>

      <div id="image-div" class="absolute inset-y-28 right-0">
        <img id="image" src="../assets/logo.svg">
      </div>
    </div>

  </div>
</template>

<script>
  import BlueButton from '../components/Blue_btn';
  import BorderedButton from '../components/Bordered_btn';
  import BorderlessButton from '../components/Borderless_btn';

  export default {
    name: 'Landing',
    components: {
      BlueButton,
      BorderedButton,
      BorderlessButton
    }
  }
</script>