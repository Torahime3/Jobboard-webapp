<script>

    import Cookies from 'js-cookie';
    import { createJobAdvertisement } from '../../stores/admin/jobadvertisements/createjobadvertisements';
    import { getUserData } from '../../stores/getuserdata';

    let jobadvertisement = {
        title: "",
        job_domain: "",
        description: "",
        location: "",
        contract_type: "",
        duration_week: "",
        id_company: "",
        id_people: "",
    }
    
    let recruiter;
    let token = Cookies.get('userToken');
    getUserData(token).then(data => {
        if(data.role === 'Recruiter'){
            recruiter = true;
            jobadvertisement.id_people = data.id;
            jobadvertisement.id_company = data.id_company;
        }
    })

let result;
async function submit(){
    event.preventDefault();
    result = await createJobAdvertisement(Cookies.get('userToken'), jobadvertisement);
    if(result.message === "success"){
        if(recruiter){
            window.location.href = '/profil';
        } else {
            window.location.href = '/admin';
        }
    }
}

</script>

<main>

    <div class="container applying">
        <h2>
            <h3>Create Job Advertisement</h3>

            <form method="POST" action="">
                <div class="input">
                    <label for="title">Titre</label><br>
                    <input type="text" bind:value={jobadvertisement.title} id="title" placeholder="title">
                </div>
                <div class="input">
                    <label for="job_domain">Job Domain</label><br>
                    <input type="text" bind:value={jobadvertisement.job_domain} id="job_domain" placeholder="job_domain">
                </div>

                <div class="input">
                    <label for="description">Description</label><br>
                    <input type="text" bind:value={jobadvertisement.description} id="description" placeholder="description">
                </div>
                
                <div class="input">
                    <label for="location">Location</label><br>
                    <input type="text" bind:value={jobadvertisement.location} id="location" placeholder="location">
                </div>

                <div class="input">
                    <label for="contract_type">Contract Type</label><br>
                    <input type="text" bind:value={jobadvertisement.contract_type} id="contract_type" placeholder="contract_type">
                </div>

                <div class="input">
                    <label for="duration_week">Duration Week</label><br>
                    <input type="text" bind:value={jobadvertisement.duration_week} id="duration_week" placeholder="duration_week">
                </div>


                {#if !recruiter}
                <div class="input">
                    <label for="id_company">ID Company</label><br>
                    <input type="text" bind:value={jobadvertisement.id_company} id="id_company" placeholder="id_company">
                </div>

                <div class="input">
                    <label for="id_people">ID People</label><br>
                    <input type="text" bind:value={jobadvertisement.id_people} id="id_people" placeholder="id_people">
                </div>
                {/if}


                <div class="input">
                    <button on:click={submit}>Submit </button>
                </div>
            </form> 

             {#if result}
                {#if result.message === 'error'}
                <p class="status error">An error occured!</p>
                {/if}
            {/if}

        </h2>
    </div>
    


</main>

<style>

    form{
        margin-top: 20px;
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    input{
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        background-color: rgb(249, 238, 255);
    }

    button{
        padding: 10px 20px;
        margin: 5px;
        border-radius: 10px;
        border: none
    }

    button:hover{
        cursor: pointer;
        background-color: rgb(220, 220, 220);
    }

    .container{
        padding: 10px;
        margin: 15px;
        border-radius: 10px;
        background-color: white;
        border: 3px solid rgb(236, 236, 236);
    }

    h3{
        font-size: 20px;
    }

    span, label, p{
        font-size: 16px;
    }

    .status{
        color: white;
        width: fit-content;
        margin-top: 10px;
        padding: 10px;
        border-radius: 10px;
    }

    .good{
        background-color: rgb(39, 199, 39);
    }

    .error{
        background-color: rgb(207, 71, 71);
    }

</style>