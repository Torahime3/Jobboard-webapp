<script>
    import { getPeoples } from "../stores/admin/peoples/getallpeoples";


    export let app;
    export let rhView = false;

</script>

<main>
    
    <div class="box">
        {#if !rhView}
        <div class="title">
        <h3>{app.jobA_contract_type} - {app.jobA_title} </h3>
        </div>
        <span>Company : {app.company_name}</span><br>
        <span>Location : {app.jobA_location}</span><br>
        <span>Date of Application : {app.date_of_application}</span><br><br>

        {:else}
        
        <div class="title">
        <h3>{app.contract_type} - {app.title} </h3>
        </div>
        <span>Location : {app.location}</span><br>
        <details>
            <summary>Appliers</summary>
            {#each app.peoples as people}
                <p class="appliers"><strong>Name</strong> : {people.firstname} {people.lastname} | <strong>Email</strong> : {people.email} | <strong>Phone</strong> : {people.phone_number}</p>
            {/each}
        </details>

        {/if}
        
    </div>

</main>

<style>

    .appliers{
        background-color: white;
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
    }

    .box{
        padding: 10px;
        margin: 15px;
        border-radius: 10px;
        background-color: #f1f1f1;
    }

</style>