CONFIG = {
    # -----------------------------------------------------------------------------
    # Cache System Settings
    # -----------------------------------------------------------------------------
    #
    # This section defines the cache system settings. You can enable or disable
    # caching, as well as choose which caching driver to use for storing cached
    # data. Laravel supports several cache drivers like file, Redis, Memcached,
    # and more. Configure the settings below according to your requirements.
    #

    # Whether or not the cache system is enabled. Set to 'True' to enable caching.
    "enabled": True,

    # -----------------------------------------------------------------------------
    # Cache Driver
    # -----------------------------------------------------------------------------
    #
    # This option defines which cache driver should be used. You can choose from
    # various drivers including:
    # - 'file': Store cache in files on the local filesystem.
    # - 'redis': Use Redis as the cache store for faster in-memory caching.
    # - 'memcached': Use Memcached for caching data in-memory.
    #
    # Feel free to add custom cache drivers as per your application's requirements.
    #
    "driver": "file",  # Default is 'file'. Other options: 'redis', 'memcached', etc.

    # -----------------------------------------------------------------------------
    # Cache Stores
    # -----------------------------------------------------------------------------
    #
    # This section defines different cache "stores". A store is essentially a
    # configuration set for a particular caching method, such as file, Redis,
    # or Memcached. You can define multiple stores and group data types under
    # each store for better organization and performance.
    #
    # For example, you might have a file-based cache for small objects and
    # Redis for large, frequently accessed data.
    #

    "stores": {
        # 'file' Store: Caches data in files on the local disk
        "file": {
            "driver": "file",  # Cache stored as files on the filesystem
            "path": "/path/to/cache",  # Directory where cache files will be stored
        },

        # 'redis' Store: Caches data using Redis (an in-memory data structure store)
        "redis": {
            "driver": "redis",  # Redis driver
            "host": "127.0.0.1",  # Redis host (default is localhost)
            "port": 6379,  # Redis port (default is 6379)
            "password": "",  # Password for Redis (leave empty for no password)
        },

        # 'memcached' Store: Caches data using Memcached (another in-memory caching system)
        "memcached": {
            "driver": "memcached",  # Memcached driver
            "host": "127.0.0.1",  # Memcached server (default is localhost)
            "port": 11211,  # Memcached port (default is 11211)
        },
    },

    # -----------------------------------------------------------------------------
    # Cache Key Prefix
    # -----------------------------------------------------------------------------
    #
    # When using shared cache systems like Redis, Memcached, or database cache stores,
    # you may want to avoid key collisions with other applications. You can define
    # a prefix for your cache keys to ensure they remain unique within your cache store.
    #
    # This value can be set using the application name and ensures there are no key
    # collisions if other applications are using the same cache store.
    #

    "prefix": "myapp_cache_",  # Prefix for cache keys to avoid collisions
}
