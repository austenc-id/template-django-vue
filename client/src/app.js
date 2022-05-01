import { createApp } from 'vue'
import { createStore } from 'vuex'
import Index from './Index.vue'

const store = createStore({
    state(){
        return {
            active: {
                form: {
                    login: false,
                    register: false,
                },
                section: {
                    home: false,
                    profile: false,
                    settings: false,
                }

              }
        }
    },
    getters: {},
    mutations: {
        resetElements(state){

        },
        toggleElement(state, {group, element}){
            let elements = state.active[group]
            for (let key in elements){
                if (key != element){
                    state.active[group][key] = false
                }
                if (key === element){
                    elements[key] = !elements[key]
                }
            }
        }
    },
    actions: {},
})
const app = createApp(Index)

app.use(store)
app.mount('#app')
