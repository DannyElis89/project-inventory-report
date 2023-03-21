# Project Inventory Repository

Durante o módulo de Ciência da Computação no curso de Desenvolvimento Web da Trybe, desenvolvemos um projeto que utilizou conceitos de `POO` e `Padrões de Projeto` em `Python` (`Design Patterns` - `Strategy`).

A aplicação suporta a importação de arquivos nos formatos `CSV`, `JSON` e `XML`, e pode gerar relatórios **simples** ou **completos**, dependendo da necessidade do usuário.

<details>
<summary><strong>🚵 Habilidades trabalhadas:</strong></summary>
Durante o projeto, trabalhamos com diversas habilidades valiosas para o desenvolvimento de software em Python:
<ul>
<li>Utilização dos conceitos de Orientação a Objetos para a construção de uma aplicação robusta e escalável;</li>
<li>Implementação de padrões de projeto que promovem a reutilização de código e a manutenibilidade do projeto;</li>
<li>Leitura e escrita de arquivos nos formatos XML, CSV e JSON, que são comumente utilizados para armazenar dados estruturados.</li>
</ul>
Essas habilidades são fundamentais para a construção de aplicações eficientes e de alta qualidade em Python, e foram aplicadas de forma prática e contextualizada durante o projeto desenvolvido na Trybe.
</details>

<details>
<summary><strong>🧱 Estrutura do Projeto</strong></summary><br />
  O projeto em questão já foi iniciado com um template que fornece uma estrutura de diretórios e arquivos, tanto de código quanto de testes, criados pela Trybe. Dessa forma, o projeto segue um padrão bem definido, que facilita a sua compreensão e manutenção. Abaixo, você pode conferir mais detalhes sobre essa estrutura:

  > Para facilitar a compreensão do projeto, utilizamos uma legenda que diferencia os arquivos fornecidos pela Trybe daqueles que foram criados por mim para implementação do projeto. Dessa forma, fica mais fácil visualizar quais arquivos fazem parte do template original e quais foram criados ou modificados durante o desenvolvimento do projeto.
  ```
  Legenda:
  🔸Arquivos forrnecidos pela Trybe
  🔹Arquivos com código autoral para implementação do projeto.
  .
  ├── inventory_report
  │   ├── data
  │   │   ├── 🔸inventory.csv
  │   │   ├── 🔸inventory.json
  │   │   └── 🔸inventory.xml
  │   ├── importer
  │   │   ├── 🔹csv_importer.py
  │   │   ├── 🔹importer.py
  │   │   ├── 🔹json_importer.py
  │   │   └── 🔹xml_importer.py
  │   ├── inventory
  │   │   ├── 🔹inventory_iterator.py
  │   │   ├── 🔹inventory_refactor.py
  │   │   └── 🔹inventory.py
  │   │   └── 🔸product.py
  │   ├── reports
  │   │   ├── 🔸colored_report.py
  │   │   ├── 🔹complete_report.py
  │   │   └── 🔹simple_report.py
  │   └── 🔹main.py
  └── tests
  │   ├── factories
  │   │   ├── 🔸__init__.py
  │   │   └── 🔸product_factory.py
  │   ├── product
  │   │   ├── 🔸__init__.py
  │   │   ├── 🔸conftest.py
  │   │   ├── 🔸mocks.py
  │   │   └── 🔹test_product.py
  │   ├── product_report
  │   │   ├── 🔸__init__.py
  │   │   ├── 🔸conftest.py
  │   │   ├── 🔸mocks.py
  │   │   └── 🔹test_product_report.py
  │   ├── report_decorator
  │   │   ├── 🔸__init__.py
  │   │   ├── 🔸conftest.py
  │   │   ├── 🔸mocks.py
  │   │   └── 🔹test_report_decorator.py
  │   ├── 🔸__init__.py
  ├── 🔹dev-requirements.txt
  ├── 🔸docker-compose.yml
  ├── 🔸Dockerfile
  ├── 🔸pyproject.toml
  ├── 🔸README.md
  ├── 🔸requirements.txt
  ├── 🔸setup.cfg
  └── 🔸setup.py
  ```
</details>


<details>
<summary><strong>Rodando o projeto</strong></summary>
1. Clonar o repositório e entrar no diretório;
2. Criar ambiente virtual:
   * `python3 -m venv .venv && source .venv/bin/activate`
