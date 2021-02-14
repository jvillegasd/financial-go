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
      <a href="/sign_in">
        <BorderedButton
          title="Sign in"
          :width=174
          :height=44.45
          :fontSize=19
          :marginTop=32
          class="absolute right-14"
        ></BorderedButton>
      </a>
    </div>

    <div class="Flex flex-row relative ">
      <div id="text" class="absolute inset-y-96 left-32">
        <h1 class="font-regular text-6xl">Financial Go</h1>
        <p id="content" class="font-regular text-4xl">The easiest way to manage your budget.</p>
        <a href="/sign_up">
          <BlueButton
            title="Start saving"
            :width=233
            :height=44.45
            :fontSize=19
            :marginTop=30
          ></BlueButton>
        </a>
      </div>

      <div id="image-div" class="absolute inset-y-28 right-0">
        <img id="image" src="../assets/logo.svg">
      </div>
    </div>

  </div>
</template>

<script>
  import BlueButton from '../components/Buttons/Blue_btn';
  import BorderedButton from '../components/Buttons/Bordered_btn';
  import BorderlessButton from '../components/Buttons/Borderless_btn';

  export default {
    name: 'Landing',
    components: {
      BlueButton,
      BorderedButton,
      BorderlessButton
    }
  }
</script>

<style scoped>
  #content {
    margin-top: 32px;
  }

  #text {
    width: 585px;
    height: 258.45px;
    z-index: 1;
  }

  #image-div, #image {
    height: 829px;
    width: 977px;
  }
</style>