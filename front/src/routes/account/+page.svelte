<script>
	import { page } from "$app/stores";
	import Login from "$lib/sign_in.svelte";
	import Signup from "$lib/sign_up.svelte";

	let currentTab = "Login";
	const isSignup = $page.url.searchParams.has("msg");
	const afterSignup = () => {
		currentTab = "Login";
	};
	const changeTab = (tab) => {
		currentTab = tab;
	};
	$: if (isSignup) afterSignup;
</script>

<section class="hero is-primary is-halfheight">
	<div class="hero-body">
		<main class="container mt-4">
			<div class="columns">
				<div class="box column is-4 is-offset-4">
					<div class="columns has-text-centered">
						<div
							class="column"
							class:has-text-link={currentTab === "Login"}
							on:click={() => changeTab("Login")}
						>
							<p>Login</p>
						</div>
						<div
							class="column"
							class:has-text-link={currentTab === "Signup"}
							on:click={() => changeTab("Signup")}
						>
							<p>Create Account</p>
						</div>
					</div>
					{#if currentTab === "Login"}
						<Login />
					{:else}
						<Signup />
					{/if}
				</div>
			</div>
		</main>
	</div>
</section>
