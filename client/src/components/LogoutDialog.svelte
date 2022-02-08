<script>
    import ApiCall from '../api/api.js'
    import UserState from '../stores/userstate.js'

    let loadingClass = ''
    let loading = false

    function logout(){
        loadingClass = 'loading'
        loading = true

        ApiCall("/login", {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'apikey': $UserState.apikey
            }
        }, logoutSuccess, logoutFailure)

        function logoutSuccess(response){
            console.log("Logout succesfull")
            console.log(response.status)
            console.log(response.data)

            UserState.update(current => {
                current.loggedin = false
                current.apikey = ''
                return current
            })
        }

        function logoutFailure(error){
            console.log("Logout failed")
            alert("Logging out failed! Please try again")
        }
    }
</script>

<div class="logoutButtonContainer">
    {#if $UserState.loggedin}
        <button class="ui button {loadingClass}" disabled={loading} on:click={logout}>Logout</button>
    {:else}
        <button class="ui button">Login</button>
        <i>Todo: route to login page when clicked</i>
    {/if}
</div>
