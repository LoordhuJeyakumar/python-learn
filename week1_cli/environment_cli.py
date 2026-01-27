#!/usr/bin/env python3
"""
ENVIRONMENT VARIABLES & COMMAND-LINE ARGUMENTS - Complete Guide
==============================================================

Configuration is key to backend applications. Like a restaurant's settings:
- Environment variables = Chef's secret recipes (sensitive config)
- Command-line args = Daily specials menu (runtime options)
- Configuration files = Recipe book (persistent settings)

ANALOGY: Restaurant Configuration
- Environment variables = Secret ingredients (API keys, passwords)
- CLI arguments = Today's specials (debug mode, port number)
- Config files = Master recipe book (database settings, features)

WHY CONFIGURATION MATTERS:
- Security (keep secrets out of code)
- Flexibility (different settings per environment)
- Deployment (dev/prod/staging configs)
- Debugging (enable features dynamically)
"""

import os
import sys
import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional
import getpass

# ==========================================
# 1. ENVIRONMENT VARIABLES - System Configuration
# ==========================================

print("🌍 ENVIRONMENT VARIABLES - System Configuration")
print("=" * 55)



# Common environment variables
print(f"HOME directory: {os.environ.get('HOME', 'Not set')}")
print(f"Current user: {os.environ.get('USER', 'Unknown')}")
print(f"Shell: {os.environ.get('SHELL', 'Unknown')}")
print(f"PATH length: {len(os.environ.get('PATH', ''))} characters")
print()


# Safe environment variable access
def get_env_var(name: str, default: str = 'Not set') -> str:
    """
    Safely get environment variable with default
    checks if variable is set and returns default if not
    """
    value = os.environ.get(name, default)
    if not value and not default:
        raise ValueError(f"Environment variable {name} is not set and no default provided")
    return value


def get_env_bool(name: str, default: bool = False) -> bool:
    """
    Safely get environment variable as boolean with default
    checks if variable is set and returns default if not
    """
    value = os.environ.get(name, str(default)).lower()
    return value in ['true', '1', 'yes', 'y', 'on']

def get_env_int(name: str, default: int = 0) -> int:
    """Get integer environment variable."""
    try:
        return int(os.environ.get(name, str(default)))
    except ValueError:
        print(f"⚠️  Warning: '{name}' is not a valid integer, using default {default}")
        return default


# Example usage
try:
    api_key = get_env_var('API_KEY', 'default_key')
    print(f"API_KEY: {api_key}")
except ValueError as e:
    print(f"Error: {e}")
print()

try:
    is_debug = get_env_bool('DEBUG', False)
    print(f"DEBUG: {is_debug}")
except ValueError as e:
    print(f"Error: {e}")
print()

try:
    port = get_env_int('PORT', 8000)
    print(f"PORT: {port}")
except ValueError as e:
    print(f"Error: {e}")
print()


#Setting environment variables
os.environ['API_KEY'] = '1234567890'
os.environ['DEBUG'] = 'True'
os.environ['PORT'] = '8000'

print(f"API_KEY: {os.environ.get('API_KEY', 'Not set')}")
print(f"DEBUG: {os.environ.get('DEBUG', 'Not set')}")
print(f"PORT: {os.environ.get('PORT', 'Not set')}")
print()

# ==========================================
# 2. PRACTICAL BACKEND CONFIGURATION
# ==========================================

print("🏪 PRACTICAL BACKEND CONFIGURATION - Real App Settings")
print("=" * 55)

class AppConfig:
    """
    Application configuration from environment variables.

    ANALOGY: Restaurant settings loaded from the manager's notebook
    """

    def __init__(self):
        # Database settings
        self.db_host = get_env_var('DB_HOST', 'localhost')
        self.db_port = get_env_int('DB_PORT', 5432)
        self.db_name = get_env_var('DB_NAME', 'restaurant_db')
        self.db_user = get_env_var('DB_USER', 'admin')
        self.db_password = get_env_var('DB_PASSWORD', '1234567890')


        # Application settings
        self.app_name = get_env_var('APP_NAME', 'Restaurant App')
        self.app_version = get_env_var('APP_VERSION', '1.0.0')
        self.debug_mode = get_env_bool('DEBUG', False)
        self.port = get_env_int('PORT', 8000)

         # Feature flags
        self.enable_logging = get_env_bool('ENABLE_LOGGING', True)
        self.enable_metrics = get_env_bool('ENABLE_METRICS', False)
        self.max_connections = get_env_int('MAX_CONNECTIONS', 100)

    def get_database_url(self) -> str:
        """Build database connection URL."""
        if self.db_password:
            return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        else:
            return f"postgresql://{self.db_user}@{self.db_host}:{self.db_port}/{self.db_name}"


    def is_production(self) -> bool:
        """Check if running in production."""
        return get_env_var('ENVIRONMENT', 'development').lower() == 'production'

    def __str__(self) -> str:
        """String representation of config."""
        return f"{self.app_name} v{self.app_version} (Debug: {self.debug_mode})"



