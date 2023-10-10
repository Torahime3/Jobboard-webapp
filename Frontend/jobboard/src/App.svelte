<script>
    import JobAdvertisement from './components/JobAdvertisements.svelte';

	function bonjour() {
        alert('bonjour');
    }
</script>

<main>

    <h1>Offres d'emploi</h1>
    <JobAdvertisement number="42"/>
    <JobAdvertisement />
    <JobAdvertisement />

    <button on:click={bonjour}>Charger les offres</button>

</main>

<style>

    button{
        padding: 5px 15px;
        margin: 15px;
    }


</style>
