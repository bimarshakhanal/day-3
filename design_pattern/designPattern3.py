class ConfigurationManager:
    '''Singeleton class to manage configuration file.'''
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConfigurationManager, cls).__new__(
                cls, *args, **kwargs)
            cls._instance._configurations = {}
            cls._instance._load_configurations()
        return cls._instance

    def _load_configurations(self):
        try:
            with open('config.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    key, value = line.strip().split('=')
                    self._configurations[key.strip()] = value.strip()
        except FileNotFoundError:
            print("Configuration file not found.")

    def get_configuration(self, key):
        return self._configurations.get(key)


# Example usage:
config_manager1 = ConfigurationManager()
config_manager2 = ConfigurationManager()

# config_manager1._load_configurations()
# config_manager2._load_configurations()

if config_manager1 == config_manager2:
    print('Both instances are same.')

print("Config manager 1 configurations:")
print(config_manager1.get_configuration("POST"))
print(config_manager1.get_configuration("HOST"))

print("\nConfig manager 2 configurations:")
print(config_manager2.get_configuration("PORT"))
print(config_manager2.get_configuration("HOST"))
