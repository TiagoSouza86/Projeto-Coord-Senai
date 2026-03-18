
from processamento import validar_dados, calcular_media, definir_situacao

# Estrutura: Lista de Tuplas [("Nome", [notas])]
alunos = [
    ("Gustavo Silva", [8.5, 7.0, 9.0]),
    ("Maria Rosa", [6.0, 5.5, 4.0, 6.7]),
    ("João Pedro", []),             # Caso de lista vazia
    ("Ana Cristine ", [10, "erro", 8]), #
    ("Pedro Santos ", [9.5, 10.0, 7.8]),
    ("Tiago Henrique", [7.8, 10.0, 7.6, ]),
    ("Fernanda Vasconcelo", [5.5, 7.8, 5.4]),
    ("Luana Pires", [7.5, 7.8, 8.9]),
    ("Carla Tocantis", [8.7, 6.7, 7,8]),
    ("Caroline Andrade", [5.4, 6.8, 7.0]),
    ("Receba Souza", [5.4, 5.5, 5.0]),
    ("Felipe Pires", [9.9, 8.8, 8,7]), 
    ("Anne Flavia", [9.9, 8.8, 10.0]),
]

def rodar_sistema():
    resultados = []
    top_student = {"nome": "", "media": -1}

    print("--- PROCESSANDO DESEMPENHO ACADÊMICO ---")

    for nome, notas in alunos:
        # TRATAMENTO DE DADOS
        if validar_dados(notas):
            media = calcular_media(notas)
            situacao = definir_situacao(media)
            
            # Lógica para o Top Student
            if media > top_student["media"]:
                top_student["nome"] = nome
                top_student["media"] = media

            resultados.append(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}\n")
        else:
            resultados.append(f"Aluno: {nome} | ERRO: Dados inválidos ou incompletos.\n")

    # BÔNUS: Geração do arquivo .txt
    with open("resultado.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("RELATÓRIO FINAL DE NOTAS\n")
        arquivo.write("="*30 + "\n")
        arquivo.writelines(resultados)
        arquivo.write("="*30 + "\n")
        arquivo.write(f"TOP STUDENT: {top_student['nome']} com média {top_student['media']:.2f}")

    print("Relatório 'resultado.txt' gerado com sucesso!")

if __name__ == "__main__":
    rodar_sistema()