from rest_framework.response import Response
from rest_framework import status



class ManyOnListMixin:
    """
    Initialize serializer with many=True
    """

    def get_serializer(self, *args, **kwargs):
        if self.action == "create" and isinstance(kwargs.get("data"), list):
            kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)

class NoReturnCreateModelMixin:
    """
    Truncate results and return only text when action
    is create
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(None, status=status.HTTP_204_NO_CONTENT)