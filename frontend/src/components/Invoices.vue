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
                        class="block text-sm font-medium text-gray-700 dark:text-white"
                        >Your Business Information</label
                      >
                      <p class="text-sm mb-4 text-gray-500">Click on the card to edit your business.</p>
                      <span v-if="businessExists">
                        <a @click.prevent="navigateToBusiness" class="mb-4 text-base block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
                          <h7 class="mb-2 font-semibold tracking-tight text-gray-900 dark:text-white">{{this.businessName}}</h7>
                          <p class="font-normal text-gray-700 dark:text-gray-400">{{ this.businessAddress}}</p>
                          <p class="font-normal text-gray-700 dark:text-gray-400">{{ this.businessCity}}, {{ this.businessCountry}}</p>
                          <p class="font-normal text-gray-700 dark:text-gray-400">{{ this.businessPhoneNumber}}</p>
                        </a>
                      </span>
                      <span v-else>
                        <a @click.prevent="navigateToBusiness" class="mb-4 text-base block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700 flex flex-col items-center justify-center">
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
                        class="block text-sm font-medium text-gray-700 dark:text-white"
                        >Customer Information</label
                      >
                      <p class="text-sm text-gray-500 mb-4">Click on selected customer card to edit the customer information</p>
                      <select
                        v-model="selectedCustomer"
                        id="organization-input"
                        class="mb-4 bg-gray-50 border border-gray-300 text-gray-900 text-xs rounded-lg focus:ring-gray-950 focus:border-gray-950 block w-full p-2 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        style="width: 60%"

                      >
                        <option v-for="customer in customers" :key="customer" :value="customer">{{ customer.name }} | {{customer.phone_number}}</option>
                      </select>

                      <span v-if="selectedCustomer">
                        <a @click.prevent="naviagateToCustomer" class="mb-4 text-base block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
                          <h7 class="mb-2 font-semibold tracking-tight text-gray-900 dark:text-white">{{selectedCustomer.name}}</h7>
                          <p class="font-normal text-gray-700 dark:text-gray-400">{{ selectedCustomer.address}}</p>
                          <p class="font-normal text-gray-700 dark:text-gray-400">{{ selectedCustomer.city}}, {{ selectedCustomer.country}}</p>
                          <p class="font-normal text-gray-700 dark:text-gray-400">{{ selectedCustomer.phone_number}}</p>
                        </a>
                      </span>
                    </div>
                    <div>
                      <label
                        for="invoice-number-input"
                        class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                        >Invoice Number</label
                      >
                      <input
                        v-model="invoiceNumber"
                        type="text"
                        id="invoice-number-input"
                        class="mb-4 block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-gray-950 focus:border-gray-950 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        style="width: 60%"
                      />
                    </div>
                    <!-- City and Country inputs in the same line -->
                    <div class="flex mb-4">
                      <div class="mr-2" style="width: 30%">
                        <label
                          for="invoice-date-input"
                          class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                          >Invoice Date</label
                        >
                        <input
                          v-model="invoiceDate"
                          type="date"
                          id="invoice-date-input"
                          class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-gray-950 focus:border-gray-950 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        />
                      </div>
                      <div class="ml-2" style="width: 28%">
                        <label
                          for="invoice-due-input"
                          class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                          >Invoice Due Date</label
                        >
                        <input
                          v-model="invoiceDue"
                          type="date"
                          id="invoice-due-input"
                          class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-gray-950 focus:border-gray-950 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        />
                      </div>
                    </div>

                    <div style="width: 60%;">
                      <label
                        for="work-description-input"
                        class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                        >Work Descripton</label
                      >
                      <input
                          v-model="invoiceDescription"
                          type="text"
                          id="invoice-due-input"
                          class="block mb-4 w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-gray-950 focus:border-gray-950 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        />
                    </div>

                    <div class="flex mb-4">
                      <div class="mr-2" style="width: 30%">
                        <label
                          for="Hours-input"
                          class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                          >Hours</label
                        >
                        <input
                          v-model="invoiceHours"
                          type="number"
                          id="hours-input"
                          class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-gray-950 focus:border-gray-950 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        />
                      </div>
                      <div class="ml-2" style="width: 28%">
                        <label
                          for="rate-input"
                          class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                          >Rate</label
                        >
                        <input
                          v-model="invoiceRate"
                          type="number"
                          id="rate-input"
                          class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-gray-950 focus:border-gray-950 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        />
                      </div>
                    </div>

                    <div>
                      <label
                        for="currency-input"
                        class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                        >Business Currency</label
                      >
                      <input 
                        v-model="businessCurrency"
                        class="pointer-events-none block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-gray-950 focus:border-gray-950 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        style="width: 60%;"
                      />
                      <p
                        id="helper-text-explanation"
                        class="mt-2 text-xs text-gray-500 dark:text-gray-400 w-8/12"
                      >
                        Selected currency would be used in the invoice. To change the currency in
                        the invoice, the business information would have to be updated.
                      </p>
                    </div>
                    <div class="flex justify-start">
                      <button
                        @click="createInvoice"
                        class="mt-4 mb-4 rounded-md bg-black px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-white hover:text-black border-2 border-black"
                      >
                        Create Invoice
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      <!-- <main class="flex-1 overflow-y-auto"></main> -->
    </div>
  </div>
