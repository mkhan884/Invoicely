import { createStore } from 'vuex'

const store = createStore({
  state: {
    isAuthenticated: false
  },
  mutations: {
    setAuthenticated(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated
    }
  }
})

export default store
