import { writable } from 'svelte/store'

const UserState = writable({
    username: '',
    userid: '',
    loggedin: false,
    apikey: ''
})

export default UserState
