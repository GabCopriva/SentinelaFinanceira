import pandas as pd
import numpy as np
from faker import Faker
from random import choice, randint

fake = Faker('pt_BR')

np.random.seed(42)

qtd = 10000

fornecedores = [
    "Tech Solutions",
    "Global Services",
    "Alpha Consultoria",
    "Mega Transportes",
    "Delta Logística",
    "Fornecedor X",
    "Fornecedor Y",
    "Fornecedor Z"
]

centros = [
    "TI",
    "Financeiro",
    "RH",
    "Marketing",
    "Operações",
    "Jurídico"
]

dados = []

for i in range(qtd):

    valor = round(np.random.normal(5000, 2500), 2)

    if valor < 100:
        valor = round(np.random.uniform(100, 1000), 2)

    data = fake.date_between(
        start_date='-2y',
        end_date='today'
    )

    fornecedor = choice(fornecedores)

    centro = choice(centros)

    dados.append([
        f"TRX{i+1:05}",
        data,
        fornecedor,
        centro,
        valor
    ])

df = pd.DataFrame(
    dados,
    columns=[
        "ID",
        "Data",
        "Fornecedor",
        "Centro_Custo",
        "Valor"
    ]
)

# ==========================
# DUPLICADOS
# ==========================

duplicados = df.sample(250)

df = pd.concat(
    [df, duplicados],
    ignore_index=True
)

# ==========================
# VALORES FORA DO PADRÃO
# ==========================

for i in np.random.choice(df.index, 300):

    df.loc[i, "Valor"] = np.random.uniform(
        50000,
        250000
    )

# ==========================
# PAGAMENTOS FRACIONADOS
# ==========================

for i in range(150):

    fornecedor = choice(fornecedores)

    data = fake.date_between(
        start_date='-1y',
        end_date='today'
    )

    valor_total = randint(
        60000,
        150000
    )

    partes = randint(3, 6)

    valor_parte = round(
        valor_total / partes,
        2
    )

    for j in range(partes):

        nova_linha = {
            "ID": f"SPLIT{i}{j}",
            "Data": data,
            "Fornecedor": fornecedor,
            "Centro_Custo": choice(centros),
            "Valor": valor_parte
        }

        df = pd.concat(
            [df, pd.DataFrame([nova_linha])],
            ignore_index=True
        )

# ==========================
# FORNECEDORES SUSPEITOS
# ==========================

suspeitos = [
    "Fornecedor X",
    "Fornecedor Y"
]

indices = df[
    df["Fornecedor"].isin(suspeitos)
].sample(400).index

for i in indices:

    df.loc[i, "Valor"] *= np.random.uniform(
        3,
        8
    )

# ==========================
# CENTROS INCOMPATÍVEIS
# ==========================

for i in np.random.choice(df.index, 200):

    df.loc[i, "Centro_Custo"] = "RH"

    df.loc[i, "Fornecedor"] = choice([
        "Mega Transportes",
        "Delta Logística"
    ])

# ==========================
# FINS DE SEMANA
# ==========================

for i in np.random.choice(df.index, 300):

    df.loc[i, "Data"] = pd.Timestamp(
        "2025-08-02"
    )

# ==========================
# SALVAR
# ==========================

import os

pasta_projeto = r"C:\Users\User\Desktop\Sentinela Financeira"

arquivo = os.path.join(
    pasta_projeto,
    "Sentinela_Financeira_Transacoes.xlsx"
)

df.to_excel(
    arquivo,
    index=False
)

print("Base criada com sucesso!")
print("Salvo em:")
print(arquivo)