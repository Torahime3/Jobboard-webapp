<script>
    export let job;

</script>

<main>

    <div class="container">
        <h3>{job.name} </h3>
        <span>Entreprise : {job.description}</span><br><br>
        <details>
            <summary>Plus d'informations</summary>
            <p>{job.description}</p>
        </details>
    </div>

</main>

<style>

    .container{
        padding: 10px;
        margin: 15px;
        border: 3px solid black;
    }

</style>