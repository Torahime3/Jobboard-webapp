<script>
    import JobAdvertisement from './components/JobAdvertisements.svelte';

    async function fetchJobs(){

        const response = await fetch("localhost:8000/companies")
        const result = response.json();
        console.log(result);

    }

</script>

<main>

    <h1>Offres d'emploi</h1>
    <JobAdvertisement number="42"/>
    <JobAdvertisement />
    <JobAdvertisement />

    <button on:click=>Charger les offres</button>

</main>

<style>

    button{
        padding: 5px 15px;
        margin: 15px;
    }


</style>
