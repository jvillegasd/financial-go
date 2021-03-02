<template>
  <div>
    <table-base>
      <template v-slot:header>
        <tr style="height: 42px;">
          <th class="w-1/2 ...">Title</th>
          <th class="w-1/4 ...">Author</th>
          <th class="w-1/4 ...">Views</th>
        </tr>
      </template>

      <template v-slot:body>
        <tr>
          <td>Intro to CSS</td>
          <td>Adam</td>
          <td>858</td>
        </tr>
        <tr class="bg-blue-200">
          <td>A Long and Winding Tour of the History of UI Frameworks and Tools and the Impact on Design</td>
          <td>Adam</td>
          <td>112</td>
        </tr>
        <tr>
          <td>Intro to JavaScript</td>
          <td>Chris</td>
          <td>1,280</td>
        </tr>
      </template>
    </table-base>
  </div>
</template>

<script>
import TableBase from './TableBase.vue';

export default {
  components: { TableBase },
  name: "lasted-transactions",
  componentes: {TableBase}
}
</script>

<style scoped>

</style>