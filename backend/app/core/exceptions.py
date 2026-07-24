from fastapi import HTTPException


def not_found_error(entity: str, entity_id: int):

    raise HTTPException(

        status_code=404,

        detail={
            "status": "error",
            "code": 404,
            "message": f"{entity} with ID {entity_id} not found"
        }

    )