<script>

    import Cookies from 'js-cookie';
    
    //Stores
    import { checkAdmin } from '../stores/checkadmin';
    import { getCompanies } from '../stores/admin/companies/getallcompanies.js';
    import { getPeoples } from '../stores/admin/peoples/getallpeoples.js';
    import { getAllJobAdvertisements } from '../stores/admin/jobadvertisements/getalljobadvertisements';
    import { getAllJobApplications } from '../stores/admin/jobapplications/getalljobapplications';
    import { getAllLogins } from '../stores/admin/login/getalllogins';
    import { getUserData } from '../stores/getuserdata';

    //Components
    import AdminCompany from '../components/admin/AdminCompany.svelte';
    import AdminPeople from '../components/admin/AdminPeople.svelte';
    import AdminJobAdvertisements from '../components/admin/AdminJobAdvertisement.svelte';
    import AdminJobApplications from '../components/admin/AdminJobApplications.svelte';
    import AdminLogin from '../components/admin/AdminLogin.svelte';

    let token = Cookies.get('userToken');
    if(token === undefined){
        window.location.href = '/login';
    }

    // checkAdmin(token).then(data => {
    //     if(data.message !== 'success'){
    //         window.location.href = '/';
    //     }
    // })

    let recruiter;
    getUserData(token).then(data => {
        if(data.role === 'Recruiter'){
            recruiter = true;
        }
    });


    let selectData = {};

    function create(){
        window.location.href = '/admin/create/'+selectData.value;
    }

</script>

<main>

    <div class="box">
        <nav class="container">
            {#if !recruiter}
            <div>
                <label for="tables">Choose a table:</label>
                <select id="tables" name="tables" bind:value={selectData.value}>
                    <option value="company">Company</option>
                    <option value="jobadvertisement">JobAdvertisements</option>
                    <option value="jobapplication">JobApplications</option>
                    <option value="login">Login</option>
                    <option value="people">Peoples</option>
                </select>
            </div>
            {:else}
            <div>
                <select id="tables" name="tables" bind:value={selectData.value}>
                    <option value="jobadvertisement">JobAdvertisements</option>
                </select>
            </div>
            {/if}

             
            {#if selectData.value !== 'login'}
                <button on:click={create}>Create {selectData.value}</button>
            {/if}

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
                <p>WEBSITE</p>
            </div>
            {#await getCompanies(token)}
                <p>Loading...</p>
            {:then companies}
                {#each companies as company}
                    <AdminCompany company={company} token={token} isEditing={false}/>
                {/each} 
            {/await}
        {/if}

        {#if selectData.value === 'jobadvertisement'}
            <div class="jobadvertisements_row">
                <p>ID</p>
                <p>TITLE</p>
                <p>JOB DOMAIN</p>
                <!-- <p>DESCRIPTION</p> -->
                <p>DATE OF PUBLICATION</p>
                <p>LOCATION</p>
                <p>CONTRACT</p>
                <p>DURATION WEEK</p>
                <p>ID COMPANY</p>
                <p>ID PEOPLE</p>
            </div>
            {#await getAllJobAdvertisements(token)}
                <p>Loading...</p>
            {:then jobs}
                {#each jobs as job}
                    <AdminJobAdvertisements job={job} token={token}/>
                {/each} 
            {/await}
        {/if}

        {#if selectData.value === 'people'}
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
                    <AdminPeople people={people} token={token} isEditing={false} />
                {/each} 
            {/await}
        {/if}

        {#if selectData.value === 'jobapplication'}
            <div class="jobapplication_row">
                <p>ID</p>
                <p>FIRSTNAME</p>
                <p>LASTNAME</p>
                <p>EMAIL</p>
                <p>PHONE NUMBER</p>
                <p>ID ADVERTISEMENT</p>
                <p>ID PEOPLE</p>
                <p>DATE OF APPLICATION </p>
            </div>
            {#await getAllJobApplications()}
                <p>Loading...</p>
            {:then apps}
                {#each apps as app}
                    <AdminJobApplications app={app} token={token} isEditing={false} />
                {/each} 
            {/await}
        {/if}

        {#if selectData.value === 'login'}
            <div class="login_row">
                <p>ID</p>
                <p>USERNAME</p>
                <p class="password">PASSWORD</p>
                <p>EMAIL</p>
                <p>ID PEOPLE</p>
            </div>
            {#await getAllLogins(token)}
                <p>Loading...</p>
            {:then logins}
                {#each logins as login}
                    <AdminLogin login={login} token={token} isEditing={false} />
                {/each} 
            {/await}
        {/if}
    </div>

</main>

<style>

.login_row{
    margin: 15px;
    display: grid;
    grid-template-columns: repeat(8, 0.5fr) repeat(2, 0.3fr);
    gap: 10px;
}

.jobapplication_row{
    margin: 15px;
    display: grid;
    grid-template-columns: repeat(8, 1fr) repeat(2, 0.3fr);
    gap: 10px;
}

.peoples_row{
    margin: 15px;
    display: grid;
    grid-template-columns: repeat(9, 1fr) repeat(2, 0.3fr);
    gap: 10px;
}

.jobadvertisements_row{
    margin: 15px;
    display: grid;
    grid-template-columns: repeat(11, 0.8fr);
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

.password{
    grid-column-start: 3;
    grid-column-end: 7;
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