# 📊 DataApp - Análise de Dados com Interface Gráfica

Este projeto é uma aplicação desenvolvida em Python utilizando `tkinter` para análise de dados a partir de planilhas CSV ou Excel. A ferramenta permite visualizar dados em formato de tabela, realizar análises estatísticas, calcular frequência relativa e coeficiente de correlação, inserir novos dados e exportar os resultados para o Tableau.

---

## 🚀 Funcionalidades

- 📂 **Carregar Planilha**: Importa arquivos `.csv`, `.xlsx` ou `.xls`.
- 📈 **Frequência Relativa**: Calcula a frequência relativa da coluna `dual_sim`.
- 🔗 **Coeficiente de Correlação**: Calcula a correlação entre as colunas `ram` e `battery_power`.
- 📊 **Estatísticas**: Exibe média, mediana, soma e contagem da coluna `battery_power`.
- ⬆️ **Máximo e Mínimo**: Mostra os valores máximos e mínimos das colunas `px_height` e `px_width`.
- ➕ **Inserir Valor**: Permite adicionar manualmente uma nova linha de dados à tabela.
- 📤 **Exportar para Tableau**: Exporta os dados tratados para um arquivo `.csv`, pronto para importação no Tableau.

---

## 🧰 Tecnologias Utilizadas

- Python 3.x  
- tkinter (interface gráfica)  
- pandas (manipulação de dados)  
- openpyxl (leitura de arquivos Excel)

---

## 💡 Como Usar

Clone o repositório:

```bash
git clone https://github.com/FelipeAugLGoncalves/dataapp.git
cd dataapp

Instale as dependências:

pip install pandas openpyxl

Execute a aplicação:

python dataapp.py

📑 Requisitos da Planilha

    Para frequência relativa, a planilha deve conter a coluna dual_sim.

    Para correlação, as colunas ram e battery_power devem estar presentes e conter valores numéricos.

    Para estatísticas, a coluna battery_power deve estar presente.

    Para mínimo/máximo, as colunas px_height e px_width devem existir.

📤 Exportação para Tableau

A opção "Exportar para Tableau" salva os dados tratados em .csv, permitindo fácil importação na ferramenta de visualização Tableau para construção de dashboards.
🖼️ Exemplo da Interface

(Adicione aqui um print da interface se desejar)
📄 Licença

Este projeto está licenciado sob a MIT License.

Desenvolvido com ❤️ por Felipe Gonçalves, Nicolas Povoa e Thiago Garcia
