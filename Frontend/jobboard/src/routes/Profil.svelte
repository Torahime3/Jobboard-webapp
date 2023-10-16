<script>
    import Cookies from 'js-cookie';
    import { getUserData } from '../stores/getuserdata.js';
    import JobApplications from '../components/JobApplications.svelte';

    function disconnect(){
        Cookies.remove('userToken');
        window.location.href = '/';
    }


    async function getInfos(){
        if(!Cookies.get('userToken')){
            window.location.href = '/';
        } else {
            let promise = await getUserData(Cookies.get('userToken'));
            return promise;
        }
    }
    

</script>

<main>
    
    <div class="container_profil box">
        <h3 class="title">My Profile</h3>
        {#await getInfos()}
            <p>Loading...</p>
        {:then data}
        <div class="myprofil">
            <div class="img">
                <img src="https://picsum.photos/200" alt="something">
            </div>
            <div class="infos">
                <p><strong>First name:</strong> {data.firstname}</p>
                <p><strong>Last name:</strong> {data.lastname}</p>
                <p><strong>Email:</strong> {data.email}</p>
                <p><strong>Phone number:</strong> {data.phone_number}</p>
                <p><strong>Date of birth:</strong> {data.date_of_birth}</p>
                <p><strong>Domain:</strong> {data.domain}</p>
                {#if data.id_company}
                    <p><strong>Company :</strong> {data.company_name}</p>
                {/if}
                <button class="disconnect" on:click={disconnect}>Disconnect</button>
            </div>
        </div>

        {:catch error}
            <p>Error loading data</p>
        {/await}
        
    </div>
<!-- 
    <div class="container_companyapplications box">
        <h3>Company's job applications</h3>
        <button> Create </button>
    </div> -->

    <div class="container_myapplications box">
        <h3 class="title">My job applications</h3>
        <JobApplications />
    </div>
</main>


<style>

    .disconnect{
        border: none;
        border-radius: 5px;
        padding: 10px;
        color: red;
        background-color: rgb(255, 234, 234);
        cursor: pointer;
    }

    .disconnect:hover{
        background-color: rgb(255, 214, 214);
    }

    .myprofil{
        display: flex;
    }

    .infos{
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 10px;
        margin-left: 10px;
    }

    .title{
        border-bottom: 2px solid black;
        padding-bottom: 10px;
        margin-bottom: 10px;
    }

    .img{
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    img{
        border-radius: 10px;
    }

    .box{
        padding: 10px;
        margin: 15px;
        border-radius: 10px;
        background-color: white;
        border: 3px solid rgb(236, 236, 236);
    }

    @media screen and (min-width: 768px) {
        main{
            display: grid;
            grid-template-columns: 1fr 1fr;
        }

        .container_profil{
            grid-row-start: 1;
            grid-row-end: 3;
        }
    }

</style>