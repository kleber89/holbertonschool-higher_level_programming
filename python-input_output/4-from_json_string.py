#!/usr/bin/python3
def from_json_string(my_str):
    """Devuelve un objeto (estructura de datos de Python) representado por una cadena JSON."""
    
    def parse_value(s, index):
        if s[index] == '"':
            return parse_string(s, index)
        elif s[index] == '{':
            return parse_object(s, index)
        elif s[index] == '[':
            return parse_array(s, index)
        elif s[index:index + 4] == 'true':
            return True, index + 4
        elif s[index:index + 5] == 'false':
            return False, index + 5
        elif s[index:index + 4] == 'null':
            return None, index + 4
        else:
            return parse_number(s, index)
    
    def parse_string(s, index):
        end_index = index + 1
        while s[end_index] != '"':
            if s[end_index] == '\\':
                end_index += 1
            end_index += 1
        return s[index + 1:end_index].replace('\\"', '"').replace('\\\\', '\\'), end_index + 1
    
    def parse_number(s, index):
        end_index = index
        while end_index < len(s) and (s[end_index].isdigit() or s[end_index] in '-+eE.'):
            end_index += 1
        return float(s[index:end_index]) if '.' in s[index:end_index] else int(s[index:end_index]), end_index
    
    def parse_object(s, index):
        obj = {}
        index += 1
        while s[index] != '}':
            if s[index] == ',':
                index += 1
            key, index = parse_string(s, index)
            index += 1  # skip colon
            value, index = parse_value(s, index)
            obj[key] = value
        return obj, index + 1
    
    def parse_array(s, index):
        arr = []
        index += 1
        while s[index] != ']':
            if s[index] == ',':
                index += 1
            value, index = parse_value(s, index)
            arr.append(value)
        return arr, index + 1

    result, _ = parse_value(mi_str.strip(), 0)
    return result
