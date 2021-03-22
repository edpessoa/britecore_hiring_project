import json
from django.http import JsonResponse
from rest_framework import viewsets, status

from apps.risks.models import RiskTypeFields, RiskType, FieldType


def _query_to_data(queryset):
    data = {}
    for risk in queryset:
        if risk.risk_type.id not in data:
            data[risk.risk_type.id] = {}
        if "fields" not in data[risk.risk_type.id]:
            data[risk.risk_type.id]["fields"] = []
        payload = json.loads(risk.payload) if risk.field_type.payload_field else None
        data[risk.risk_type.id]["name"] = risk.risk_type.name
        data[risk.risk_type.id]["fields"].append(
            {
                "type": risk.field_type.type,
                "name": risk.field_name,
            }
        )
        if payload is not None:
            data[risk.risk_type.id]["fields"][-1][
                risk.field_type.payload_field
            ] = payload[risk.field_type.payload_field]
    return data


def _invalid_request():
    data = {"status": "false", "message": "Method not allowed"}
    return JsonResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED, data=data)


class RiskTypeViewSet(viewsets.ViewSet):
    def list(self, request):
        if request.method != "GET":
            return _invalid_request()

        queryset = RiskTypeFields.objects.all().select_related(
            "risk_type", "field_type"
        )
        data = _query_to_data(queryset)

        return JsonResponse(data, safe=False)

    def retrieve(self, request, pk=None):
        if request.method != "GET":
            return _invalid_request()

        queryset = RiskTypeFields.objects.select_related(
            "risk_type", "field_type"
        ).filter(risk_type__id=pk)

        data = _query_to_data(queryset)
        if not data:
            data = {"status": "false", "message": "Not found"}
            return JsonResponse(
                status=status.HTTP_404_NOT_FOUND,
                data=data,
            )
        return JsonResponse(data, safe=False)
