from typing import Type, Union
import inspect
import re
from dependency_injector.providers import Singleton, Factory
from dependency_injector.wiring import Provide, inject
from dependency_injector.containers import DeclarativeContainer


def injectable(
    name: str | None = None,
    provider_class: Type[Union[Singleton, Factory]] = Singleton,
    abstract: bool = False,
):
    """
    Декоратор для автоматической регистрации класса в DependencyInjector.

    Также автоматически подтягивает зависимости из контейнера в конструктор.

    :param name: имя регистрации в контейнере. Если не указано, используется имя класса.
    :param provider_class: Тип провайдера из dependency_injector, по умолчанию - singleton
    :param abstract: Абстрактный ли класс
    """

    def __modify_init_signature(cls: object):
        # Автоматическое применение @inject к __init__
        original_init = cls.__init__

        if not inspect.isfunction(original_init):
            return

        sig = inspect.signature(original_init)
        new_parameters = []

        for _, param in sig.parameters.items():
            # Проверяем, есть ли Provide в аннотации
            if param.annotation != inspect.Parameter.empty:
                if isinstance(param.default, Provide):
                    default_value = param.default
                elif inspect.isclass(param.annotation):
                    provide_key = re.sub(
                        r"(?<!^)(?=[A-Z])", "_", param.annotation.__name__
                    ).lower()
                    default_value = Provide[provide_key]
                else:
                    default_value = param.default

                new_parameters.append(param.replace(default=default_value))
            else:
                new_parameters.append(param)

        # Создаем новую сигнатуру для конструктора
        new_sig = sig.replace(parameters=new_parameters)

        original_init.__signature__ = new_sig

        cls.__init__ = inject(original_init)

    def decorator(cls: object):
        # Автоматическое применение @inject к __init__
        __modify_init_signature(cls)

        cls.__injectable__ = {
            "name": name,
            "provider_class": provider_class,
            "abstract": abstract,
        }

        registration_name: str = (
            name or re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()
        )

        def perform_injection(
            container: Type[DeclarativeContainer] | None = None,
        ):
            if abstract:
                return

            # Если элемент уже есть в контейнере то не оверрайдим
            if hasattr(container, registration_name):
                return

            setattr(container, registration_name, provider_class(cls))

        setattr(cls, "perform_injection", perform_injection)

        return cls

    return decorator
