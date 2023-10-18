<script>

    import Cookies from 'js-cookie';
    import { createJobApplication } from '../../stores/createjobapplications';


    let jobapplication = {
        first_name: "",
        last_name: "",
        email: "",
        phone_number: "",
        id_user: "",
        id_advertisement: "",
    }

let result;
async function submit(){
    event.preventDefault();
    result = await createJobApplication(jobapplication);
    console.log(result);
    if(result.message === "success"){
        window.location.href = '/admin';
    }
}

</script>

<main>

    <div class="container applying">
        <h2>
            <h3>Create Job Application</h3>

            <form method="POST" action="">
                <div class="input">
                    <label for="firstname">First Name</label><br>
                    <input type="text" bind:value={jobapplication.first_name} id="firstname" placeholder="firstname">
                </div>
                <div class="input">
                    <label for="lastname">Last name</label><br>
                    <input type="text" bind:value={jobapplication.last_name} id="lastname" placeholder="lastname">
                </div>

                <div class="input">
                    <label for="email">Email</label><br>
                    <input type="text" bind:value={jobapplication.email} id="email" placeholder="email">
                </div>
                
                <div class="input">
                    <label for="phone_number">Phone number</label><br>
                    <input type="text" bind:value={jobapplication.phone_number} id="phone_number" placeholder="phone_number">
                </div>

                <div class="input">
                    <label for="id_user">ID User</label><br>
                    <input type="text" bind:value={jobapplication.id_user} id="id_user" placeholder="id_user">
                </div>

                <div class="input">
                    <label for="id_advertisement">ID Advertisement</label><br>
                    <input type="text" bind:value={jobapplication.id_advertisement} id="id_advertisement" placeholder="id_advertisement">
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