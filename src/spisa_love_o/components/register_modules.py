import importlib
import pkgutil
from typing import Type
from dependency_injector.containers import DeclarativeContainer

def register_modules(package_name: str, container: Type[DeclarativeContainer]):
    """
    Регистрирует все модули в указанном пакете и подключает их к контейнеру
    :param package_name: Имя пакета для сканирования
    :param container: Контейнер для DI
    """
    stack = [importlib.import_module(package_name)]

    while stack:
        package = stack.pop()

        for _, module_name, is_pkg in pkgutil.iter_modules(package.__path__):
            full_module_name = f"{package.__name__}.{module_name}"
            module = importlib.import_module(full_module_name)

            if is_pkg:
                stack.append(module)

            if container:
                for attr in vars(module).values():
                    if getattr(attr, "__injectable__", False):
                        attr.perform_injection(container=container)