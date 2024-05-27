#!/usr/bin/python3
def to_json_string(my_obj):
    """Devuelve la representación JSON de un objeto como una cadena."""
    if isinstance(mi_obj, str):
        return '"' + mi_obj.replace('\\', '\\\\').replace('"', '\\"') + '"'
    elif isinstance(mi_obj, (int, float)):
        return str(mi_obj)
    elif isinstance(mi_obj, bool):
        return 'true' if mi_obj else 'false'
    elif mi_obj is None:
        return 'null'
    elif isinstance(mi_obj, dict):
        elementos = []
        for clave, valor in mi_obj.items():
            elementos.append(a_cadena_json(clave) + ':' + a_cadena_json(valor))
        return '{' + ','.join(elementos) + '}'
    elif isinstance(mi_obj, list):
        elementos = [a_cadena_json(elemento) for elemento in mi_obj]
        return '[' + ','.join(elementos) + ']'
    else:
        raise TypeError("El objeto de tipo {} no es serializable a JSON".format(type(mi_obj).__name__))
