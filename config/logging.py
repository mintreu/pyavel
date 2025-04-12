CONFIG = {
    # -----------------------------------------------------------------------------
    # Logging Configuration
    # -----------------------------------------------------------------------------
    #
    # This section defines how logging should be handled in your application. You can specify the
    # log level (e.g., debug, info, error) and the log handler (e.g., file, console).
    #

    # The log level to use. Common levels include 'debug', 'info', 'error' etc.
    "level": "debug",  # Defines the level of logging. For development, 'debug' is common; 'error' for production.

    # The handler defines where the log should be written. Common options include 'file' and 'console'.
    "handler": "file",  # Defines where logs should be written. Can be a file or console.

    # -----------------------------------------------------------------------------
    # Log Channels Configuration
    # -----------------------------------------------------------------------------
    #
    # Here you can configure the various logging channels like 'syslog', 'errorlog', 'null',
    # and 'emergency', similar to how it's done in Laravel's Monolog configuration.
    #

    # Syslog channel configuration
    "syslog": {
        # The syslog driver allows logging system-level events.
        "driver": "syslog",  # Syslog driver for logging system-level events.
        "level": "debug",  # Log level (e.g., 'debug', 'info', 'error').
        "facility": "LOG_USER",  # The syslog facility (e.g., LOG_USER, LOG_LOCAL0, etc.).
        "replace_placeholders": True,  # Whether to replace placeholders in the logs.
    },

    # Errorlog channel configuration
    "errorlog": {
        # The errorlog driver is for logging to PHP's error_log or stderr.
        "driver": "errorlog",  # Error log driver for logging to PHP's error_log or stderr.
        "level": "debug",  # Log level (e.g., 'debug', 'info', 'error').
        "replace_placeholders": True,  # Whether to replace placeholders in the logs.
    },

    # Null channel configuration (no logging, essentially a disabled channel)
    "null": {
        # The 'null' handler simply discards all logs (no logging occurs).
        "driver": "monolog",  # Monolog driver for logging.
        "handler": "NullHandler",  # Handler that ignores logs.
    },

    # Emergency channel configuration (for emergency logs)
    "emergency": {
        # Path to the emergency log file, which is used for critical logging.
        "path": "logs/laravel.log",  # Path to the emergency log file.
    },

    # -----------------------------------------------------------------------------
    # Default Log Channel
    # -----------------------------------------------------------------------------
    #
    # The default log channel is used when no specific channel is defined for the log.
    # Here, we are using 'errorlog' as the default channel.
    #

    "default": "errorlog",  # Default log channel to use. Here, we're stacking syslog, errorlog, and null.
}
