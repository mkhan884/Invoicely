<template>
  <Disclosure as="nav" class="bg-gray-900">
    <div class="max-w-7xl mx-auto px-2">
      <div class="relative flex items-center justify-between h-16">
        <!-- Placeholder for potential left side content -->
        <div class="flex-1 flex items-center justify-start">
          <!-- Optionally you can add icons or logos if needed here -->
        </div>

        <!-- Profile dropdown aligned to the right -->
        <div class="flex items-center">
          <Menu as="div" class="ml-auto mr-12 relative">
            <div>
              <MenuButton class="flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                <span class="sr-only">Open user menu</span>
                <img
                  class="h-8 w-8 rounded-full"
                  src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                  alt=""
                />
              </MenuButton>
            </div>
            <transition
              enter-active-class="transition ease-out duration-100"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <MenuItems class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                <MenuItem v-slot="{ active }">
                  <a
                    href="#"
                    :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']"
                    >Your Profile</a
                  >
                </MenuItem>
                <MenuItem v-slot="{ active }">
                  <button
                    class="w-full text-left block px-4 py-2 text-sm text-gray-700 focus:outline-none focus:bg-gray-100"
                    :class="{ 'bg-gray-100': active }"
                    type="submit"
                    @click.prevent="logout"
                  >
                    Sign out
                  </button>
                </MenuItem>
              </MenuItems>
            </transition>
          </Menu>
        </div>
      </div>
    </div>
  </Disclosure>
</template>

<script>
import {
  Disclosure,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems
} from '@headlessui/vue'
export default {
  components: {
    Disclosure,
    Menu,
    MenuButton,
    MenuItem,
    MenuItems
  },
  data() {
    return {
    }
  },
  methods: {
    navigateTo(route) {
      this.$router.push(route)
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
