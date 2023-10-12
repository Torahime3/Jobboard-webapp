<script>
    import { Router, Route, Link } from "svelte-routing";
    import Index from "../routes/Home.svelte";
    import Login from "../routes/Login.svelte";

    export let url = "";

</script>


<main>

    <Router url="{url}">
        <nav>
            <Link to="/accueil">Home</Link>
            <Link to="login">Login</Link>
        </nav>
        <div>
            <Route path="/accueil"> <Index /> </Route>
            <Route path="login"> <Login /> </Route>
        </div>
    </Router>

</main>

<style>

    header{
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .box{
            padding: 10px;
            margin: 15px;
            border: 3px solid black;
            border-radius: 5px;
        }

    button{
        padding: 5px 15px;
        margin: 15px;
    }

</style>