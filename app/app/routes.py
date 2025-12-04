"""
app Application routing module.
Version: 0.1.0
"""


# Import your pages here
from fletx.navigation import (
    ModuleRouter, TransitionType, RouteTransition
)
from fletx.decorators import register_router

from .pages import CounterPage, NotFoundPage

# Define App routes here
routes = [
    {
        'path': '/',
        'component': CounterPage,
    },
    {
        'path': '/**',
        'component': NotFoundPage,
    },
]

@register_router
class AppRouter(ModuleRouter):
    """app Routing Module."""

    name = 'app'
    base_path = '/'
    is_root = True
    routes = routes
    sub_routers = []