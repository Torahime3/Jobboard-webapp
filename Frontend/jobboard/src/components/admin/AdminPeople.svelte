<script>

    import { deletePeople } from "../../stores/admin/peoples/deletepeople.js";
    export let people;
    export let token;

    let isEditing = false;

    function toggleEditing() {
        isEditing = !isEditing;
    }

    function Delete(token, id){
        // console.log(token + " | " + id);
        console.log(deletePeople(token, id));
    }

</script>

<main>

    <div class="container">
        <div class="row">
            <p>{people.id}</p>
            {#if isEditing}
                <input type="text" value={people.firstname} />
                <input type="text" value={people.lastname} />
                <input type="text" value={people.date_of_birth} />
                <input type="text" value={people.phone_number} />
                <input type="text" value={people.email} />
                <input type="text" value={people.domain} />
                <input type="text" value={people.role} />
                <input type="text" value={people.id_company} />
            {:else}
                <p>{people.firstname}</p>
                <p>{people.lastname}</p>
                <p>{people.date_of_birth}</p>
                <p>{people.phone_number}</p>
                <p>{people.email}</p>
                <p>{people.domain}</p>
                <p>{people.role}</p>
                <p>{people.id_company}</p>
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