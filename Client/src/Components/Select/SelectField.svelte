<script lang="ts">

    import { FormSelect } from 'materialize-css'

    export let selectList:{
        value: number,
        str: string
    }[] = [];


    const init = (el: HTMLDivElement) => {
        FormSelect.init(el);
    }
</script>

<!-- <div class="input-field col s12" use:init>
    <select>
        <option value="1">Option 1</option>
        <option value="2">Option 2</option>
        <option value="3">Option 3</option>
    </select>
    <label>Materialize Select</label>
</div> -->
