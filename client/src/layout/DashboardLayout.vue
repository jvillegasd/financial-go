<template>
  <div>
    <nav id="navbar" class="fixed w-full flex items-center justify-end text-center">
      <p class="text-3xl font-bold mr-8">Hello, Admin</p>
      <span class="bg-blue-80 text-3xl font-bold text-white flex items-center justify-center mr-24" id="letter_circle">A</span>
    </nav>

    <aside id="sidebar" class="fixed h-full flex justify-top text-center">
      <div id="title" class="flex justify-center mt-5">
        <img id="image" src="../assets/logo.svg" class="">
        <p class="font-bold text-3xl ml-3 mt-2">Financial Go</p>
      </div>
    </aside>
  </div>
</template>

<script>
export default {
  name: "dashboard_layout",
  beforeCreate: function() {
    document.body.className = "dashboard";
  }
}
</script>
<style scoped>
  #navbar {
    background-color: white;
    height: 84px;
    border-bottom-right-radius: 50px;
    box-shadow: 0px 3px 4px 0 rgba(0, 0, 0, 0.03);
  }
  #letter_circle {
    height: 50px;
    width: 50px;
    border-radius: 50%;
  }
  #sidebar {
    background-color: white;
    width: 312px;
    box-shadow: 5px 4px 4px 0 rgba(0, 0, 0, 0.07);
  }
  #image {
    width: 50.03px;
    height: 39.24px;
  }
  #title {
    height: 56px;
    width: 312px;
  }
</style>