<script>
    export let job;


    function alertTest(){
        alert("test")
    }

</script>

<main>

    <div class="container">
        <h3>{job.contract_type} - {job.title} </h3>
        <span>Entreprise : {job.id_company}</span><br>
        <span>Location : {job.location}</span><br><br>
        <div>
            <details>
                <summary on:keydown={alertTest}>Plus d'informations</summary>
                <div class="details container">
                <p>{job.description}</p>
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