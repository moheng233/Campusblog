<script lang="ts">
    import { link } from 'svelte-spa-router/Router.svelte';

    import {fade} from 'svelte/transition'

    export let id: number;

    export let title: string = "标题";
    export let post_user: string = "我";
    export let created_at: string = "今天";
    export let subtitle: string = "";
    export let subimage: string = "//cdn.shopify.com/s/files/1/2030/2737/articles/sintel-bamboo.jpg?v=1503530930";


    export let content_visible: boolean = false;

    function openContent(){
        content_visible = true;
    }
</script>

<div class="featured-product-wrapper container" in:fade="{{ delay: 100 }}">
    <div class="gallery row">
        <div class="col s12 m6">
            <div class="product-description">
                <h2 style="white-space: nowrap;text-overflow: ellipsis;overflow: hidden;">{title}</h2>
                <p class="blog-author">
                    由{post_user}发布在
                    <time datetime="">{created_at}</time>
                </p>
                <div class="rte" style="max-width: 400px;word-break:break-all;">
                    <meta charset="utf-8" /><span>{subtitle}</span>
                </div>
            </div>
        </div>
        <div
            class="col s12 m8 l6 gallery-item gallery-expand gallery-filter gallery-fillscreen registered">
            <div class="placeholder">
                <!-- svelte-ignore a11y-missing-attribute -->
                <div class="gallery-curve-wrapper">
                    <a class="gallery-cover gray" href="/blog/{id}" use:link>
                        <img
                            class="responsive-img"
                            src="{subimage}" />
                        <div class="gradient" style="" /></a>
                    <div class="gallery-header">
                        <span>{title}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
