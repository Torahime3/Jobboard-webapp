<script>
    import JobAdvertisement from './components/JobAdvertisements.svelte';

    async function fetchJobs(){

        const response = await fetch("http://127.0.0.1:8000/companies/");
        const result = await response.json();
        console.log(result);
    }
fetchJobs();

</script>

<main>
<!--    <h1>Offres d'emploi</h1>-->
<!--    <JobAdvertisement number="42"/>-->
<!--&lt;!&ndash;    <JobAdvertisement />&ndash;&gt;-->
<!--&lt;!&ndash;    <JobAdvertisement />&ndash;&gt;-->

    <!--{#await fetchJobs()}-->
    <!--    <p> ... waiting </p>-->
    <!--{:then data}-->
    <!--    <p>{data.name}</p>-->
    <!--{:catch error}-->
    <!--    <p> {error.message} </p>-->
    <!--{/await}-->

</main>

<style>

    button{
        padding: 5px 15px;
        margin: 15px;
    }


</style>