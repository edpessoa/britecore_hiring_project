from rest_framework import routers

from apps.risks.views import RiskTypeViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = "/?"

api.register(r"risks", RiskTypeViewSet, basename="risks")
