<script>

import JobAdvertisements from "../components/JobAdvertisements.svelte";

import { getJobsAdvertisements } from "../stores/jobadvertisements";
import Cookies from 'js-cookie';

const token = Cookies.get('userToken');
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
                <JobAdvertisements job={job} token={token} />
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
        border-radius: 15px;
        background-color: white;
        border: 3px solid rgb(236, 236, 236);
    }

    button{
        padding: 10px 15px;
        margin: 15px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
    }


</style>