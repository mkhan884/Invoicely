<template>
  <div class="overflow-hidden bg-white py-12">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div
        class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2"
      >
        <div class="lg:pr-8 lg:pt-4">
          <div class="lg:max-w-lg mt-20">
            <h2 class="text-base font-semibold leading-7 text-gray-600">Invoicely</h2>
            <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              Invoicing made easier!
            </p>
            <p class="mt-6 text-lg leading-8 text-gray-600">
              No nonsense Invoicing app that lets users create modern looking invoices without a
              hassle. Sign up and get started today!
            </p>
            <button
              type="submit"
              @click="navigateToLogin"
              class="flex justify-center rounded-md mt-6 bg-black px-3 py-1.5 text-white text-sm font-semibold leading-6 shadow-sm hover:bg-white hover:text-black hover:border-black border border-transparent border-2 transition duration-300 ease-in-out focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-black"
            >
              Get Started
            </button>
          </div>
        </div>
        <img
          src="../assets/logo/product_screenshot2.png"
          alt="Product screenshot"
          class="mt-16 w-[48rem] max-w-none rounded-xl shadow-xl ring-1 ring-gray-400/10 sm:w-[57rem] md:-ml-4 lg:-ml-0"
          width="2432"
          height="1600"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    navigateToLogin() {
      this.$router.push('/signup')
    }
  }
}
</script>
