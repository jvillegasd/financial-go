<template>
  <div>

    <table class="table-base rounded-t-3xl bg-grey-table">
      <thead class="table-header">
        <slot name="header"></slot>
      </thead>

      <tbody>
        <slot name="body"></slot>
      </tbody>
    </table>

  </div>
</template>

<script>
export default {
  name: "table-base"
}
</script>

<style scoped>
  .table-base{
    border-collapse: collapse;
    overflow: hidden;
  }
  .table-header {
    background: rgba(196, 196, 196, 0.25);
  }
</style>