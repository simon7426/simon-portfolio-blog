from fastapi import APIRouter, Request, Response, status

from project.core.route import route
from project.models.client import CommentPost

router = APIRouter(prefix="/api/v1/blogs", tags=["client"])


@route(
    request_method=router.get,
    path="",
    status_code=status.HTTP_200_OK,
    service_config="client_url",
    recaptcha_validation=True,
)
async def get_all_blogs(request: Request, response: Response):
    pass


@route(
    request_method=router.get,
    path="/{id}",
    status_code=status.HTTP_200_OK,
    service_config="client_url",
    recaptcha_validation=True,
)
async def get_blog(id: str, request: Request, response: Response):
    pass


@route(
    request_method=router.post,
    path="/{id}/comment",
    status_code=status.HTTP_201_CREATED,
    service_config="client_url",
    payload_key="comment",
    recaptcha_validation=True,
)
async def add_comment(
    id: str, comment: CommentPost, request: Request, response: Response
):
    pass
