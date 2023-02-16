from inventory_report.inventory.product import Product

id: 198
nome_do_produto = "Cafe"
nome_da_empresa = "Cafes Nature"
data_de_fabricacao = "2020-07-04"
data_de_validade = "2023-02-09"
numero_de_serie = "FR48"
instrucoes_de_armazenamento = "instrucao"


def my_product_report():
    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    return (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )


def test_relatorio_produto():
    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert product.__repr__() == my_product_report()
