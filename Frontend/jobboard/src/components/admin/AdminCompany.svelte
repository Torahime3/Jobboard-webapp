<script>

    export let company;

    let isEditing = false;

  function toggleEditing() {
    isEditing = !isEditing;
  }

</script>

<main>

    <div class="container">
        <div class="row">
            <p>{company.id}</p>
            {#if isEditing}
                <input type="text" value={company.name} />
                <input type="text" class="description" value={company.description} />
                <input type="text" value={company.address} />
                <input type="text" value={company.city} />
                <input type="text" value={company.zipcode} />
            {:else}
                <p>{company.name}</p>
                <p class="description">{company.description}</p>
                <p>{company.address}</p>
                <p>{company.city}</p>
                <p>{company.zipcode}</p>
            {/if}
            <button class="edit" on:click={toggleEditing}><img src="/src/assets/stylo.png" alt="Edit"></button>
            <button class="delete"><img src="/src/assets/corbeille.png" alt="Delete"></button>
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