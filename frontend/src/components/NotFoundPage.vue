<template>
  <main class="grid min-h-full place-items-center mt-12 bg-white px-6 py-24 sm:py-32 lg:px-8">
    <div class="text-center">
      <p class="text-base font-semibold text-gray-600">404</p>
      <h1 class="mt-4 text-3xl font-bold tracking-tight text-gray-900 sm:text-5xl">
        Page not found
      </h1>
      <p class="mt-6 text-base leading-7 text-gray-600">
        Sorry, we couldn’t find the page you’re looking for.
      </p>
      <div class="mt-6 flex items-center justify-center gap-x-6">
        <a
          @click="navigateToHome"
          class="flex justify-center cursor-pointer rounded-md bg-black px-5 py-1.5 text-white text-sm font-semibold leading-6 shadow-sm hover:bg-white hover:text-black hover:border-black border border-transparent border-2 transition duration-300 ease-in-out focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-black"
          >Go back home</a
        >
      </div>
    </div>
  </main>
</template>

<script>
export default {
  methods: {
    navigateToHome() {
      this.$router.push('/')
    }
  }
}
</script>
