import os
import yaml
from typing import Dict


class Config:
    """
    A singleton class that manages configuration settings for the Agentarium framework.

    This class handles configuration loading from multiple sources with the following priority:
    1. Environment variables (highest priority)
    2. config.yaml file
    3. Default values (lowest priority)

    The configuration currently supports:
    - LLM provider and model settings

    Environment variables:
    - AGENTARIUM_LLM_PROVIDER: The LLM provider to use
    - AGENTARIUM_LLM_MODEL: The specific model to use

    Example config.yaml:
        llm:
          provider: "openai"
          model: "gpt-4o-mini"
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        """
        Implement the singleton pattern to ensure only one config instance exists.

        Returns:
            Config: The single instance of the Config class.
        """
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Initialize the configuration if not already initialized.

        Due to the singleton pattern, this will only execute once,
        even if multiple instances are created.
        """
        if not self._initialized:
            self._config = {}
            self._load_config()
            self._initialized = True

    def _load_config(self) -> None:
        """
        Load configuration from all sources in order of priority.

        The configuration is loaded in the following order:
        1. Set default values
        2. Override with values from config.yaml if it exists
        3. Override with environment variables if they exist
        """
        # Default values
        self._config = {
            "aisuite": dict(),
            "llm": {
                "provider": "openai",
                "model": "gpt-4o-mini"
            }
        }

        # Try to load from config.yaml in the current directory
        config_path = "config.yaml"
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                yaml_config = yaml.safe_load(f)
                if yaml_config:
                    self._deep_update(self._config, yaml_config)

        # Override with environment variables if they exist
        self._config["aisuite"] = os.getenv("AGENTARIUM_AISUITE", self._config["aisuite"])
        self._config["llm"]["provider"] = os.getenv("AGENTARIUM_LLM_PROVIDER", self._config["llm"]["provider"])
        self._config["llm"]["model"] = os.getenv("AGENTARIUM_LLM_MODEL", self._config["llm"]["model"])


    def _deep_update(self, d: Dict, u: Dict) -> Dict:
        """
        Recursively update a dictionary with values from another dictionary.

        Args:
            d (Dict): The base dictionary to update
            u (Dict): The dictionary containing update values

        Returns:
            Dict: The updated dictionary
        """
        for k, v in u.items():
            if isinstance(v, dict):
                d[k] = self._deep_update(d.get(k, {}), v)
            else:
                d[k] = v
        return d

    @property
    def llm_provider(self) -> str:
        """
        Get the configured LLM provider.

        Returns:
            str: The name of the LLM provider (e.g., "openai", "anthropic")
        """
        return self._config["llm"]["provider"]

    @property
    def llm_model(self) -> str:
        """
        Get the configured LLM model.

        Returns:
            str: The name of the specific model to use (e.g., "gpt-4o-mini")
        """
        return self._config["llm"]["model"]

    @property
    def aisuite(self) -> dict:
        """
        Get the configured aisuite configuration.
        """
        return self._config["aisuite"]
