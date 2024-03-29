<script>
	import {capitalize} from '@svizzle/utils';
	import Icon from '@svizzle/ui/src/icons/Icon.svelte';
	import Download from '@svizzle/ui/src/icons/feather/Download.svelte';
	import Info from '@svizzle/ui/src/icons/feather/Info.svelte';
	import Menu from '@svizzle/ui/src/icons/feather/Menu.svelte';
	import X from '@svizzle/ui/src/icons/feather/X.svelte';
	import A11yPerson from '@svizzle/ui/src/icons/svizzle/A11yPerson.svelte';
	import Link from '@svizzle/ui/src/Link.svelte';

	import theme from '$lib/theme';
	import {zipUrl} from '$lib/utils/assets';
	import {isServerSide} from '$lib/env';
	import {version} from '$lib/utils/version';

	const changelogUrl = 'https://github.com/nestauk/eurito_indicators/blob/staging/CHANGELOG.md';

	// `_screen` shape at https://github.com/nestauk/svizzle/tree/dev/packages/components/ui/src/gauges/screen#screen-store
	export let _screen;
	export let contentHeight;
	export let segment;
	export let showA11yMenu = false;
	export let isA11yDirty = false;

	let showMenu = false;

	const closeMenu = () => showMenu = false;
	const toggleA11yMenu = event => {
		showA11yMenu = !showA11yMenu;
		event.target.setAttribute('aria-expanded', showA11yMenu.toString());
	}
	const toggleMenu = event => {
		showMenu = !showMenu;
		event.target.setAttribute('aria-expanded', showMenu.toString());
	}

	$: makeColor = id => segment === id ? theme.colorLink : undefined;
</script>

<nav
	class={$_screen?.classes}
	style='--content-height: {contentHeight}px'
	role='none'
>
	{#if isServerSide || !$_screen?.sizes.medium}
		<header>
			{segment ? capitalize(segment) : 'Home'}
		</header>
		{#if !$_screen?.sizes.medium}
			<button
				aria-label='Accessibility settings'
				class='clickable'
				on:click={toggleA11yMenu}
			>
				<Icon
					glyph={A11yPerson}
					stroke={isA11yDirty ? 'white' : 'black'}
					strokeWidth=1
					fill={isA11yDirty ? 'black' : ''}
				/>
			</button>
		{/if}
		<button
			aria-label='Website links'
			class='clickable'
			on:click={toggleMenu}
		>
			{#if showMenu}
				<Icon glyph={X} />
			{:else}
				<Icon glyph={Menu} />
			{/if}
		</button>
	{/if}
	{#if !$_screen?.sizes.medium && showMenu || $_screen?.sizes.medium}
		<menu on:click={closeMenu}>
			<div role='none'>
				<ul role='none'>
					<li
						class:selected='{segment === undefined}'
						role='none'
					>
						<Link
							href='/'
							theme={{color: makeColor('')}}
						>
							Home
						</Link>
					</li>
					<li
						class:selected='{segment === 'methodology'}'
						role='none'
					>
						<Link
							href='/methodology'
							theme={{color: makeColor('methodology')}}
						>
							Methodology
						</Link>
					</li>
					<li
						class:selected='{segment === 'guides'}'
						role='none'
					>
						<Link
							href='/guides'
							theme={{color: makeColor('guides')}}
						>
							Guides
						</Link>
					</li>
					<li
						class:selected='{segment === 'accessibility'}'
						role='none'
					>
						<Link
							href='/accessibility'
							theme={{color: makeColor('accessibility')}}
						>
							Accessibility
						</Link>
					</li>
					<li
						class:selected='{segment === 'indicators'}'
						role='none'
					>
						<Link
							href='/indicators'
							rel='prefetch'
							theme={{color: makeColor('indicators')}}
						>
							Indicators
						</Link>
					</li>
				</ul>
			</div>
			<div role='none'>
				<ul role='none'>
					<li role='none'>
						<Link
							download
							href={zipUrl}
						>
							Download
							<Icon
								glyph={Download}
								size=20
								strokeWidth=1.5
							/>
						</Link>
					</li>
					<li
						class:selected='{segment === 'info'}'
						role='none'
					>
						<Link
							href='/info'
							rel='prefetch'
							theme={{color: makeColor('info')}}
						>
							Info
							<Icon
								glyph={Info}
								size=20
								strokeWidth=1.5
							/>
						</Link>
					</li>
					<li
						aria-label='Source code repository'
						role='none'
					>
						<Link
							href={changelogUrl}
							type='external'
							theme={{
								color: 'black',
								iconStroke: theme.colorMain
							}}
						>
							{version}
						</Link>
					</li>
					{#if $_screen?.sizes.medium}
						<li role='none'>
							<button
								aria-label='Accessibility settings'
								on:click={toggleA11yMenu}
								class='clickable'
							>
								<Icon
									glyph={A11yPerson}
									stroke={isA11yDirty ? 'white' : 'black'}
									strokeWidth=1
									fill={isA11yDirty ? 'black' : ''}
								/>
							</button>
						</li>
					{/if}
				</ul>
			</div>
		</menu>
	{/if}
</nav>

<style>
	nav, menu {
		align-items: center;
		display: flex;
		height: 100%;
		width: 100%;
		z-index: var(--z-1000);
	}
	nav {
		gap: 12px;
		justify-content: end; /* Align to the right on Firefox */
		justify-content: flex-end; /* Align to the right on Chrome */
		position: relative;
	}
	header {
		color: var(--color-link);
		font-weight: bold;
		margin: 0 auto;
		position: absolute;
		text-align: center;
		width: 100%;
	}
	div {
		z-index: var(--z-1000);
	}
	menu {
		background: white;
		flex-direction: column-reverse;
		height: var(--content-height);
		justify-content: space-evenly;
		left: 0;
		position: fixed;
		top: 0;
		width: 100%;
	}
	.medium menu {
		flex-direction: row;
		height: 100%;
		justify-content: space-between;
		position: unset;
	}
	ul {
		align-items: center;
		display: flex;
		flex-direction: column-reverse;
		margin: 0;
		padding: 0;
	}
	.medium ul {
		flex-direction: row;
	}
	li {
		height: 100%;
		display: block;
		float: left;
		margin-right: 0.5rem;
		padding: 1em 0.5em;
		white-space: nowrap;
	}
	.medium li.selected {
		color: var(--color-link);
		display: inline-block;
		position: relative;
	}
	li {
		display: block;
		float: none;
		margin-right: 0;
		padding: 1.5em 0.5em;
	}
	.medium li {
		padding: 0 0.5em;
	}
	button {
		border: none;
		background: transparent;
		width: min-content;
		height: min-content;
		z-index: var(--z-1000);
	}
</style>
