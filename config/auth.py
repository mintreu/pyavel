import os

# Authentication Configuration
CONFIG = {

    # -----------------------------------------------------------------------------
    # Authentication Defaults
    # -----------------------------------------------------------------------------
    #
    # This section defines the default authentication settings, such as the guard
    # (similar to Laravel's 'web') and the password reset broker (defaulting to 'users').
    #

    'defaults': {
        'guard': os.getenv('AUTH_GUARD', 'web'),  # Default authentication guard (e.g., 'web', 'admin')
        'passwords': os.getenv('AUTH_PASSWORD_BROKER', 'users'),  # Default password reset broker.
    },

    # -----------------------------------------------------------------------------
    # Authentication Guards
    # -----------------------------------------------------------------------------
    #
    # Guards define how authentication will be handled, such as using sessions.
    # For example, we have guards for 'web' and 'admin' (like Laravel).
    #

    'guards': {
        'web': {
            'driver': 'session',  # Authentication driver (e.g., session-based authentication)
            'provider': 'users',  # The provider that retrieves users for the 'web' guard.
        },
        'admin': {
            'driver': 'session',  # Admin authentication driver.
            'provider': 'admins',  # The provider for admins.
        },
    },

    # -----------------------------------------------------------------------------
    # User Providers
    # -----------------------------------------------------------------------------
    #
    # Providers define how users are retrieved from the database or other storage systems.
    # Here we use 'eloquent' (like Laravel) for object-relational mapping (ORM) or database.
    #

    'providers': {
        'users': {
            'driver': 'eloquent',  # The driver to use for retrieving user models.
            'model': os.getenv('AUTH_MODEL', 'app.models.User'),  # Path to the user model (e.g., User class in a Django model).
        },
        'admins': {
            'driver': 'eloquent',  # The driver to use for retrieving admin models.
            'model': 'app.models.Admin',  # Path to the admin model.
        },
        # Uncomment for database-driven user authentication
        # 'users': {
        #     'driver': 'database',  # Database-based user provider.
        #     'table': 'users',  # Table for user data.
        # },
    },

    # -----------------------------------------------------------------------------
    # Resetting Passwords
    # -----------------------------------------------------------------------------
    #
    # Configures how the password reset functionality will work, including the
    # expiration time of reset tokens and the throttle time between generating
    # multiple reset tokens to avoid abuse.
    #

    'passwords': {
        'users': {
            'provider': 'users',  # The provider for user password resets.
            'table': os.getenv('AUTH_PASSWORD_RESET_TOKEN_TABLE', 'password_reset_tokens'),  # Table for storing reset tokens.
            'expire': 60,  # Time in minutes for which the reset token will be valid.
            'throttle': 60,  # Time in seconds a user must wait before generating another reset token.
        },
        'admins': {
            'provider': 'admins',  # The provider for admin password resets.
            'table': 'password_reset_tokens',  # Table for admin reset tokens.
            'expire': 60,  # Token expiration time for admins.
            'throttle': 60,  # Throttle setting for admins.
        },
    },

    # -----------------------------------------------------------------------------
    # Password Confirmation Timeout
    # -----------------------------------------------------------------------------
    #
    # Defines the number of seconds before the password confirmation window expires,
    # at which point users must re-enter their password. Default is set to 10800 seconds (3 hours).
    #

    'password_timeout': os.getenv('AUTH_PASSWORD_TIMEOUT', 10800),  # Timeout for password confirmation.
}
