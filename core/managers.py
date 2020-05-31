from django.db import models


class VectorModelManager(models.Manager):
    # TODO make this compatible with related fields.
    # get_queryset returns all instances even that are not related
    # to base model.
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class FrameModelManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs