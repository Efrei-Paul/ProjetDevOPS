#!/usr/bin/python3

import model_dashboard
import pytest

def test_model_dashboard():
	assert model_dashboard.build_model(0,0,0)
