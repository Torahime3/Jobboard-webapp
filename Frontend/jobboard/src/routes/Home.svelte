<script>

import Advertisements from "../components/Advertisements.svelte";
import Header from "../components/Header.svelte"

let promise = getJobs();
    async function getJobs(){
        const response = await fetch('http://127.0.0.1:8000/jobadvertisements/')
        return await response.json();
    }

    function refresh(){
        promise = getJobs();
    }

</script>

<main>

    <div class="box">
        <h2>Offres d'emploi</h2>
        {#await promise}
            <p>Chargement des offres d'emploi...</p>
        {:then jobs}
            {#each jobs as job}
                <Advertisements {job} />
            {/each}
        {:catch error}
            <p>Impossible de charger les offres d'emploi</p>
        {/await}

        <button on:click={refresh}>Rafraichir</button>
    </div>

</main>

<style>

.box{
        padding: 10px;
        margin: 15px;
        border: 3px solid black;
        border-radius: 5px;
    }

    button{
        padding: 5px 15px;
        margin: 15px;
    }


</style>