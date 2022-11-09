from fastapi import APIRouter, Request, Response, status

from project.core.route import route
from project.models.admin import BlogIn, UserLogin

router = APIRouter(prefix="/api/v1/admin", tags=["admin"])


@route(
    request_method=router.post,
    path="/auth/login",
    status_code=status.HTTP_200_OK,
    service_config="admin_url",
    payload_key="login",
    recaptcha_validation=True,
)
async def login(login: UserLogin, request: Request, response: Response):
    pass


@route(
    request_method=router.post,
    path="/blogs",
    status_code=status.HTTP_201_CREATED,
    service_config="admin_url",
    payload_key="blog",
    jwt_validation=True,
)
async def add_blog(blog: BlogIn, request: Request, response: Response):
    pass


@route(
    request_method=router.put,
    path="/blogs/{id}",
    status_code=status.HTTP_200_OK,
    service_config="admin_url",
    payload_key="blog",
    jwt_validation=True,
)
async def update_blog(id: str, blog: BlogIn, request: Request, response: Response):
    pass


@route(
    request_method=router.delete,
    path="/blogs/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    service_config="admin_url",
    jwt_validation=True,
)
async def delete_blog(id: str, request: Request, response: Response):
    pass


@route(
    request_method=router.delete,
    path="/blogs/{blog_id}/comment/{comment_id}",
    status_code=status.HTTP_200_OK,
    service_config="admin_url",
    jwt_validation=True,
)
async def delete_comment(
    blog_id: str, comment_id: str, request: Request, response: Response
):
    pass


@route(
    request_method=router.get,
    path="/blogs",
    status_code=status.HTTP_200_OK,
    service_config="client_url",
    jwt_validation=True,
    route_default=False,
    original_prefix="/api/v1/admin",
    new_prefix="/api/v1",
)
async def get_all_blogs(request: Request, response: Response):
    pass


@route(
    request_method=router.get,
    path="/blogs/{id}",
    status_code=status.HTTP_200_OK,
    service_config="client_url",
    jwt_validation=True,
    route_default=False,
    original_prefix="/api/v1/admin",
    new_prefix="/api/v1",
)
async def get_blog(id: str, request: Request, response: Response):
    pass
