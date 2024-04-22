<template>
  <div class="flex h-screen">
    <!-- Sidebar -->
    <NewSidebar class="w-64 fixed h-full bg-gray-900 z-30" />

    <!-- Main container for Navbar and content -->
    <div class="flex flex-col ml-64 flex-1">
      <!-- Navbar -->
      <Navbar class="bg-gray-800 w-full" />

      <!-- Main content area -->
      <main class="flex-1 overflow-y-auto"></main>
    </div>
  </div>
</template>

<script>
import Navbar from './Navbar.vue'
import NewSidebar from './NewSidebar.vue'
export default {
  components: {
    Navbar,
    NewSidebar
  }
}
</script>
