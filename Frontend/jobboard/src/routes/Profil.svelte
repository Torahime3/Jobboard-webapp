<script>
    import Cookies from 'js-cookie';

    function disconnect(){
        Cookies.remove('userToken');
        window.location.href = '/';
    }

    if(!Cookies.get('userToken')){
        window.location.href = '/';
    }

</script>

<main>
    
    <div class="container_profil box">
        <button class="disconnect" on:click={disconnect}>Déconnexion</button>
        <h3>My Profil</h3>
        <img src="https://picsum.photos/200" alt="profil picture">
        <p>First name: </p>
        <p>Last name: </p>
        <p>Email: </p>
        <p>Phone number: </p>
        <p>Date of birth: </p>
        <p>Domain:</p>
        <p>Company</p>
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