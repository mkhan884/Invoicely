<template>
  <div class="flex h-screen">
    <!-- Sidebar -->
    <NewSidebar class="w-64 fixed h-full bg-gray-900 z-30" />

    <!-- Main container for Navbar and content -->
    <div class="flex flex-col ml-64 flex-1">
      <!-- Navbar -->
      <Navbar class="bg-gray-800 w-full" />
      <div class="createInvoiceForm flex justify-center">
          <div class="max-w-screen-xl mx-auto mt-8 flex">
            <!-- Left column (70%) -->
            <div class="formWrapper">
              <!-- Form content here -->
              <div class="max-w-screen-xl mx-auto mt-0">
                <div class="w-full flex">
                  <!-- Left column -->
                  <div class="w-2/6">
                    <div>
                      <h2 class="text-l font-semibold mb-0">Invoice Information</h2>
                      <p class="text-sm text-gray-500 mb-4">
                        Enter information to create an invoice.
                      </p>
                    </div>
                  </div>
                  <!-- Right column -->
                  <div class="w-4/6">
                    <div>
                      <label
                        for="business-input"
                        class="block mb-4 text-sm font-medium text-gray-700 dark:text-white"
                        >Your Business Information</label
                      >
                      <span v-if="businessExists">
                        <a @click.prevent="navigateTo" class="mb-4 text-base block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
                          <h7 class="mb-2 font-semibold tracking-tight text-gray-900 dark:text-white">{{this.businessName}}</h7>
                          <p class="font-normal text-gray-700 dark:text-gray-400">{{ this.businessAddress}}</p>
                          <p class="font-normal text-gray-700 dark:text-gray-400">{{ this.businessCity}}, {{ this.businessCountry}}</p>
                          <p class="font-normal text-gray-700 dark:text-gray-400">{{ this.businessPhoneNumber}}</p>
                        </a>
                      </span>
                      <span v-else>
                        <a @click.prevent="navigateTo" class="mb-4 text-base block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700 flex flex-col items-center justify-center">
                          <svg class="w-6 h-6 text-gray-400 dark:text-white mb-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 7.757v8.486M7.757 12h8.486M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
                          </svg>
                          <h7 class="text-gray-400">
                            Add business information to continue
                          </h7>
                        </a>
                      </span>
                    </div>
                    <!-- Add more form elements here -->
                    <div>
                      <label
                        for="customer-input"
                        class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                        >Customer Information</label
                      >
                      <input
                        v-model="phoneNumber"
                        type="text"
                        id="phone-input"
                        class="mb-4 block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-gray-950 focus:border-gray-950 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        style="width: 60%"
                      />
                    </div>
                    <div>
                      <label
                        for="address-input"
                        class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                        >Street Address</label
                      >
                      <input
                        v-model="streetAddress"
                        type="text"
                        id="address-input"
                        class="mb-4 block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-gray-950 focus:border-gray-950 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        style="width: 60%"
                      />
                    </div>
                    <!-- City and Country inputs in the same line -->
                    <div class="flex mb-4">
                      <div class="mr-2" style="width: 30%">
                        <label
                          for="city-input"
                          class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                          >City</label
                        >
                        <input
                          v-model="city"
                          type="text"
                          id="city-input"
                          class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-gray-950 focus:border-gray-950 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        />
                      </div>
                      <div class="ml-2" style="width: 28%">
                        <label
                          for="country-input"
                          class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                          >Country</label
                        >
                        <input
                          v-model="country"
                          type="text"
                          id="country-input"
                          class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-gray-950 focus:border-gray-950 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        />
                      </div>
                    </div>
                    <div>
                      <label
                        for="organization-input"
                        class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                        >Type of Organization</label
                      >
                      <select
                        v-model="organization"
                        id="organization-input"
                        class="mb-4 bg-gray-50 border border-gray-300 text-gray-900 text-xs rounded-lg focus:ring-gray-950 focus:border-gray-950 block w-full p-2 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        style="width: 60%"
                      >
                        <option>Sole Proprietorship</option>
                        <option>Partnership</option>
                        <option>Corporation</option>
                      </select>
                    </div>
                    <div>
                      <label
                        for="currency-input"
                        class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                        >Business Currency</label
                      >
                      <select
                        v-model="currency"
                        id="currency-input"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-xs rounded-lg focus:ring-gray-950 focus:border-gray-950 block w-full p-2 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        style="width: 60%"
                      >
                        <option>Canadian Dollar (CAD)</option>
                        <option>United States of America Dollar (USD)</option>
                        <option>United Arab Emirates Dirham (AED)</option>
                      </select>
                      <p
                        id="helper-text-explanation"
                        class="mt-2 text-xs text-gray-500 dark:text-gray-400"
                        style="width: 70%"
                      >
                        Selected currency would be used in the invoice. To change the currency in
                        the invoice, the business information would have to be updated.
                      </p>
                    </div>
                    <div class="flex justify-start">
                      <button
                        @click="addBusiness"
                        class="mt-4 rounded-md bg-black px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-white hover:text-black border-2 border-black"
                      >
                        Create Business
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      <main class="flex-1 overflow-y-auto"></main>
    </div>
  </div>
</template>
<script>
import Navbar from './Navbar.vue'
import NewSidebar from './NewSidebar.vue'
import axios from 'axios'
export default {
  components: {
    Navbar,
    NewSidebar
  },
  data(){
    return{
      businessName: '',
      businessAddress: '',
      businessCity: '',
      businessCountry: '',
      businessPhoneNumber: '',
      businessExists: false
    }
  },
  created(){
    this.getBusinessInformation()
  },
  methods: {
    async getBusinessInformation(){
      const profileId = this.$store.getters['getProfileId']
      try {
        const response = await axios.get(`http://localhost:8000/user/${profileId}/getBusiness/`)
        if (response.data.business.length > 0){
          this.businessExists = true
          this.businessName = response.data.business[0].business_name
          this.businessAddress = response.data.business[0].business_address
          this.businessCity = response.data.business[0].business_city
          this.businessCountry = response.data.business[0].business_country
          this.businessPhoneNumber = response.data.business[0].business_phone_number
        }
      } catch (error) {
        console.error(error)
      }
    },
    navigateTo(){
      const profileId = this.$store.getters['getProfileId']
      this.$router.push(`/${profileId}/business`)
    }
  }
}
</script>
