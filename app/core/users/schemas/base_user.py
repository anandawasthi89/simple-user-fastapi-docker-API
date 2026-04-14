from pydantic import BaseModel, computed_field, field_validator

class BaseUser(BaseModel):
    first_name: str
    last_name: str
    bank_id: str
    bank_account: str
    email: str

    @field_validator('bank_account')
    def validate_bank_account(cls, value):
        if len(value) != 10:
            raise ValueError('Invalid bank account number')
        return value

    @field_validator('email')
    def validate_email(cls, value):
        if '@'  not in value or '.' not in value:
            raise ValueError('Invalid email address')
        return value
    
    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"