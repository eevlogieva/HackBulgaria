def extract_type(elements, given_type):
    filtered = [str(x[0]) * x[1] for x in elements if type(x[0]) == given_type]
    return "".join(filtered)


def reversed_dict(to_be_reversed):
    return {to_be_reversed[item]: item for item in to_be_reversed}


def reps(elements):
    return tuple([elem for elem in elements if elements.count(elem) > 1])


def flatten_dict(elements):
    result = {}
    for key in elements:
        if type(elements[key]) is not dict:
            result[key] = elements[key]
        else:
            flat = flatten_dict(elements[key])
            result.update({"{}.{}".format(key, x): flat[x] for x in flat})
    return result


def merge_dicts(elements1, elements2):
    for key in elements2:
        if key not in elements1:
            elements1[key] = elements2[key]
        else:
            merge_dicts(elements1[key], elements2[key])


def unflatten_dict(elements):
    result = {}
    for key in elements:
        split_key = key.split('.')
        if len(split_key) == 1:
            result[key] = elements[key]
        elif split_key[0] not in result:
            result[split_key[0]] = unflatten_dict({'.'.join(split_key[1:]):
                                                   elements[key]})
        else:
            merge_dicts(result[split_key[0]],
                        unflatten_dict({'.'.join(split_key[1:]):
                                        elements[key]}))
    return result
