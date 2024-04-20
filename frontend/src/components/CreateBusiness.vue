<template>
  <div v-if="!businessExists" class="createBusinessForm flex justify-center">
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
                  class="mb-4 block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-gray-950 focus:border-gray-950 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
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
                  Selected currency would be used in the invoice. To change the currency in the
                  invoice, the business information would have to be updated.
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

  <div v-else class="businessDisplay mx-auto" style="width: 60%">
    <div class="displayBusiness">
      <div>
        <div class="mt-6 px-4 sm:px-0">
          <h3 class="text-base font-semibold leading-7 text-gray-900">Business Information</h3>
          <p class="mt-1 max-w-2xl text-sm leading-6 text-gray-500">
            Details and settings for your business. This is the information that would be used on
            your invoice.
          </p>
        </div>
        <div class="mt-6 border-t border-gray-100">
          <dl class="divide-y divide-gray-100">
            <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt class="text-sm font-medium leading-6 text-gray-900">Business Name</dt>
              <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                {{ this.business.business_name }}
              </dd>
            </div>
            <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt class="text-sm font-medium leading-6 text-gray-900">Business Address</dt>
              <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                {{ this.business.business_address }}
              </dd>
            </div>
            <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt class="text-sm font-medium leading-6 text-gray-900">Business City</dt>
              <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                {{ this.business.business_city }}
              </dd>
            </div>
            <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt class="text-sm font-medium leading-6 text-gray-900">Country</dt>
              <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                {{ this.business.business_country }}
              </dd>
            </div>
            <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt class="text-sm font-medium leading-6 text-gray-900">Phone Number</dt>
              <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                {{ this.business.business_phone_number }}
              </dd>
            </div>
            <div class="px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt class="text-sm font-medium leading-6 text-gray-900">Organization Type</dt>
              <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                {{ this.business.organization_type }}
              </dd>
            </div>
            <div class="mb-4 px-4 py-4 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
              <dt class="text-sm font-medium leading-6 text-gray-900">Currency</dt>
              <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">
                {{ this.business.currency }}
              </dd>
            </div>
          </dl>
        </div>
      </div>
      <div>
        <button
          type="submit"
          @click="openEditModal(business)"
          class="flex justify-center rounded-md bg-black px-5 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-white hover:text-black border-2 border-black"
        >
          Edit
        </button>
      </div>
    </div>
  </div>

  <div class="editWrapper">
    <div
      v-if="editModal"
      tabindex="-1"
      class="overflow-y-auto overflow-x-hidden fixed top-0 right-0 bottom-0 left-0 z-50 flex justify-center items-center bg-black bg-opacity-50"
    >
      <div class="relative p-4 w-full max-w-md max-h-full">
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
          <div
            class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600"
          >
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Edit Business</h3>
            <button
              @click="closeEditModal"
              type="button"
              class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
            >
              <svg
                class="w-3 h-3"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 14 14"
              >
                <path
                  stroke="currentColor"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
                />
              </svg>
              <span class="sr-only">Close modal</span>
            </button>
          </div>
          <!-- Modal body -->
          <form class="p-4 md:p-5">
            <div class="grid gap-4 mb-4 grid-cols-2">
              <div class="col-span-2">
                <label
                  for="name"
                  class="block mb-1 text-sm font-medium text-gray-900 dark:text-white"
                  >Business Name</label
                >
                <input
                  v-model="businessName"
                  type="text"
                  @input="validateForm"
                  name="name"
                  id="name"
                  class="bg-gray-50 border border-gray-300 focus:ring-gray-950 focus:border-gray-950 text-gray-900 text-sm rounded-lg block w-full p-2.5"
                  required
                />
              </div>
              <div class="col-span-2">
                <label
                  for="Address"
                  class="block mb-1 text-sm font-medium text-gray-900 dark:text-white"
                  >Business Address</label
                >
                <input
                  v-model="streetAddress"
                  type="text"
                  @input="validateForm"
                  name="address"
                  id="address"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-gray-950 focus:border-gray-950 block w-full p-2.5"
                  placeholder="Type Business Address"
                  required
                />
              </div>
              <div class="col-span-2 sm:col-span-1">
                <label
                  for="City"
                  class="block mb-1 text-sm font-medium text-gray-900 dark:text-white"
                  >City</label
                >
                <input
                  v-model="city"
                  type="text"
                  @input="validateForm"
                  name="city"
                  id="city"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-gray-950 focus:border-gray-950 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  placeholder="City"
                  required
                />
              </div>
              <div class="col-span-2 sm:col-span-1">
                <label
                  for="Country"
                  class="block mb-1 text-sm font-medium text-gray-900 dark:text-white"
                  >Country</label
                >
                <input
                  v-model="country"
                  type="text"
                  @input="validateForm"
                  name="Country"
                  id="Country"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-gray-950 focus:border-gray-950 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  placeholder="Country"
                  required
                />
              </div>
              <div class="col-span-2">
                <label
                  for="phone_number"
                  class="block mb-1 text-sm font-medium text-gray-900 dark:text-white"
                  >Phone Number</label
                >
                <input
                  v-model="phoneNumber"
                  type="text"
                  @input="validateForm"
                  name="phone_number"
                  id="phone_number"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-gray-950 focus:border-gray-950 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  placeholder="Phone Number"
                  required
                />
              </div>
              <div class="col-span-2">
                <label
                  for="organization_type"
                  class="block mb-1 text-sm font-medium text-gray-900 dark:text-white"
                  >Organization Type</label
                >
                <select
                  v-model="organization"
                  @input="validateForm"
                  id="organization_type"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-gray-950 focus:border-gray-950 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                >
                  <option>Sole Proprietorship</option>
                  <option>Partnership</option>
                  <option>Corporation</option>
                </select>
              </div>
              <div class="col-span-2">
                <label
                  for="currency"
                  class="block mb-1 text-sm font-medium text-gray-900 dark:text-white"
                  >Currency</label
                >
                <select
                  v-model="currency"
                  @input="validateForm"
                  id="currency"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-gray-950 focus:border-gray-950 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                >
                  <option>United States of America Dollar (USD)</option>
                  <option>Canadian Dollar (CAD)</option>
                  <option>United Arab Emirates Dirham (AED)</option>
                </select>
              </div>
            </div>

            <div class="col-span-2 flex justify-between">
              <button
                @click="updateCustomerToDB"
                type="button"
                :class="{
                  'bg-black text-semibold hover:bg-white hover:text-black hover:border-black border border-transparent border-2 transition duration-300 ease-in-out focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-black cursor-pointer':
                    isFormValid,
                  'bg-gray-300 text-gray-500 cursor-not-allowed': !isFormValid
                }"
                :disabled="!isFormValid"
                class="inline-flex items-center text-white font-medium rounded-lg text-sm px-5 py-2.5 text-center transition duration-300 ease-in-out"
              >
                <svg
                  class="me-1 -ms-1 w-5 h-5"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                Update
              </button>

              <!-- Delete button -->
              <button
                @click="deleteCustomerFromDB"
                type="button"
                class="bg-white hover:bg-black hover:text-white cursor-pointer text-bg-black font-semibold rounded-lg text-sm px-5 py-2.5 text-center transition duration-300 ease-in-out border-2 border-black"
              >
                Delete Business
              </button>
            </div>
          </form>
        </div>
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
      // Form Elements
      businessName: '',
      phoneNumber: '',
      streetAddress: '',
      city: '',
      country: '',
      organization: '',
      currency: '',
      business: [],
      businessExists: false,

      // Popup Elements
      popupTitle: '',
      popupDescription: '',
      buttonText: '',
      iconType: '',
      showPopup: false,

      // Edit Modal
      editModal: false
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
        // Call getBusiness to update the form
        this.getBusiness()
        // Hide the form
        this.businessExists = true
      } catch (error) {
        console.log(error)
      }
    },
    // Call BE method getBusiness and assign the response to array this.business
    async getBusiness() {
      const profileId = this.$store.getters['getProfileId']
      try {
        const response = await axios.get(`http://localhost:8000/user/${profileId}/getBusiness/`)
        const businessData = response.data.business

        if (businessData.length === 0) {
          // If no business data is returned, set businessExists to false
          this.businessExists = false
        } else {
          // If business data is returned, set businessExists to true and populate business object
          this.business = businessData[0]
          this.businessExists = true
        }
      } catch (error) {
        // Handle errors and set businessExists to false
        console.error('Error fetching business:', error)
        this.businessExists = false
      }
    },

    // async updateBusiness(){
    //     const profileId = this.$store.getters['getProfileId']

    //     try {
    //         await axios.post(`http://localhost:8000/user/${profileId}/updateBusiness`{

    //         })
    //     } catch (error) {

    //     }

    // },

    closePopup() {
      this.showPopup = false
    },
    // Opening the modal sets the Form elements to the values from the this.business array
    openEditModal() {
      this.businessName = this.business.business_name
      this.streetAddress = this.business.business_address
      this.city = this.business.business_city
      this.country = this.business.business_country
      this.phoneNumber = this.business.business_phone_number
      this.organization = this.business.organization_type
      this.currency = this.business.currency
      this.editModal = true
    },
    closeEditModal() {
      this.editModal = false
    },
    validateForm() {
      this.isFormValid =
        !!this.businessName &&
        !!this.phoneNumber &&
        !!this.city &&
        !!this.country &&
        !!this.streetAddress &&
        !!this.currency &&
        !!this.organization
    }
  }
}
</script>