3. Instalar dependências do projeto:
   * `python3 -m pip install -r dev-requirements.txt`
</details>

## 🧱 Requisitos

<details>
<summary><strong>1 - Testar o construtor/inicializador do objeto Produto</strong></summary>

> **Teste criado em:** tests/product/test_product.py

A classe `Product` é um objeto do sistema de gerenciamento de estoque e está implementada no arquivo `inventory_report/inventory/product.py`.

Durante o desenvolvimento, foi criado o teste `test_cria_produto` para certificar que o método `__init__` da classe `Product` esteja funcionando corretamente. Esse teste verifica se os seguintes atributos estão sendo preenchidos corretamente:

- id (int)
- nome_da_empresa (string)
- nome_do_produto (string)
- data_de_fabricacao (string)
- data_de_validade (string)
- numero_de_serie (string)
- instrucoes_de_armazenamento (string)
</details>


<details><summary><strong>2 - Gerar a versão simplificada do relatório</strong></summary>

> **Classe criada em:** inventory_report/reports/simple_report.py

O relatório é gerado pelo método de classe `generate` definido dentro da classe `SimpleReport`.

É possível chamar o método generate sem instanciar um objeto da classe `SimpleReport`.
O método espera uma lista de dicionários como parâmetro de entrada, onde cada dicionário representa um produto com as seguintes chaves:

```json
   [
     {
       "id": 1,
       "nome_do_produto": "CADEIRA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar em local fresco"
     }
   ]
```

- O método retorna uma `string` de saída com o seguinte formato:
   ```bash
   Data de fabricação mais antiga: YYYY-MM-DD
   Data de validade mais próxima: YYYY-MM-DD
   Empresa com mais produtos: NOME DA EMPRESA
   ```
- A data de validade mais próxima considera apenas os produtos que ainda não venceram.
</details>


<details>
<summary><strong>3 - Gerar a versão completa do relatório</strong></summary>

> **Desenvolvido em:** inventory_report/reports/complete_report.py

O relatório é gerado através do método `generate` da classe `CompleteReport`. Este método recebe uma lista de dicionários no formato especificado abaixo e retorna uma string formatada como um relatório.

A classe `CompleteReport` herda da classe `SimpleReport` e sobrescreve o método `generate` para especializar seu comportamento. É possível executar o método `generate` sem instanciar um objeto de `CompleteReport`.