# Demo configuration
print("⚙️ Application configuration:")
config = AppConfig()
print(f"App: {config}")
print(f"Database URL: {config.get_database_url()}")
print(f"Production mode: {config.is_production()}")
print(f"Max connections: {config.max_connections}")
print()


# ==========================================
# 3. COMMAND-LINE ARGUMENTS - Runtime Options
# ==========================================
print("💻 COMMAND-LINE ARGUMENTS - Runtime Options")
print("=" * 55)

#Basic argument parsing
def basic_cli_demo():
    """Basic command-line argument parsing."""
    print(f"Script name: {sys.argv[0]}")
    print(f"Number of arguments: {len(sys.argv) - 1}")

    if len(sys.argv) > 1:
        print(f"Arguments: {sys.argv[1:]}")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")
    else:
        print("No arguments provided")
    print()

# Example usage
basic_cli_demo()



# Advanced argument parsing with argparse
def create_argument_parser():
    """Create a comprehensive argument parser."""

    parser = argparse.ArgumentParser(
        description="Restaurant Management System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python environment_cli.py --port 8080 --debug
  python environment_cli.py --config config.json --verbose
  python environment_cli.py --help
        """
    )

    # Basic options
    parser.add_argument('--port', '-p',
                       type=int,
                       default=8000,
                       help='Port to run the server on (default: 8000)')

    parser.add_argument('--host',
                       default='localhost',
                       help='Host to bind to (default: localhost)')

    # Flags
    parser.add_argument('--debug', '-d',
                       action='store_true',
                       help='Enable debug mode')

    parser.add_argument('--verbose', '-v',
                       action='store_true',
                       help='Enable verbose output')

    # Choices
    parser.add_argument('--environment', '-e',
                       choices=['development', 'staging', 'production'],
                       default='development',
                       help='Environment to run in')

    # File paths
    parser.add_argument('--config', '-c',
                       type=Path,
                       help='Path to configuration file')

    parser.add_argument('--log-file',
                       type=Path,
                       default=Path('app.log'),
                       help='Path to log file')

    # Numbers with ranges
    parser.add_argument('--max-connections',
                       type=int,
                       choices=range(1, 101),
                       default=10,
                       metavar='1-100',
                       help='Maximum number of connections (1-100)')

    # Multiple values
    parser.add_argument('--features',
                       nargs='*',
                       choices=['logging', 'metrics', 'caching', 'auth'],
                       help='Enable specific features')

    return parser



def main_with_args():
    """Main function demonstrating argument parsing."""
    parser = create_argument_parser()
    args = parser.parse_args()

    print("🍽️ Restaurant Management System Starting...")
    print(f"Host: {args.host}")
    print(f"Port: {args.port}")
    print(f"Environment: {args.environment}")
    print(f"Debug mode: {args.debug}")
    print(f"Verbose: {args.verbose}")
    print(f"Max connections: {args.max_connections}")
    print(f"Log file: {args.log_file}")
    print(f"Config file: {args.config}")

    if args.features:
        print(f"Enabled features: {', '.join(args.features)}")
    else:
        print("No specific features enabled")

    # Configuration summary
    config_status = "✅ Loaded" if args.config and args.config.exists() else "⚠️  Not loaded"
    print(f"Configuration: {config_status}")

    print("🚀 Server starting...")
    return args


main_with_args()



# ==========================================
# 4. CONFIGURATION FILES - Persistent Settings
# ==========================================

print("📄 CONFIGURATION FILES - Persistent Settings")
print("=" * 55)

def load_config_file(config_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Load configuration from JSON file.

    ANALOGY: Reading the restaurant's master recipe book
    """
    config_path = Path(config_path)

    if not config_path.exists():
        print(f"⚠️  Config file not found: {config_path}")
        return {}

    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
        print(f"✅ Loaded config from {config_path}")
        return config
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in config file: {e}")
        return {}
    except Exception as e:
        print(f"❌ Error loading config: {e}")
        return {}

def save_config_file(config: Dict[str, Any], config_path: Union[str, Path]) -> bool:
    """Save configuration to JSON file."""
    config_path = Path(config_path)

    try:
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, 'w', encoding='utf-8') as file:
            json.dump(config, file, indent=2, ensure_ascii=False)
        print(f"✅ Saved config to {config_path}")
        return True
    except Exception as e:
        print(f"❌ Error saving config: {e}")
        return False

