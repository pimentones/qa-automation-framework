# Central settings for the framework, loaded from environment variables or from .env file
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file if it exists. By default uses environment values

def _env_bool(name: str, default: bool) -> bool:
    return os.getenv(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}

@dataclass(frozen=True)
class Config:
    api_base_url: str
    ui_base_url: str
    api_timeout: float
    ui_timeout: float
    headless: bool
    browser: str

    @classmethod
    def from_env(cls) -> "Config":
        return cls(
            api_base_url=os.getenv("API_BASE_URL", "https://api.practicesoftwaretesting.com"),
            ui_base_url=os.getenv("UI_BASE_URL", "https://practicesoftwaretesting.com"),
            api_timeout=float(os.getenv("API_TIMEOUT", "15.0")),
            ui_timeout=float(os.getenv("UI_TIMEOUT", "10.0")),
            headless=_env_bool("HEADLESS", True),
            browser=os.getenv("BROWSER", "chrome").strip().lower(),
        )

config = Config.from_env()