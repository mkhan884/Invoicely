<template>
  <aside
    class="fixed top-0 left-0 z-40 h-screen transition-transform -translate-x-full sm:translate-x-0 bg-gray-900 text-xs text-gray-400"
  >
    <!-- Logo and title -->
    <div class="flex justify-center items-center space-x-2 px-4 mb-10 mt-6">
      <img src="../assets/logo/invoicely-white.png" class="h-6 w-auto" />
    </div>
    <!-- Navigation -->
    <nav class="mt-10">
      <div class="mb-2 ml-4">
        <span class="text-gray-500" style="font-size: 0.65rem"> Navigation </span>
      </div>
      <router-link
        v-for="item in navigation"
        :key="item.name"
        :to="item.href"
        class="ml-2 flex items-center py-2.5 px-4 rounded transition duration-200 hover:bg-gray-800 hover:text-white"
        :class="{ 'bg-gray-800 text-white': item.current }"
      >
        <svg class="h-5 w-6 mr-1" viewBox="0 0 24 24">
          <path
            v-for="(path, index) in item.iconPaths"
            :key="index"
            :d="path"
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
          ></path>
        </svg>
        {{ item.name }}
      </router-link>

      <div class="mb-2 ml-4 mt-6">
        <span class="text-gray-500" style="font-size: 0.65rem"> Quick Actions </span>
      </div>
      <div
        v-for="item in quickActions"
        :key="item.name"
        class="ml-2 flex items-center py-2.5 px-4 rounded transition duration-200 hover:bg-gray-800 hover:text-white cursor-pointer"
        :class="{ 'bg-gray-800 text-white': item.current }"
      >
        <a
          :href="item.href"
          @click.prevent="handleAction(item)"
          class="flex items-center w-full text-left"
        >
          <svg class="h-5 w-6 mr-1" viewBox="0 0 24 24" fill="none">
            <path
              v-for="(path, index) in item.iconPaths"
              :key="index"
              :d="path"
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
            ></path>
          </svg>
          {{ item.name }}
        </a>
      </div>
    </nav>
  </aside>
</template>

<script>
export default {
  data() {
    return {
      navigation: [
        {
          name: 'Dashboard',
          href: `/${this.$route.params.profileId}/dashboard`,
          current: this.$route.path.includes('dashboard'),
          iconPaths: [
            'M10 6.025A7.5 7.5 0 1 0 17.975 14H10V6.025Z',
            'M13.5 3c-.169 0-.334.014-.5.025V11h7.975c.011-.166.025-.331.025-.5A7.5 7.5 0 0 0 13.5 3Z'
          ]
        },
        {
          name: 'Customers',
          href: `/${this.$route.params.profileId}/customers`,
          current: this.$route.path.includes('customers'),
          iconPaths: [
            'M16 19h4a1 1 0 0 0 1-1v-1a3 3 0 0 0-3-3h-2m-2.236-4a3 3 0 1 0 0-4M3 18v-1a3 3 0 0 1 3-3h4a3 3 0 0 1 3 3v1a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1Zm8-10a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z'
          ]
        },
        {
          name: 'Business',
          href: `/${this.$route.params.profileId}/business`,
          current: this.$route.path.includes('business'),
          iconPaths: [
            'M8 7H5a2 2 0 0 0-2 2v4m5-6h8M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2m0 0h3a2 2 0 0 1 2 2v4m0 0v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-6m18 0s-4 2-9 2-9-2-9-2m9-2h.01'
          ]
        },
        {
          name: 'Invoices',
          href: `/${this.$route.params.profileId}/invoices`,
          current: this.$route.path.includes('invoices'),
          iconPaths: [
            'M10 3v4a1 1 0 0 1-1 1H5m4 8h6m-6-4h6m4-8v16a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V7.914a1 1 0 0 1 .293-.707l3.914-3.914A1 1 0 0 1 9.914 3H18a1 1 0 0 1 1 1Z'
          ]
        },
        {
          name: 'Expenses',
          href: '',
          current: false,
          iconPaths: [
            'M8 7V6a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1h-1M3 18v-7a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1Zm8-3.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z'
          ]
        }
      ],
      quickActions: [
        {
          name: 'Create New Invoice',
          href: '',
          current: '',
          iconPaths: [
            'M18 9V4a1 1 0 0 0-1-1H8.914a1 1 0 0 0-.707.293L4.293 7.207A1 1 0 0 0 4 7.914V20a1 1 0 0 0 1 1h4M9 3v4a1 1 0 0 1-1 1H4m11 6v4m-2-2h4m3 0a5 5 0 1 1-10 0 5 5 0 0 1 10 0Z'
          ]
        },
        {
          name: 'Sign out',
          href: '',
          current: '',
          iconPaths: ['M16 12H4m12 0-4 4m4-4-4-4m3-4h2a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3h-2']
        }
      ]
    }
  },
  methods: {
    handleAction(item) {
      if (item.name === 'Sign out') {
        this.logout()
      } else {
        this.$router.push(item.href) // Manually handle navigation for other links
      }
    },

    logout() {
      // Clear authentication state and global profile ID
      this.$store.commit('setAuthenticated', false)
      this.$store.commit('setProfileId', '')
      // Redirect to login
      this.$router.push('/login')
    }
  }
}
</script>