O método `generate` recebe uma lista de dicionários no seguinte formato:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "MESA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-05-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
     }
   ]
   ```

- O método retorna uma saída com o seguinte formato:

```bash
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
Produtos estocados por empresa:
- Physicians Total Care, Inc.: QUANTIDADE
- Newton Laboratories, Inc.: QUANTIDADE
- Forces of Nature: QUANTIDADE
```
</details>


<details>
<summary><strong>4 - Gerar os relatórios através de um arquivo CSV, JSON ou XML </strong></summary>

> **Desenvolvido em:** inventory_report/inventory/inventory.py

O processo de importação de dados do arquivo `CSV` é executado pelo método `import_data` criado na classe `Inventory`.

Esse método tem dois parâmetros de entrada: o primeiro é uma `string` que contém o caminho para o arquivo, que pode estar nos formatos `CSV`, `JSON` ou `XML`; o segundo é uma `string` que indica o tipo de relatório que deve ser gerado. Os tipos disponíveis são `simples` e `completo`.

Com base nos parâmetros de entrada, o método `import_data` recupera os dados do arquivo e chama o método `generate` da classe correspondente para gerar o relatório adequado.

Em outras palavras, a classe `Inventory` delega a geração do relatório para uma das classes que implementam a interface `InventoryReport`. As classes que implementam essa interface são `SimpleReport` e `CompleteReport`
</details>


<details>
<summary><strong>5 - Organizar o código de importação com o padrão Strategy</strong></summary>

> **Implementado em:** inventory_report/importer/importer.py

Com o objetivo de simplificar o método `import_data` e melhorar a manutenção do código, utilizamos o padrão de projeto `Strategy` para separar as responsabilidades de cada formato de arquivo em classes específicas. Para garantir a padronização dos métodos, criamos uma classe abstrata chamada `Importer` que define a interface que as classes estratégias devem seguir.

Assim, cada classe estratégia (como `CsvImporter`, `JsonImporter` e `XmlImporter`) pode tratar o formato de arquivo de forma específica, sem a necessidade de modificar a lógica do método `import_data`. Cada classe estratégia foi criada em um arquivo separado seguindo a convenção de nomenclatura `inventory_report/importer/{nome_do_formato}_importer.py`.

Essa abordagem torna o código mais organizado, simplifica a manutenção e permite a escalabilidade da aplicação.

</details>


<details>
<summary><strong>6 - Testar o relatório individual do produto</strong></summary>

> **Desenvolvido em:** tests/product_report/test_product_report.py

O teste test_relatorio_produto abrange todo o código desenvolvido no arquivo `inventory_report/inventory/product.py`. Ele instanciará um objeto `Product` e verificará se a frase de retorno está correta ao acessá-lo.

Para elaborar esse relatório, foi utilizado o recurso `__repr__` do Python, o qual permite alterar a representação do objeto. Dessa forma, toda vez que usarmos a função print para esse objeto, em vez de receber um endereço de memória, teremos uma string personalizada, como esta abaixo:

> O produto `farinha` fabricado em `01-05-2021` por `Farinini` com validade até `02-06-2023` precisa ser armazenado `ao abrigo de luz`.

</details>


<details>
<summary><strong>7 - Testar a geração de uma versão do relatório em cores</strong></summary>

> **Teste desenvolvido em:** tests/report_decorator/test_report_decorator.py

Na estrutura inicial do projeto, já estava desenvolvido um método que retorna relatórios em letreiros de LED, presente no arquivo `inventory_report/reports/colored_report.py`.

Esse método utiliza o padrão de projeto `Decorator`, que permite receber o tipo do relatório por composição (`SimpleReport` ou `CompleteReport`) e colorir o resultado retornado pelo método `generate`, o qual recebe uma lista de produtos e retorna o relatório já colorido.

O teste `test_decorar_relatorio` certifica se o método `generate` da classe `ColoredReport` funciona corretamente, seguindo o padrão mencionado a seguir:
- Verde:
    - "Data de fabricação mais antiga:"
    - "Data de validade mais próxima:"
    - "Empresa com mais produtos:"
- Azul: As datas
- Vermelho: Nome da empresa com mais produtos
</details>


<details>
<summary><strong>8 - Criar uma classe InventoryIterator</strong></summary>

> **Desenvolvido em:** inventory_report/inventory/inventory_iterator.py

O estoque é exibido por meio de painéis de LED, sem sobrecarregar a memória desses dispositivos. Para que isso aconteça, é necessário iterar pelos itens do estoque, um item de cada vez. Para isso, a solução proposta é refatorar a forma como os dados são importados e, em seguida, aplicar o Padrão `Iterator`.

A classe `Inventory` foi refatorada em outro arquivo chamado `inventory_report/inventory/inventory_refactor.py` e renomeada como `InventoryRefactor`.

A classe `InventoryRefactor` utiliza as classes definidas no requisito 6 para lidar com a lógica de importação por meio de composição no método `import_data`.

A classe `InventoryRefactor` recebe a classe que será utilizada para lidar com a lógica de importação por meio de seu construtor, armazenando-a em um atributo chamado `importer`.

A classe `InventoryRefactor` possui um método de instância que recebe um caminho para o arquivo a ser importado e carrega seus dados.

Ao importar os dados, eles são armazenados na instância, em adição aos itens já presentes. O atributo que armazena esses dados é chamado de `data`.

A classe `InventoryIterator` implementa a interface de um iterador (Iterator) com o método `__next__`. Além disso, a classe `InventoryRefactor` implementa o método `__iter__`, que retorna este iterador.

As classes `InventoryIterator` e `InventoryRefactor` implementam a interface do Padrão Iterator, tornando possível iterar sobre os itens em estoque, um item de cada vez.

</details>


<details>
<summary><strong>9 - Preencha a função main no módulo inventory_report/main.py</strong></summary>

Ao receber o caminho de um arquivo e o tipo de relatório pela linha de comando, a função é capaz de gerar e imprimir na tela o relatório correspondente. Para isso, ela utiliza a classe `InventoryRefactor` para recuperar os dados do arquivo e gerar o relatório.

O comando para executar a função segue o formato abaixo:
```bash
inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>
```

Ao executar o comando no terminal, o relatório correspondente é impresso na tela, podendo ser do tipo simplificado ou completo.

</details>
