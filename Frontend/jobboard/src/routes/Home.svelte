<script>
import Advertisements from "../components/JobAdvertisements.svelte";
import { getJobsAdvertisements } from "../stores/jobAdvertisements";

let promise = getJobsAdvertisements();

function refresh(){
    promise = getJobsAdvertisements();
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