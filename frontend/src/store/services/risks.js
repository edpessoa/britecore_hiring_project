import axios from 'axios'

const state = {
  risks: []
}

const getters = {}

const mutations = {
  setRisks (state, risks) {
    state.risks = risks
  },
  setRisk (state, risk) {
    state.risk = risk
  }
}

const actions = {
  getRisksList (context) {
    return axios.get('/api/risks')
      .then(response => { context.commit('setRisks', response.data) })
      .catch(e => { console.log(e) })
  },
  getRisk (context, riskId) {
    return axios.get('/api/risks/' + riskId)
      .then(response => { context.commit('setRisk', response.data) })
      .catch(e => { console.log(e) })
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
