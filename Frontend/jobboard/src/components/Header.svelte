<script>
    import Cookies from 'js-cookie';
    import { Router, Route, Link } from "svelte-routing";

    import Home from "../routes/Home.svelte";
    import Login from "../routes/Login.svelte";
    import Profil from "../routes/Profil.svelte";
    import Apply from "../routes/Apply.svelte";

    export let url = "";
    const token = Cookies.get('userToken');

</script>


<main>

    
    <Router url="{url}">
        <header class="box">
            <h2>Jobboard</h2>
            <nav>
                <button><Link to="/">Home</Link></button>
                {#if token}
                    <button><Link to="profil">Profil</Link></button>
                {:else}
                    <button><Link to="login">Login</Link></button>
                {/if}
            </nav>
        </header>
            <div>
                <Route path="/"> <Home /> </Route>
                <Route path="login"> <Login /> </Route>
                <Route path="profil"> <Profil /> </Route>
                <Route path="apply"> <Apply /> </Route>
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
            padding: 10px;
            margin: 15px;
            border: 3px solid black;
            border-radius: 5px;
        }

    button{
        padding: 5px 15px;
        margin: 5px;
    }

</style>