import pandas as pd
import glob
local = 'Dados Separados\\rid'
diretorio = f'D:\\Google Drive Copia\\Doutorado_Renato\\data\[OURO]\[HPLC][Ouro][CH4][KOH + H2SO4 + H2O2]\\{local}'


class Uni_colunas:
    def __init__(self, diretorio):
        self.diretorio = diretorio

    def arquivos(self):
        os.chdir(self.diretorio)
        files = glob.glob(r'*.txt')
        return files

    def etapas(self, file2):
        df2 = pd.read_csv(file2, sep='\t')
        ext_col = df2['Intensity']
        #ext_col.rename(column={'Intensity': file2[0:-4]}, inplace=True)
        self.df = self.df.join(ext_col)
        self.df.rename(columns={'Intensity': file2[5:-4]}, inplace=True)

    def executa(self):
        os.chdir(self.diretorio)
        nomesArquivos = self.arquivos()
        file1 = nomesArquivos[0]
        self.df = pd.read_csv(file1, sep='\t')
        self.df.rename(columns={'R.Time (min)': 'time (min)',
                                'Intensity': file1[5:-4]}, inplace=True)
        nomesArquivos = nomesArquivos[1:-1]

        for nmA in nomesArquivos:
            print(nmA)
            self.etapas(nmA)
        return self.df


uc = Uni_colunas(diretorio)
df = uc.executa()
df.head()
