def template():
    return '''
            import unittest

            {imports}


            class {classname}(unittest.TestCase):
            \"\"\"{description}\"\"\"
                def testCase1(self):
                    self.assertTrue(is_prime(7), "7 should noot be prime")

                {test cases}

            if __name__ == '__main__':
                unittest.main()

                '''


def is_empty(word):
    return len(word.strip()) != 0


def lines(textContents):
    return textContents.split("\n")


# def unlines(lineData):
#     return "\n".join(lineData)


def capitalize(word):
    return word[0].upper() + word[1:]


def get_test_filename(dsl_filename):
    return dsl_filename.replace(".dsl", ".py")


def get_test_classname(dsl_filename):
    raw_classname = dsl_filename.replace(".dsl", "")

    parts = raw_classname.split("_")
    parts = filter(is_empty, parts)
    parts = map(capitalize, parts)
    parts = list(parts)

    return "".join(parts)


def get_file(file):
    return open(file).read()


# def compose(f, g):
#     return lambda x: f(g(x))


def is_import(line):
    return "->" not in line and "import" in line


def strip(string):
    return string.strip()


def test_has_assertTrue(line):
    parts = line.split("==")
    parts = list(map(strip, parts))
    return "True" in parts


def test_has_assertFalse(line):
    parts = line.split("==")
    parts = list(map(strip, parts))
    return "False" in parts


def get_imports(contents):
    result = list(filter(is_import, contents))
    contents = list(filter(not is_import, contents))
    return result


def main():
    contents = lines(get_file("is_prime_test.dsl"))
    no_empty_lines = list(filter(is_empty, contents))
    imports = get_imports(no_empty_lines)
    description = contents[0]
    contents = contents[1:]
    tests_true = list(filter(test_has_assertTrue, contents))
    tests_false = list(filter(test_has_assertFalse, contents))
    tests_equal = contents - tests_true - tests_false


if __name__ == '__main__':
    main()
