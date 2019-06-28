<script>
    let name = "";
    eel.get_my_name()(
        function(ret){
            name = ret;
        }
    );
</script>

<h1>Hello {name}!</h1>
