<script>

    import Cookies from 'js-cookie';
    import { getJobsAdvertisements } from '../stores/jobadvertisements';
    import { createJobApplication } from '../stores/createjobapplications';
    import { getUserData } from '../stores/getuserdata';

    if(!Cookies.get('userToken')){
        window.location.href = '/';
    }

    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');

    async function getJobAdvertisement(){
        return await getJobsAdvertisements(id);
    }

    function getUser(){
        return getUserData(Cookies.get('userToken')).then(result => { return result})
    }

    let userData = getUser();
    userData.then(function(result) {
        apply_infos.id_user = result.id;
    })

    async function submit(){
        event.preventDefault();
        let result = createJobApplication(apply_infos);
        console.log(result)
    }


    let apply_infos = {
        id_user: "",
        id_advertisement: id,
        first_name: "",
        last_name: "",
        email: "",
        phone_number: "",
    }

</script>

<main>

    <div class="container applying">
        <h2>
            {#await getJobAdvertisement()}
            <p>Loading...</p>
            {:then data}
            <h3>Applying {data.contract_type} - {data.title} </h3>
            <span>Entreprise : {data.company_name}</span><br>

            <form method="POST" action="">
                <div class="input">
                    <label for="first_name">First Name</label><br>
                    <input type="text" bind:value={apply_infos.first_name} id="first_name" placeholder="First Name">
                </div>
                <div class="input">
                    <label for="last_name">Last Name</label><br>
                    <input type="text" bind:value={apply_infos.last_name} id="last_name" placeholder="Last Name">
                </div>

                <div class="input">
                    <label for="email">Email</label><br>
                    <input type="email" bind:value={apply_infos.email} id="email" placeholder="Email">
                </div>

                <div class="input">
                    <label for="phone">Phone number</label><br>
                    <input type="tel" bind:value={apply_infos.phone_number} id="phone" placeholder="Phone number">
                </div>

                <div class="input">
                    <button on:click={submit}>Submit </button>
                </div>
            </form>
            {/await}
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

    span, label{
        font-size: 16px;
    }

</style>