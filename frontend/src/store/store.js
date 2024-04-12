import { createStore } from 'vuex'

const store = createStore({
  state: {
    isAuthenticated: false,
    profileId: ''
  },
  mutations: {
    setAuthenticated(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated
    },
    setProfileId(state, profileId) {
      state.profileId = profileId
    }
  },
  getters: {
    getProfileId(state) {
      return state.profileId
    }
  }
})

export default store
