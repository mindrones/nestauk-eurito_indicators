<script context="module">
	import {_screen} from '@svizzle/ui/src/sensors/screen/ScreenSensor.svelte';

	import a from './a.svelte';
	import code from './code.svelte';
	import h1 from './h1.svelte';
	import h2 from './h2.svelte';
	import h3 from './h3.svelte';
	import h4 from './h4.svelte';
	import p from './p.svelte';
	import ul from './ul.svelte';

	export {a, code, h1, h2, h3, h4, p, ul};
</script>

<section class={$_screen?.classes}>
	<slot />
</section>

<style>
	section {
		background-color: white;
		max-width: 900px;
		overflow-y: auto;
		padding: 0;
	}
</style>
