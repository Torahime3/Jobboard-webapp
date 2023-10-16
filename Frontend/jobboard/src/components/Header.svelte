<script>
    import Cookies from 'js-cookie';
    import { Router, Route, Link } from "svelte-routing";
    import { checkAdmin } from '../stores/checkadmin';

    import Home from "../routes/Home.svelte";
    import Login from "../routes/Login.svelte";
    import Profil from "../routes/Profil.svelte";
    import Apply from "../routes/Apply.svelte";
    import Admin from '../routes/Admin.svelte';

    export let url = "";
    const token = Cookies.get('userToken');

</script>


<main>

    
    <Router url="{url}">
        <header class="box">
            <h2>Jobboard</h2>
            <nav>
                {#await checkAdmin(token)}
                <p>Loading...</p>
                {:then data}
                    {#if data.message === 'success'}
                        <Link to="admin"><button style="background-color: #c884fa">Admin panel</button></Link>
                    {/if}
                {/await}

                <Link to="/"><button>Home</button></Link>

                {#if token}
                <Link to="profil"><button>Profile</button></Link>
                {:else}
                <Link to="login"><button>Login</button></Link>
                {/if}
            </nav>
        </header>
            <div>
                <Route path="/"> <Home /> </Route>
                <Route path="login"> <Login /> </Route>
                <Route path="profil"> <Profil /> </Route>
                <Route path="apply"> <Apply /> </Route>
                <Route path="admin"> <Admin /> </Route>
            </div>
    </Router>

</main>

<style>

    header{
        display: flex;
        justify-content: space-between;
        align-items: center;

    }

    .box{
        background-color: rgb(140, 0, 255);
        padding: 15px;
        color: white;
        }

    button{
        padding: 10px 20px;
        margin: 5px;
        border: none;
        border-radius: 10px;
    }

    button:hover{
        cursor: pointer;
        background-color: rgb(230, 230, 230);
    }

</style>