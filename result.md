```shell
$ pipenv run make test
'python3' -m pytest funcs.py tests
========================================================================= test session starts ==========================================================================
platform darwin -- Python 3.8.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- /Users/nvzhiga/.local/share/virtualenvs/avito-hw-6-functional-hqFcUw5j/bin/python3
cachedir: .pytest_cache
rootdir: /Users/nvzhiga/code/python/avito-hw-6-functional, configfile: setup.cfg
plugins: flake8-1.0.7
collected 28 items

funcs.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)                                                                                               [  3%]
funcs.py::funcs.chunks PASSED                                                                                                                                    [  7%]
funcs.py::funcs.distinct PASSED                                                                                                                                  [ 10%]
funcs.py::funcs.first PASSED                                                                                                                                     [ 14%]
funcs.py::funcs.flatten PASSED                                                                                                                                   [ 17%]
funcs.py::funcs.groupby PASSED                                                                                                                                   [ 21%]
funcs.py::funcs.ilen1 PASSED                                                                                                                                     [ 25%]
funcs.py::funcs.ilen2 PASSED                                                                                                                                     [ 28%]
funcs.py::funcs.ilen3 PASSED                                                                                                                                     [ 32%]
funcs.py::funcs.last PASSED                                                                                                                                      [ 35%]
tests/test_funcs.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)                                                                                    [ 39%]
tests/test_funcs.py::test_flatten[given0-expected0] PASSED                                                                                                       [ 42%]
tests/test_funcs.py::test_flatten[given1-expected1] PASSED                                                                                                       [ 46%]
tests/test_funcs.py::test_flatten[given2-expected2] PASSED                                                                                                       [ 50%]
tests/test_funcs.py::test_flatten[given3-expected3] PASSED                                                                                                       [ 53%]
tests/test_funcs.py::test_distinct[given0-expected0] PASSED                                                                                                      [ 57%]
tests/test_funcs.py::test_distinct[given1-expected1] PASSED                                                                                                      [ 60%]
tests/test_funcs.py::test_distinct[given2-expected2] PASSED                                                                                                      [ 64%]
tests/test_funcs.py::test_distinct[given3-expected3] PASSED                                                                                                      [ 67%]
tests/test_ilen.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)                                                                                     [ 71%]
tests/test_ilen.py::test_ilen[<genexpr>-10] SKIPPED (unconditional skip)                                                                                         [ 75%]
tests/test_ilen.py::test_ilen[<genexpr>-0] SKIPPED (unconditional skip)                                                                                          [ 78%]
tests/test_ilen.py::test_ilen[given2-5] SKIPPED (unconditional skip)                                                                                             [ 82%]
tests/test_ilen.py::test_ilen[given3-0] SKIPPED (unconditional skip)                                                                                             [ 85%]
tests/test_ilen.py::test_ilen[given4-3] SKIPPED (unconditional skip)                                                                                             [ 89%]
tests/test_ilen.py::test_measure1 SKIPPED (unconditional skip)                                                                                                   [ 92%]
tests/test_ilen.py::test_measure2 SKIPPED (unconditional skip)                                                                                                   [ 96%]
tests/test_ilen.py::test_measure3 SKIPPED (unconditional skip)                                                                                                   [100%]

==================================================================== 17 passed, 11 skipped in 0.11s ====================================================================
```