def merge_configs(*configs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge multiple configuration sources.
    Priority: Later configs override earlier ones.
    """
    merged = {}
    for config in configs:
        merged.update(config)
    return merged

# Demo configuration file operations
print("📝 Configuration file operations:")

# Sample configuration
sample_config = {
    "app": {
        "name": "Restaurant Management System",
        "version": "1.0.0",
        "port": 8000
    },
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "restaurant_db"
    },
    "features": {
        "logging": True,
        "metrics": False,
        "caching": True
    }
}

# Save sample config
config_file = Path("sample_config.json")
save_config_file(sample_config, config_file)

# Load config
loaded_config = load_config_file(config_file)
print(f"App name from config: {loaded_config.get('app', {}).get('name')}")
print()



# ==========================================
# 5. SECURE INPUT HANDLING - Passwords & Secrets
# ==========================================

print("🔒 SECURE INPUT HANDLING - Passwords & Secrets")
print("=" * 55)

def get_password_secure(prompt: str = "Password: ") -> str:
    """
    Securely get password from user (hidden input).

    ANALOGY: Whispering the secret recipe
    """
    try:
        password = getpass.getpass(prompt)
        return password
    except Exception:
        # Fallback for environments without getpass
        import builtins
        return builtins.input("Password (visible): ")

def validate_password(password: str) -> Dict[str, bool]:
    """Validate password strength."""
    checks = {
        "length": len(password) >= 8,
        "has_upper": any(c.isupper() for c in password),
        "has_lower": any(c.islower() for c in password),
        "has_digit": any(c.isdigit() for c in password),
        "has_special": any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    }

    checks["strong"] = all(checks.values())
    return checks

print("🔑 Password security:")

# Password validation demo
# test_passwords = ["weak", "Stronger123", "VeryStrong123!"]

# for pwd in test_passwords:
#     validation = validate_password(pwd)
#     strength = "✅ Strong" if validation["strong"] else "❌ Weak"
#     print(f"Password '{pwd}': {strength}")
# print()

# input_password = get_password_secure("Enter your password: ")
# print(f"Password: {input_password}")
# print()

# validation = validate_password(input_password)
# strength = "✅ Strong" if validation["strong"] else "❌ Weak"
# print(f"Password strength: {strength}")
# print()

# print("🔑 Password validation:")
# print(f"Length: {'✅' if validation['length'] else '❌'}")
# print(f"Uppercase: {'✅' if validation['has_upper'] else '❌'}")
# print(f"Lowercase: {'✅' if validation['has_lower'] else '❌'}")
# print(f"Digit: {'✅' if validation['has_digit'] else '❌'}")
# print(f"Special: {'✅' if validation['has_special'] else '❌'}")




# ==========================================
# 6. COMPLETE CONFIGURATION SYSTEM
# ==========================================

print("⚙️ COMPLETE CONFIGURATION SYSTEM - Production Ready")
print("=" * 55)

class ProductionConfig:
    """
    Production-ready configuration system that combines:
    1. Default values
    2. Configuration files
    3. Environment variables
    4. Command-line arguments
    """

    def __init__(self):
        self._config = {}
        self._load_configuration()

    def _load_configuration(self):
        """Load configuration in order of precedence."""

        # 1. Default values (lowest priority)
        defaults = {
            "app_name": "Restaurant App",
            "version": "1.0.0",
            "host": "localhost",
            "port": 8000,
            "debug": False,
            "environment": "development",
            "database_url": "sqlite:///app.db",
            "log_level": "INFO",
            "max_connections": 100,
            "enable_metrics": False
        }

        # 2. Configuration file (medium priority)
        config_file_config = {}
        config_file_path = os.environ.get('CONFIG_FILE', 'config.json')
        if Path(config_file_path).exists():
            config_file_config = load_config_file(config_file_path)

        # 3. Environment variables (high priority)
        env_config = {
            "app_name": os.environ.get('APP_NAME'),
            "version": os.environ.get('APP_VERSION'),
            "host": os.environ.get('HOST'),
            "port": get_env_int('PORT'),
            "debug": get_env_bool('DEBUG'),
            "environment": os.environ.get('ENVIRONMENT'),
            "database_url": os.environ.get('DATABASE_URL'),
            "log_level": os.environ.get('LOG_LEVEL'),
            "max_connections": get_env_int('MAX_CONNECTIONS'),
            "enable_metrics": get_env_bool('ENABLE_METRICS')
        }

        # Remove None values from env_config
        env_config = {k: v for k, v in env_config.items() if v is not None}

        # 4. Merge configurations (CLI args would be highest priority)
        self._config = merge_configs(defaults, config_file_config, env_config)

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value."""
        return self._config.get(key, default)

    def __getitem__(self, key: str) -> Any:
        """Allow dictionary-style access."""
        return self._config[key]

    def __contains__(self, key: str) -> bool:
        """Check if key exists."""
        return key in self._config

    def __str__(self) -> str:
        """String representation."""
        return f"ProductionConfig({len(self._config)} settings)"

# Demo production configuration
print("🏭 Production configuration system:")
prod_config = ProductionConfig()
print(f"Config loaded: {prod_config}")
print(f"App name: {prod_config.get('app_name')}")
print(f"Port: {prod_config.get('port')}")
print(f"Debug mode: {prod_config.get('debug')}")
print(f"Environment: {prod_config.get('environment')}")
print()

# ==========================================
# 7. DEMONSTRATION - CLI Application
# ==========================================

print("🚀 DEMONSTRATION - Complete CLI Application")
print("=" * 55)

if __name__ == "__main__":
    # Only run CLI demo if this file is executed directly
    print("🍽️ Starting Restaurant Management System...")
    print()

    # Parse command-line arguments
    parser = create_argument_parser()
    args = parser.parse_args()

    # Load configuration
    config = ProductionConfig()

    # Override config with CLI args
    if hasattr(args, 'port') and args.port != 8000:  # If not default
        config._config['port'] = args.port
    if hasattr(args, 'debug'):
        config._config['debug'] = args.debug
    if hasattr(args, 'host'):
        config._config['host'] = args.host

    print("📋 Final Configuration:")
    print(f"  App: {config.get('app_name')} v{config.get('version')}")
    print(f"  Server: {config.get('host')}:{config.get('port')}")
    print(f"  Environment: {config.get('environment')}")
    print(f"  Debug: {config.get('debug')}")
    print(f"  Database: {config.get('database_url')}")
    print(f"  Log Level: {config.get('log_level')}")
    print(f"  Max Connections: {config.get('max_connections')}")
    print(f"  Metrics: {config.get('enable_metrics')}")
    print()

    if config.get('debug'):
        print("🐛 Debug mode enabled - extra logging active")

    print("✅ System ready!")
else:
    print("📚 Module imported - run directly to see CLI demo")

# ==========================================
# CLEANUP
# ==========================================

print("\n🧹 Cleaning up demo files:")
cleanup_files = ["sample_config.json"]
for file in cleanup_files:
    if Path(file).exists():
        Path(file).unlink()
        print(f"🗑️ Removed {file}")

print("\n✅ Demo complete!")

# ==========================================
# SUMMARY
# ==========================================

print("\n🎓 ENVIRONMENT & CLI CONFIGURATION SUMMARY")
print("=" * 55)
print("✅ Environment Variables:")
print("   • os.environ.get('VAR_NAME') - Read variables")
print("   • os.environ['VAR_NAME'] = 'value' - Set variables")
print("   • Secure storage for secrets and config")
print()
print("✅ Command-Line Arguments:")
print("   • argparse.ArgumentParser() - Create parser")
print("   • parser.add_argument() - Define arguments")
print("   • args = parser.parse_args() - Parse args")
print("   • Flexible runtime configuration")
print()
print("✅ Configuration Files:")
print("   • JSON for structured configuration")
print("   • Path management with pathlib")
print("   • Persistent settings storage")
print()
print("✅ Security Best Practices:")
print("   • Never hardcode secrets in code")
print("   • Use environment variables for sensitive data")
print("   • Validate and sanitize inputs")
print("   • Use secure password input methods")
print()
print("✅ Configuration Priority:")
print("   • Defaults (lowest)")
print("   • Configuration files")
print("   • Environment variables")
print("   • Command-line arguments (highest)")
print()
print("💡 Proper configuration management is crucial for:")
print("   • Security (secrets management)")
print("   • Deployment (environment-specific settings)")
print("   • Maintenance (easy configuration changes)")
print("   • Debugging (feature flags and logging)")