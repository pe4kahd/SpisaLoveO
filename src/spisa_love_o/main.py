from src.spisa_love_o.components.register_modules import register_modules
from src.spisa_love_o.di import DependencyInjector

register_modules(
    package_name="src",
    container=DependencyInjector,
)
container = DependencyInjector()
container.wire(packages=["src"])
app = container.fast_api_app().app