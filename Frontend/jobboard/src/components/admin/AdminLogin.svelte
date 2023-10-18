<script>

    import { deleteLogin } from "../../stores/admin/login/deletelogin";
    import { updateLogin } from "../../stores/admin/login/updatelogin";

    export let login;
    export let token;
    export let isEditing = false;

    let updatedLogin = {
        "id": login.id,
        "username": login.username,
        "password": login.password,
        "email": login.email,
        "id_people": login.id_people,
    }

    async function toggleEditing() {
        isEditing = !isEditing;
        if(!isEditing){
            console.log(updatedLogin)
            console.log(await updateLogin(token, updatedLogin));
        }
    }

  function Delete(token, id){
    console.log(deleteLogin(token, id));
  }

</script>

<main>

    <div class="container">
        <div class="row">
            <p>{updatedLogin.id}</p>
            {#if isEditing}
            <input type="text" bind:value={updatedLogin.username} />
            <input type="text" bind:value={updatedLogin.password} />
            <input type="text" bind:value={updatedLogin.email} />
            <input type="text" bind:value={updatedLogin.id_people} />
            {:else}
                <p>{updatedLogin.username}</p>
                <p class="password">{updatedLogin.password}</p>
                <p>{updatedLogin.email}</p>
                <p>{updatedLogin.id_people}</p>
            {/if}
            <button class="edit" on:click={toggleEditing}><img src="/src/assets/stylo.png" alt="Edit"></button>
            <button class="delete" on:click={Delete(token, login.id)}><img src="/src/assets/corbeille.png" alt="Delete"></button>
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

.password{
    grid-column-start: 3;
    grid-column-end: 7;
}

.row{
    display: grid;
    grid-template-columns: repeat(8, 0.5fr) repeat(2, 0.3fr);
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