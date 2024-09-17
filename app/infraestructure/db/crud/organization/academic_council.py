from app.infraestructure.db.crud.base import CRUDBase
from app.infraestructure.db.models.organization.academic_council import AcademicCouncil
from app.schemas.organization.academic_council import AcademicCouncilCreate, AcademicCouncilUpdate

class AcademicCouncilCrud(CRUDBase[AcademicCouncil, AcademicCouncilCreate, AcademicCouncilUpdate]):
    pass

academic_council_crud = AcademicCouncilCrud(AcademicCouncil)