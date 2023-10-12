<script>
    export let job;

    let result;

    async function getJob(){
        const response = await fetch('http://127.0.0.1:8000/jobadvertisements/'+job.id)
        result = await response.json()
        console.log(result)
    }

</script>

<main>


    <div class="container">
        <h3>{job.contract_type} - {job.title} </h3>
        <span>Entreprise : {job.id_company}</span><br>
        <span>Location : {job.location}</span><br><br>
        <div>
            <details on:toggle|once={getJob}>
                <summary>Plus d'informations</summary>

                <div class="details container">

                    {#if result}    
                        <p>{result.description}</p>
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