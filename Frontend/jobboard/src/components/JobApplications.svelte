<script>

    export let app;

</script>

<main>
    
    <div class="box">
        <div class="title">
        <h3>{app.jobA_contract_type} - {app.jobA_title} </h3>
        </div>
        <span>Company : {app.company_name}</span><br>
        <span>Location : {app.jobA_location}</span><br>
        <span>Date of Application : {app.date_of_application}</span><br><br>
    </div>

</main>

<style>

    .box{
        padding: 10px;
        margin: 5px;
        border-radius: 10px;
        background-color: #f1f1f1;
    }

</style>