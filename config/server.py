CONFIG = {
    # --------------------------------------------------------------------------
    # Application Environment
    # --------------------------------------------------------------------------
    # This value determines the "environment" your application is currently
    # running in. This may determine how you prefer to configure various
    # services your application utilizes. Set to 'production' in real deployments.
    #
    # Possible values: "development", "production", "staging", etc.
    # Usage:
    #   config("server.env") => "development"
    # --------------------------------------------------------------------------
    "env": "production",

    # --------------------------------------------------------------------------
    # Server Configuration
    # --------------------------------------------------------------------------
    # These values control how the server is exposed. Use 127.0.0.1 for local
    # development or 0.0.0.0 for public access in production environments.
    # --------------------------------------------------------------------------
    "host": "127.0.0.1",  # Localhost (use "0.0.0.0" for external access)
    "port": 8080          # Port number the server listens on
}
