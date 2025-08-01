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

Blazingly fast background queue manager plugin for running coroutines with fine-tuned control.
Makes use of [uvloop](https://github.com/MagicStack/uvloop) to achieve simple, but powerful
speed upgrade while maintaining [AsyncIO](https://docs.python.org/3/library/asyncio.html)-compliant
This plugin designed and tested on the following ASGI frameworks.

* [FastAPI](https://fastapi.tiangolo.com)
  framework, high performance, easy to learn, fast to code, ready for production
* [Litestar](https://litestar.dev)
  \- build performant APIs with Litestar; powerful, lightweight & flexible ASGI framework
* [Starlette](https://www.starlette.io/)
  , the little ASGI framework that shines ✨

### Alternatives

* [FastAPI BackgroundTasks](https://fastapi.tiangolo.com/tutorial/background-tasks)
  > :information_source: see [Starlette BackgroundTasks](https://www.starlette.io/background)
* [Litestar BackgroundTasks](https://docs.litestar.dev/2/reference/background_tasks.html)
* [Starlette BackgroundTasks](https://www.starlette.io/background)
* [Celery]()
  > :information_source: see [Asynchronous Tasks with FastAPI and Celery, TestDriven](https://testdriven.io/blog/fastapi-and-celery)
* [Dramatiq: background tasks](https://dramatiq.io) [(repository)](https://github.com/Bogdanp/dramatiq)
  > :information_source: see [daconjurer/fastapi-dramatiq](https://github.com/daconjurer/fastapi-dramatiq)

### Prerequisites

* [python](https://www.python.org) 3.9 and above - High-level general-purpose programming language
* [pip](https://pypi.org/project/pip/) - The PyPA recommended tool for installing Python packages.

### Getting started

You can use `etiquette` simply by installing via `pip` on your terminal emulator of choice.

```sh
pip install 'etiquette[standard]'
```

Or opt out from `uvloop` by running the following command:

```sh
pip install etiquette
```

Then you can integrate this library in your ASGI codebase using the lifespan manager
as such:

```python
from asyncio import sleep
from contextlib import asynccontextmanager
from etiquette import Decorum, Etiquette
from fastapi import Depends, FastAPI
from typing import Annotated

@asynccontextmanager
async def lifespan(app):
  Etiquette.initiate(max_concurrent_tasks=16)
  yield
  await Etiquette.release()

app = FastAPI(lifespan=lifespan)

@app.get("/sleep")
async def add_sleep_task_to_queue(decorum: Annotated[Decorum, Depends(Decorum)]) -> str:
  async def sleep_3() -> None:
    await sleep(3)
    print("task done")

  await decorum.add_task(sleep_3)
  return "OK"
```

The above is an example written in FastAPI framework, for Litestar see below:

```python
from asyncio import sleep
from contextlib import asynccontextmanager
from etiquette import Decorum, Etiquette
from litestar import Litestar, get
from litestar.di import Provide
from typing import AsyncGenerator

@asynccontextmanager
async def lifespan(app):
  Etiquette.initiate(max_concurrent_tasks=16)
  yield
  await Etiquette.release()

@get("/sleep", dependencies={"decorum": Provide(Decorum, sync_to_thread=True)})
async def add_sleep_task_to_queue(decorum: Decorum) -> str:
  async def sleep_3() -> None:
    await sleep(3)
    print("task done")

  await decorum.add_task(sleep_3)
  return "OK"

app = Litestar(lifespan=[lifespan], route_handlers=[add_sleep_task_to_queue])
```

See other examples such as Starlette, ... under `examples` directory.

## Contributions

### Project structure

```
etiquette/
│
├── src/
│   └── etiquette/
│       ├── __init__.py       # Entrypoint to the etiquette package
│       ├── _types.py         # Defines internal dataclass object `TaskData`
│       ├── core.py           # Defines `Etiquette` core where shared class vars are initiated
│       └── decorum.py        # Defines `Decorum` class utilized by Dependency Injection
│
├── static/
│   ├── etiquette.svg         # Graphics representing project
│   ├── etiquette-banner.svg  # Project banner displayed on README.md
│   └── etiquette-social.svg  # Social media preview banner
│
├── LICENSE                   # Details of MIT License
└── README.md                 # Descriptions and roadmap
```

Notable exemptions: `dotfiles`, `examples` and, `tests`

### Change-logs

* **0.0.1** proof of concept, with FastAPI and Litestar examples
* **0.0.2** integrate with Starlette State, and annotate types 
* **0.0.3** define `etiquette[standard]` install with `uvloop`

### Roadmap

* Validates task failing will retry a pre-determined set of times
* Add [testcontainers](https://github.com/testcontainers/testcontainers-python)
  and attempt complex I/O bound tasks
* Experiment with Server-Side Events

### Prerequisites

* [git](https://git-scm.com/) - --fast-version-control
* [python](https://www.python.org) 3.9 and above - High-level general-purpose programming language
* [uv](https://docs.astral.sh/uv) - Extremely fast Python package & project manager, written in Rust

The following guide walks through setting up your local working environment using `git`
as distributed version control system and `uv` as Python package and version manager.
If you do not have `git` installed, run the following command.

<details>
  <summary> Install using Homebrew (Darwin) </summary>
  
  ```bash
  brew install git
  ```
</details>

<details>
  <summary> Install via binary installer (Linux) </summary>
  
  * Debian-based package management
  ```bash
  sudo apt install git-all
  ```

  * Fedora-based package management
  ```bash
  sudo dnf install git-all
  ```
</details>

If you do not have `uv` installed, run the following command.

<details>
  <summary> Install using Homebrew (Darwin) </summary>

  ```bash
  brew install uv
  ```
</details>

<details>
  <summary> Install using standalone installer (Darwin and Linux) </summary>

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
</details>

Once you have `git` distributed version control system installed, you can
clone the current repository and  install any version of Python above version
3.9 for this project. The following commands help you set up and activate a
Python virtual environment where `uv` can download project dependencies from the `PyPI`
open-sourced registry defined under `pyproject.toml` file.

<details>
  <summary> Set up environment and synchronize project dependencies </summary>

  ```bash
  git clone git@github.com:aekasitt/etiquette.git
  cd etiquette
  uv venv --python 3.13.5
  source .venv/bin/activate
  uv sync --dev
  ```
</details>

### Run examples

We need to install a few extra dependencies to run attached examples found
under the `examples` directory on root. First run the following command:

```sh
uv sync --dev --group examples
```

<details>
  <summary> Sample installation output for examples' dependencies </summary>

  ```sh
  $ uv sync --dev --group examples
  > Resolved 48 packages in 1ms
  > Installed 29 packages in 58ms
  >  + annotated-types==0.7.0
  >  + anyio==4.9.0
  >  + certifi==2025.7.14
  >  + click==8.2.1
  >  + faker==37.4.2
  >  + fastapi==0.116.1
  >  + h11==0.16.0
  >  + httpcore==1.0.9
  >  + httpx==0.28.1
  >  + idna==3.10
  >  + litestar==2.16.0
  >  + litestar-htmx==0.5.0
  >  + markdown-it-py==3.0.0
  >  + mdurl==0.1.2
  >  + msgspec==0.19.0
  >  + multidict==6.6.3
  >  + multipart==1.2.1
  >  + polyfactory==2.22.1
  >  + pydantic==2.11.7
  >  + pydantic-core==2.33.2
  >  + pygments==2.19.2
  >  + pyyaml==6.0.2
  >  + rich==14.0.0
  >  + rich-click==1.8.9
  >  + sniffio==1.3.1
  >  + starlette==0.47.2
  >  + typing-inspection==0.4.1
  >  + tzdata==2025.2
  >  + uvicorn==0.35.0
  ```
</details>

Now you can run all four attached examples as such using the `uvicorn` command installed
above: The four examples include:

1. FastAPI using Decorum to add an AsyncIO sleeping task
    ```sh
    uvicorn examples.fastapi_sleeper:app --port 8000 --reload
    ```
2. FastAPI using Decorum to interact with a thread-safe [AtomicCounter](https://gist.github.com/benhoyt/8c8a8d62debe8e5aa5340373f9c509c7)
    ```sh
    uvicorn examples.fastapi_counter:app --port 8000 --reload
    ```
3. Litestar using Decorum to add an AsyncIO sleeping task
    ```sh
    uvicorn examples.litestar_sleeper:app --port 8000 --reload
    ```
4. Litestar using Decorum to interact with a thread-safe [AtomicCounter](https://gist.github.com/benhoyt/8c8a8d62debe8e5aa5340373f9c509c7)
    ```sh
    uvicorn examples.litestar_counter:app --port 8000 --reload
3. Starlette using Decorum to add an AsyncIO sleeping task
    ```sh
    uvicorn examples.starlette_sleeper:app --port 8000 --reload
    ```
4. Starlette using Decorum to interact with a thread-safe [AtomicCounter](https://gist.github.com/benhoyt/8c8a8d62debe8e5aa5340373f9c509c7)
    ```sh
    uvicorn examples.starlette_counter:app --port 8000 --reload
    ```

### Tests

This project uses `pytest` to run automated tests. Install the dependencies with:

```sh
uv sync --dev --group tests
```

<details>
  <summary> Sample installation output for development and test dependencies </summary>

  ```sh
  $ uv sync --dev --group tests
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
  > │ root /.../.../.../etiquette                                                              │
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

1. [หมึกหมด - Muekmod](https://www.f0nt.com/release/sov-muekmod/)
  typeface by [uvSOV - Worawut Thanawatanawanich](https://fb.com/worawut.thanawatanawanich)

## License

This project is licensed under the terms of the MIT license.
