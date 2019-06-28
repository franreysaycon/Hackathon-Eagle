<script>
    import { LOG_FILES } from './config.json';

    let currentLog = undefined;
    let content = "";
    let lines = [];

    function handleClick(event) {
        const LOG_FILE = event.target.id;

        if (currentLog) {
            const active = document.getElementById(currentLog);
            active.className = active.className.replace("active", "").trim();
        }

        setLog(LOG_FILE);
    }

    function setLog(logFile) {
        currentLog = logFile;

        const active = document.getElementById(currentLog);
        active.className += " active";

        // get/set content

        lines = JSON.stringify(content, null, 8).split("\\n");
    }

    function getLabel(file) {
        return file.replace(new RegExp('_', 'g'), ' ');
    }
</script>

<style type="text/css">
    .container {
        display: flex;
        width: 100vw;
        height: 100vh;
        font-family: 'Noto Sans HK', sans-serif;
        font-size: 12px;
        background-color: #272822;
        color: #F8F8F2;
    }

    .navigation {
        overflow-y: auto;
    }

    .navigation-item {
        padding: 4px;
        border: solid 1px black;
        flex-wrap: wrap;
        display: flex;
        word-break: break-all;
    }

    .navigation-item.active {
        background-color: #49483E !important;
    }

    .navigation-item:hover {
        background-color: #3E3D32;
    }

    .content {
        overflow-y: auto;
        overflow-x: auto;
        padding: 16px;
        max-width: 70vw;
        flex-grow: 1;
        white-space: pre-wrap;
        word-break: break-all;
    }
</style>

<div class="container">
    <div class="navigation">
        {#each Object.keys(LOG_FILES) as file}
            <div
                class="navigation-item"
                id={file}
                on:click={handleClick}
            >
                {getLabel(file)}
            </div>
        {/each}
    </div>
    <code class="content">
        {#each lines as line}
            {line}<br />
        {/each}
    </code>
</div>
