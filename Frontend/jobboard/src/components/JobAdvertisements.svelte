<script>
    import { getJobsAdvertisements } from "../stores/jobadvertisements";

    export let job;
    export let token;
    console.log(job)

    let promise;

    async function getJobAdvertisement(){
        promise = await getJobsAdvertisements(job.id);
    }

    function apply(){
        console.log('apply', job.id);
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

                <div class="details">

                    {#if promise}    
                        <p>{promise.description}</p>
                        {#if token}
                            <button class="postuler" on:click={apply}>Postuler</button>
                        {/if}
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

    button{
        padding: 10px 20px;
        margin: 5px;
    }

</style>