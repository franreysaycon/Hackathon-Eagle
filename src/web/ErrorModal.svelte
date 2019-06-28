<script>
    export let message;
    export let handleClose;
</script>

<style>
    div.modal-container {
        display: flex;
        background-color: rgba(0,0,0,.53);
        position: absolute;
        top: 0;
        bottom: 0;
        align-items: center;
        justify-content: center;
        width: 100vw;
        height: 100vh;
        font-family: 'Noto Sans HK', sans-serif;
    }

    div.modal-proper{
        display: flex;
        opacity: 1;
        flex-direction: column;
        width: 500px;
        font-size: 1.5em;
        background-color: white;
        align-items: center;
        justify-content: center;
        z-index: 3;
        padding: 50px;
    }

    button {
        margin-top: 20px;
        border: none;
        background-color: #B80F0A;
        font-size: 1.5em;
        border-radius: 10px;
        color: white;
        padding: 10px;
        width: 200px;
    }
</style>

<div class="modal-container">
    <div class="modal-proper">
        {message}
        <button on:click={handleClose}>OK</button>
    </div>
</div>
