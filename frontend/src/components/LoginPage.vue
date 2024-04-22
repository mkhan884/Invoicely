<template>
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 mt-6 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img
        class="mx-auto h-10 w-auto"
        src="../assets/logo/invoicely-black.png"
        alt="Invoicely Logo"
      />
      <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
        Sign in to your account
      </h2>
    </div>
    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6">
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
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-gray-950 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900"
              >Password</label
            >
            <!-- <div class="text-sm">
              <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500"
                >Forgot password?</a
              >
            </div> -->
          </div>
          <div class="mt-2">
            <input
              v-model="password"
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-gray-950 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            @click.prevent="login"
            class="flex w-full justify-center rounded-md bg-black px-3 py-1.5 text-white text-sm font-semibold leading-6 shadow-sm hover:bg-white hover:text-black hover:border-black border border-transparent border-2 transition duration-300 ease-in-out focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-black"
          >
            Sign in
          </button>
        </div>
      </form>
      <div v-if="error" class="mt-4 text-red-500">{{ error }}</div>
      <div class="mt-4 text-center text-sm text-gray-600">
        Don't have an account?
        <button
          @click="navigateToRegistration"
          class="text-bg-black font-semibold transition transform hover:scale-110"
        >
          Sign Up!
        </button>
      </div>
    </div>
    <GenericPopup
      v-if="showPopup"
      :popupTitle="popupTitle"
      :popupDescription="popupDescription"
      :buttonText="buttonText"
      :iconType="iconType"
      @closePopup="closePopup"
      @buttonClick="closePopup"
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
    async login() {
      try {
        // Make a POST request to the user/authenticate endpoint in the backend
        const response = await axios.post('http://localhost:8000/user/authenticate', {
          email: this.email,
          password: this.password
        })
        // Returns authenticated variable and ProfileID
        // Handle successful login
        if (response.data.authenticated) {
          this.$store.commit('setAuthenticated', true)
          this.$store.commit('setProfileId', response.data.profileId)
          this.$router.push({ path: `/${response.data.profileId}/dashboard` })
        }
      } catch (error) {
        // Handle authentication error
        this.popupTitle = 'Unsuccessful'
        this.popupDescription = error.response.data.errorDescription
        this.buttonText = 'Try Again'
        this.iconType = 'Failure'
        this.showPopup = true
      }
    },
    navigateToRegistration() {
      this.$router.push('/signup')
    },
    closePopup() {
      this.showPopup = false
    }
  }
}
</script>
