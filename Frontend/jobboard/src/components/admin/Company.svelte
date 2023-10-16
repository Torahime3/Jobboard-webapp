<script>

    // export let company;

</script>

<main>

    <div class="container">
        <div class="row">
            <p>1</p>
            <p>2</p>
            <p>3</p>
            <p>4</p>
            <p>5</p>
            <p>6</p>
            <p>7</p>
            <button>Edit</button>
            <button>Delete</button>
        </div>
    </div>

</main>

<style>

.container{
    padding: 10px;
    margin: 15px;
    border-radius: 10px;
    background-color: #f1f1f1;
    border: 2px solid #f7f7f7;
}

.row{
    display: grid;
    grid-template-columns: repeat(9, 1fr);
    gap: 10px;
}

p{
    background-color: aqua;
}


</style>