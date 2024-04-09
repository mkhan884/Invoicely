<template>
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-12 w-auto" src="../assets/logo/invoicely.jpeg" alt="logo" />
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
        Sign up for your Invoicely Account!
      </h2>
    </div>
    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" @submit.prevent="register">
        <div>
          <label for="name" class="block text-sm font-medium leading-6 text-gray-900">Name</label>
          <div class="mt-2">
            <input
              v-model="name"
              id="name"
              name="name"
              type="text"
              autocomplete="name"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900"
            >Email address</label
          >
          <div class="mt-2">
            <input
              v-model="email"
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900"
              >Password</label
            >
          </div>
          <div class="mt-2">
            <input
              v-model="password"
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>
        <div>
          <button
            type="submit"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Sign Up
          </button>
        </div>
      </form>
      <div v-if="error" class="mt-4 text-red-500">{{ error }}</div>
    </div>
    <div class="mt-4 text-center text-sm text-gray-600">
      Already have an account?
      <button @click="navigateToLogin" class="text-indigo-600 hover:text-indigo-500">Log in</button>
    </div>

    <GenericPopup
      v-if="showPopup"
      :popupTitle="popupTitle"
      :popupDescription="popupDescription"
      :buttonText="buttonText"
      :iconType="iconType"
      @close-popup="closePopup"
      @button-click="buttonClick"
    />
  </div>
</template>

<script>
import axios from 'axios'
import GenericPopup from './GenericPopup.vue'
export default {
  components: {
    GenericPopup
  },
  data() {
    return {
      name: '',
      email: '',
      password: '',
      error: '',
      popupTitle: '',
      popupDescription: '',
      buttonText: '',
      iconType: '',
      showPopup: false
    }
  },
  methods: {
    async register() {
      try {
        // Make a POST request to the user/addUser endpoint in the backend
        const response = await axios.post('http://localhost:8000/user/addUser', {
          name: this.name,
          email: this.email,
          password: this.password
        })
        // Handle succesful login.
        // Show success popup and update iconType to success.
        this.showPopup = true
        this.iconType = 'success'
        this.popupTitle = 'Success'
        ;(this.popupDescription = 'Successfully created an account. Log in to continue.'),
          (this.buttonText = 'Log in')
      } catch (error) {
        // Handle unsuccessful login.
        // Show popup and update iconType to failure.
        // Also update title, description, and buttonText.
        this.showPopup = true
        this.iconType = 'failure'
        this.popupTitle = 'Unsuccesful'
        this.popupDescription = error.response.data.error
        this.buttonText = 'Continue'
      }
    },
    navigateToLogin() {
      this.$router.push('/login')
    },
    closePopup() {
      this.showPopup = false
    },
    buttonClick() {
      // Check if registration was a success then make the button in the pop redirect to /login page
      if (this.iconType == 'success') this.$router.push('/login')
      // Else just close the popup.
      else this.showPopup = false
    }
  }
}
</script>
