def limpar_preco(df, coluna):
    df[coluna] = (
        df[coluna]
            .str.replace("R$", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.strip()
            .astype(float)
    )

    return df

def ajusta_nome(df, coluna):
    df[coluna] = (
        df[coluna]
        .str.split(", ", expand=True)
        .apply(lambda x: f"{x[1]} {x[0]}", axis=1)
    )
    return df

def substitui_genero(df, coluna):
    df[coluna] = (df[coluna].replace({
        "M": "Masculino",
        "F": "Feminino"})
    )
    return df