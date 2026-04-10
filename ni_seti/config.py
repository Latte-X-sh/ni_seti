"""Configuration management for ni_seti"""
import json
from pathlib import Path
from typing import Optional, Dict, Any


CONFIG_DIR = Path.home() / ".config" / "ni_seti"
CONFIG_FILE = CONFIG_DIR / "config.json"


def ensure_config_dir():
    """Ensure the config directory exists"""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def config_exists() -> bool:
    """Check if configuration file exists"""
    return CONFIG_FILE.exists()


def load_config() -> Dict[str, Any]:
    """Load configuration from file"""
    if not config_exists():
        return {}

    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)


def save_config(config: Dict[str, Any]):
    """Save configuration to file"""
    ensure_config_dir()
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)


def get_aws_profile() -> Optional[str]:
    """Get the configured AWS profile"""
    config = load_config()
    return config.get('aws', {}).get('profile')


def set_aws_profile(profile: str):
    """Set the AWS profile in configuration"""
    config = load_config()
    if 'aws' not in config:
        config['aws'] = {}
    config['aws']['profile'] = profile
    save_config(config)


def get_program_mappings() -> Dict[str, str]:
    """Get program-specific AWS profile mappings"""
    config = load_config()
    return config.get('aws', {}).get('program_mappings', {})


def set_program_mapping(program: str, profile: str):
    """Set AWS profile for a specific program"""
    config = load_config()
    if 'aws' not in config:
        config['aws'] = {}
    if 'program_mappings' not in config['aws']:
        config['aws']['program_mappings'] = {}
    config['aws']['program_mappings'][program] = profile
    save_config(config)
