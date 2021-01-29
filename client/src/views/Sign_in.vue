<template>
  <div class="flex flex-col h-screen justify-center items-center">

      <div id="title" class="mb-10">
        <img id="image" src="../assets/logo.svg" class="block mx-auto">
        <a id="landing_redirect" class="text-5xl font-regular text-white text-center">Financial Go</a>
      </div>
  
      <div id="card" class="mb-20 text-center xs:w-full sm:w-full md:w-c-507">
        <h1 class="text-4xl font-regular">Login</h1>

        <Textbox
          label="Email"
          :width=360
          :labelFontSize=20
          :inputFontSize=25
          class="mx-auto mb-14">
        </Textbox>

        <Textbox
          label="Password"
          :width=360
          :lineWidth=245
          :labelFontSize=20
          :inputFontSize=25
          :isPassword=true
          class="mx-auto">
        </Textbox>
      </div>
  </div>

</template>

<script>
  import Textbox from '../components/textbox/Texbox';

  export default {
    name: 'Sign-in',
    components: {
      Textbox
    },
    beforeCreate: function() {
      document.body.className = 'sign_in';
    }
  }
</script>

<style scoped>
  #card {
    background-color: white;
    height: 419px;
    border-radius: 53px;
    margin-top: 0px;
  }
  
  #card > h1 {
    padding: 44px;
  }
  
  #image {
    width: 119.03px;
    height: 93.36px;
  }



  #landing_redirect {
    display: block;
    width: 300px;
  }
</style>