<script>
    import Cookies from 'js-cookie';
    import { getUserData } from '../stores/getuserdata.js';

    function disconnect(){
        Cookies.remove('userToken');
        window.location.href = '/';
    }

    // let promise;
    async function checkInfos(){
        if(!Cookies.get('userToken')){
            window.location.href = '/';
        } else {
            let promise = await getUserData(Cookies.get('userToken'));
            return promise;
        }
    }

    // checkInfos();
    

</script>

<main>
    
    <div class="container_profil box">
        <button class="disconnect" on:click={disconnect}>Déconnexion</button>
        <h3>My Profil</h3>
        {#await checkInfos()}
            <p>Loading...</p>
        {:then data}
            <img src="https://picsum.photos/200" alt="something">
            <p>First name: {data.firstname}</p>
            <p>Last name: {data.lastname}</p>
            <p>Email: {data.email}</p>
            <p>Phone number: {data.phone_number}</p>
            <p>Date of birth: {data.date_of_birth}</p>
            <p>Domain: {data.domain}</p>
            {#if data.id_company}
                <p>Company : {data.id_company}</p>
            {/if}
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
        <h3>My job applications</h3>
    </div>
</main>


<style>

    .disconnect{
        padding: 5px;
        color: red;
    }

    .box{
        padding: 10px;
        margin: 15px;
        border: 3px solid black;
        border-radius: 5px;
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