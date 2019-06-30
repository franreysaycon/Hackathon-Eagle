<style type="text/css">
    .container {
        display: grid;
        grid-template-columns: 250px auto;
        width: 100vw;
        height: 100vh;
        font-family: 'Noto Sans HK', sans-serif;
        font-size: 12px;
        background-color: #E0E0E0;
        color: #101010;
    }

    .navigation {
        overflow-y: auto;
    }

    .navigation-item {
        padding: 4px;
        border: solid .5px #101010;
        flex-wrap: wrap;
        display: flex;
        word-break: break-all;
    }

    .navigation-item.active {
        background-color: #FF6961 !important;
    }

    .navigation-item:hover {
        background-color: #C0C0C0;
    }

    .content {
        overflow-y: auto;
        overflow-x: auto;
        white-space: pre-wrap;
        word-break: break-all;
    }

    .area {
        width: 100%;
        height: 100%;
    }

    div.json {
       background-color: ghostwhite;
       border: 1px solid silver;
       padding: 10px;
       min-height: 100%;
    }

    b{
        color: red;
        margin-left: 2px;
    }
</style>

<div class="container">
    <div class="navigation">
        {#each LOG_FILES as file}
            <div
                class="{currentLog === file ? 'navigation-item active' : 'navigation-item' }"
                id={file}
                on:click={handleClick}
            >
                {getLabel(file)} {#if logs[file] && logs[file].new} <b>(new)</b> {/if}
            </div>
        {/each}
    </div>
    <div class="content" id="content">
        <div class="json">{#if logs[currentLog]}{@html processLog(logs[currentLog].msg)}{/if}</div>
    </div>
</div>

<script>
    import { LOG_FILES } from './config.json';
    import helper from './helpers.js';

    let currentLog = LOG_FILES[0];
    let logs = {};
    LOG_FILES.map( (k) => {
        logs[k] = {
            new: false,
            msg: "",
        };
    })

    function handleClick(event) {
        currentLog = event.target.id;
        if(logs[currentLog].new){
            logs[currentLog].new = false;
        }
    }

    function getLabel(file) {
        return file.replace(new RegExp('_', 'g'), ' ');
    }

    function processLog(msg){

        let message = "";
        if(msg){
            message = JSON.parse(msg);
        }
        if(message.length){
            let output = message.map( m => {

                let converted = helper.convertJson(m);
                if(converted){
                    return helper.prettyPrint(converted);
                }
                return m;
            });

            return output.join("<br/>").replace(/(\\r\\n|\\n|\\r)/gm, "<br/>");
        }
        return "<center>Nothing to see here</center>"
    }

    eel.expose(push);
    function push(log){
        log = JSON.parse(log);
        if(LOG_FILES.includes(log.name)){
            if(log.name !== currentLog){
               logs[log.name].new = true;
            }
            logs[log.name].msg = log.value;
        }
    }
</script>
