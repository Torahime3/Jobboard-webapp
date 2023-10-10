<div class="container_companies">
    <h3>{company_info.name}</h3>
    <p>{company_info.description}</p>
    <p>{company_info.adress}</p>
</div>

{#if company_info.name === "Epitech"}
    <p>Je suis à Epitech</p>
{:else}
    <p>Je ne suis pas à Epitech</p>
{/if}

<script>

    let company_info = {
        "name": "Epitech",
        "description": "Le futur de l'informatique, le meilleur de l'innovation",
        "adress": "40 Boulevard de la Marquette",
        "city": "Toulouse",
    }

</script>