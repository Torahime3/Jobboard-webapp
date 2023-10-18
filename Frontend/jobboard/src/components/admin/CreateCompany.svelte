<script>

    import Cookies from 'js-cookie';
    import { createCompany } from '../../stores/admin/companies/createcompany'

    import { checkAdmin } from '../../stores/checkadmin';
    let token = Cookies.get('userToken');
    checkAdmin(token).then(data => {
        if(data.message !== 'success'){
            window.location.href = '/';
        }
    })

    let company = {
        name: "",
        description: "",
        address: "",
        city: "",
        zipcode: "",
        url_website: "",
    }

let result;
async function submit(){
    event.preventDefault();
    result = await createCompany(Cookies.get('userToken'), company);
    if(result.message === "success"){
        window.location.href = '/admin';
    }
}

</script>

<main>

    <div class="container applying">
        <h2>
            <h3>Create company </h3>

            <form method="POST" action="">
                <div class="input">
                    <label for="Name">Name</label><br>
                    <input type="text" bind:value={company.name} id="Name" placeholder="Name">
                </div>
                <div class="input">
                    <label for="Description">Description</label><br>
                    <input type="text" bind:value={company.description} id="Description" placeholder="Description">
                </div>

                <div class="input">
                    <label for="Address">Address</label><br>
                    <input type="text" bind:value={company.address} id="Address" placeholder="Address">
                </div>

                <div class="input">
                    <label for="City">City</label><br>
                    <input type="text" bind:value={company.city} id="City" placeholder="City">
                </div>
                
                <div class="input">
                    <label for="Zipcode">Zipcode</label><br>
                    <input type="text" bind:value={company.zipcode} id="Zipcode" placeholder="Zipcode">
                </div>

                <div class="input">
                    <label for="url_website">URL Website</label><br>
                    <input type="text" bind:value={company.url_website} id="url_website" placeholder="url_website">
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