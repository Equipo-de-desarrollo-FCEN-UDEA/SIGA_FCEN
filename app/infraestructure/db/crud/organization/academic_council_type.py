from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.organization.academic_council_type import AcademicCouncilType
from app.schemas.organization.academic_council_type import AcademicCouncilTypeCreate, AcademicCouncilTypeUpdate

class AcademicCouncilTypeCrud(CRUDBase[AcademicCouncilType, AcademicCouncilTypeCreate, AcademicCouncilTypeUpdate]):
    pass

academic_council_type_crud = AcademicCouncilTypeCrud(AcademicCouncilType)