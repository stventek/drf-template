from django_filters import rest_framework as filters

class AnyModelFilter(filters.FilterSet):

    @classmethod
    def get_fields(cls):
        fields = super().get_fields()
        fields['id'] = 'exact'
        for field_name in fields.copy():
            print(field_name, cls.Meta.model._meta.get_field(field_name).get_lookups().keys())
            lookup_list = cls.Meta.model._meta.get_field(field_name).get_lookups().keys()
            fields[field_name] = lookup_list
        return fields
