class RoseDictionary:
    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        try:
            return self._data[key]
        except KeyError as e:
            raise KeyError(f"KeyError: '{key}'") from e

    def __setitem__(self, key, value):
        self._data[key] = value

    def pop_item(self, raise_error=False, error_msg=None, default=None):
        try:
            key, value = self._data.popitem()
            return value
        except KeyError as e:
            if raise_error:
                if error_msg:
                    raise KeyError(error_msg) from e
                else:
                    raise KeyError('error_msg') from e
            elif default is not None:
                return default
            else:
                if error_msg:
                    raise KeyError(error_msg) from e
                else:
                    raise KeyError('Dictionary was empty and no default value/message was specified.')

    def get_item(self, key, raise_error=True, error_msg=None, default=None):
        try:
            return self._data[key]
        except KeyError as e:
            if raise_error:
                if error_msg is not None:
                    raise KeyError(error_msg) from e
                elif default is not None:
                    raise KeyError(f"{default}") from e
                else:
                    raise KeyError('Value was not found and no default value/message was specified.') from e
            elif default is not None:
                return default
            else:
                if error_msg is not None:
                    return error_msg
                else:
                    return 'Value was not found and no default value/message was specified.'





'''d = RoseDictionary()
d["key1"] = "value1"
d["key2"] = "value2"

try:
    print(d["key1"])
except Exception as e:
    print(e)
try:
    print(d.get_item("key1"))
except Exception as e:
    print(e)
try:
    print(d.get_item("key3", default = "Default Value"))
except Exception as e:
    print(e)
try:
    d.get_item("key3")
except Exception as e:
    print(e)
try:
    print(d.pop_item())
except Exception as e:
    print(e)
try:
    print(d.get_item("key1", error_msg = "error message"))
except Exception as e:
    print(e)
try:
    print(d.get_item("key2", error_msg = "error message2"))
except Exception as e:
    print(e)
try:
    d.pop_item()
except Exception as e:
    print(e)
try:
    d.get_item("key3", default = "Default Value", raise_error = True, error_msg = "Hi")
except Exception as e:
    print(e)'''
