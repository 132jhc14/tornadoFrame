from datetime import datetime
import peewee
from runSevers import database


class BaseModel(peewee.Model):
    create_time = peewee.DateTimeField(default=datetime.now(), verbose_name='创建时间')
    update_time = peewee.DateTimeField(default=datetime.now(), verbose_name='更新时间')
    is_delete = peewee.BooleanField(default=False, verbose_name='删除标记')

    def to_json(self) -> dict:
        r = self.__data__
        r['create_time'] = str(r['create_time'])
        r['update_time'] = str(r['update_time'])
        r['is_delete'] = str(r['is_delete'])
        return r

    class Meta:
        database = database