<template>
  <div v-if="!businessExists" class="flex justify-center">
    <div class="max-w-screen-xl mx-auto mt-8 flex">
      <!-- Left column (70%) -->
      <div class="formWrapper">
        <!-- Form content here -->
        <div class="max-w-screen-xl mx-auto mt-0">
          <div class="w-full flex">
            <!-- Left column -->
            <div class="w-2/6">
              <div>
                <h2 class="text-l font-semibold mb-0">Business Information</h2>
                <p class="text-sm text-gray-500 mb-4">Enter information that is used to invoice.</p>
              </div>
            </div>
            <!-- Right column -->
            <div class="w-4/6">
              <div>
                <label
                  for="small-input"
                  class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                  >Business Name</label
                >
                <input
                  v-model="businessName"
                  type="text"
                  id="small-input"
                  class="mb-4 block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  style="width: 60%"
                />
              </div>
              <!-- Add more form elements here -->
              <div>
                <label
                  for="phone-input"
                  class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                  >Phone Number</label
                >
                <input
                  v-model="phoneNumber"
                  type="text"
                  id="phone-input"
                  class="mb-4 block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
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
                  class="mb-4 block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
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
                    class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
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
                    class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
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
                  class="mb-4 bg-gray-50 border border-gray-300 text-gray-900 text-xs rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
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
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-xs rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
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
                  Selected currency would be used in the invoice. To change the currency in the
                  invoice, the business information would have to be updated.
                </p>
              </div>
              <div class="flex justify-start">
                <button
                  @click="addBusiness"
                  class="mt-4 rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
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

  <div v-if="businessExists" class="mx-auto" style="width: 60%">
  <div class="displayBusiness">
    <div>
      <div class="mt-3 px-4 sm:px-0">
        <h3 class="text-base font-semibold leading-7 text-gray-900">Business Information</h3>
        <p class="mt-1 max-w-2xl text-sm leading-6 text-gray-500">
          Details and settings for your business. This is the information that would be used on your invoice.
        </p>
      </div>
      <div class="mt-6 border-t border-gray-100">
        <dl class="divide-y divide-gray-100">
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm font-medium leading-6 text-gray-900">Business Name</dt>
            <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{ this.businessName }}
            </dd>
          </div>
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm font-medium leading-6 text-gray-900">Business Address</dt>
            <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{ this.streetAddress }}
            </dd>
          </div>
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm font-medium leading-6 text-gray-900">Business City</dt>
            <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{ this.city }}
            </dd>
          </div>
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm font-medium leading-6 text-gray-900">Country</dt>
            <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{ this.country }}
            </dd>
          </div>
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm font-medium leading-6 text-gray-900">Organization Type</dt>
            <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{ this.organization }}
            </dd>
          </div>
          <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
            <dt class="text-sm font-medium leading-6 text-gray-900">Currency</dt>
            <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
              {{ this.currency }}
            </dd>
          </div>
        </dl>
      </div>
    </div>
    <div>
        <button
            type="submit"
            @click.prevent="editBusiness"
            class="flex justify-center rounded-md bg-indigo-600 px-5 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Edit
          </button>
    </div>
  </div>
</div>


  <div class="popup">
    <GenericPopup
      v-if="showPopup"
      :popupTitle="popupTitle"
      :popupDescription="popupDescription"
      :buttonText="buttonText"
      :iconType="iconType"
      @close-popup="closePopup"
      @button-click="closePopup"
    />
  </div>
</template>

<script>
import GenericPopup from './GenericPopup.vue'
import axios from 'axios'

export default {
  components: {
    GenericPopup
  },
  data() {
    return {
      //Form Elements
      businessName: '',
      phoneNumber: '',
      streetAddress: '',
      city: '',
      country: '',
      organization: '',
      currency: '',
      businessExists: false,

      //Popup Elements
      popupTitle: '',
      popupDescription: '',
      buttonText: '',
      iconType: '',
      showPopup: false
    }
  },
  created() {
    this.getBusiness()
  },
  methods: {
    async addBusiness() {
      const profileId = this.$store.getters['getProfileId']
      try {
        await axios.post(`http://localhost:8000/user/${profileId}/addBusiness/`, {
          name: this.businessName,
          phone_number: this.phoneNumber,
          address: this.streetAddress,
          city: this.city,
          country: this.country,
          organization: this.organization,
          currency: this.currency
        })
        this.popupTitle = 'Success'
        this.popupDescription = 'Business created successfully. You may begin invoicing.'
        this.buttonText = 'continue'
        this.iconType = 'success'
        this.showPopup = true

        // Hide the form
        this.businessExists = true
      } catch (error) {
        console.log(error)
      }
    },

    async getBusiness() {
      const profileId = this.$store.getters['getProfileId']
      try {
        const response = await axios.get(`http://localhost:8000/user/${profileId}/getBusiness/`)
        
        const { business_name: businessName, business_phone_number: phoneNumber, business_address: streetAddress, business_city: city, business_country: country, organization_type: organization, currency } = response.data.business[0]
        this.businessName = businessName
        this.phoneNumber = phoneNumber
        this.streetAddress = streetAddress
        this.city = city
        this.country = country
        this.organization = organization
        this.currency = currency

        // Hide the form and display the business card
        this.businessExists = true
      } catch (error) {
        this.businessExists = false
      }
    },

    closePopup() {
      this.showPopup = false
    }
  }
}
</script>
