import json
from collections import defaultdict
from dataclasses import dataclass


def flatten_json(y):
    out = {}

    def flatten(z, name=''):
        if type(z) is dict:
            for x in z:
                flatten(z[x], name + x.replace('-', '_') + '_')
        elif type(z) is list:
            i = 0
            for x in z:
                flatten(x.replace('-', '_'), name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = z

    flatten(y)
    return out


@dataclass
class I18NFlatten:
    def __init__(self, json_file: str = None, json_dict: dict = None, language: str = None):
        self._fields = {}
        self.language = language
        if json_file:
            with open(json_file, "r") as f:
                json_dict = json.load(f)
        if json_dict:
            self._fields.update(flatten_json(json_dict))

    def __getattribute__(self, name: str):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            if self.language:
                field_name = f'{name}_{self.language}'
                if field_name in self._fields:
                    return self._fields[field_name]
            if name in self._fields:
                return self._fields[name]
            else:
                raise AttributeError(f'{name} not found')

    def __delproperty__(self, name):
        if hasattr(self, name):
            delattr(self, name)


    def modify_text(self, property_name: str, **kwargs):
        """
        Modify the text of the specified property by replacing placeholders with the provided parameters
        """
        # Get the value of the specified property
        property_value = getattr(self, property_name)
        # Modify the text by replacing placeholders with the provided parameters
        kwargs = defaultdict(str, kwargs)
        property_value = property_value.format_map(kwargs)
        # setattr(self, property_name, property_value)
        return property_value

    def get_language_object(self, language_prefix: str):
        new_fields = {field: value for field, value in self._fields.items() if field.endswith(f'_{language_prefix}')}
        return I18NFlatten(json_dict=new_fields, language=language_prefix)

