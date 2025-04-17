# 📊 DataApp - Análise de Dados com Interface Gráfica

Este projeto é uma aplicação desenvolvida em Python utilizando `tkinter` para análise de dados a partir de planilhas CSV ou Excel. A ferramenta permite visualizar dados em formato de tabela, calcular frequência relativa e coeficiente de correlação, além de exportar os dados para o Tableau.

## 🚀 Funcionalidades

- 📂 **Carregar Planilha**: Importa arquivos `.csv`, `.xlsx` ou `.xls`.
- 📈 **Frequência Relativa**: Calcula a frequência relativa da coluna `dual_sim`.
- 🔍 **Coeficiente de Correlação**: Calcula a correlação entre as colunas `ram` e `battery_power`.
- 📤 **Exportar para Tableau**: Exporta os dados tratados para um arquivo `.csv`, pronto para ser importado no Tableau.

## 🧰 Tecnologias Utilizadas

- Python 3.x
- tkinter (interface gráfica)
- pandas (manipulação de dados)
- openpyxl (para leitura de arquivos Excel)

## 💡 Como Usar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/FelipeAugLGoncalves/dataapp.git
   cd dataapp
2. Instale as dependências:

   pip install pandas openpyxl

4. Execute a aplicação:

    python dataapp.py

🧪 Requisitos da Planilha
Para cálculo da frequência relativa, a planilha deve conter a coluna dual_sim.

Para o coeficiente de correlação, as colunas ram e battery_power devem estar presentes e conter apenas valores numéricos.

📤 Exportação para Tableau
A opção "Tableau" salva os dados tratados em .csv, permitindo fácil importação na ferramenta de visualização Tableau para construção de dashboards.

🖼️ Exemplo da Interface
<!-- Se desejar, adicione um arquivo chamado `screenshot.png` no repositório -->

📄 Licença
Este projeto está licenciado sob a MIT License.

Desenvolvido com ❤️ por Felipe Gonçalves
