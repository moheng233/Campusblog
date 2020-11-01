<script lang="ts">
    import { createEventDispatcher } from 'svelte'

    const dispatch = createEventDispatcher();

    export let size: '' | 'smell' | 'large' = '';
    export let href: '#' | string = '#';
    export let style: string = '';

    function click(){
        dispatch('click',{});
    };
</script>

<a class="btn-{size} waves-effect waves-light" {style} on:click={click}>
    <slot></slot>
</a>