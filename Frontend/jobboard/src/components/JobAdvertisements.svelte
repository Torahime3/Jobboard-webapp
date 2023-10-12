<script>
    import { getJobsAdvertisements } from "../stores/jobAdvertisements";

    export let job;

    let promise;

    async function getJobAdvertisement(){
        promise = await getJobsAdvertisements(job.id);
    }

</script>

<main>


    <div class="container">
        <h3>{job.contract_type} - {job.title} </h3>
        <span>Entreprise : {job.id_company}</span><br>
        <span>Location : {job.location}</span><br><br>
        <div>
            <details on:toggle|once={getJobAdvertisement}>
                <summary>Plus d'informations</summary>

                <div class="details container">

                    {#if promise}    
                        <p>{promise.description}</p>
                    {:else}
                        <p>Loading</p>
                    {/if}


                </div>
            </details>
        </div>
    </div>

</main>

<style>

    .container{
        padding: 10px;
        margin: 15px;
        border: 3px solid black;
        border-radius: 5px;
    }

</style>