import os
import jwt
import pytest
from sqlalchemy import delete
from tests import clients_session
from database.postgres_schemas import Address, Client
from faker import Faker
from faker.providers import DynamicProvider
from sqlalchemy import insert
from dotenv import load_dotenv

load_dotenv()

valid_address_provider = DynamicProvider(
    provider_name="address_fields",
    elements=[
        (97, "Санкт-Петербург", "пер.", "Кустарный", "4"),
        (97, "Санкт-Петербург", "ул.", "Софийская", "60"),
        (97, "Санкт-Петербург", "ул.", "Седова", "65"),
        (97, "Санкт-Петербург", "ул.", "Садовая", "50"),
        (59, "Гатчина", "ул.", "Варшавская", "5"),
        (78, "Кронштадт", "шоссе", "Цитадельское", "38Б"),
        (80, "Выборг", "ул.", "Октябрьская", "32А")
    ],
)
fake = Faker("ru_RU")
fake.add_provider(valid_address_provider)


@pytest.fixture(scope="session")
def temp_db():

    db_client_values = Client(
        company_id=7,
        date_created=fake.date_time_between(start_date="-1y", end_date="now"),
        created_by=1,
        come_from="Другое",
        sms=fake.numerify("####"),
        type=fake.boolean(),
        name=fake.first_name(),
        phone=fake.numerify(text="+7(###) ###-####"),
        email=fake.email(),
        contract_company=1,
        contact_person=fake.name(),
        inn=fake.numerify(text="78########"),
        accounting_phone=fake.bothify(text="+7(###) ###-####"),
        manager_notice=fake.paragraph(nb_sentences=2),
        mailing_consent=True,
    )

    clients_session.add(db_client_values)
    clients_session.commit()

    # получение и вывод полей только что созданного клиента
    new_client_id = db_client_values.id
    print(new_client_id)

    for k, v in vars(db_client_values).items():
        print(k, v)

    # получение полей случайного адреса из Faker
    # full_address = fake.address_fields()
    #
    # db_address_values = Address(
    #     client_id=new_client_id,
    #     company_id=7,
    #     date_created=fake.date_time_between(start_date="-1y", end_date="now"),
    #     created_by=1,
    #     address=f"{full_address[1]}, {full_address[2]} {full_address[3]}, {full_address[4]}",
    #     delivery_area_id=full_address[0],
    #     region=full_address[1],
    #     street=full_address[2],
    #     house=full_address[3]
    # )
    #
    # # получение и вывод полей только что созданного адреса
    # new_address_id = db_address_values.id
    # print(new_address_id)
    #
    # for k, v in vars(db_address_values).items():
    #     print(k, v)

    # генерация JWT-токена, содержащего айди созданного клиента
    new_client_token = jwt_gen(new_client_id)

    # создание словаря с данными, которые передает в себе фикстура
    fixture_dict = {
        "new_client_id": new_client_id,
        "db_client_data": db_client_values,
        "new_client_token": new_client_token,
        # "new_address_id": new_address_id
    }

    yield fixture_dict
    print("\nEnding of tests")
    new_id_client = clients_session.query(Client).filter(Client.id == new_client_id).first()
    clients_session.delete(new_id_client)
    clients_session.commit()
    clients_session.close()


# метод генерации токена который принимает айди клиента
def jwt_gen(new_client_id):
    token_dict = {
        "sub": f"{new_client_id}",
        "company_id": 7,
        "isF": "Android",
        "exp": 1704056400
    }
    return jwt.encode(token_dict, os.getenv("SECRET_HASH"), algorithm="HS256")
