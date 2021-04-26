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
    is_memorize_quran = Boolean()
    is_recite_all_quran = Boolean()
    date_to_recit_all_quran = DateTime()
    is_write_quran = Boolean()
    current_surate = String()
    date_of_memorize_quran = DateTime()
    date_to_start_write_quran = DateTime()
    current_write_quran = String()
    date_to_finish_write_quran = DateTime()
    god_parent_id = Int()
    tutor_id = Int()
    tutor = TutorInput()
    god_parent = GodParentInput()
