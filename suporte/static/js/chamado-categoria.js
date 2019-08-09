$(document).ready(function() {
    $(':input[name$=setor]').on('change', function() {
        var prefix = $(this).getFormPrefix();
        $(':input[name=' + prefix + 'categoria]').val(null).trigger('change');
    });
});