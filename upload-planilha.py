import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd

class DataApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Análise de Dados")
        self.master.geometry("1200x600")

        self.tree = ttk.Treeview(master)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Botões
        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Carregar Planilha", command=self.load_file).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Frequência Relativa", command=self.show_freq).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Coeficiente de Correlação", command=self.show_corr).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Tableau", command=self.export_to_tableau).grid(row=0, column=3, padx=5)

        self.df = None

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx *.xls")])
        if file_path:
            try:
                if file_path.endswith('.csv'):
                    self.df = pd.read_csv(file_path)
                else:
                    raw_df = pd.read_excel(file_path, header=None)

                    # Verifica se está tudo em uma única coluna separada por vírgulas
                    if raw_df.shape[1] == 1:
                        self.df = raw_df[0].str.split(",", expand=True)
                        self.df.columns = self.df.iloc[0]  # define cabeçalho
                        self.df = self.df[1:]  # remove linha de cabeçalho dos dados
                        self.df.reset_index(drop=True, inplace=True)
                    else:
                        self.df = pd.read_excel(file_path)

                self.display_data()

            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")

    def display_data(self):
        # Limpar TreeView
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(self.df.columns)
        self.tree["show"] = "headings"

        for col in self.df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        for _, row in self.df.iterrows():
            self.tree.insert("", tk.END, values=list(row))

    def show_freq(self):
        if self.df is not None:
            col = "dual_sim"
            if col in self.df.columns:
                freq_abs = self.df[col].value_counts()
                freq_rel = self.df[col].value_counts(normalize=True)

                result = "Frequência relativa de 'dual_sim':\n"
                for val in freq_abs.index:
                    result += f"{val}: {freq_abs[val]} ({freq_rel[val]*100:.2f}%)\n"

                messagebox.showinfo("Frequência Relativa", result)
            else:
                messagebox.showwarning("Coluna não encontrada", f"A coluna '{col}' não existe no arquivo.")
        else:
            messagebox.showwarning("Aviso", "Carregue um arquivo primeiro.")

    def show_corr(self):
        if self.df is not None:
            col1 = "ram"
            col2 = "battery_power"
            if col1 in self.df.columns and col2 in self.df.columns:
                try:
                    # Garante que os dados são numéricos
                    df_corr = self.df[[col1, col2]].apply(pd.to_numeric, errors='coerce').dropna()
                    corr = df_corr.corr().iloc[0, 1]
                    messagebox.showinfo("Correlação", f"Coeficiente de Correlação entre '{col1}' e '{col2}': {corr:.4f}")
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao calcular correlação: {e}")
            else:
                messagebox.showwarning("Coluna não encontrada", f"Verifique se as colunas '{col1}' e '{col2}' existem.")
        else:
            messagebox.showwarning("Aviso", "Carregue um arquivo primeiro.")

    def export_to_tableau(self):
        if self.df is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if file_path:
                try:
                    self.df.to_csv(file_path, index=False)
                    messagebox.showinfo("Exportação", f"Arquivo CSV gerado com sucesso em {file_path}. Agora você pode importar no Tableau.")
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao exportar arquivo: {e}")
        else:
            messagebox.showwarning("Aviso", "Carregue um arquivo primeiro.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataApp(root)
    root.mainloop()
