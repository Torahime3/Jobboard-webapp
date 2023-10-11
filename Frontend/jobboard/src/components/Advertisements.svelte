<script>
    export let job;

    async function getJob(){
        const response = await fetch('http://127.0.0.1:8000/jobadvertisements/'+job.id)
        const result = await response.json()
        return result;
    }

    // function testAlert(){
    //     alert("test")
    // }
</script>

<main>

    <div class="container">
        <h3>{job.id} - {job.title} </h3>
        <span>Entreprise : {job.id_company}</span><br>
        <span>Location : {job.location}</span><br><br>
        <div>
            <details on:toggle|once={getJob}>
                <summary>Plus d'informations</summary>
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