<script>
    export let loading = 0
    let roundedLoading = 0

    $: {
        roundedLoading = Math.round(loading)
    }
</script>

<div class="loadbar">
    <div class="bar" style="width:{loading}%; height:20px; background:green;">
    </div>
</div>
<div class="bar-label">{roundedLoading}%</div>

<style>
    .loadbar{
        text-align:center;
        margin-top:1rem;
        border-radius:10px;
        box-shadow:0px 0px 5px 1px black;
    }

    .bar{
        border-radius:10px;

    }

    .bar-label{
        text-align:center;
        margin-bottom:1rem;
    }
</style>
