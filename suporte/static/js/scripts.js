<script type="text/javascript">
    $(document).ready(function() {
        function newParameters(query) {
            query.setor = $('#id_setor').val();
        }
        $('#id_categoria_0').djselectable('option', 'prepareQuery', newParameters);
    });
</script>