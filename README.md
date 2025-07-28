# Etiquette

[![Package version](https://img.shields.io/pypi/v/etiquette)](https://pypi.org/project/etiquette)
[![Format](https://img.shields.io/pypi/format/etiquette)](https://pypi.org/project/etiquette)
[![Python version](https://img.shields.io/pypi/pyversions/etiquette)](https://pypi.org/project/etiquette)
[![License](https://img.shields.io/pypi/l/etiquette)](https://pypi.org/project/etiquette)
[![Top](https://img.shields.io/github/languages/top/aekasitt/etiquette)](.)
[![Languages](https://img.shields.io/github/languages/count/aekasitt/etiquette)](.)
[![Size](https://img.shields.io/github/repo-size/aekasitt/etiquette)](.)
[![Last commit](https://img.shields.io/github/last-commit/aekasitt/etiquette/master)](.)
[![Documentation](https://img.shields.io/badge/pdoc-555?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwBAMAAAClLOS0AAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAkUExURUdwTJHtkZDtkI/vj2rOYFXBQn3deZDukDuzAHDTaFrES4HhfmcEZqoAAAAHdFJOUwCAv0Df788Wv3t3AAACCElEQVQ4y42UsXKcMBCGuVC4Pc6FJuPGRzLDnK/xnAsKP0IeIU+QLhyFEHoAVlJlNxJHlwbBVY4LyeeXs4BLCnQzCTOAZj+0K+3/iyD4zwvhIIiiey/+iVRB8LnJPJBq6QA8eeBRuI8R8UFKTYbc7QGqQRIAOa++KKAD6LW4nQMFwgIB7gMlLaPQz8GVMlhxjD2AoKVcSeKl2jCAyq2K/5yBsiINRqSx+QwUcmhgFNmXOWivzO2CZsWTlyrl2U69qPmMjUi0pBqreY0bvi8BGGHzVaVKJnWHi2o5bwlhOI4JGF9yzeuTPua+5qoHEHvfDAvF398qPz70vboRl4DV8vESCC3HqSfsAAotkNf0sY1HhnR+AZTQruzrBXAHLLe/h9HDtIRwFa+v3XvL4bX8NXpvrLTDb31tImdezvO7dgipAYTOmhyYXAYptOvNuPVR99Ry24BieJlqEX8bdzhUWlBo3JQTMExZ//X7BNplmCgN4t3FFdecnUHJcHLi6ogfEurCujdlMwK38AMItd/FETp0TD2vi6nvW3AHYkje1VmcKJ6humyn46hB1ebkqPwhsYkJs8+jmLYp2Z5AgwkfnlRLPR7BsBTYUH3M7pEVRAMcT2dXbbWLM6d/SEFi6pKayVU75z2Oh3FKoKt7Lv/IkRw6M4mJXKrerP8aII6vz8MVxvsv//gNfQBIOvQNeKr0GQAAAABJRU5ErkJggg==)](https://aekasitt.github.io/etiquette)

[![Etiquette Banner](./static/etiquette-banner.svg)](https://github.com/aekasitt/etiquette/blob/master/static/etiquette-banner.svg)

Plugin designed for `dependency injection` pattern offered by following ASGI frameworks

* [FastAPI](https://fastapi.tiangolo.com)
  framework, high performance, easy to learn, fast to code, ready for production
* [Litestar](https://litestar.dev)
  \- build performant APIs with Litestar; powerful, lightweight & flexible ASGI framework

### Prerequisites

* [python](https://www.python.org) 3.9 and above - High-level general-purpose programming language
* [pip](https://pypi.org/project/pip/) - The PyPA recommended tool for installing Python packages.

### Getting started

You can use `etiquette` simply by installing via `pip` on your terminal emulator of choice.

```sh
pip install etiquette
```

TODO: TBD;

### Run examples

## Contribution

### Prerequisites

* [python](https://www.python.org) 3.9 and above - High-level general-purpose programming language
* [uv](https://docs.astral.sh/uv) - Extremely fast Python package & project manager, written in Rust

TODO: TBD;

### Tests

This project uses `pytest` to run automated tests. Install the dependencies with:

```sh
uv sync --dev --group=tests
```

<details>
  <summary> Sample installation output for development and test dependencies </summary>

  ```sh
  $ uv sync --dev --group=tests
  > Resolved 48 packages in 9ms
  > Installed 40 packages in 104ms
  >  + annotated-types==0.7.0
  >  + anyio==4.9.0
  >  + certifi==2025.7.14
  >  + click==8.2.1
  >  + etiquette==0.0.1 (from file:///.../.../.../etiquette)
  >  + faker==37.4.2
  >  + fastapi==0.116.1
  >  + h11==0.16.0
  >  + httpcore==1.0.9
  >  + httpx==0.28.1
  >  + idna==3.10
  >  + iniconfig==2.1.0
  >  + litestar==2.16.0
  >  + litestar-htmx==0.5.0
  >  + markdown-it-py==3.0.0
  >  + mdurl==0.1.2
  >  + msgspec==0.19.0
  >  + multidict==6.6.3
  >  + multipart==1.2.1
  >  + mypy==1.17.0
  >  + mypy-extensions==1.1.0
  >  + packaging==25.0
  >  + pathspec==0.12.1
  >  + pluggy==1.6.0
  >  + polyfactory==2.22.1
  >  + pydantic==2.11.7
  >  + pydantic-core==2.33.2
  >  + pygments==2.19.2
  >  + pytest==8.4.1
  >  + pytest-asyncio==1.1.0
  >  + pytest-modern==0.7.3
  >  + pyyaml==6.0.2
  >  + rich==14.0.0
  >  + rich-click==1.8.9
  >  + ruff==0.12.4
  >  + sniffio==1.3.1
  >  + starlette==0.47.2
  >  + typing-extensions==4.14.1
  >  + typing-inspection==0.4.1
  >  + tzdata==2025.2
  ```
</details>

Then, run the tests with 

```sh
pytest
```

<details>
  <summary> Sample outputs of successful test running </summary>

  ```sh
  $ pytest
  > ╭─────────────────────────────────── test session starts ──────────────────────────────────╮
  > │ platform darwin pytest 8.4.1 python 3.13.5                                               │
  > │ plugins anyio-4.9.0, modern-0.7.3, asyncio-1.1.0, Faker-37.4.2                           │
  > │ root /Users/mackasitt/workspaces/pypi-etiquette                                          │
  > │ configfile pyproject.toml                                                                │
  > ╰──────────────────────────────────────────────────────────────────────────────────────────╯
  > Collected 14 items (14 selected)
  >       PASS [   1.293ms] tests/fastapi/cancelled.py::test_sure_fail_counter
  >       PASS [   27.17ms] tests/fastapi/race.py::test_safe_counter
  >       PASS [   8.912ms] tests/fastapi/race.py::test_unsafe_counter
  >       PASS [   27.29ms] tests/fastapi/splat.py::test_safe_counter_using_path_parameters
  >       PASS [   26.56ms] tests/fastapi/splat.py::test_safe_counter_using_query_parameters
  >       PASS [   8.681ms] tests/fastapi/splat.py::test_unsafe_counter_using_path_parameters
  >       PASS [   10.18ms] tests/fastapi/splat.py::test_unsafe_counter_using_query_parameters
  >       PASS [   1.919ms] tests/litestar/cancelled.py::test_sure_fail_counter
  >       PASS [   28.65ms] tests/litestar/race.py::test_safe_counter
  >       PASS [   10.62ms] tests/litestar/race.py::test_unsafe_counter
  >       PASS [   29.04ms] tests/litestar/splat.py::test_safe_counter_using_path_parametes
  >       PASS [   31.94ms] tests/litestar/splat.py::test_safe_counter_using_query_parameters
  >       PASS [   10.45ms] tests/litestar/splat.py::test_unsafe_counter_using_path_parameters
  >       PASS [   11.25ms] tests/litestar/splat.py::test_unsafe_counter_using_query_parameters
  > ──────────
  >    Summary [   234.0ms] 14 tests run: 14 passed
  ```
</details>

Refer to the [pytest documentation](https://docs.pytest.org/) for more advanced options.

## Acknowledgements

TODO: TBD;

## License

This project is licensed under the terms of the MIT license.
