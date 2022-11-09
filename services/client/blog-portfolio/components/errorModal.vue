<template>
  <div class="modal-overlay">
    <div class="flex flex-column justify-center items-center">
      <div
        class="p-6 max-w-sm bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700"
      >
        <h5
          class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
        >
          Error
        </h5>
        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
          Please enter a valid email.
        </p>
        <button
          class="inline-flex items-center py-2 px-3 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          @click="$emit('close-modal')"
        >
          Go Back
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  background-color: #000000da;
}
</style>
