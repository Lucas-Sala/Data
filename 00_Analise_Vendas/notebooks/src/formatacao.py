from matplotlib.ticker import FuncFormatter

def formatar_real(x,pos):
    return ( f"R$ {x:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
    

def quantia(x, pos):
    return f"{x:,.0f}".replace(",", ".")

def moeda_milhao(x, pos):
    return f"{x/1_000_000:,.0f}"

def moeda_mil(x, pos):
    return f"{x/1_000:,.0f}"