"""dosn't support multiple url kwargs with same name
"""
from rest_framework.routers import SimpleRouter, DefaultRouter


class NestedMixin(object):
    def __init__(self, parent_router, parent_prefix, *args, **kwargs):
        self.parent_router = parent_router
        self.parent_prefix = parent_prefix
        self.nest_count = getattr(parent_router, 'nest_count', 0) + 1
        self.nest_prefix = kwargs.pop('lookup', 'nested_%i' % self.nest_count) + '_'

        super(NestedMixin, self).__init__(*args, **kwargs)

        if 'trailing_slash' not in kwargs:
            self.trailing_slash = parent_router.trailing_slash

        parent_registry = [registered for registered
                           in self.parent_router.registry
                           if registered[0] == self.parent_prefix]
        try:
            parent_registry = parent_registry[0]
            parent_prefix, parent_viewset, parent_basename = parent_registry
        except:
            raise RuntimeError('parent registered resource not found')

        nested_routes = []
        parent_lookup_regex = parent_router.get_lookup_regex(parent_viewset)

        self.parent_regex = '{parent_prefix}/{parent_lookup_regex}/'.format(
            parent_prefix=parent_prefix,
            parent_lookup_regex=parent_lookup_regex
        )
        if not self.parent_prefix and self.parent_regex[0] == '/':
            self.parent_regex = self.parent_regex[1:]
        if hasattr(parent_router, 'parent_regex'):
            self.parent_regex = parent_router.parent_regex + self.parent_regex

        for route in self.routes:
            route_contents = route._asdict()
            escaped_parent_regex = self.parent_regex.replace('{', '{{').replace('}', '}}')
            route_contents['url'] = route.url.replace('^', '^' + escaped_parent_regex)
            nested_routes.append(type(route)(**route_contents))

        self.routes = nested_routes


class NestedDefaultRouter(NestedMixin, DefaultRouter):
    pass


class NestedSimpleRouter(NestedMixin, SimpleRouter):
    pass
