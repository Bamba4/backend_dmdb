from graphene import  String, DateTime, InputObjectType, Int, Boolean


from graphene_django import DjangoObjectType

from dmdbBaseManagement.godParent.type import GodParentInput
from dmdbBaseManagement.models import Student
from dmdbBaseManagement.tutor.type import TutorInput


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class StudentInput(InputObjectType):
    id = Int()
    first_name = String()
    last_name = String()
    mother = String()
    father = String()
    address = String()
    date_of_birth = DateTime()
    surate = String()
    joined_at = DateTime()
    avatar = String()
    pseudonyme = String()
    has_memorized = Boolean()
    has_recited = Boolean()
    recite_date = DateTime()
    has_written = Boolean()
    current_surate = String()
    memorize_date = DateTime()
    writting_begin_date = DateTime()
    current_step_writting = String()
    writting_end_date = DateTime()
    god_parent_id = Int()
    tutor_id = Int()
    tutor = TutorInput()
    god_parent = GodParentInput()
