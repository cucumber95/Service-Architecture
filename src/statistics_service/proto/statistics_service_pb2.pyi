from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIKES: _ClassVar[Type]
    VIEWS: _ClassVar[Type]
LIKES: Type
VIEWS: Type

class GetStatsRequest(_message.Message):
    __slots__ = ("taskId",)
    TASKID_FIELD_NUMBER: _ClassVar[int]
    taskId: int
    def __init__(self, taskId: _Optional[int] = ...) -> None: ...

class GetStatsResponce(_message.Message):
    __slots__ = ("likes", "views")
    LIKES_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    likes: int
    views: int
    def __init__(self, likes: _Optional[int] = ..., views: _Optional[int] = ...) -> None: ...

class GetTopTasksRequest(_message.Message):
    __slots__ = ("type", "taskId")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    type: Type
    taskId: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, type: _Optional[_Union[Type, str]] = ..., taskId: _Optional[_Iterable[int]] = ...) -> None: ...

class TaskStats(_message.Message):
    __slots__ = ("taskId", "count")
    TASKID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    taskId: int
    count: int
    def __init__(self, taskId: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class GetTopTasksResponce(_message.Message):
    __slots__ = ("tasks",)
    TASKS_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[TaskStats]
    def __init__(self, tasks: _Optional[_Iterable[_Union[TaskStats, _Mapping]]] = ...) -> None: ...

class UserTasks(_message.Message):
    __slots__ = ("login", "taskId")
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    login: str
    taskId: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, login: _Optional[str] = ..., taskId: _Optional[_Iterable[int]] = ...) -> None: ...

class GetTopUsersRequest(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[UserTasks]
    def __init__(self, users: _Optional[_Iterable[_Union[UserTasks, _Mapping]]] = ...) -> None: ...

class UserStats(_message.Message):
    __slots__ = ("login", "likes")
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    login: str
    likes: int
    def __init__(self, login: _Optional[str] = ..., likes: _Optional[int] = ...) -> None: ...

class GetTopUsersResponce(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[UserStats]
    def __init__(self, users: _Optional[_Iterable[_Union[UserStats, _Mapping]]] = ...) -> None: ...
