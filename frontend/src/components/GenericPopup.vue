<template>
  <div
    class="fixed inset-0 z-50 overflow-auto flex items-center justify-center bg-black bg-opacity-50"
  >
    <div class="bg-white p-6 rounded-lg shadow-lg">
      <div class="relative p-4 max-w-md text-center">
        <!-- Modal content -->
        <button
          @click="closePopup"
          type="button"
          class="text-gray-400 absolute top-2.5 right-2.5 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center"
        >
          <svg
            aria-hidden="true"
            class="w-5 h-5"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
              clip-rule="evenodd"
            ></path>
          </svg>
          <span class="sr-only">Close modal</span>
        </button>
        <div>
          <!-- Success icon -->
          <div
            v-if="iconType === 'success'"
            class="w-12 h-12 rounded-full bg-green-100 p-2 flex items-center justify-center mx-auto mb-3.5"
          >
            <svg
              aria-hidden="true"
              class="w-8 h-8 text-green-500"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
              ></path>
            </svg>
            <span class="sr-only">Success</span>
          </div>

          <!-- Failure icon -->
          <div
            v-else
            class="w-12 h-12 rounded-full bg-red-100 p-2 flex items-center justify-center mx-auto mb-3.5"
          >
            <svg
              aria-hidden="true"
              class="w-8 h-8 text-red-500"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              ></path>
            </svg>
            <span class="sr-only">Failure</span>
          </div>
        </div>
        <p class="mb-0 text-lg font-semibold">{{ popupTitle }}</p>
        <p class="mb-4 text-sm">{{ popupDescription }}</p>
        <button
          @click="buttonClick"
          type="button"
          class="py-2 px-7 text-sm font-medium text-center text-white rounded-md bg-black hover:bg-white hover:text-black hover:border-black border border-transparent border-2 transition duration-300 ease-in-out focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-black"
        >
          {{ buttonText }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    popupTitle: {
      type: String,
      default: 'Popup Title'
    },
    popupDescription: {
      type: String,
      default: 'Popup Description'
    },
    buttonText: {
      type: String,
      default: 'Continue'
    },
    iconType: {
      type: String,
      default: 'success' // Default to success, change this to 'failure' from the parent component to display the failure icon
    }
  },
  methods: {
    closePopup() {
      this.$emit('close-popup')
    },
    buttonClick() {
      this.$emit('button-click')
    }
  }
}
</script>
