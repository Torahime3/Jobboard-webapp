<script>

    import Cookies from 'js-cookie';
    import { checkAdmin } from '../stores/checkadmin';

    let token = Cookies.get('token');

</script>

<main>
    
        {#await checkAdmin(token)}
            <p>Loading...</p>
        {:then data} 
            {#if data.message !== 'success'}
                <p>You are not allowed to go there</p>
            {:else}
                <h1>Admin panel</h1>
            {/if}
        {/await}

</main>

<style>

</style>