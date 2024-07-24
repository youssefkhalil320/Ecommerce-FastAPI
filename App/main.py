from modules.user import User
from modules.business import Business
from modules.product import Product
from tortoise.contrib.pydantic import pydantic_model_creator
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


user_pydantic = pydantic_model_creator(
    User, name="User", exclude=("is_verified", ))

user_pydanticIn = pydantic_model_creator(
    User, name="UserIn", exclude_readonly=True)

user_pydanticOut = pydantic_model_creator(
    User, name="UserOut", exclude=("password", ))


business_pydantic = pydantic_model_creator(
    Business, name="Business")

business_pydanticIn = pydantic_model_creator(
    Business, name="BusinessIn", exclude_readonly=True)

product_pydantic = pydantic_model_creator(Product, name="Product")

product_pydanticIn = pydantic_model_creator(
    Product, name="ProductIn", exclude=("percentage_discount", "id"))


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World!"}


register_tortoise(app, db_url="sqlite://db.sqlite3",
                  modules={"models": ["modules.user",
                                      "modules.business", "modules.product"]},
                  generate_schemas=True,
                  add_exception_handlers=True)
