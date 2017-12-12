import * as types from './mutation-types'

export default {
  updateSearchkey({ commit }, key) {
    commit(types.UPDATE_SEARCHKEY, key)
  },
  AddinSearchList({ commit }, Element) {
    commit(types.ADDIN_SEARCHKEY_LIST, Element)
  },
  ClearSearchList({ commit }) {
    commit(types.CLEAR_SEARCHKEY_LIST)
  }
}
