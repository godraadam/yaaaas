import os

from app.config.config_dev import DevConfig


def get_app_settings():
    app_env = os.environ.get("YAAAAS_ENV") or "dev"

    configs = {
        "dev": DevConfig,
        # add here later prod, test, etc.
    }

    return configs[app_env]()


settings = get_app_settings()
