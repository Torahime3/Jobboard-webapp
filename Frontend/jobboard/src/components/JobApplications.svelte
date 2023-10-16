<script>

    export let app;
    console.log(typeof(app.id_advertisement))


</script>

<main>
    
    <div class="box">
        <div class="title">
        <h3>{app.contract_type} - {app.title} </h3>
        </div>
        <span>Company : {app.company_name}</span><br>
        <span>Location : {app.location}</span><br><br>
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