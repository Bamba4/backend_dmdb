from graphene_django import DjangoObjectType
from graphene import String, InputObjectType, DateTime, Int

from dmdbBaseManagement.models import GodParent


class GodParentType(DjangoObjectType):
    class Meta:
        model = GodParent


class GodParentInput(InputObjectType):
    id = Int()
    first_name = String()
    last_name = String()
    address = String()
    email = String()
    date_of_birth = DateTime()
    avatar = String()
