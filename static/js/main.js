$(document).ready(function() {
    /**summernote**/
    $('.summernote, .summernote-readonly').summernote({
        /**set widget behavior**/
        lang: 'pt-BR',
        minHeight: 100,
        toolbar: [
            // ['style', ['style']],
            ['font', ['bold', 'italic', 'clear']],
            // ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link',]],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    });
    
    $('.summernote-readonly').each(function(){
        /**customize behavior of non-editable field**/
        var el = $(this);
        el.summernote('disable');
        el.next('div').find('div[contenteditable=false]').css("background-color", "#fff");
        el.next('div').find('.note-toolbar').hide();
        el.next('div').find('.note-statusbar').hide();
    });
});