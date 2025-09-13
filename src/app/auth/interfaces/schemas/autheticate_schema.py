import re

from pydantic import BaseModel, field_validator


class AuthenticateSchema(BaseModel):
    password: str
    cpf: str


    @field_validator("password")
    def validar_senha(cls, v):
        if len(v) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres")
        if not re.search(r"[A-Z]", v):
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula")
        if not re.search(r"[a-z]", v):
            raise ValueError("A senha deve conter pelo menos uma letra minúscula")
        if not re.search(r"\d", v):
            raise ValueError("A senha deve conter pelo menos um número")
        return v

    @field_validator("cpf")
    def validar_cpf(cls, v):
        padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
        if not re.match(padrao, v):
            raise ValueError("CPF deve estar no formato 000.000.000-00")

        cpf_numerico = re.sub(r"\D", "", v)
        if not cls.validar_digitos_verificadores(cpf_numerico):
            raise ValueError("CPF inválido")
        return v

    @staticmethod
    def validar_digitos_verificadores(cpf: str) -> bool:
        if cpf == cpf[0] * len(cpf):
            return False

        def calcular_digito(cpf, pesos):
            soma = sum(int(d) * p for d, p in zip(cpf, pesos))
            resto = soma % 11
            return "0" if resto < 2 else str(11 - resto)

        digito1 = calcular_digito(cpf[:9], range(10, 1, -1))
        digito2 = calcular_digito(cpf[:10], range(11, 1, -1))
        return cpf[-2:] == digito1 + digito2