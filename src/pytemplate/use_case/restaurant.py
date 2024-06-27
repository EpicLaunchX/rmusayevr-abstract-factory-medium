from typing import Any

from pytemplate.service.restaurant import RestaurantService
from src.pytemplate.domain.models import Restaurant


def restaurant(data: dict[str, Any], registry: dict[str, type[RestaurantService]]) -> Restaurant:
    cuisine = data["cuisine"]
    service_class = registry.get(cuisine)
    if service_class is None:
        raise ValueError(f"No service found for cuisine: {cuisine}")
    service_instance = service_class()
    return service_instance.create(data)
