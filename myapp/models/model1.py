from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey,Float
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Boolean,
    Column,
    create_engine,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    Text,
)


# 添加自定义model
from sqlalchemy import Column, Integer, String, ForeignKey ,Date,DateTime
from flask_appbuilder.models.decorators import renders
from flask import Markup
import datetime
metadata = Model.metadata

# model关系的表
model1_model2 = Table(
    "model1_model2",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("model1_id", Integer, ForeignKey("model1.id")),
    Column("model2_id", Integer, ForeignKey("model2.id")),
)


# 定义model
class Model2(Model):
    __tablename__ = 'model2'
    id = Column(Integer, primary_key=True)
    attr1 = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.attr1


# 定义model
class Model1(Model):
    __tablename__='model1'
    id = Column(Integer, primary_key=True)
    attr1 = Column(String(150), unique = True, nullable=False)
    attr2 = Column(DateTime,default=datetime.datetime.now)   # 定义时间字段，默认值为函数，这样才能在每次写入时都是当时的时间
    attr3 = Column(Integer, ForeignKey('model2.id'))    # 定义外键
    attr4 = relationship(Model2,secondary=model1_model2)  # 一对多关系，不存储数据库。第一个参数可以是model或者或者model的名称

    def __repr__(self):
        return self.attr1

    # 自定义一个函数字段和渲染样式，供前端显示
    @renders('date')
    def my_date(self):
        return Markup('<b style="color:red">' + self.attr2 + '</b>')

    @property
    def aa(self):
        return 'attr1:'+self.attr1




