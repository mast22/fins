import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    dafault_currency: "RUB",
    table: {},
  },
  mutations: {
    SET_TABLE_STATE(state, data) {
      state.table = data;
    },
  },
  actions: {
    async getTableData({ commit }) {
      axios
        .get("http://127.0.0.1:8000/table", {
          headers: {
            Authorization:
              "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTIxNjQyMDksInN1YiI6IjEifQ.Cd_9J1H9XFHFUaIecqN7X_Dl4KBJNHTQaQNJPqn5O4A",
          },
        })
        .then((response) => {
          commit("SET_TABLE_STATE", response.data);
        });
    },
  },
  modules: {},
});
