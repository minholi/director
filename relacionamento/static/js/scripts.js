(function($){
    $(document).ready(function() {
        $('div#atividade_set-group table').DataTable({
            language: {
                url: '//cdn.datatables.net/plug-ins/1.10.19/i18n/Portuguese-Brasil.json'
            }
        });
    });
}(django.jQuery));