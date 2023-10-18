<script>

    export let app;
    export let token;
    export let isEditing = false;

    import { updateJobApplications } from "../../stores/admin/jobapplications/updatejobapplication";
    import { deleteJobApplication } from "../../stores/admin/jobapplications/deletejobapplication";

    let updatedJobApplications = {
        "id": app.id,
        "firstname": app.firstname,
        "lastname": app.lastname,
        "email": app.email,
        "phone_number": app.phone_number,
        "id_advertisement": app.id_advertisement,
        "id_people": app.id_people,
        "date_of_application": app.date_of_application,
    }

    async function toggleEditing() {
        isEditing = !isEditing;
        if(!isEditing){
            console.log(updatedJobApplications)
            console.log(await updateJobApplications(token, updatedJobApplications));
        }
    }

    function Delete(token, id){
    
        console.log(deleteJobApplication(token, id));

    }

</script>

<main>

    <div class="container">
        <div class="row">
            <p>{app.id}</p>
            {#if isEditing}

                <input type="text" bind:value={updatedJobApplications.firstname} />
                <input type="text" bind:value={updatedJobApplications.lastname} />
                <input type="text" bind:value={updatedJobApplications.email} />
                <input type="text" bind:value={updatedJobApplications.phone_number} />
                <input type="text" bind:value={updatedJobApplications.id_advertisement} />
                <input type="text" bind:value={updatedJobApplications.id_people} />
                <input type="date" bind:value={updatedJobApplications.date_of_application} />

            {:else}
                <p>{updatedJobApplications.firstname}</p>
                <p>{updatedJobApplications.lastname}</p>
                <p>{updatedJobApplications.email}</p>
                <p>{updatedJobApplications.phone_number}</p>
                <p>{updatedJobApplications.id_advertisement}</p>
                <p>{updatedJobApplications.id_people}</p>
                <p>{updatedJobApplications.date_of_application}</p>

            {/if}
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