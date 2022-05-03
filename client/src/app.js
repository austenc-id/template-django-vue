import { createApp } from "vue";
import { createStore } from "vuex";
import Cookies from "js-cookie";
import Index from "./Index.vue";

const store = createStore({
  state() {
    return {
      csrftoken: Cookies.get("csrftoken"),
      url: "http://127.0.0.1:8000",
      active: {
        form: {
          login: false,
          register: false,
        },
        section: {
          home: false,
          profile: false,
          settings: false,
        },
        user: false,
      },
      color: false,
    };
  },
  getters: {},
  mutations: {
    resetElements(state) {},
    toggleElement(state, { group, element }) {
      let elements = state.active[group];
      for (let key in elements) {
        if (key != element) {
          state.active[group][key] = false;
        }
        if (key === element) {
          elements[key] = !elements[key];
          console.log(state.active.user)
        }
      }
    },
    setActiveUser(state, { user }) {
      state.active.user = user;
    },
    toggleUserColor(state) {
        if (state.active.user){
            if (state.color) {
                console.log("setting default");
                document.getElementById("main").style.color = "#5c4646";
                state.color = false;
                return;
              }
              if (!state.color) {
                console.log("setting favorite");
                document.getElementById("main").style.color = state.active.user.color;
                state.color = true;
                return;
              }
        }
    },
  },
  actions: {},
});
const app = createApp(Index);

app.use(store);
app.mount("#app");
