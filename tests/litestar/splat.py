#!/usr/bin/env python3.9
# coding:utf-8
# Copyright (C) 2025 All rights reserved.
# FILENAME:    ~~/tests/litestar/splat.py
# VERSION:     0.0.1
# CREATED:     2025-07-26 12:21
# AUTHOR:      Sitt Guruvanich <aekazitt+github@gmail.com>
# DESCRIPTION: Test script to demonstrate Decorum passing splat arguments
#
# HISTORY:
# *************************************************************
"""
Tests for Etiquette plugin for Decorum passing splat arguments on Litestar
"""

### Third-party packages ###
from litestar.testing import TestClient
from httpx import Response
from pytest import mark

### Local modules ###
from tests.litestar import test_client


@mark.asyncio
async def test_safe_counter(test_client: TestClient) -> None:
  """Test to demonstrate passing splat arguments on SafeCounter"""
  for i in range(20):
    test_client.get(f"/safe-counter/{i}")
  response: Response = test_client.get(f"/safe-counter/{i}")
  assert int(response.text) == sum(range(20))


@mark.asyncio
async def test_unsafe_counter(test_client: TestClient) -> None:
  """Test to demonstrate passing splat arguments on UnsafeCounter"""
  for i in range(20):
    test_client.get(f"/unsafe-counter/{i}")
  response: Response = test_client.get(f"/unsafe-counter/{i}")
  assert int(response.text) < sum(range(20))
