# Writing Tests

It is expected that all test scripts will be in the same directory. Some people use this organizations:

```
area/
├── area
│   └── area.py
└── tests
    └── test_area.py
```

Others embed the tests directory in this form:

```
area/
└── area
    ├── area.py
    └── tests
        └── test_area.py
```

Either layout is acceptable.
While pytest, nosetests, and others would find the tests in other locations these forms make it more human readable and follow the convention of other python developers

As far as the actual code, test scripts should have the form `test_[name].py` or `[name]_test.py` to be detected. Also functions inside those files should have `test` at the beginning or end of their names as well (with the `_` separation). You can provide other functions in your tests scripts if you need them, but if they aren't testing the package you should not include `test` in their name.
