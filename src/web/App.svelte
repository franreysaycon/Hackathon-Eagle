<style>
    div.main-container {
        display: flex;
        width: 100vw;
        height: 100vh;

        flex-direction: column;
        align-items: center;
        justify-content: center;
        font-family: 'Noto Sans HK', sans-serif;
    }

    div.form-container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        width: 600px;
        margin-bottom: 10px;
    }

    input {
        width: 300px;
        height: 50px;
        border-radius: 10px;
        border: none;
        font-family: 'Noto Sans HK', sans-serif;
        font-size: 2em;
    }

    h1{
        font-size: 3em;
    }
    h2{
        font-size: 2em;
    }

    button {
        border: none;
        background-color: #B80F0A;
        font-size: 2em;
        border-radius: 10px;
        color: white;
        padding: 10px;
    }

    button:hover {
        opacity: 0.9;
    }
</style>
<script>
    let name = "";
    eel.get_my_name()(
        function(ret){
            name = ret;
        }
    );
</script>

<div class="main-container">

    <h1>What is your dev box? </h1>
    <div class="form-container">
        <input type="text"/>
        <h2>.syd1.fln-dev.net</h2>
    </div>
    <button>GET STARTED</button>
</div>
