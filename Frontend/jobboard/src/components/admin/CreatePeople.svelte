<script>

    import Cookies from 'js-cookie';
    import { createPeople } from '../../stores/admin/peoples/createpeople';

    import { checkAdmin } from '../../stores/checkadmin';
    let token = Cookies.get('userToken');
    checkAdmin(token).then(data => {
        if(data.message !== 'success'){
            window.location.href = '/';
        }
    })

    let people = {
        firstname: "",
        lastname: "",
        date_of_birth: "",
        phone_number: "",
        email: "",
        domain: "",
        url_profilpicture: "",
        role: "",
        id_company: "",
        password: "",
    }

let result;
async function submit(){
    event.preventDefault();
    result = await createPeople(Cookies.get('userToken'), people);
    console.log(result);
    if(result.message === "success"){
        window.location.href = '/admin';
    }
}

</script>

<main>

    <div class="container applying">
        <h2>
            <h3>Create people </h3>

            <form method="POST" action="">
                <div class="input">
                    <label for="firstname">First Name</label><br>
                    <input type="text" bind:value={people.firstname} id="firstname" placeholder="firstname">
                </div>
                <div class="input">
                    <label for="lastname">Last Name</label><br>
                    <input type="text" bind:value={people.lastname} id="lastname" placeholder="lastname">
                </div>

                <div class="input">
                    <label for="Address">Birthdate</label><br>
                    <input type="date" bind:value={people.date_of_birth} id="date_of_birth" placeholder="date_of_birth">
                </div>

                <div class="input">
                    <label for="phone_number">Phone number</label><br>
                    <input type="text" bind:value={people.phone_number} id="phone_number" placeholder="phone_number">
                </div>
                
                <div class="input">
                    <label for="email">Email</label><br>
                    <input type="text" bind:value={people.email} id="email" placeholder="email">
                </div>

                <div class="input">
                    <label for="domain">Domain</label><br>
                    <input type="text" bind:value={people.domain} id="domain" placeholder="domain">
                </div>

                <div class="input">
                    <label for="id_company">ID company</label><br>
                    <input type="text" bind:value={people.url_profilpicture} id="id_company" placeholder="id_company">
                </div>

                <div class="input">
                    <label for="password">Password</label><br>
                    <input type="password" bind:value={people.password} id="password" placeholder="password">
                </div>


                <div class="input">
                    <button on:click={submit}>Submit </button>
                </div>
            </form>
            {#if result}
                {#if result.message === 'error'}
                <p class="status error">An error occured!</p>
                {/if}
            {/if}
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

    span, label, p{
        font-size: 16px;
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