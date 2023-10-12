<script>

    let register = false;

    function inverse(){
        register = !register;
    }

    // Form connexion
    let email = "";
    let password = "";

    let infoMessage;

    async function checkValidity(){
        event.preventDefault();

        if(email == "" || password == ""){
            infoMessage = "Veuillez remplir tous les champs"
            return;
        }

        const response = await fetch("http://localhost:8000/login/checkValidity", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "email": email,
                "password": password
            })
        });

        const result = await response.json();
        infoMessage = result.message === "success" ? "Vous êtes connectés" : "Email ou mot de passe incorrect";

    }

</script>

<main>

    <div class="container">

        {#if !register}
         <form action="#" method="post" name="connexion_form">

            <div class="container_connexion box">
                <h2 class="box">Connexion</h2>
                <div class="connexion_input">
                    <label for="email">Email</label>
                    <input type="email" bind:value={email} name="email" id="email" placeholder="Email" required>
                </div>

                <div class="connexion_input">
                    <label for="password">Password</label>
                    <input type="password" bind:value={password} name="password" id="password" placeholder="Password" required>
                </div>

                <div class="connexion_input">
                    <input type="submit" on:click={checkValidity}>
                </div>

                <p class="changeOption" on:click={inverse}>Didn't have an account?</p>
            </div>

        </form>

        {:else}
        <form name="connexion_form">

            <div class="container_connexion box">

                <h2 class="box">Register</h2>

                    <div class="connexion_input">
                        <label for="first_name">First name</label>
                        <input type="text" name="first_name" id="first_name" placeholder="First name" required>
                    </div>
        
                    <div class="connexion_input">
                        <label for="last_name">Last name</label>
                        <input type="text" name="last_name" id="last_name" placeholder="Last name" required>
                    </div>

                    <div class="connexion_input">
                        <label for="birthdate">Birth date</label>
                        <input type="date" name="birthdate" id="birthdate" placeholder="Birth date" required>
                    </div>

                    <div class="connexion_input">
                        <label for="email">Email</label>
                        <input type="email" name="email" id="email" placeholder="Email" required>
                    </div>

                    <div class="connexion_input">
                        <label for="Phone number">Phone number</label>
                        <input type="tel" name="tel" id="tel" placeholder="Phone number" required>
                    </div>

                    <div class="connexion_input">
                        <label for="domain">Domain</label>
                        <input type="text" name="domain" id="domain" placeholder="Domain" required>
                    </div>

                    <div class="connexion_input">
                        <label for="password">Password</label>
                        <input type="password" name="password" id="password" placeholder="Password" required>
                    </div>

                    <div class="connexion_input">
                        <label for="confirm_password">Confirm Password</label>
                        <input type="password" name="confirmpassword" id="confirmpassword" placeholder="Confirm password" required>
                    </div>

                    <div class="connexion_input">
                        <input type="submit">
                    </div>
                    
                     <p class="changeOption" on:click={inverse}>Already have an account ?</p>
            
            </div>
    
        </form>
        {/if}

        {#if infoMessage && !register}
            <p>{infoMessage}</p>
        {/if}

    </div>

</main>

<style>
    
.container{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 80vh;
}

h2{
    text-align: center;
    grid-column-start: 1;
    grid-column-end: 3;
}

.container_connexion{
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 10px;
}


.connexion_input{
    margin-top: 20px;
    display: flex;
    flex-direction: column;
}

.connexion_input:last-child{
    grid-column-start: 1;
    grid-column-end: 3;
}

input[type="submit"]{
    cursor: pointer;
}

.changeOption{
    margin-top: 20px;
    text-align: center;
    border: 1px solid black;
    border-radius: 5px;
    padding-top: 2px;


}

p:hover{
    cursor: pointer;
}

.connexion_input input{
    padding: 5px 10px;
    margin: 0px 15px;
    border: none;
    border-radius: 5px;
    background-color: rgb(230, 230, 230);
}

.connexion_input label{
    margin-left: 15px;
    margin-bottom: 5px;
}

.box{
    padding: 10px;
    margin: 15px;
    border: 3px solid black;
    border-radius: 5px;
}

</style>