<script lang="ts">
    import Vditor from "vditor";
    import "~vditor/src/assets/scss/index.scss";

    let mdeditor: HTMLDivElement;

    function init(node: HTMLDivElement) {
        const vditor = new Vditor(node, {
            cache: {
                id: "vditor",
            },
            icon: "material",
            preview: {
                hljs: {
                    lineNumber: true
                }
            }
        });
    }
</script>
<div class="gallery-curve-wrapper">
    <div style="margin-top: 184px; padding: 40px; min-height: 613px; display: block;" class="gallery-body">
        <div use:init />
    </div>
    
</div>


<svelte:head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/vditor/dist/index.css" />
</svelte:head>
