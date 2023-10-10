<script>

    let advertisement = {
        "title": "Coordinateur - Formateur de formations informatiques (H/F)",
        "description": "Vous rejoignez l'équipe de formation de la DSI d'Airbus",
        "date": "2020-10-10",
        "location": "Toulouse",
        "contract": "CDI",
        "duration": "undefined",
        "job-domain": "Informatique",
        "company": "Airbus",
    }

    export let number;

</script>

<main>

    <div class="container">
        <h3>{advertisement.title} - {number} </h3>
        <span>Entreprise : {advertisement.company}</span> - <span>Location : {advertisement.location}</span><br><br>
        <details>
            <summary>Infos supplémentaires</summary>
            <p>{advertisement.description}</p>
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