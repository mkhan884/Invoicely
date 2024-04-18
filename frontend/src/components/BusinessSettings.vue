<template>
  <div>
    <Navbar />
  </div>
  <div>
    <CreateBusiness />
  </div>
</template>

<script>
import Navbar from './Navbar.vue'
import CreateBusiness from './CreateBusiness.vue'

export default {
  components: {
    Navbar,
    CreateBusiness
  }
}
</script>
