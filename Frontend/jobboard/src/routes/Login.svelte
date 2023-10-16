<script>

    import { checkValidity } from "../stores/checkvalidity";
    import { createAccount } from "../stores/createuseraccount";
    import Cookies from 'js-cookie';

    let register = false;
    function inverse(){
        register = !register;
    }

    let infoMessage;
    let registerMessage = "";
    let promise;

    // Login
    let login_credentials = {
        email: "",
        password: ""
    }

    //Register
    let register_credentials  = {
        first_name: "",
        last_name: "",
        birthdate: "",
        email: "",
        tel: "",
        domain: "",
        password: "",
        confirmpassword: ""
    }
 

    async function submitLogin(){
        promise = await checkValidity(login_credentials);
        if(promise.message !== "success"){
            infoMessage = "Invalid credentials";
        }else{
            Cookies.set('userToken', promise.token, { expires: 7 });
            window.location.href = '/profil';
            }
        }

    async function submitRegister(){
        event.preventDefault();
        promise = await createAccount(register_credentials);
        registerMessage = promise.message;

        if(promise.message === "success"){
            register = false;
        }
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
                    <input type="email" bind:value={login_credentials.email} name="email" id="email" placeholder="Email" required>
                </div>

                <div class="connexion_input">
                    <label for="password">Password</label>
                    <input type="password" bind:value={login_credentials.password} name="password" id="password" placeholder="Password" required>
                </div>

                <div class="connexion_input">
                    <input type="submit" on:click={submitLogin}>
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
                        <input type="text" bind:value={register_credentials.first_name} name="first_name" id="first_name" placeholder="First name" required>
                    </div>
        
                    <div class="connexion_input">
                        <label for="last_name">Last name</label>
                        <input type="text" bind:value={register_credentials.last_name} name="last_name" id="last_name" placeholder="Last name" required>
                    </div>

                    <div class="connexion_input">
                        <label for="birthdate">Birth date</label>
                        <input type="date" bind:value={register_credentials.birthdate} name="birthdate" id="birthdate" placeholder="Birth date" required>
                    </div>

                    <div class="connexion_input">
                        <label for="email">Email</label>
                        <input type="email" bind:value={register_credentials.email} name="email" id="email" placeholder="Email" required>
                    </div>

                    <div class="connexion_input">
                        <label for="Phone number">Phone number</label>
                        <input type="tel" bind:value={register_credentials.tel} name="tel" id="tel" placeholder="Phone number" required>
                    </div>

                    <div class="connexion_input">
                        <label for="domain">Domain</label>
                        <input type="text" bind:value={register_credentials.domain} name="domain" id="domain" placeholder="Domain" required>
                    </div>

                    <div class="connexion_input">
                        <label for="password">Password</label>
                        <input type="password" bind:value={register_credentials.password} name="password" id="password" placeholder="Password" required>
                    </div>

                    <div class="connexion_input">
                        <label for="confirm_password">Confirm Password</label>
                        <input type="password" bind:value={register_credentials.confirmpassword} name="confirmpassword" id="confirmpassword" placeholder="Confirm password" required>
                    </div>

                    <div class="connexion_input">
                        <input type="submit" on:click={submitRegister}>
                    </div>
                    
                     <p class="changeOption" on:click={inverse}>Already have an account ?</p>
            
            </div>
    
        </form>
        {/if}

        {#if infoMessage && !register}
            <p>{infoMessage}</p>
        {/if}

        {#if registerMessage === 'success'}
            <p class="status good">Successfully created your account</p>
        {:else if registerMessage === 'exist' && register}
            <p class="status error">{registerMessage}</p>
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

input[type="submit"]:hover{
    cursor: pointer;
    background-color: rgb(244, 223, 254);
}


.changeOption{
    margin-top: 20px;
    text-align: center;
    border: 2px dashed rgb(146, 146, 146);
    border-radius: 5px;
    padding-top: 7px;
}

.changeOption:hover{
    cursor: pointer;
    color: rgb(146, 146, 146);
}

.connexion_input input{
    padding: 10px 15px;
    margin: 0px 15px;
    border: none;
    border-radius: 5px;
    background-color: rgb(249, 238, 255);
}

.connexion_input label{
    margin-left: 15px;
    margin-bottom: 5px;
}

.box{
    padding: 10px;
    margin: 15px;
    border-radius: 10px;
    background-color: white;
    border: 3px solid rgb(236, 236, 236);
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