<script>

    import Cookies from 'js-cookie';

    if(!Cookies.get('userToken')){
        window.location.href = '/';
    }

    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    console.log(id);

</script>

<main>

    <div class="container applying"></div>


</main>

<style>

.container{
        padding: 10px;
        margin: 15px;
        border: 3px solid black;
        border-radius: 5px;
    }

</style>