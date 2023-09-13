from datetime import datetime

from sqlalchemy import Integer, String, Text, Float, DateTime, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

Base = declarative_base()


class CustomerSampling(Base):
    __tablename__ = "customer_sampling"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    company_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text)
    params: Mapped[dict] = mapped_column(JSON)


class Client(Base):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    company_id: Mapped[int] = mapped_column(Integer, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    created_by: Mapped[int] = mapped_column(Integer, nullable=True)
    last_update_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    last_update_by: Mapped[int] = mapped_column(Integer, nullable=True)
    avg_difference: Mapped[float] = mapped_column(Float, nullable=True)
    last_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    come_from: Mapped[str] = mapped_column(String, nullable=True)
    activity_status: Mapped[bool] = mapped_column(Boolean, default=True, nullable=True)
    auto_task_status: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=True
    )
    sms: Mapped[str] = mapped_column(String, nullable=True)
    session: Mapped[str] = mapped_column(String, nullable=True)
    app_registration_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    type: Mapped[bool] = mapped_column(Boolean, nullable=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    contract_company: Mapped[int] = mapped_column(Integer, nullable=True)
    contact_person: Mapped[str] = mapped_column(String, nullable=True)
    verified: Mapped[bool] = mapped_column(Boolean, default=True, nullable=True)
    inn: Mapped[int] = mapped_column(Integer, nullable=True)
    accounting_phone: Mapped[str] = mapped_column(String, nullable=True)
    inactivity_date: Mapped[datetime] = mapped_column(
        DateTime, default=None, nullable=True
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)
    manager_notice: Mapped[str] = mapped_column(Text, nullable=True)
    favorites_list: Mapped[dict] = mapped_column(JSON, nullable=True)
    personal_discount_set: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=True
    )
    mailing_consent: Mapped[bool] = mapped_column(Boolean, nullable=True)


class ClientSources(Base):
    __tablename__ = "client_sources"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    company_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)


class ContractCompany(Base):
    __tablename__ = "company_contracts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    company_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)


class ClientAttributes(Base):
    __tablename__ = "client_attributes"

    client_id: Mapped[int] = mapped_column(Integer, primary_key=True)


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(Integer, nullable=True)
    company_id: Mapped[int] = mapped_column(Integer, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    created_by: Mapped[int] = mapped_column(Integer, nullable=True)
    updated_by: Mapped[int] = mapped_column(Integer, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    region: Mapped[str] = mapped_column(String, nullable=True)
    floor: Mapped[str] = mapped_column(String, nullable=True)
    entrance: Mapped[str] = mapped_column(String, nullable=True)
    city: Mapped[str] = mapped_column(String, nullable=True)
    street: Mapped[str] = mapped_column(String, nullable=True)
    house: Mapped[str] = mapped_column(String, nullable=True)
    building: Mapped[str] = mapped_column(String, nullable=True)
    flat: Mapped[str] = mapped_column(String, nullable=True)
    coords: Mapped[str] = mapped_column(String, default=None, nullable=True)
    delivery_area_id: Mapped[int] = mapped_column(Integer, nullable=True)
    verified: Mapped[bool] = mapped_column(Boolean, default=True, nullable=True)
    courier_notice: Mapped[str] = mapped_column(Text, nullable=True)
    contact: Mapped[str] = mapped_column(String, nullable=True)
    phone_contact: Mapped[str] = mapped_column(String, nullable=True)
    name_contact: Mapped[str] = mapped_column(String, nullable=True)
    notice: Mapped[str] = mapped_column(String, nullable=True)


class Districts(Base):
    __tablename__ = "districts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    main_district_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)
    subject_type: Mapped[bool] = mapped_column(Boolean)


class PersonalDiscount(Base):
    __tablename__ = "personal_discount"

    client_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer)
    discount_type: Mapped[int] = mapped_column(Integer)
    discount_value: Mapped[int] = mapped_column(Integer, nullable=True)
    personal_price: Mapped[str] = mapped_column(String(255), nullable=True)
