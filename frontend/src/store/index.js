import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    default_currency: "RUB",
    table: {},
  },
  mutations: {
    SET_TABLE_STATE(state, data) {
      state.table = data;
    },
    SET_SAVING_VALUE(state, { value, id }) {
      state.table.data.forEach((date) => {
        date.savings.forEach((saving) => {
          if (saving.id == id) {
            saving.amount = value;
          }
        });
      });
    },
  },
  actions: {
    async getTableData({ commit }) {
      axios
        .get("http://127.0.0.1:8000/table", {
          headers: {
            Authorization:
              "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTIyNTIyNjMsInN1YiI6IjEifQ.jPsvwN0dJwGELzmwBz6SgjikRYYv4pHPUam4X0majAc",
          },
        })
        .then((response) => {
          commit("SET_TABLE_STATE", response.data);
        });
    },
    set_saving_value({ commit }, payload) {
      commit("SET_SAVING_VALUE", payload);
    },
  },
  modules: {},
});
