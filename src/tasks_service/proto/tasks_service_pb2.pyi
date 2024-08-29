from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Statuses(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IN_PROGRESS: _ClassVar[Statuses]
    HIGH_PRIORITY: _ClassVar[Statuses]
    ON_PAUSE: _ClassVar[Statuses]
    CLOSED: _ClassVar[Statuses]
IN_PROGRESS: Statuses
HIGH_PRIORITY: Statuses
ON_PAUSE: Statuses
CLOSED: Statuses

class ITask(_message.Message):
    __slots__ = ("id", "title", "content", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    content: str
    status: Statuses
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., status: _Optional[_Union[Statuses, str]] = ...) -> None: ...

class CreateTaskRequest(_message.Message):
    __slots__ = ("authorLogin", "title", "content", "status")
    AUTHORLOGIN_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    authorLogin: str
    title: str
    content: str
    status: Statuses
    def __init__(self, authorLogin: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., status: _Optional[_Union[Statuses, str]] = ...) -> None: ...

class UpdateTaskRequest(_message.Message):
    __slots__ = ("taskId", "authorLogin", "title", "content", "status")
    TASKID_FIELD_NUMBER: _ClassVar[int]
    AUTHORLOGIN_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    taskId: int
    authorLogin: str
    title: str
    content: str
    status: Statuses
    def __init__(self, taskId: _Optional[int] = ..., authorLogin: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., status: _Optional[_Union[Statuses, str]] = ...) -> None: ...

class UpdateTaskResponse(_message.Message):
    __slots__ = ("isUpdated", "task")
    ISUPDATED_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    isUpdated: bool
    task: ITask
    def __init__(self, isUpdated: bool = ..., task: _Optional[_Union[ITask, _Mapping]] = ...) -> None: ...

class DeleteTaskRequest(_message.Message):
    __slots__ = ("taskId", "authorLogin")
    TASKID_FIELD_NUMBER: _ClassVar[int]
    AUTHORLOGIN_FIELD_NUMBER: _ClassVar[int]
    taskId: int
    authorLogin: str
    def __init__(self, taskId: _Optional[int] = ..., authorLogin: _Optional[str] = ...) -> None: ...

class DeleteTaskResponse(_message.Message):
    __slots__ = ("IsDeleted",)
    ISDELETED_FIELD_NUMBER: _ClassVar[int]
    IsDeleted: bool
    def __init__(self, IsDeleted: bool = ...) -> None: ...

class GetTaskRequest(_message.Message):
    __slots__ = ("taskId", "authorLogin")
    TASKID_FIELD_NUMBER: _ClassVar[int]
    AUTHORLOGIN_FIELD_NUMBER: _ClassVar[int]
    taskId: int
    authorLogin: str
    def __init__(self, taskId: _Optional[int] = ..., authorLogin: _Optional[str] = ...) -> None: ...

class GetTaskResponse(_message.Message):
    __slots__ = ("isAccessible", "task")
    ISACCESSIBLE_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    isAccessible: bool
    task: ITask
    def __init__(self, isAccessible: bool = ..., task: _Optional[_Union[ITask, _Mapping]] = ...) -> None: ...

class GetTasksListRequest(_message.Message):
    __slots__ = ("authorLogin", "pageSize", "page")
    AUTHORLOGIN_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    authorLogin: str
    pageSize: int
    page: int
    def __init__(self, authorLogin: _Optional[str] = ..., pageSize: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class GetTasksListResponse(_message.Message):
    __slots__ = ("tasks",)
    TASKS_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[ITask]
    def __init__(self, tasks: _Optional[_Iterable[_Union[ITask, _Mapping]]] = ...) -> None: ...
