def validate(result, expected, raise_assertion: bool = True):
    print(result, expected)
    try:
        assert result == expected, f'{result} != {expected}'
    except AssertionError as e:
        if raise_assertion:
            raise e
