<script>
	import * as _ from 'lamb';

	import ChevronLeft from '@svizzle/ui/src/icons/feather/ChevronLeft.svelte';
	import ChevronRight from '@svizzle/ui/src/icons/feather/ChevronRight.svelte';
	import Icon from '@svizzle/ui/src/icons/Icon.svelte';
	import Link from '@svizzle/ui/src/Link.svelte';
	import LinkButton from '@svizzle/ui/src/LinkButton.svelte';
	import ResponsiveFlex from '@svizzle/ui/src/ResponsiveFlex.svelte';
	import {_screen} from '@svizzle/ui/src/sensors/screen/ScreenSensor.svelte';
	import {isNotNil} from '@svizzle/utils';

	import {page as _page} from '$app/stores';
	import theme from '$lib/theme';

	const segments = ['app', 'indicators', 'a11ymenu'];
	const titles = {
		app:'App',
		indicators: 'Indicators',
		a11ymenu: 'Accessibility menu',
	};


	$: [,,segment] = $_page.url.pathname.split('/');
	$: currentValueIndex = _.findIndex(segments, _.is(segment));
	$: prevSegment = segments[currentValueIndex - 1];
	$: nextSegment = segments[currentValueIndex + 1];
	$: hasPrevSegment = isNotNil(prevSegment);
	$: hasNextSegment = isNotNil(nextSegment);
</script>

<main class={$_screen?.classes}>
	<section>
		<h1>Guides</h1>
		<menu class='tabs'>
			{#if $_screen?.sizes?.medium}
				<ul>
					{#each segments as id}
						<li
							class:selected={segment === id}
						>
							<Link
								href='/guides/{id}'
								theme={{
									color: segment === id ? 'white' : theme.colorLink,
								}}
							>
								<span>
									{titles[id]}
								</span>
							</Link>
						</li>
					{/each}
				</ul>
			{:else}
				<div class='tab-selector'>
					<label for=''>
						{titles[segment]}
					</label>

					<div>
						<Link
							href={hasPrevSegment && `/guides/${prevSegment}`}
							theme={{
								color: hasPrevSegment ? theme.colorLink : 'gray',
							}}
						>
							<Icon glyph={ChevronLeft} />
						</Link>
					</div>
					<div>
						<Link
							href={hasNextSegment && `/guides/${nextSegment}`}
							theme={{
								color: hasNextSegment ? theme.colorLink : 'gray',
							}}
						>
							<Icon glyph={ChevronRight} />
						</Link>
					</div>
				</div>
			{/if}
		</menu>
		<div>
			<slot />

			<ResponsiveFlex>
				<LinkButton
					href='/accessibility'
					text='Read the accessibility statement'
					theme={{backgroundColor: theme.colorLink}}
				/>
				<LinkButton
					href='/indicators'
					text='Explore the indicators'
					theme={{backgroundColor: theme.colorLink}}
				/>
			</ResponsiveFlex>
		</div>
	</section>
</main>

<style>
	main {
		background-color: var(--color-background);
		display: flex;
		font-weight: 200;
		height: 100%;
		justify-content: space-around;
		width: 100%;
	}

	section {
		background-color: white;
		display: grid;
		max-width: 900px;
		overflow-y: auto;
		padding: 2rem;
		width: 100%;
	}

	.small section {
		grid-template-areas: 'header' 'slot' 'menu';
		grid-template-rows: auto 1fr auto;
	}

	.medium section {
		grid-template-areas: 'header' 'menu' 'slot';
		grid-template-rows: auto auto 1fr;
	}

	div {
		background-color: white;
		max-width: 900px;
		overflow-y: auto;
	}

	h1 {
		font-weight: bold;
		grid-area: header;
	}

	ul {
		list-style: initial;
		margin-left: 20px;
	}

	.tabs {
		user-select: none;
		grid-area: menu;
	}

	.small .tabs {
		margin-top: 2rem;
	}
	.medium .tabs {
		margin-top: 0;
	}
	.tabs ul {
		display: flex;
		flex-direction: row;
		justify-content: center;
		list-style-type: none;
		margin: 3rem 0 1rem 0;
	}
	.tab-selector label{
		display: block;
		padding: 0.5em 1em;
	}
	.tab-selector div {
		padding: 0.5em 0.5em;
		border-left: thin solid var(--color-main);
	}
	.tabs li {
		border-bottom: thin solid var(--color-main);
		border-top: thin solid var(--color-main);
		border-right: thin solid var(--color-main);
	}
	.tabs li:first-child {
		border-left: thin solid var(--color-main);
	}
	.tabs li.selected {
		background: var(--color-main);
	}

	.tabs li span {
		display: block;
		padding: 0.5em 1em;
	}

	.tabs .tab-selector {
		border: thin solid var(--color-main);
		display: grid;
		grid-template-columns: 1fr min-content min-content;
	}
	.spinner {
		display: inline-block !important;
		margin-left: 1em;
		height: 1rem;
		width: 1rem;
	}
</style>
