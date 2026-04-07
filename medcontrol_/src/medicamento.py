class Medicamento:
    def __init__(self, nome, horario):
        if not nome:
            raise ValueError("Nome inválido")
        self.nome = nome
        self.horario = horario

    def to_dict(self):
        return {"nome": self.nome, "horario": self.horario}