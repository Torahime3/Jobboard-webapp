<script>

    export let job;
    export let token;
    export let isEditing = false;

    import { updateJobAdvertisement } from '../../stores/admin/jobadvertisements/updatejobadvertisement.js';
    import { deleteJobAdvertisement } from '../../stores/admin/jobadvertisements/deletejobadvertisement.js';

    let updatedJobAdvertisements = {
        "id": job.id,
        "title": job.title,
        "job_domain": job.job_domain,
        "description": job.description,
        "date_of_jobadvertisements": job.date_of_jobadvertisements,
        "location": job.location,
        "contract_type": job.contract_type,
        "duration_week": job.duration_week,
        "id_company": job.id_company,
        "id_people": job.id_people,

    }

    async function toggleEditing() {
        isEditing = !isEditing;
        if(!isEditing){
            await updateJobAdvertisement(token, updatedJobAdvertisements);
        }
    }

    function Delete(token, id){
    deleteJobAdvertisement(token, id);
    }

</script>

<main>

    <div class="container">
        <div class="row">
            <p>{updatedJobAdvertisements.id}</p>
            {#if isEditing}

                <input type="text" bind:value={updatedJobAdvertisements.title} />
                <input type="text" bind:value={updatedJobAdvertisements.job_domain} />
                <input type="text" bind:value={updatedJobAdvertisements.description} />
                <input type="date" bind:value={updatedJobAdvertisements.date_of_jobadvertisements} />
                <input type="text" bind:value={updatedJobAdvertisements.location} />
                <input type="text" bind:value={updatedJobAdvertisements.contract_type} />
                <input type="text" bind:value={updatedJobAdvertisements.duration_week} />
                <input type="text" bind:value={updatedJobAdvertisements.id_company} />
                <input type="text" bind:value={updatedJobAdvertisements.id_people} />

            {:else}
                <p>{updatedJobAdvertisements.title}</p>
                <p>{updatedJobAdvertisements.job_domain}</p>
                <!-- <p class="description">{updatedJobAdvertisements.description}</p> -->
                <p>{updatedJobAdvertisements.date_of_jobadvertisements}</p>
                <p>{updatedJobAdvertisements.location}</p>
                <p>{updatedJobAdvertisements.contract_type}</p>
                <p>{updatedJobAdvertisements.duration_week}</p>
                <p>{updatedJobAdvertisements.id_company}</p>
                <p>{updatedJobAdvertisements.id_people}</p>
            {/if}
            <button class="edit" on:click={toggleEditing}><img src="/src/assets/stylo.png" alt="Edit"></button>
            <button class="delete" on:click={Delete(token, job.id)}><img src="/src/assets/corbeille.png" alt="Delete"></button>
         </div>
    </div>

</main>

<style>

@media screen and (max-width: 1024px){
    .row{
        overflow-x: scroll;
    }
}

.container{
    padding: 10px;
    margin: 15px;
    border-radius: 10px;
    background-color: #f1f1f1;
    border: 2px solid #f7f7f7;
}

.container:hover{
    background-color: #eaeaea;
}

  /* .description{
    overflow-y: ;
    height: 40px; 
}  */

.row{
    display: grid;
    gap: 10px;
    height: 60px;
}

img{
    width: 20px;
    filter: brightness(0) invert(1);
}

button{
    cursor: pointer;
    padding: 10px;
    margin: 5px;
    border-radius: 10px;
    background-color: white;
    /* box-shadow: 0px 3px 5px 0px rgba(0,0,0,0.15); */
    border: none;
    width: 55px;
}


.edit{
    background-color: rgb(118, 255, 182);
    border: 2px solid #f7f7f7;
    grid-column-start: 10;
}

.delete{
    background-color: rgb(255, 118, 118);
    border: 2px solid #f7f7f7;
    grid-column-start: 11;
}

.delete:hover{
    background-color: rgb(255, 148, 148);
}

.edit:hover{
    background-color: rgb(148, 255, 182);
}



</style>