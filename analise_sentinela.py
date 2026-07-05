import pandas as pd

df = pd.read_excel(
    r"C:\Users\User\Desktop\Sentinela Financeira\Sentinela_Financeira_Transacoes.xlsx"
)

print(df.head())

duplicados = df[
    df.duplicated(
        subset=[
            "Fornecedor",
            "Valor",
            "Data"
        ],
        keep=False
    )
]

valores_suspeitos = df[
    df["Valor"] > 50000
]

df["Data"] = pd.to_datetime(
    df["Data"]
)

fim_semana = df[
    df["Data"].dt.dayofweek >= 5
]

split_payments = (
    df.groupby(
        ["Fornecedor", "Data"]
    )
    .agg(
        Quantidade=("ID", "count"),
        Valor_Total=("Valor", "sum")
    )
    .reset_index()
)

split_payments = split_payments[
    (split_payments["Quantidade"] >= 3)
    &
    (split_payments["Valor_Total"] > 50000)
]

incompativeis = df[
    (
        df["Fornecedor"]
        .isin([
            "Mega Transportes",
            "Delta Logística"
        ])
    )
    &
    (
        df["Centro_Custo"] == "RH"
    )
]

df["Score_Fraude"] = 0

df.loc[
    df["Valor"] > 50000,
    "Score_Fraude"
] += 25

df.loc[
    df["Data"].dt.dayofweek >= 5,
    "Score_Fraude"
] += 15

df.loc[
    df["Fornecedor"].isin(
        [
            "Fornecedor X",
            "Fornecedor Y"
        ]
    ),
    "Score_Fraude"
] += 30

df["Nivel_Risco"] = pd.cut(
    df["Score_Fraude"],
    bins=[
        -1,
        15,
        35,
        60,
        100
    ],
    labels=[
        "Baixo",
        "Médio",
        "Alto",
        "Crítico"
    ]
)

print("\n===== RESUMO DA ANÁLISE =====")

print(f"Total de Transações: {len(df)}")
print(f"Duplicados: {len(duplicados)}")
print(f"Valores Suspeitos: {len(valores_suspeitos)}")
print(f"Pagamentos em Fim de Semana: {len(fim_semana)}")
print(f"Incompatibilidades: {len(incompativeis)}")
print(f"Possíveis Split Payments: {len(split_payments)}")

with pd.ExcelWriter(
    r"C:\Users\User\Desktop\Sentinela Financeira\Relatorio_Sentinela.xlsx"
) as writer:

    duplicados.to_excel(
        writer,
        sheet_name="Duplicados",
        index=False
    )

    valores_suspeitos.to_excel(
        writer,
        sheet_name="Valores_Suspeitos",
        index=False
    )

    fim_semana.to_excel(
        writer,
        sheet_name="Fim_Semana",
        index=False
    )

    incompativeis.to_excel(
        writer,
        sheet_name="Incompativeis",
        index=False
    )

    split_payments.to_excel(
        writer,
        sheet_name="Split_Payments",
        index=False
    )

    df.to_excel(
        writer,
        sheet_name="Base_Completa",
        index=False
    )
    
    print("\nRelatório gerado com sucesso!")
    print(
    r"C:\Users\User\Desktop\Sentinela Financeira\Relatorio_Sentinela.xlsx"
    )