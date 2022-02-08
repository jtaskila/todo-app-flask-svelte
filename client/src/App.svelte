<script>
	import LoginDialog from './components/LoginDialog.svelte'
	import LogoutDialog from './components/LogoutDialog.svelte'
	import AddTodoDialog from './components/AddTodoDialog.svelte'
	import TaskList from './components/TaskList.svelte'
	let taskList

	import { onDestroy } from 'svelte'
	import Loadbar from './components/Loadbar.svelte'
	import UserState from './stores/userstate.js'

	let loggedin = false

	// subbing to userstate so we can see if we're logged in
	const unsubUserState = UserState.subscribe(data => {
		loggedin = data.loggedin
	})
	onDestroy(() => {
		console.log("Destroy")
		unsubUserState()
	})


	function testLogin(){
		UserState.update(current => {
			current.loggedin = true
			return current
		})
	}

	function testLogout(){
		UserState.update(current => {
			current.loggedin = false
			return current
		})
	}

	function updateTaskList(){
		console.log("Trying to update...")
		taskList.updateTaskList()
	}

</script>

<main>
	<div class="ui container">
		<h1>The greatest todo app of all time</h1>
		<div class="ui divider"></div>
		{#if !loggedin}
			<LoginDialog />
		{:else}
			<LogoutDialog />
			<div class="ui divider"></div>
			<AddTodoDialog on:newTodo={updateTaskList} />
			<div class="ui divider"></div>
			<TaskList bind:this={taskList} />
		{/if}

	</div>
</main>

<style>

</style>