</template>
<script>
import Navbar from './Navbar.vue'
import NewSidebar from './NewSidebar.vue'
import axios from 'axios'
import { jsPDF } from "jspdf";

export default {
  components: {
    Navbar,
    NewSidebar
  },
  data(){
    return{
      
      // Business Information
      businessName: '',
      businessAddress: '',
      businessCity: '',
      businessCountry: '',
      businessPhoneNumber: '',
      businessCurrency: '',
      businessExists: false,

      // Customer Information
      customers: [],
      customerSelected: false,
      selectedCustomer: null,

      //Invoice information
      invoiceNumber: '',
      invoiceDate: '',
      invoiceDue: '',
      invoiceDescription: '',
      invoiceHours: '',
      inoviceRate: '',
    }
  },
  created(){
    this.getBusinessInformation()
    this.getCustomerInformation()
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
          this.businessCurrency = response.data.business[0].currency
        }
      } catch (error) {
        console.error(error)
      }
    },
    async getCustomerInformation(){
      const profileId = this.$store.getters['getProfileId']
      try {
        const response = await axios.get(`http://localhost:8000/user/${profileId}/getCustomers/`)
        this.customers = response.data.customers
      } catch (error) {
        console.error(error)
      }
    },
    createInvoice(){
      const doc = new jsPDF()

      const marginRight = 10
      const marginLeft = 10
      
      // Invoice Title

      doc.setFontSize(26);
      // Create the full title string
      const title = `Invoice ${this.invoiceNumber}`;
      // Calculate the width of the text in millimeters
      const textWidth = doc.getStringUnitWidth(title) * doc.internal.getFontSize() / doc.internal.scaleFactor;
      // Set the x position for right alignment at 210 mm (width of an A4 page) minus textWidth and a right margin
      var xPos = 210 - textWidth - marginRight;
      // Position the text at calculated x position and y = 10 mm from the top
      doc.text(title, xPos, 25);

      // Business information
      doc.setFontSize(11)
      doc.setFont('undefined', 'bold')
      const nameWidth = doc.getStringUnitWidth(this.businessName) * doc.internal.getFontSize() / doc.internal.scaleFactor
      var xPos = 210 - nameWidth - marginRight
      doc.text(this.businessName, xPos, 35)
      doc.setFont('undefined', 'normal')

      //Business Address
      const addressWidth = doc.getStringUnitWidth(this.businessAddress) * doc.internal.getFontSize() / doc.internal.scaleFactor
      var xPos = 210 - addressWidth - marginRight
      doc.text(this.businessAddress, xPos, 40)

      const cityCountry = `${this.businessCity}, ${this.businessCountry}`
      const cityCountryWidth = doc.getStringUnitWidth(cityCountry) * doc.internal.getFontSize() / doc.internal.scaleFactor
      var xPos = 210 - cityCountryWidth - marginRight
      doc.text(cityCountry, xPos, 45)

      // Business Phone Number
      const phoneNumberWidth = doc.getStringUnitWidth(this.businessPhoneNumber) * doc.internal.getFontSize() / doc.internal.scaleFactor
      var xPos = 210 - phoneNumberWidth - marginRight
      doc.text(this.businessPhoneNumber, xPos, 55)

      doc. setDrawColor(228, 228, 228)
      doc.setLineWidth(0.25)
      doc.line(10, 60, 200, 60)
      
      doc.setTextColor(150,150,150)
      doc.setFont('undefined', 'bold')
      doc.setFontSize(9)
      doc.text('Bill To', 10, 65)
      
      doc.setFontSize(12);
      doc.setTextColor(0,0,0)
      doc.text(this.selectedCustomer.name, 10, 73)
      doc.setFont('undefined', 'normal')
      doc.text(this.selectedCustomer.address, 10, 78)
      doc.text(`${this.selectedCustomer.city}, ${this.selectedCustomer.country}`, 10, 83)
      doc.text(this.selectedCustomer.phone_number, 10, 88)


        // Invoice Details Table Header
        doc.setFontSize(11);
        doc.text('Item Description', 20, 105);
        doc.text('Qty', 120, 105);
        doc.text('Unit Price', 140, 105);
        doc.text('Total', 170, 105);

        // Example Item Details
        const items = [
          { description: 'Product 1', qty: 2, unitPrice: 50, total: 100 },
          { description: 'Product 2', qty: 3, unitPrice: 30, total: 90 },
          { description: 'Product 3', qty: 1, unitPrice: 70, total: 70 }
        ];

        let startY = 113;
        items.forEach(item => {
          doc.text(item.description, 20, startY);
          doc.text(item.qty.toString(), 120, startY, null, null, 'right');
          doc.text(item.unitPrice.toFixed(2), 140, startY, null, null, 'right');
          doc.text(item.total.toFixed(2), 170, startY, null, null, 'right');
          startY += 8;
        });

        // Total Cost
        doc.setFontSize(12);
        doc.text('Total Amount:', 140, startY + 5);
        doc.text('$260.00', 170, startY + 5, null, null, 'right');

        // Save the PDF
        doc.save('invoice.pdf');

    },
    navigateToBusiness(){
      const profileId = this.$store.getters['getProfileId']
      this.$router.push(`/${profileId}/business`)
    },
    naviagateToCustomer(){
      const profileId = this.$store.getters['getProfileId']
      this.$router.push(`/${profileId}/customers`)
    }
  }
}
</script>
