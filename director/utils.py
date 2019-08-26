class ReadOnlyTabularInline():
    """
    Classe base para as demais inlines da aplicação.
    Já que todas as inlines são somente para leitura dos dados, todas devem ter os mesmos métodos que indicam tal comportamento. 
    """
    template = 'director/tabular-readonly.html'
    extra = 0

    def get_readonly_fields(self, request, obj=None):
        return self.fields

    def save_formset(self, request, form, formset, change):
        pass

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False