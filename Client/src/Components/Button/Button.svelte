<script lang="ts">
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher<{
        "click": {};
    }>();

    export let size: "" | "smell" | "large" = "";
    export let href: "#" | string = "#";
    export let style: string = "";
</script>

<a class="btn-{size} waves-effect waves-light" {style} on:click={() => {dispatch("click", {});}}>
    <slot />
</a>
