<script>

    import Cookies from 'js-cookie';
    import { checkAdmin } from '../stores/checkadmin';
    import Company from '../components/admin/Company.svelte';

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
                <p>DESCRIPTION</p>
                <p>ADDRESS</p>
                <p>CITY</p>
                <p>ZIPCODE</p>
            </div>
            <Company/>
        {/if}
    </div>

</main>

<style>

    .company_row{
        margin: 15px;
        display: grid;
        grid-template-columns: repeat(9, 1fr);
        gap: 10px;
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