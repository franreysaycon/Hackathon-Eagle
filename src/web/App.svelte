<script>
    import Loading from './Loading.svelte';
    import Logs from './Logs.svelte';
    import ErrorModal from './ErrorModal.svelte';

    const VIEWS = {
        CONNECT: 0,
        LOGS: 1
    };

    let currentView = VIEWS.CONNECT;
    let host = "";
    let loading = false;
    let error = "";
    let modalOpen = false;

    function handleSubmit(){
        loading = true;
        eel.connect(host)(
            function(result) {
                loading=false;
                console.log(result)
                if(result.success){
                    setView(VIEWS.LOGS);
                }
                else {
                    error = "Something went wrong. Please check if your host is already provisioned. Error encountered: " + result.message;
                    modalOpen = true;
                }
            }
        );
    }

    function setView(view) {
        currentView = view;
    }

    function toggleErrorModal(){
        if(modalOpen){
            modalOpen = false;
        }
        else{
            modalOpen = true;
        }
    }

    eel.expose(push);
    function push(log){
        console.log(log);
    }

</script>

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
        text-align: right;
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

{#if currentView === VIEWS.CONNECT }
    <div class="main-container">

        <h1>What is your dev box? </h1>
        <div class="form-container">
            <input bind:value={host} type="text"/>
            <h2>.syd1.fln-dev.net</h2>
        </div>
        {#if loading }
             <Loading />
        {:else}
            <button on:click={handleSubmit}>GET STARTED</button>
        {/if}
    </div>
{/if}

{#if currentView === VIEWS.LOGS }
    <Logs />
{/if}

{#if modalOpen}
    <ErrorModal message={error} handleClose={toggleErrorModal} />
{/if}
