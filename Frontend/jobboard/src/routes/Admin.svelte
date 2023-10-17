<script>

    import Cookies from 'js-cookie';
    
    import { checkAdmin } from '../stores/checkadmin';
    import { getCompanies } from '../stores/admin/getallcompanies.js';
    import { getPeoples } from '../stores/admin/getallpeoples.js';

    import AdminCompany from '../components/admin/AdminCompany.svelte';
    import AdminPeople from '../components/admin/AdminPeople.svelte';

    let token = Cookies.get('userToken');
    if(token === undefined){
        window.location.href = '/login';
    }

    checkAdmin(token).then(data => {
        if(data.message !== 'success'){
            window.location.href = '/';
        }
    })

    let selectData = {};



</script>

<main>

    <div class="box">
        <nav class="container">
            <div>
                <label for="tables">Choose a table:</label>
                <select id="tables" name="tables" bind:value={selectData.value}>
                    <option value="company" selected>Company</option>
                    <option value="jobadvertisements">JobAdvertisements</option>
                    <option value="login">Login</option>
                    <option value="peoples">Peoples</option>
                </select>
            </div>

            <button>Create new row</button>
        </nav> 

    </div>

    <div class="box">

        {#if selectData.value === 'company'}
            <div class="company_row">
                <p>ID</p>
                <p>NAME</p>
                <p class="description">DESCRIPTION</p>
                <p>ADDRESS</p>
                <p>CITY</p>
                <p>ZIPCODE</p>
            </div>
            {#await getCompanies(token)}
                <p>Loading...</p>
            {:then companies}
                {#each companies as company}
                    <AdminCompany company={company} token={token} />
                {/each} 
            {/await}
        {/if}

        <!-- {#if selectData.value === 'jobadvertisements'}
            <div class="jobadvertisements_row">
                <p>ID</p>
                <p>TITLE</p>
                <p>JOB DOMAIN</p>
                <p>DESCRIPTION</p>
                <p>DATE OF PUBLICATION</p>
                <p>LOCATION</p>
                <p>CONTRACT TYPE</p>
                <p>DURATION WEEK</p>
                <p>ID COMPANY</p>
            </div>
            {#await getCompanies(token)}
                <p>Loading...</p>
            {:then companies}
                {#each companies as company}
                    <AdminCompany company={company} />
                {/each} 
            {/await}
        {/if} -->

        {#if selectData.value === 'peoples'}
            <div class="peoples_row">
                <p>ID</p>
                <p>FIRSTNAME</p>
                <p>LASTNAME</p>
                <p>DATE OF BIRTH</p>
                <p>PHONE NUMBER</p>
                <p>EMAIL</p>
                <p>DOMAIN</p>
                <p>ROLE</p>
                <p>ID COMPANY</p>
            </div>
            {#await getPeoples(token)}
                <p>Loading...</p>
            {:then peoples}
                {#each peoples as people}
                    <AdminPeople people={people} token={token} />
                {/each} 
            {/await}
        {/if}
    </div>

</main>

<style>

.peoples_row{
    margin: 15px;
    display: grid;
    grid-template-columns: repeat(9, 1fr) repeat(2, 0.3fr);
    gap: 10px;
}

.jobadvertisements_row{
    margin: 15px;
    display: grid;
    grid-template-columns: repeat(11, 1fr) repeat(2, 0.3fr);
    gap: 10px;
}

.company_row{
    margin: 15px;
    display: grid;
    grid-template-columns: repeat(9, 1fr) repeat(2, 0.3fr);
    gap: 10px;
}

.description{
    grid-column-start: 3;
    grid-column-end: 5;
}

.box{
    margin: 15px;
    border-radius: 15px;
    background-color: white;
    border: 3px solid rgb(236, 236, 236);
}


.container{
    padding: 10px;
    margin: 15px;
    border-radius: 10px;
    background-color: #f1f1f1;
    border: 2px solid #f7f7f7;
}

nav{
    display: flex;
    justify-content: space-between;
}

select, button{
    cursor: pointer;
    padding: 10px;
    margin: 5px;
    border-radius: 10px;
    background-color: white;
    border: 2px solid #f7f7f7;
}

button:hover{
    background-color: rgb(179, 0, 255);
    color: white;
}

</style>