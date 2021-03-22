import Vue from 'vue'
import Vuex from 'vuex'

import risks from '@/store/services/risks'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    risks
  }
})

export default store
