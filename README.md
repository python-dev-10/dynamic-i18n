# dynamic-i18n

[![PyPI version](https://badge.fury.io/py/dynamic-i18n.svg)](https://pypi.org/project/dynamic-i18n/)

## Introduction
dynamic-i18n is a python package that helps to flatten complex JSON files into a simple and accessible format. It also provides functionality to modify the text of specific properties and get an object that only contains properties of a specified language.

## Installation
To install dynamic-i18n, run the following command:

```shell
pip install dynamic-i18n
```
## Usage
To use dynamic-i18n, you need to pass either a file name or a dictionary to the I18NFlatten class. You can also specify a language prefix to limit the properties to a specific language.

```python
import json
from dynamic_i18n.flatten import I18NFlatten

# Using a file
json_file = 'file.json'
i18n = I18NFlatten(json_file=json_file)

# Using a dictionary
json_dict = {...}
i18n = I18NFlatten(json_dict=json_dict)
```

The **flattened properties** can be accessed as attributes of the I18NFlatten object.

```python
property_value = i18n.property_name
```
The **modify_text** method can be used to modify the text of a specified property by replacing placeholders with the provided parameters.

```python
modified_text = i18n.modify_text('property_name', param1='value1', param2='value2')
```

The **get_language_object** method can be used to get a new **I18NFlatten** object that only contains properties of a specified language.

```python
language_object = i18n.get_language_object('en')
```

## Practical Example

```python
from dynamic_i18n.flatten import I18NFlatten

data_json = {
    'i18n': {
        'welcome_message': {
            'en_us': "Hello World {name}",
            'pt_br': "Olá Mundo",
            'es': "Hola mundo"
        },
        'other_message': {
            'en_us': "{programming_language} programming language",
            'pt_br': "{programming_language} linguagem de programação",
            'es': "{programming_language} lenguaje de programación"
        }
    }
}

data = I18NFlatten(json_dict=data_json)
print(data._fields)
# {'i18n_welcome_message_en_us': 'Hello World {name}', 'i18n_welcome_message_pt_br': 'Olá Mundo', 'i18n_welcome_message_es': 'Hola mundo', 'i18n_other_message_en_us': '{programming_language} programming language', 'i18n_other_message_pt_br': '{programming_language} linguagem de programação', 'i18n_other_message_es': '{programming_language} lenguaje de programación'}

print(data.modify_text('i18n_welcome_message_en_us', name='Jeferson Peter'))
# IN: 'Hello World {name}'
# OUT: 'Hello World Jeferson Peter'

print(data.modify_text('i18n_other_message_pt_br', programming_language='Python'))
# IN: '{programming_language} linguagem de programação'
# OUT: 'Python linguagem de programação'

data_en = data.get_language_object(language_prefix='en_us')
print(data_en._fields)
# {'i18n_welcome_message_en_us': 'Hello World {name}', 'i18n_other_message_en_us': '{programming_language} programming language'}
```

# Conclusion
dynamic-i18n provides a simple and convenient way to access and manipulate complex JSON files for internationalization purposes. Give it a try and see how it can help you in your next project.