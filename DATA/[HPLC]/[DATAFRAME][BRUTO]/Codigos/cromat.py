import os


class Cromatografia:
    def __init__(self, diretorio):
        self.diretorio = diretorio

    def arquivos(self):
        os.chdir(self.diretorio)
        files = glob.glob(r'*.txt')
        os.chdir('..')
        os.chdir('..')
        return files

    def cromatografia(entrada):
        # list to store file lines
        lines = []
        # read file
        with open(entrada, 'r') as fp:
            # read an store all lines into list
            lines = fp.readlines()

        # Write file
        saida = 'saida.txt'
        with open(saida, 'w') as fp:
            # iterate each line
            for number, line in enumerate(lines):
                # delete line 5 and 8. or pass any Nth line you want to remove
                # note list index starts from 0
                if number not in [i for i in range(0, 102)]:
                    fp.write(line)

        with open(saida, 'r') as fp:
            # read an store all lines into list
            lines = fp.readlines()

        saida2 = f'[rid][{entrada[0:-4]}].txt'
        # Write file
        with open(saida2, 'w') as fp:
            # iterate each line
            for number, line in enumerate(lines):
                # delete line 5 and 8. or pass any Nth line you want to remove
                # note list index starts from 0
                if number not in [i for i in range(6603, 11774)]:
                    fp.write(line)

        with open(saida, 'r') as fp:
            # read an store all lines into list
            lines = fp.readlines()

        saida2 = f'[uV][{entrada[0:-4]}].txt'
        # Write file
        with open(saida2, 'w') as fp:
            # iterate each line
            for number, line in enumerate(lines):
                # delete line 5 and 8. or pass any Nth line you want to remove
                # note list index starts from 0
                if number not in [i for i in range(0, 6613)]:
                    fp.write(line)
        os.remove(saida)

    def executa():
        nomesArquivos = self.arquivos()
        for nomeArquivo in nomesArquivos:
            self.cromatografia(nomeArquivo)
