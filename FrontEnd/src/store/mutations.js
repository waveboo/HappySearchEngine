import * as types from './mutation-types'

export default {
  [types.UPDATE_SEARCHKEY] (state, key) {
    state.SearchKey = key;
  },
  [types.ADDIN_SEARCHKEY_LIST] (state, Element) {
    state.SearchList = state.SearchList.concat(Element);
  },
  [types.CLEAR_SEARCHKEY_LIST] (state) {
    state.SearchList = [];
  }
}
