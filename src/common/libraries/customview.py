from rest_framework.mixins import *
from rest_framework.status import HTTP_200_OK
from rest_framework_mongoengine.viewsets import GenericViewSet

__author__ = ["Arun Reghunathan"]


class CreateCustomMixin(CreateModelMixin):
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        response = dict()
        serializer = super(CreateCustomMixin, self).create(request, *args, **kwargs)

        response.update(serializer.data)
        response['status'] = "Success"
        response['status_code'] = HTTP_200_OK
        return Response(response)


class ListCustomMixin(ListModelMixin):
    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        response = dict()
        serializer = super(ListCustomMixin, self).list(request, *args, **kwargs)
        # response.data['response'] = dict(success=True, status_code=HTTP_200_OK)
        response.update(serializer.data)
        response['status'] = "Success"
        response['status_code'] = HTTP_200_OK
        return Response(response)


class RetrieveCustomMixin(RetrieveModelMixin):
    """
    Retrieve a model instance.
    """

    def retrieve(self, request, *args, **kwargs):
        response = dict()
        serializer = super(RetrieveCustomMixin, self).retrieve(request, *args, **kwargs)
        # response.data['response'] = dict(success=True, status_code=HTTP_200_OK)
        response.update(serializer.data)
        response['status'] = "Success"
        response['status_code'] = HTTP_200_OK
        return Response(response)


class UpdateCustomMixin(UpdateModelMixin):
    """
    Update a model instance.
    """

    def update(self, request, *args, **kwargs):
        response = dict()
        serializer = super(UpdateCustomMixin, self).update(request, *args, **kwargs)

        response.update(serializer.data)
        response['status'] = "Success"
        response['status_code'] = HTTP_200_OK
        return Response(response)


class CustomModelViewSet(CreateCustomMixin,
                         RetrieveCustomMixin,
                         UpdateCustomMixin,
                         DestroyModelMixin,
                         ListCustomMixin,
                         GenericViewSet):
    """ Adaptation of DRF CustomViewSet """
    pass


class ReadOnlyCustomModelViewSet(RetrieveCustomMixin, ListCustomMixin, GenericViewSet):
    """ Adaptation of DRF ReadOnlyModelViewSet """
    pass


class RetrieveUpdateCustomViewSet(RetrieveCustomMixin, UpdateCustomMixin, GenericViewSet):
    pass
