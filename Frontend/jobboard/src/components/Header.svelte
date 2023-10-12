<script>
    import { Router, Route, Link } from "svelte-routing";
    import Home from "../routes/Home.svelte";
    import Login from "../routes/Login.svelte";

    export let url = "";

</script>


<main>

    
    <Router url="{url}">
        <header class="box">
            <h2>Jobboard</h2>
            <nav>
                <button><Link to="/">Home</Link></button>
                <button><Link to="login">Login</Link></button>
            </nav>
        </header>
            <div>
                <Route path="/"> <Home /> </Route>
                <Route path="login"> <Login /> </Route>
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