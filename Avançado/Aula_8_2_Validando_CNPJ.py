from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if self.tipo_documento == "cpf":
            if self.cpf_eh_Valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!")
        elif self.tipo_documento == "cnpj":
            if self.cnpj_eh_Valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido!")

    def cpf_eh_Valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida!")

    def format_cpf(self):
        mascara_cpf = CPF()
        mascara_cnpj = CNPJ()
        if self.tipo_documento == 'cpf':
            return mascara_cpf.mask(self.cpf)
        else:  
            return mascara_cnpj.mask(self.cnpj)

    def __str__(self):
        return self.format_cpf()

    def cnpj_eh_Valido(self, cnpj):
        if len(cnpj)==14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos inválida!")
    
cpf = "70988043475"
objeto_cpf = CpfCnpj(cpf, "cpf")

print(objeto_cpf)    

cnpj = "35379838000112"
objeto_cnpj = CpfCnpj(cnpj, "cnpj")

print(objeto_cnpj)