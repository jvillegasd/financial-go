<template>
  <div class="flex h-screen justify-center items-center">
    
    <div class="space-y-2">

      <div id="title" class="block text-center -mt-20">
        <img id="image" src="../assets/logo.svg" class="">
        <a id="landing_redirect" class="text-5xl font-regular text-white text-center">Financial Go</a>
      </div>
  
      <div id="card" class="block text-center sm:w-full">
        <h1 class="text-4xl font-regular">Login</h1>
  
      </div>

    </div>
  
  </div>
</template>

<script>
  export default {
    name: 'Sign-in',
    beforeCreate: function() {
      document.body.className = 'sign_in';
    }
  }
</script>

<style scoped>
  #card {
    background-color: white;
    width: 500px;
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