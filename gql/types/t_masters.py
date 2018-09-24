from graphene_django.types import DjangoObjectType
from common.models.data_models.region import City, FDIC_Region, Federal_Reserve_District, OCC_District, OTS_Region, \
    QBP_Region, State, Supervisory_Region
from common.models.data_models.misc import Asset_Concentration, Office_Type, Structure_Code
from common.models.data_models.regulatory import Charter_Class, Charting_Agency, Regulator

class Asset_Concentration_Type(DjangoObjectType):
    class Meta:
        model = Asset_Concentration

class Office_Type_Type(DjangoObjectType):
    class Meta:
        model = Office_Type

class Structure_Code_Type(DjangoObjectType):
    class Meta:
        model = Structure_Code

class Charter_Class_Type(DjangoObjectType):
    class Meta:
        model = Charter_Class

class Charting_Agency_Type(DjangoObjectType):
    class Meta:
        model = Charting_Agency

class Regulator_Type(DjangoObjectType):
    class Meta:
        model = Regulator


class City_Type(DjangoObjectType):
    class Meta:
        model = City

class FDIC_Region_Type(DjangoObjectType):
    class Meta:
        model = FDIC_Region


class Federal_Reserve_District_Type(DjangoObjectType):
    class Meta:
        model = Federal_Reserve_District


class OCC_District_Type(DjangoObjectType):
    class Meta:
        model = OCC_District


class OTS_Region_Type(DjangoObjectType):
    class Meta:
        model = OTS_Region


class QBP_Region_Type(DjangoObjectType):
    class Meta:
        model = QBP_Region


class State_Type(DjangoObjectType):
    class Meta:
        model = State


class Supervisory_Region_Type(DjangoObjectType):
    class Meta:
        model = Supervisory_Region
