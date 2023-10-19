<script>
    import Cookies from 'js-cookie';
    import { getUserData } from '../stores/getuserdata.js';
    import { getJobsApplications } from '../stores/getjobapplications.js';
    import { getJobsApplicationsByCompany } from '../stores/getjobapplications.js';
    import { getJobsAvertisementsByCompany } from '../stores/jobadvertisements.js';
    import JobAdvertisements from '../components/JobAdvertisements.svelte';
    import JobApplications from '../components/JobApplications.svelte';


    function disconnect(){
        Cookies.remove('userToken');
        window.location.href = '/login';
    }

    let imageFile;
    async function set_profile_picture() {
    if (imageFile) {
      const formData = new FormData();
      formData.append('image', imageFile);

      const response = await fetch('http://localhost:5173/peoples/upload_img', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        console.log('Image téléchargée avec succès.');
      } else {
        console.error('Erreur lors du téléchargement de l\'image.');
        console.log(response)
      }
    } else {
      console.log("Aucun fichier sélectionné.");
    }
  }

    async function getInfos(){
        if(!Cookies.get('userToken')){
            window.location.href = '/';
        } else {
            let promise = await getUserData(Cookies.get('userToken'));
            return promise;
        }
    }

    let recruiter;
    getUserData(Cookies.get('userToken')).then(data => {
        if(data.role === 'Recruiter'){
            recruiter = true;
        }
    });
    
    getJobsApplicationsByCompany(Cookies.get('userToken')).then(data => {
        console.log(data);
    });

</script>

<main>
    
    <div class="container_profil box">
        <h3 class="title">My Profile</h3>
        {#await getInfos()}
            <p>Loading...</p>
        {:then data}
        <div class="myprofil">
            <div class="img">
                <img src="https://picsum.photos/200" alt="something">
            </div>
            <div class="infos">
                <p><strong>First name:</strong> {data.firstname}</p>
                <p><strong>Last name:</strong> {data.lastname}</p>
                <p><strong>Email:</strong> {data.email}</p>
                <p><strong>Phone number:</strong> {data.phone_number}</p>
                <p><strong>Date of birth:</strong> {data.date_of_birth}</p>
                <p><strong>Domain:</strong> {data.domain}</p>
                {#if data.id_company}
                    <p><strong>Company :</strong> {data.company_name}</p>
                {/if}
                <div>
                    <input type="file" bind:files={imageFile} accept="image/*" /> 
                    <button class="set_profile_picture" on:click={set_profile_picture}>Set profile picture</button>
                </div>
            </div>
        </div>

        {:catch error}
            <p>Error loading data</p>
        {/await}
        <button class="disconnect" on:click={disconnect}>Disconnect</button>

        
    </div>

    <div class="container_myapplications box">
        <h3 class="title">I applied for</h3>
        {#await getJobsApplications(Cookies.get('userToken'))}
            <p>Loading...</p>
        {:then applications}
            {#if applications.length === 0}
                <p>You didn't apply for any job</p>
            {/if}
            {#each applications as app}
                <JobApplications app={app}/>
            {/each}
        {:catch error}
            <p>Error while loading your job applications</p>
        {/await}
    </div>

    {#if recruiter}
    <div class="container_companyapplications box">
        <h3 class="title">Company's job advertisements</h3>
        {#await getJobsAvertisementsByCompany(Cookies.get('userToken'))}
            <p>Loading...</p>
        {:then jobs}
            {#each jobs as job}
                <JobAdvertisements job={job} token={Cookies.get('userToken')} rhView={true}/>
            {/each}
        {:catch error}
            <p>Error while loading your job applications</p>
        {/await}
    </div>

    <div class="container_companyapplications box">
        <h3 class="title">Company's job applications</h3>
        {#await getJobsApplicationsByCompany(Cookies.get('userToken'))}
            <p>Loading...</p>
        {:then jobs}
            {#each jobs as job}
                {#if job.peoples.length !== 0}
                    <JobApplications app={job} rhView={true}/>
                {/if}
            {/each}
        {:catch error}
            <p>Error while loading your job applications</p>
        {/await}
    </div>

    {/if}

</main>


<style>

    .disconnect{
        border: none;
        border-radius: 5px;
        padding: 10px;
        color: red;
        background-color: rgb(255, 234, 234);
        cursor: pointer;
    }
    .set_profile_picture{
        border: none;
        border-radius: 5px;
        padding: 10px;
        color: rgb(64, 64, 165);
        background-color: rgb(255, 234, 234);
        cursor: pointer;
    }
    .set_profile_picture:hover{
        background-color: rgb(255, 214, 214);
    }
    .disconnect:hover{
        background-color: rgb(255, 214, 214);
    }

    .myprofil{
        display: flex;
    }

    .infos{
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 10px;
        margin-left: 10px;
    }

    .container_myapplications, .container_companyapplications{
        height: 40vh;
        overflow-y: scroll;
    }

    .title{
        border-bottom: 2px solid rgb(0, 0, 0);
        padding-bottom: 10px;
        margin-bottom: 10px;
    }

    .img{
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    img{
        border-radius: 10px;
        width: clamp(150px, 20vw, 200px);
    }

    .box{
        padding: 10px;
        margin: 15px;
        border-radius: 10px;
        background-color: white;
        border: 3px solid rgb(236, 236, 236);
    }

    @media screen and (min-width: 768px) {
        main{
            display: grid;
            grid-template-columns: 1fr 1fr;
        }

    }

</style>