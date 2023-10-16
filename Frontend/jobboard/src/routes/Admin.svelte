<script>

    import Cookies from 'js-cookie';
    import { checkAdmin } from '../stores/checkadmin';

    let token = Cookies.get('userToken');
    if(token === undefined){
        window.location.href = '/login';
    }

    checkAdmin(token).then(data => {
        if(data.message !== 'success'){
            window.location.href = '/';
        }
    })

</script>

<main>

    

</main>

<style>

</style>