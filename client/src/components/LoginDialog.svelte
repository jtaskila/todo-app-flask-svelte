<script>
    import { api_url } from '../config.js'
    import ApiCall from '../api/api.js'
    import UserState from '../stores/userstate.js'

    let loading = false
    let loadingClass = ''

    let message = ''

    let username = 'Testimies'
    let password = 'asdasd'

    function login(){
        if(username == '' || password == ''){
            message = "Check the fields and try again!"
            return
        }
        loading = true
        loadingClass = 'loading'

        ApiCall('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name: username,
                    password: password
                })
            },
            loginSuccess,
            loginError,
            loginDone
        )

        function loginSuccess(response){
            if(response.status == 200){
                console.log("Login succesfull")
                console.log(response.status)
                console.log(response.data.apikey)

                UserState.update(current => {
                    current.loggedin = true
                    current.apikey = response.data.apikey
                    return current
                })
            }else{
                message = "User not found!"
            }
        }

        function loginError(error){
            alert("error")
        }

        function loginDone(){
            loading = false
            loadingClass = ''
        }
    }
</script>

<h1>Login</h1>
<form class="ui form" on:submit|preventDefault={login}>
    {#if message != ''}
        <div class="ui negative message">
            {message}
        </div>
    {/if}
    <div class="field">
        <label for="username">Username</label>
        <input id="username" type="text" placeholder="Username" disabled={loading} bind:value={username}>
    </div>

    <div class="field">
        <label for="password">Password</label>
        <input id="password" type="password" placeholder="Password" disabled={loading} bind:value={password}>
    </div>
    <button class="ui button {loadingClass}" type="submit" disabled={loading}>Login</button>
</form>
