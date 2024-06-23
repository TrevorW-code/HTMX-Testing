from decouple import config

class Settings:

    # Server Configurations
    FAST_API_HOST: str = "0.0.0.0"  # Host for the FastAPI server
    FAST_API_PORT: int = int(config("FAST_API_PORT"))

settings = Settings()

print(settings.FAST_API_HOST)

