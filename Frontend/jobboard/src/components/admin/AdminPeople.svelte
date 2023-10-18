<script>

    import { deletePeople } from "../../stores/admin/peoples/deletepeople.js";
    import { updatePeople } from "../../stores/admin/peoples/updatepeople.js";

    export let people;
    export let token;
    export let isEditing = false;
    
    let updatedPeople = {
        "id": people.id,
        "firstname": people.firstname,
        "lastname": people.lastname,
        "date_of_birth": people.date_of_birth,
        "phone_number": people.phone_number,
        "email": people.email,
        "domain": people.domain,
        "role": people.role,
        "id_company": people.id_company == null ? "" : people.id_company,
    }

    async function toggleEditing() {
        isEditing = !isEditing;
        if(!isEditing){
            console.log(await updatePeople(token, updatedPeople));
        }
    }

    function Delete(token, id){
        console.log(deletePeople(token, id));
    }

</script>

<main>

    <div class="container">
        <div class="row">
            <p>{people.id}</p>
            {#if isEditing}
                <input type="text" bind:value={updatedPeople.firstname} />
                <input type="text" bind:value={updatedPeople.lastname} />
                <input type="text" bind:value={updatedPeople.date_of_birth} />
                <input type="text" bind:value={updatedPeople.phone_number} />
                <input type="text" bind:value={updatedPeople.email} />
                <input type="text" bind:value={updatedPeople.domain} />
                <input type="text" bind:value={updatedPeople.role} />
                <input type="text" bind:value={updatedPeople.id_company} />
            {:else}
                <p>{updatedPeople.firstname}</p>
                <p>{updatedPeople.lastname}</p>
                <p>{updatedPeople.date_of_birth}</p>
                <p>{updatedPeople.phone_number}</p>
                <p>{updatedPeople.email}</p>
                <p>{updatedPeople.domain}</p>
                <p>{updatedPeople.role}</p>
                <p>{updatedPeople.id_company}</p>
            {/if}

            <button class="edit" on:click={toggleEditing}><img src="/src/assets/stylo.png" alt="something"></button>
            <button class="delete" on:click={Delete(token, people.id)}><img src="/src/assets/corbeille.png" alt="something"></button>
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

.description{
    overflow-y: scroll;
    grid-column-start: 3;
    grid-column-end: 5;
}

.row{
    display: grid;
    grid-template-columns: repeat(9, 1fr) repeat(2, 0.3fr);
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