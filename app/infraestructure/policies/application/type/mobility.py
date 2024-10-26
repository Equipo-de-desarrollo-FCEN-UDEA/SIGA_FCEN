from datetime import datetime
from app.protocols.db.models.application.application import ApplicationStatusType
from app.infraestructure.policies.application.user_application import current_status, send_to_academic_unit, create_voting
from app.schemas.application.user_application import UserApplicationStatus
from app.services.application.type.mobility import mobility_svc
from app.schemas.users.user import User

from app.services.users.user_rol_academic_unit import user_rol_academic_unit_svc


def next_status(current_status: str, response: str | None = None) -> str:
    if current_status == ApplicationStatusType.CREATE.value:
        return ApplicationStatusType.IN_COMMITEE.value
    elif current_status == ApplicationStatusType.IN_COMMITEE.value:
        if (response == "APROBADA"):
            return ApplicationStatusType.IN_INTERNATIONAL.value
        elif (response == "RECHAZADA"):
            return ApplicationStatusType.RETURNED.value
        else: return ApplicationStatusType.RETURNED.value
    elif current_status == ApplicationStatusType.IN_INTERNATIONAL.value:
        if (response == "APROBADA"):
            return ApplicationStatusType.IN_DEAN.value
        elif (response == "RECHAZADA"):
            return ApplicationStatusType.RETURNED.value
    elif current_status == ApplicationStatusType.IN_DEAN.value:
        if (response == "APROBADA"):
            return ApplicationStatusType.APPROVED.value
        elif (response == "RECHAZADA"):
            return ApplicationStatusType.RETURNED.value
    else:
        return None
    
async def flux(*, user_application_id, db_mongo, db_postgres, current_user:User) -> str:
    _current_status = await current_status(user_application_id, db_mongo, mobility_svc)
    _next_status = next_status(_current_status)
    committee = user_rol_academic_unit_svc.get_student_committee(user_id=current_user.id, db=db_postgres)

    print(_next_status)

    if _next_status == ApplicationStatusType.IN_COMMITEE.value:
        send_to_academic_unit(academic_unit_id=committee, user_application_id=user_application_id, db=db_postgres)
        await create_voting(academic_unit_id=committee, user_application_id=user_application_id, db_postgres=db_postgres, db_mongo=db_mongo)
        status = UserApplicationStatus(name=_next_status, updated_by=current_user.id, date=datetime.now())
        
        new_status = await mobility_svc.add_status(
            db_mongo=db_mongo,
            new_status=status,
            user_application_id=user_application_id
        )

        return "terminado"

    else:
        return next_status
