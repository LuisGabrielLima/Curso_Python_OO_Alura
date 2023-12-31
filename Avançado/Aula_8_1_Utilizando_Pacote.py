from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_Valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def cpf_eh_Valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
        
    def __str__(self):
        return self.format_cpf()
        
cpf = "70988043475"
objeto_cpf = Cpf(cpf)
print(objeto_cpf)