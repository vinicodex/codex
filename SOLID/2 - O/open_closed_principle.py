"""
Open/Closed Principle (OCP) – SOLID

OCP states that:
    - Software should be **open for extension**
    - But **closed for modification**

In practice, this means we should be able to add new behaviors without
modifying existing, stable, tested code.

Below is a classic “bad example” that violates OCP:
each time a new operation is needed, the `operacao` method must be modified.

Then, a refactored version uses abstractions and polymorphism to allow
adding new operations without changing existing ones.
"""

# Bad Example — violates OCP
class Calc:
    def operacao(self, tipo, a, b):
        if tipo == "soma":
            return a + b
        elif tipo == "divisao":
            return a / b
        elif tipo == "subtracao":
            return a - b
        else:
            raise ValueError(f"{tipo} não encontrado")

# OCP Applied — Open for extension, closed for modification
from abc import ABC, abstractmethod


class Operacao(ABC):
    @abstractmethod
    def calcular(self, a, b):
        """Performs a calculation using two numbers."""
        pass


class Soma(Operacao):
    def calcular(self, a, b):
        return a + b


class Divisao(Operacao):
    def calcular(self, a, b):
        return a / b


class Subtracao(Operacao):
    def calcular(self, a, b):
        return a - b


def executar_operacao(operacao: Operacao, a, b):
    return operacao.calcular(a, b)


# Example usage
if __name__ == "__main__":
    print(executar_operacao(Soma(), 10, 5))        # 15
    print(executar_operacao(Subtracao(), 10, 5))   # 5
    print(executar_operacao(Divisao(), 10, 5))     # 