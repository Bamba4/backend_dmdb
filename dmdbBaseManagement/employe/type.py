from graphene_django import DjangoObjectType
from graphene import ObjectType, List, Mutation, Field, String, InputObjectType, Int, Argument, DateTime

from dmdbBaseManagement.models import Employee


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee


class InputEmployee(InputObjectType):
    id = Int()
    first_name = String()
    last_name = String()
    address = String()
    date_of_birth = DateTime()
    role = String()
    phone_number = String()
    email = String()
    avatar = String()
