CONFIG = {
    # ----------------------------------------------------------------------
    # Database Connection Settings
    # ----------------------------------------------------------------------
    #
    # This section defines the basic connection parameters to your database.
    # You can configure the driver, host, port, username, password, and the
    # database name for connecting to different types of databases.
    #

    "driver": "mysql",  # Database driver (mysql, pgsql, sqlite)

    # ----------------------------------------------------------------------
    # Database Host and Port
    # ----------------------------------------------------------------------
    #
    # Specify the host where your database is located. If your database
    # is hosted on a remote server, provide the IP address or domain.
    # Common ports are 3306 for MySQL, 5432 for PostgreSQL, and no port is
    # needed for SQLite (use the file path instead).
    #

    "host": "localhost",  # Default: 'localhost' (Use IP for remote DB)

    "port": 3306,  # Default: 3306 for MySQL, 5432 for PostgreSQL, etc.

    # ----------------------------------------------------------------------
    # Authentication Credentials
    # ----------------------------------------------------------------------
    #
    # Set the username and password used to connect to the database.
    # The default username for MySQL and PostgreSQL is often 'root'.
    #

    "username": "root",  # Default: 'root'

    "password": "",  # Password for the username (can be empty for no password)

    # ----------------------------------------------------------------------
    # Database Name
    # ----------------------------------------------------------------------
    #
    # Define the name of the database to which you want to connect.
    # Replace this value with your actual database name.
    #

    "database": "pyavel_db",  # Your actual database name

    # ----------------------------------------------------------------------
    # MySQL-Specific Settings
    # ----------------------------------------------------------------------
    #
    # These options are specific to MySQL. You can configure settings like
    # charset and collation here to ensure proper text encoding and support
    # for multi-language data.
    #

    "mysql": {
        "charset": "utf8mb4",  # Recommended charset for modern applications, supports emojis
        "collation": "utf8mb4_unicode_ci",  # Default collation for utf8mb4 charset
    },

    # ----------------------------------------------------------------------
    # PostgreSQL-Specific Settings
    # ----------------------------------------------------------------------
    #
    # These options are specific to PostgreSQL. You can specify settings
    # like the default schema and SSL connection mode.
    #

    "pgsql": {
        "schema": "public",  # Default schema to use in PostgreSQL (optional)
        "sslmode": "prefer",  # SSL connection mode: 'disable', 'allow', 'prefer', 'require'
    },

    # ----------------------------------------------------------------------
    # SQLite-Specific Settings
    # ----------------------------------------------------------------------
    #
    # These options are specific to SQLite. Set the file path for your
    # SQLite database file and options like foreign key constraint enforcement.
    #

    "sqlite": {
        "database_file": "/path/to/database.sqlite",  # File path for SQLite database (no server required)
        "foreign_keys": True,  # Enforce foreign key constraints (SQLite only)
    },

    # ----------------------------------------------------------------------
    # Additional Connection Options
    # ----------------------------------------------------------------------
    #
    # This section includes optional settings that can be configured to
    # control various aspects of database connection behavior.
    #

    "options": {
        "timeout": 30,  # Timeout for database connections (in seconds)
        "connect_timeout": 10,  # Timeout for initial connection attempt (in seconds)
        "charset": "utf8",  # Charset for database connection
        "strict": True,  # Enable strict SQL mode (MySQL/PostgreSQL)
        "fetch_mode": "assoc",  # Fetch mode for query results: "assoc" (associative), "all" (all columns), etc.
    },
}
