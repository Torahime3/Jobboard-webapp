<script>

    export let app;
    export let token;
    export let isEditing = false;

    import { updateJobAdvertisement } from '../../stores/admin/jobadvertisements/updatejobadvertisements.js';
    import { deleteJobAdvertisement } from '../../stores/admin/jobadvertisements/deletejobadvertisement.js';

    let updatedJobApplications = {
        "id": app.id,
        "firstname": app.firstname,
        "lastname": app.lastname,
        "email": app.email,
        "phone_number": app.phone_number,
        "id_avertisement": app.id_advertisement,
        "id_people": app.id_people,
        "date_of_application": app.date_of_application,
    }

    async function toggleEditing() {
        isEditing = !isEditing;
        // if(!isEditing){
        //     // console.log(updatedJobAdvertisements)
        //     console.log(await updateJobAdvertisement(token, updatedJobAdvertisements));
        // }
    }

    function Delete(token, id){
    console.log(deleteJobAdvertisement(token, id));
    }

</script>

<main>

    <div class="container">
        <div class="row">
            <p>{app.id}</p>
            <!-- {#if isEditing}

                <input type="text" bind:value={app.title} />
                <input type="text" bind:value={app.job_domain} />
                <input type="text" bind:value={app.description} />
                <input type="text" bind:value={app.date_of_jobadvertisements} />
                <input type="text" bind:value={app.location} />
                <input type="text" bind:value={app.contract_type} />
                <input type="text" bind:value={app.duration_week} />
                <input type="text" bind:value={app.id_company} />
                <input type="text" bind:value={app.id_people} />

            {:else} -->
                <p>{app.firstname}</p>
                <p>{app.lastname}</p>
                <p>{app.email}</p>
                <p>{app.phone_number}</p>
                <p>{app.id_advertisement}</p>
                <p>{app.id_people}</p>
                <p>{app.date_of_application}</p>

            <!-- {/if} -->
            <button class="edit" on:click={toggleEditing}><img src="/src/assets/stylo.png" alt="Edit"></button>
            <button class="delete" on:click={Delete(token, app.id)}><img src="/src/assets/corbeille.png" alt="Delete"></button>
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
    grid-template-columns: repeat(7, 1fr) repeat(2, 0.3fr);
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