<script>
    import ApiCall from '../api/api.js'
    import UserState from '../stores/userstate.js'
    import {onMount} from 'svelte'
    import {fade} from 'svelte/transition'

    let todos = []
    let loading = false
    let message = ''

    onMount(() => {
        loading = true
        updateTaskList()
    })

    export function updateTaskList(){
        ApiCall('/todos', {
            method: 'GET',
            headers: {
                'apikey': $UserState.apikey
            }
        }, taskSuccess, taskFailure)
    }

    function taskSuccess(response){
        loading = false
        if(response.status == 404){
            message = "No tasks found!"
            return
        }

        if(response.status == 200){
            todos = response.data.data
            return
        }
    }

    function taskFailure(error){
        loading = false
        message = "No tasks found!"
    }

    function removeTodo(id){
        ApiCall('/todo/'+id, {
            method: 'DELETE',
            headers: {
                'apikey': $UserState.apikey
            }
        }, deleteSuccess, deleteFailure)

        function deleteSuccess(response){
            if(response.status == 200){
                updateTaskList()
            }
        }

        function deleteFailure(error){
        }
    }
</script>

<div class="TaskListContainer">
    {#if loading}
        <div class="ui active loader"></div>
    {/if}
    <table class="ui celled table">
        <thead>
            <tr>
                <th>#ID</th>
                <th>Task description</th>

                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {#each todos as todo}
                <tr>
                    <td>{todo.id}</td>
                    <td>{todo.todo}</td>

                    <td style="width:1%;">
                        <div style="white-space: nowrap;">
                            
                            <button class="ui button" on:click={() => {
                                removeTodo(todo.id)
                                }}>
                                Remove
                            </button>
                        </div>
                    </td>
                </tr>
            {/each}
        </tbody>
    </table>
    <p>{message}</p>
</div>
