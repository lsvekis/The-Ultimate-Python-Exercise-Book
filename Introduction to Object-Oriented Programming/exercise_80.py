# Exercise 80: Use a class attribute to store configuration data.
class AppConfig:
settings = {"debug": True, "version": "1.0"}

@classmethod
def get_setting(cls, key):
return cls.settings.get(key, None)

print("Debug mode:", AppConfig.get_setting("debug"))
