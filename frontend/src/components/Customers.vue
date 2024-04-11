<template>
    <div>
      <Navbar />
    </div>
    <div class="mx-6 mt-8">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">Customer Information</h2>
        <button class="bg-indigo-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:ring-opacity-50 transition duration-300 ease-in-out">Add Customer</button>
      </div>
      <div class="overflow-hidden shadow-md rounded-lg">
        <table class="w-full text-sm text-left rtl:text-right text-gray-700 dark:text-gray-400 divide-y divide-gray-200 dark:divide-gray-700">
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
            <tr v-for="(customer, index) in customers" :key="index" :class="(index % 2 === 0) ? 'bg-gray-100 dark:bg-gray-800' : 'bg-white dark:bg-gray-900'">
              <td class="px-6 py-4 font-semibold whitespace-nowrap">{{ customer.name }}</td>
              <td class="px-6 py-4">{{ customer.address }}</td>
              <td class="px-6 py-4">{{ customer.city }}</td>
              <td class="px-6 py-4">{{ customer.country }}</td>
              <td class="px-6 py-4">{{ customer.phone_number }}</td>
              <td class="px-6 py-4">
                <a href="#" class="text-indigo-600 hover:text-indigo-900 dark:text-indigo-400 dark:hover:text-indigo-600 font-semibold transition duration-300 ease-in-out">Edit</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div>
      <!-- Add Customer component or content -->
    </div>
  </template>
  
  
<script>
import Navbar from './Navbar.vue'
import axios from 'axios'
export default {
  components: {
    Navbar
  },
  data () {
    return {
        customers: []
    }
    },
    created(){
        this.getCustomersFromDB()
    },
    methods:{
        async getCustomersFromDB(){
            const profileId = this.$store.getters['getProfileId']
            try{
                const response = await axios.get(`http://localhost:8000/user/${profileId}/getCustomers`)
                this.customers = response.data.customers
            }
            catch (error){
                console.error('GET request unsuccessful', error.message)
            }
        }
    }
}
</script>
