#!/usr/bin/env python3.9
# Copyright (C) 2025 All rights reserved.
# FILENAME:    ~~/src/etiquette/__init__.py
# VERSION:     0.0.1
# CREATED:     2025-07-19 13:57
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION: https://www.w3docs.com/snippets/python/what-is-init-py-for.html
#
# HISTORY:
# *************************************************************
"""
Tests for Etiquette plugin for ASGI frameworks
"""

### Standard packages ###
from asyncio import Lock, sleep
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from typing import Annotated, AsyncGenerator, Final

### Third-party packages ###
from fastapi import FastAPI
from fastapi.param_functions import Depends
from fastapi.testclient import TestClient
from pytest import fixture
from starlette.reqeusts import Request
from starlette.responses import JSONResponse, PlainTextResponse

### Local modules ###
from etiquette import Decorum, Etiquette


@fixture
def test_client() -> TestClient:
  """
  Sets up a FastAPI TestClient wrapped around an application implementing both
  Context and Headers extension pattern

  ---
  :return: test client fixture used for local testing
  :rtype: fastapi.testclient.TestClient
  """

  @asynccontextmanager
  async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    Etiquette.initiate()
    yield
    await Etiquette.release()

  app = FastAPI(lifespan=lifespan)

  @dataclass
  class UnsafeCounter:
    """Counter without thread safety - demonstrates race condition"""
    count: int = 0

    async def increment(self) -> None:
      current = self.count
      await sleep(0.001)
      self.count = current + 1
      print(f"Unsafe: {self.count=}")

  @dataclass
  class SafeCounter:
    """Counter with thread safety - fixes race condition"""
    count: int = 0
    _lock: Lock = field(default_factory=Lock, init=False)

    async def increment(self) -> None:
      async with self._lock:
        current = self.count
        await sleep(0.001)
        self.count = current + 1
        current_count = self.count
      print(f"Safe: {current_count=}")

  safe_counter: SafeCounter = SafeCounter()

  @app.get("/safe-counter")
  def increment_safe_counter(decorum: Annotated[Decorum, Depends(Decorum)]) -> str:
    decorum.add_task(safe_counter.increment)
    return "OK"

  unsafe_counter: UnsafeCounter = UnsafeCounter()

  @app.get("/unsafe-counter", response_class=PlainTextResponse)
  def increment_unsafe_counter(decorum: Annotated[Decorum, Depends(Decorum)]) -> str:
    decorum.add_task(unsafe_counter.increment)
    return "OK"

  @app.exception_handler(ValueError)
  def csrf_protect_error_handler(request: Request, exc: ValueError) -> JSONResponse:
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})

  return TestClient(app)


__all__: Final[tuple[str, ...]] = ("test_client",)
