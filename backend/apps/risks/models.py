from django.db import models


class FieldType(models.Model):
    type = models.CharField(max_length=200)
    payload_field = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.type


class RiskType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RiskTypeFields(models.Model):
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    field_type = models.ForeignKey(FieldType, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=200)
    payload = models.JSONField(blank=True, null=True)

    def __str__(self):
        return "{} from: {}".format(self.field_name, self.risk_type)
