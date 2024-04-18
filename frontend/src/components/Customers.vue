<template>
  <div>
    <Navbar />
  </div>
  <div class="mx-6 mt-8">
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">Customer Information</h2>
      <div class="flex items-center">
        <div class="relative w-52 mr-4">
          <input
            type="text"
            class="w-full border border-gray-300 rounded-md py-2 px-4 focus:outline-none focus:border-indigo-600"
            placeholder="Search customers..."
          />
          <button class="absolute right-0 top-0 mt-2 mr-3 focus:outline-none">
            <SearchIcon class="h-6 w-6 text-gray-400" />
          </button>
        </div>
        <button
          @click="openAddCustomerModal"
          type="button"
          class="bg-indigo-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:ring-opacity-50 transition duration-300 ease-in-out"
        >
          Add Customer
        </button>
      </div>
    </div>
    <div class="overflow-hidden shadow-md rounded-lg">
      <table
        class="w-full text-sm text-left rtl:text-right text-gray-700 dark:text-gray-400 divide-y divide-gray-200 dark:divide-gray-700"
      >
        <thead class="text-xs bg-indigo-600 text-white uppercase">
          <tr>
            <th scope="col" class="px-6 py-3">Customer Name</th>
            <th scope="col" class="px-6 py-3">Address</th>
            <th scope="col" class="px-6 py-3">City</th>
            <th scope="col" class="px-6 py-3">Country</th>
            <th scope="col" class="px-6 py-3">Phone Number</th>
            <th scope="col" class="px-6 py-3">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(customer, index) in customers"
            :key="index"
            :class="index % 2 === 0 ? 'bg-gray-100 dark:bg-gray-800' : 'bg-white dark:bg-gray-900'"
          >
            <td class="px-6 py-4 font-semibold whitespace-nowrap">{{ customer.name }}</td>
            <td class="px-6 py-4">{{ customer.address }}</td>
            <td class="px-6 py-4">{{ customer.city }}</td>
            <td class="px-6 py-4">{{ customer.country }}</td>
            <td class="px-6 py-4">{{ customer.phone_number }}</td>
            <td class="px-6 py-4">
              <button @click="openEditModal(customer)">
                <a
                  class="text-indigo-600 hover:text-indigo-900 dark:text-indigo-400 dark:hover:text-indigo-600 font-semibold transition duration-300 ease-in-out"
                  >Edit</a
                >
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div>
    <div
      v-if="addCustomerModal"
      tabindex="-1"
      class="overflow-y-auto overflow-x-hidden fixed top-0 right-0 bottom-0 left-0 z-50 flex justify-center items-center bg-black bg-opacity-50"
    >
      <div class="relative p-4 w-full max-w-md max-h-full">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
          <!-- Modal header -->
          <div
            class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600"
          >
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Add New Customer</h3>
            <button
              @click="closeAddCustomerModal"
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
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Name</label
                >
                <input
                  v-model="name"
                  @input="validateForm"
                  type="text"
                  name="name"
                  id="name"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  placeholder="Type Customer Name"
                  required
                />
              </div>
              <div class="col-span-2">
                <label
                  for="Address"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Address</label
                >
                <input
                  v-model="address"
                  type="text"
                  @input="validateForm"
                  name="address"
                  id="address"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  placeholder="Type Customer Address"
                  required
                />
              </div>
              <div class="col-span-2 sm:col-span-1">
                <label
                  for="City"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >City</label
                >
                <input
                  v-model="city"
                  type="text"
                  @input="validateForm"
                  name="city"
                  id="city"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  placeholder="City"
                  required
                />
              </div>
              <div class="col-span-2 sm:col-span-1">
                <label
                  for="Country"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Country</label
                >
                <input
                  v-model="country"
                  type="text"
                  name="Country"
                  @input="validateForm"
                  id="Country"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  placeholder="Country"
                  required
                />
              </div>
              <div class="col-span-2">
                <label
                  for="phone_number"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Phone Number</label
                >
                <input
                  v-model="phone_number"
                  type="text"
                  @input="validateForm"
                  name="phone_number"
                  id="phone_number"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  placeholder="Phone Number"
                  required
                />
              </div>
            </div>
            <button
              @click="addCustomerToDB"
              type="button"
              :class="{
                'bg-indigo-600 hover:bg-indigo-700 focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 cursor-pointer':
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
              Add new customer
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>

  <div>
    <div
      v-if="editModal"
      tabindex="-1"
      class="overflow-y-auto overflow-x-hidden fixed top-0 right-0 bottom-0 left-0 z-50 flex justify-center items-center bg-black bg-opacity-50"
    >
      <div class="relative p-4 w-full max-w-md max-h-full">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
          <!-- Modal header -->
          <div
            class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600"
          >
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Edit Customer</h3>
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
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Name</label
                >
                <input
                  v-model="name"
                  type="text"
                  @input="validateForm"
                  name="name"
                  id="name"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  placeholder="Type Customer Name"
                  required
                />
              </div>
              <div class="col-span-2">
                <label
                  for="Address"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Address</label
                >
                <input
                  v-model="address"
                  type="text"
                  @input="validateForm"
                  name="address"
                  id="address"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  placeholder="Type Customer Address"
                  required
                />
              </div>
              <div class="col-span-2 sm:col-span-1">
                <label
                  for="City"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >City</label
                >
                <input
                  v-model="city"
                  type="text"
                  @input="validateForm"
                  name="city"
                  id="city"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  placeholder="City"
                  required
                />
              </div>
              <div class="col-span-2 sm:col-span-1">
                <label
                  for="Country"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Country</label
                >
                <input
                  v-model="country"
                  type="text"
                  @input="validateForm"
                  name="Country"
                  id="Country"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  placeholder="Country"
                  required
                />
              </div>
              <div class="col-span-2">
                <label
                  for="phone_number"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                  >Phone Number</label
                >
                <input
                  v-model="phone_number"
                  type="text"
                  @input="validateForm"
                  name="phone_number"
                  id="phone_number"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                  placeholder="Phone Number"
                  required
                />
              </div>
            </div>
            <div class="col-span-2 flex justify-between">
              <button
                @click="updateCustomerToDB"
                type="button"
                :class="{
                  'bg-indigo-600 hover:bg-indigo-700 focus:ring-2 focus:ring-indigo-500 focus:ring-opacity-50 cursor-pointer':
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
                class="bg-red-600 hover:bg-red-700 focus:ring-2 focus:ring-red-500 focus:ring-opacity-50 cursor-pointer text-white font-medium rounded-lg text-sm px-5 py-2.5 text-center transition duration-300 ease-in-out"
              >
                Delete Customer
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>

  <div>
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
import Navbar from './Navbar.vue'
import GenericPopup from './GenericPopup.vue'
import axios from 'axios'
export default {
  components: {
    Navbar,
    GenericPopup
  },
  data() {
    return {
      customers: [],
      name: '',
      address: '',
      city: '',
      country: '',
      phone_number: '',
      popupTitle: '',
      popupDescription: '',
      buttonText: '',
      iconType: '',
      currentName: '',
      currentAddress: '',
      showPopup: false, // Confirmation popup
      addCustomerModal: false,
      editModal: false,
      isFormValid: false
    }
  },
  created() {
    this.getCustomersFromDB()
  },
  methods: {
    async getCustomersFromDB() {
      const profileId = this.$store.getters['getProfileId']
      try {
        const response = await axios.get(`http://localhost:8000/user/${profileId}/getCustomers`)
        this.customers = response.data.customers
      } catch (error) {
        console.error('GET request unsuccessful', error.message)
      }
    },
    async addCustomerToDB() {
      const profileId = this.$store.getters['getProfileId']
      try {
        axios.post(`http://localhost:8000/user/${profileId}/addCustomer/`, {
          name: this.name,
          address: this.address,
          city: this.city,
          country: this.country,
          phone_number: this.phone_number
        })
        this.addCustomerModal = false
        this.clearForm()
        this.getCustomersFromDB()

        // Add popup information that provides confirmation
        this.popupTitle = 'Customer Added'
        this.popupDescription = 'Succesfully Added a new customer.'
        this.iconType = 'success'
        this.buttonText = 'Continue'
        this.showPopup = true
      } catch (error) {
        console.error('POST request unsuccessful', error.message)
      }
    },
    async updateCustomerToDB() {
      const profileId = this.$store.getters['getProfileId']
      try {
        axios.post(`http://localhost:8000/user/${profileId}/updateCustomer/`, {
          name: this.currentName,
          address: this.currentAddress,
          new_name: this.name,
          new_address: this.address,
          new_city: this.city,
          new_country: this.country,
          new_phone_number: this.phone_number
        })

        this.editModal = false
        this.clearForm()
        this.getCustomersFromDB()

        // Add popup information that provides confirmation
        this.popupTitle = 'Customer Updated'
        this.popupDescription = 'Succesfully updated an existing customer.'
        this.iconType = 'success'
        this.buttonText = 'Continue'
        this.showPopup = true
      } catch (error) {
        console.error('POST request unsuccessful', error.message)
      }
    },
    async deleteCustomerFromDB() {
      const profileId = this.$store.getters['getProfileId']
      try {
        await axios.post(`http://localhost:8000/user/${profileId}/deleteCustomer/`, {
          name: this.currentName,
          address: this.currentAddress
        })
        this.getCustomersFromDB()
        this.editModal = false
        this.clearForm()
      } catch (error) {
        console.error('Delete request unsuccessful', error.message)
      }
    },
    validateForm() {
      this.isFormValid =
        !!this.name && !!this.address && !!this.city && !!this.country && !!this.phone_number
    },
    clearForm() {
      this.name = ''
      this.address = ''
      this.city = ''
      this.country = ''
      this.phone_number = ''
    },
    openAddCustomerModal() {
      this.addCustomerModal = true
    },
    closeAddCustomerModal() {
      this.addCustomerModal = false
    },
    openEditModal(customer) {
      this.currentName = customer.name
      this.currentAddress = customer.address
      this.name = customer.name
      this.address = customer.address
      this.city = customer.city
      this.country = customer.country
      this.phone_number = customer.phone_number
      this.editModal = true
    },
    closeEditModal() {
      this.editModal = false
      this.clearForm()
    },
    closePopup() {
      this.showPopup = false
    }
  }
}
</script>
