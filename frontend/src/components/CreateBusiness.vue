<template>
    <div class="max-w-screen-xl mx-auto mt-8 flex">
      <!-- Left column (70%) -->
      <div class="w-7/10">
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
                      type="text"
                      id="city-input"
                      class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    />
                  </div>
                  <div class="ml-2" style="width: 28%;">
                    <label
                      for="country-input"
                      class="block mb-1 text-sm font-medium text-gray-700 dark:text-white"
                      >Country</label
                    >
                    <input
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
                    id="organization-input"
                    class="mb-4 bg-gray-50 border border-gray-300 text-gray-900 text-xs rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" style="width: 60%;"
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
                    id="currency-input"
                    class="bg-gray-50 border border-gray-300 text-gray-900 text-xs rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" style="width: 60%;"
                  >
                    <option>Canadian Dollar (CAD)</option>
                    <option>United States of America Dollar (USD)</option>
                    <option>United Arab Emirates Dirham (AED)</option>
                  </select>
                  <p id="helper-text-explanation" class="mt-2 text-xs text-gray-500 dark:text-gray-400" style="width: 70%;">Selected currency would be used in the invoice. To change the currency in the invoice, the business information would have to be updated.</p>
                </div>
                <div class="flex justify-start">
                <button class="mt-4 rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
                  Create Business
                </button>
              </div>

              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Right column (30%) -->
      <div class="w-3/10">
        <!-- Empty column -->
        <h3 class="text-lg font-semibold mb-4">Latest News</h3>
        <ul class="list-disc list-inside">
          <li class="text-sm text-gray-700 dark:text-white">Stay tuned for our upcoming events!</li>
          <li class="text-sm text-gray-700 dark:text-white">Read our blog for industry insights.</li>
          <li class="text-sm text-gray-700 dark:text-white">Follow us on social media for updates.</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
  
  }
  </script>
  