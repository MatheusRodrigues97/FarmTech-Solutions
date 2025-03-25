import os
from typing import List, Dict, Union
from dataclasses import dataclass
from math import pi


@dataclass
class Cultura:
    nome: str
    area: float
    linhas: int
    produto: str
    dosagem_por_metro: float


class SistemaDeGestaoAgricola:
    def __init__(self):
        self.culturas: List[Cultura] = []

    def calcular_area_circular(self, raio: float) -> float:
        return pi * (raio**2)

    def calcular_area_retangular(self, comprimento: float, largura: float) -> float:
        return comprimento * largura

    def calcular_produto_necessario(self, cultura: Cultura) -> float:
        return cultura.area * cultura.dosagem_por_metro

    def adicionar_cultura(self, cultura: Cultura) -> None:
        self.culturas.append(cultura)

    def atualizar_cultura(self, indice: int, cultura: Cultura) -> bool:
        if 0 <= indice < len(self.culturas):
            self.culturas[indice] = cultura
            return True
        return False

    def deletar_cultura(self, indice: int) -> bool:
        if 0 <= indice < len(self.culturas):
            self.culturas.pop(indice)
            return True
        return False

    def exibir_culturas(self) -> None:
        if not self.culturas:
            print("\nNenhuma cultura registrada ainda.")
            return

        print("\nCulturas Registradas:")
        for i, cultura in enumerate(self.culturas):
            print(f"\nCultura {i + 1}:")
            print(f"Nome: {cultura.nome}")
            print(f"Área: {cultura.area:.2f} m²")
            print(f"Número de linhas: {cultura.linhas}")
            print(f"Produto: {cultura.produto}")
            print(f"Dosagem por metro: {cultura.dosagem_por_metro:.2f} mL/m²")
            print(
                f"Total de produto necessário: {self.calcular_produto_necessario(cultura):.2f} mL"
            )


def limpar_tela():
    # Imprimir novas linhas em vez de usar os.system
    print("\n" * 50)


def obter_input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor, insira um número válido.")


def obter_input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor, insira um número inteiro válido.")


def main():
    sistema_fazenda = SistemaDeGestaoAgricola()

    while True:
        limpar_tela()
        print("\n=== Soluções FarmTech - Sistema de Gestão Agrícola ===")
        print("1. Adicionar nova cultura")
        print("2. Exibir todas as culturas")
        print("3. Atualizar cultura")
        print("4. Deletar cultura")
        print("5. Exportar dados para análise em R")
        print("6. Sair")

        escolha = input("\nDigite sua escolha (1-6): ")

        if escolha == "1":
            limpar_tela()
            print("\n=== Adicionando Nova Cultura ===")
            nome = input("Digite o nome da cultura (Soja/Café): ").capitalize()
            if nome not in ["Soja", "Café"]:
                print("Apenas Soja e Café são suportados.")
                input("Pressione Enter para continuar...")
                continue

            forma = input("Calcular área usando (R)etângulo ou (C)írculo? ").upper()
            if forma == "R":
                comprimento = obter_input_float("Digite o comprimento (metros): ")
                largura = obter_input_float("Digite a largura (metros): ")
                area = sistema_fazenda.calcular_area_retangular(comprimento, largura)
            elif forma == "C":
                raio = obter_input_float("Digite o raio (metros): ")
                area = sistema_fazenda.calcular_area_circular(raio)
            else:
                print("Seleção de forma inválida.")
                input("Pressione Enter para continuar...")
                continue

            linhas = obter_input_int("Digite o número de linhas: ")
            produto = input("Digite o nome do produto: ")
            dosagem = obter_input_float("Digite a dosagem por metro (mL/m²): ")

            cultura = Cultura(nome, area, linhas, produto, dosagem)
            sistema_fazenda.adicionar_cultura(cultura)
            print("\nCultura adicionada com sucesso!")

        elif escolha == "2":
            limpar_tela()
            sistema_fazenda.exibir_culturas()

        elif escolha == "3":
            limpar_tela()
            sistema_fazenda.exibir_culturas()
            if sistema_fazenda.culturas:
                indice = (
                    obter_input_int(
                        "\nDigite o índice da cultura para atualizar (1-{}): ".format(
                            len(sistema_fazenda.culturas)
                        )
                    )
                    - 1
                )
                if 0 <= indice < len(sistema_fazenda.culturas):
                    nome = input(
                        "Digite o novo nome da cultura (Soja/Café): "
                    ).capitalize()
                    if nome not in ["Soja", "Café"]:
                        print("Apenas Soja e Café são suportados.")
                        input("Pressione Enter para continuar...")
                        continue

                    forma = input(
                        "Calcular área usando (R)etângulo ou (C)írculo? "
                    ).upper()
                    if forma == "R":
                        comprimento = obter_input_float(
                            "Digite o comprimento (metros): "
                        )
                        largura = obter_input_float("Digite a largura (metros): ")
                        area = sistema_fazenda.calcular_area_retangular(
                            comprimento, largura
                        )
                    elif forma == "C":
                        raio = obter_input_float("Digite o raio (metros): ")
                        area = sistema_fazenda.calcular_area_circular(raio)
                    else:
                        print("Seleção de forma inválida.")
                        input("Pressione Enter para continuar...")
                        continue

                    linhas = obter_input_int("Digite o número de linhas: ")
                    produto = input("Digite o nome do produto: ")
                    dosagem = obter_input_float("Digite a dosagem por metro (mL/m²): ")

                    cultura = Cultura(nome, area, linhas, produto, dosagem)
                    sistema_fazenda.atualizar_cultura(indice, cultura)
                    print("\nCultura atualizada com sucesso!")
                else:
                    print("\nÍndice inválido!")

        elif escolha == "4":
            limpar_tela()
            sistema_fazenda.exibir_culturas()
            if sistema_fazenda.culturas:
                indice = (
                    obter_input_int(
                        "\nDigite o índice da cultura para deletar (1-{}): ".format(
                            len(sistema_fazenda.culturas)
                        )
                    )
                    - 1
                )
                if sistema_fazenda.deletar_cultura(indice):
                    print("\nCultura deletada com sucesso!")
                else:
                    print("\nÍndice inválido!")

        elif escolha == "5":
            limpar_tela()
            if not sistema_fazenda.culturas:
                print("\nNenhum dado para exportar!")
            else:
                with open("dados_fazenda.csv", "w") as f:
                    f.write(
                        "nome,area,linhas,produto,dosagem_por_metro,total_produto\n"
                    )
                    for cultura in sistema_fazenda.culturas:
                        f.write(
                            f"{cultura.nome},{cultura.area},{cultura.linhas},{cultura.produto},"
                            f"{cultura.dosagem_por_metro},{sistema_fazenda.calcular_produto_necessario(cultura)}\n"
                        )
                print("\nDados exportados para 'dados_fazenda.csv' com sucesso!")

        elif escolha == "6":
            print("\nObrigado por usar as Soluções FarmTech!")
            break

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()
