from json_parser_utils.utils import safe_int


class JsonParser:
    def __init__(self, value):
        """Allows to access JSON values conveniently with dot separated values.
        Example: {"person": {"name": "John", "age": 21, kids: [{"name": "Lorem"}]}]}}. Access with person.name or person.age
        Returns null when a key is not available like person.address.city
        Arrays can be access like person.kids.0.name"""

        self.value = value

    def access(self, key_sequence):
        # further optimisation can be used to create a list of nodes and match in that
        result = None
        try:
            assert isinstance(self.value, dict) or isinstance(self.value, list)
            keys = key_sequence.split('.')
            value = self.value
            for key in keys:
                access_key = key if isinstance(value, dict) else safe_int(key)
                value = value[access_key]
            result = value
        except KeyError as e:
            pass
        except AssertionError as e:
            pass
        except IndexError as e:
            pass
        return JsonParser(result)
