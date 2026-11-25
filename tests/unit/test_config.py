import dataclasses
import pytest
from framework.config import Config

VARS = ["API_BASE_URL", "UI_BASE_URL", "API_TIMEOUT", "UI_TIMEOUT", "HEADLESS", "BROWSER"]

def test_defaults_are_used_when_variables_are_unset(monkeypatch):
    for name in VARS:
        monkeypatch.delenv(name, raising=False)
    config = Config.from_env()
    assert config.api_base_url == "https://api.practicesoftwaretesting.com"
    assert config.ui_base_url == "https://practicesoftwaretesting.com"
    assert config.api_timeout == 15.0
    assert config.ui_timeout == 10.0
    assert config.headless is True
    assert config.browser == "chrome"

def test_environment_variables_override_defaults(monkeypatch):
    monkeypatch.setenv("API_TIMEOUT", "30")
    monkeypatch.setenv("UI_TIMEOUT", "5")
    monkeypatch.setenv("HEADLESS", "false")
    monkeypatch.setenv("BROWSER", "Firefox")
    cfg = Config.from_env()
    assert cfg.api_timeout == 30.0
    assert cfg.ui_timeout == 5.0
    assert cfg.headless is False
    assert cfg.browser == "firefox"

def test_config_cannot_be_changed_after_creation():
    cfg = Config.from_env()
    with pytest.raises(dataclasses.FrozenInstanceError):
        cfg.browser = "safari"