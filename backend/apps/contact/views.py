from .models import Label, Contact
from .serializers import LabelSerializer, ContactSerializer, ContactListSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 10000


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = ContactListPagination

    def get_queryset(self):
        queryset = Contact.objects.filter(user=self.request.user)

        sort_by = self.request.query_params.get("sort_by")
        sort_order = self.request.query_params.get("sort_order", "asc")

        if sort_by in ["name", "email", "contact_number", "id"]:
            order_field = f"-{sort_by}" if sort_order.lower() == "desc" else sort_by
            queryset = queryset.order_by(order_field)
        else:
            queryset = queryset.order_by("id")

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(
        summary="* 연락처 리스트 조회",
        description="Get a list of contacts with optional sorting and pagination.",
        parameters=[
            OpenApiParameter(
                name="sort_by",
                description="Sort by field (name, email, contact_number, id)",
                type=str,
            ),
            OpenApiParameter(
                name="sort_order",
                description="Sort order (asc or desc, default is asc)",
                type=str,
            ),
            OpenApiParameter(name="page", description="Page number", type=int),
            OpenApiParameter(
                name="page_size", description="Number of items per page", type=int
            ),
        ],
        responses={
            status.HTTP_200_OK: ContactListSerializer(many=True),
            status.HTTP_401_UNAUTHORIZED: None,
        },
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ContactListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(summary="* 연락처 입력")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="* 연락처 상세보기")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
