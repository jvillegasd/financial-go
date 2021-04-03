<template>
  <div class="table-modal rounded-2xl bg-white shadow-md flex items-center">
    <ul class="pl-4 pt-1 space-y-2">
      <li>
        <button class="flex justify-start table-modal-btn">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M9 18C13.9706 18 18 13.9706 18 9C18 4.02944 13.9706 0 9 0C4.02944 0 0 4.02944 0 9C0 13.9706 4.02944 18 9 18ZM9 16.4938C4.8613 16.4938 1.50622 13.1387 1.50622 9C1.50622 4.8613 4.8613 1.50622 9 1.50622C13.1387 1.50622 16.4938 4.8613 16.4938 9C16.4938 13.1387 13.1387 16.4938 9 16.4938ZM11.601 12.87C11.952 13.221 12.519 13.221 12.87 12.87C13.212 12.519 13.212 11.943 12.87 11.601L10.269 9.00005L12.87 6.39905C13.221 6.04805 13.221 5.48105 12.87 5.13005C12.519 4.77905 11.952 4.77905 11.601 5.13005L9 7.73105L6.399 5.13005C6.048 4.77905 5.481 4.77905 5.13 5.13005C4.96147 5.2982 4.86676 5.52648 4.86676 5.76455C4.86676 6.00261 4.96147 6.2309 5.13 6.39905L7.731 9.00005L5.13 11.601C4.96147 11.7692 4.86676 11.9975 4.86676 12.2355C4.86676 12.4736 4.96147 12.7019 5.13 12.87C5.481 13.221 6.048 13.221 6.399 12.87L9 10.269L11.601 12.87Z" fill="#FF0000" fill-opacity="0.88"/>
          </svg>
          <p class="pl-2 font-medium">Delete</p>
        </button>
      </li>
      <li>
        <button class="flex justify-start table-modal-btn">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M18.7087 3.63126C19.0987 4.02127 19.0987 4.65127 18.7087 5.04127L16.8787 6.87126L13.1287 3.12126L14.9587 1.29126C15.1456 1.10401 15.3992 0.998779 15.6637 0.998779C15.9283 0.998779 16.1819 1.10401 16.3687 1.29126L18.7087 3.63126ZM0.998749 18.5013V15.4613C0.998749 15.3213 1.04875 15.2013 1.14875 15.1013L12.0587 4.19126L15.8087 7.94127L4.88875 18.8513C4.79875 18.9513 4.66875 19.0013 4.53875 19.0013H1.49875C1.21875 19.0013 0.998749 18.7813 0.998749 18.5013Z" fill="black" fill-opacity="0.54"/>
          </svg>
          <p class="pl-2 font-medium">Edit</p>
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "table-modal"
}
</script>

<style>
  .table-modal {
    width: 123px;
    height: 89px;
  }
  .table-modal-btn {
    transition-duration: 0.4s;
  }
  .table-modal-btn:hover {
    background-color: #e7e7e7;
  }

</style>