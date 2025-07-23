from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import UTC, datetime
from app.core.database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    uuid = Column(String(36), unique=True)
    nickname = Column(String(255))
    status = Column(Integer, default=0)  # 0: 미인증, 1: 인증, 2: 성적대기중
    grade = Column(Float)
    lang = Column(String(255))
    modify_count = Column(Integer, default=3)
    created_at = Column(DateTime, default=datetime.now(UTC))
    updated_at = Column(DateTime, default=datetime.now(UTC))


class PartnerUniversity(Base):
    __tablename__ = "partner_university"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    country = Column(String(255))
    slot = Column(Integer)
    duration = Column(String)  # "1개학기" or "2개학기"
    created_at = Column(DateTime, default=datetime.now(UTC))
    updated_at = Column(DateTime, default=datetime.now(UTC))


class Application(Base):
    __tablename__ = "application"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    partner_university_id = Column(Integer, ForeignKey("partner_university.id"))
    choice = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(UTC))
    updated_at = Column(DateTime, default=datetime.now(UTC))
