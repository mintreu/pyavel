CONFIG = {
    # -----------------------------------------------------------------------------
    # Application Settings
    # -----------------------------------------------------------------------------
    #
    # This section contains general settings for the application, such as the
    # application name, environment, debug mode, timezone, and locale configurations.
    #

    # The name of the application, which will be used for various purposes across the system.
    "app_name": "Pyavel",  # The name of your application, typically used in branding or logging.

    # -----------------------------------------------------------------------------
    # Environment Settings
    # -----------------------------------------------------------------------------
    #
    # This option defines the environment in which your application is running.
    # Common environments are 'local', 'development', 'production', and 'staging'.
    #
    # It's essential to set this appropriately, as different environments might require
    # different configurations (e.g., enabling/disabling debugging, different database settings).
    #

    "env": "development",  # The environment for the application. E.g., 'production', 'development'.

    # -----------------------------------------------------------------------------
    # Debugging Mode
    # -----------------------------------------------------------------------------
    #
    # Enable or disable debugging mode. In a production environment, debugging should be set to 'False'
    # to prevent exposure of sensitive information.
    #

    "debug": True,  # Whether debugging is enabled. Set to 'False' in production for security reasons.

    # -----------------------------------------------------------------------------
    # Timezone Configuration
    # -----------------------------------------------------------------------------
    #
    # Set the default timezone for your application. This affects things like time and date handling.
    # Ensure to set this according to your server or user's timezone.
    #

    "timezone": "UTC",  # The default timezone. Adjust according to your server's or user's timezone.

    # -----------------------------------------------------------------------------
    # Locale Configuration
    # -----------------------------------------------------------------------------
    #
    # Set the default language/locale for the application. This affects the language used for
    # error messages, translations, and more.
    #

    "locale": "en",  # The default language/locale (e.g., 'en' for English, 'fr' for French).

    # -----------------------------------------------------------------------------
    # Fallback Locale Configuration
    # -----------------------------------------------------------------------------
    #
    # This locale will be used when a translation is not available in the specified locale.
    # It's important to set this to a language that you want to fallback to in case of missing translations.
    #

    "fallback_locale": "en",  # Fallback locale used when the specified locale has no available translation.

    # -----------------------------------------------------------------------------
    # Service Providers
    # -----------------------------------------------------------------------------
    #
    # List the service providers to load when the application is bootstrapped.
    # Providers are responsible for initializing various services, such as routing, database,
    # caching, and more. You can add custom providers as needed.
    #

    "providers": [
        "bramha.kernel.Kernel",  # Core kernel for application bootstrapping.
        "bramha.route.Router",   # Router provider for defining routes and handling HTTP requests.
    ],


}
