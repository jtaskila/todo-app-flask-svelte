<script>
    import { createEventDispatcher } from 'svelte'
    import ApiCall from '../api/api.js'
    import UserState from '../stores/userstate.js'

    const dispatch = createEventDispatcher()

    let loading = false
    let loadingClass = ''
    let todoDescription = ''

    function addTodo(){
        if(todoDescription == ''){
            return 
        }

        loading = true
        loadingClass = 'loading'

        ApiCall('/todos',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'apikey': $UserState.apikey
            },
            body: JSON.stringify({
                todo: todoDescription
            })
        }, onSuccess, onFailure)

        function onSuccess(response){
            loading = false
            loadingClass = ''
            todoDescription = ''
            dispatch('newTodo')
        }

        function onFailure(error){
            loading = false
            loadingClass = ''
        }
    }
</script>

<div class="AddTodoDialogContainer">
    <h3>Add new todo</h3>
    <form class="ui form" on:submit|preventDefault={addTodo}>
        <div class="field">
            <label for="todo">Todo description</label>
            <textarea id="todo" name="todo" disabled={loading} bind:value={todoDescription}></textarea>
        </div>
        <button type="submit" class="ui button {loadingClass}" disabled={loading}>Save todo</button>
    </form>
</div>
