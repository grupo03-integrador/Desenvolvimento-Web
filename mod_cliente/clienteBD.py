from BancoBD import Banco 

class Clientes(object):
    def __init__(self, id_cliente=0, nome="", endereco="", numero=0, observacao="", cep="", bairro="", cidade="", estado="SC", telefone="", email="", login="", senha="", grupo="SOLIC"):
        self.id_cliente = id_cliente
        self.nome = nome
        self.endereco = endereco
        self.numero = numero
        self.cep = cep
        self.observacao = observacao
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.telefone = telefone
        self.email = email
        self.login = login
        self.senha = senha
        self.grupo = grupo
    
    def selectALL(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("select id_cliente,nome,endereco,numero,observacao,cep,bairro,cidade,estado,telefone,email,login,senha,grupo from tb_clientes")

            result = c.fetchall()

            c.close()

            return result
        except:
            return "Ocorreu um erro na busca do cliente"

    def selectONE(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select id_cliente,nome,endereco,numero,observacao,cep,bairro,cidade,estado,telefone,email,login,senha,grupo from tb_clientes where id_cliente = %s", (self.id_cliente))
            for linha in c:
                self.id_cliente = linha[0]
                self.nome = linha[1]
                self.endereco = linha[2]
                self.numero = linha[3]
                self.observacao = linha[4]
                self.cep = linha[5]
                self.bairro = linha[6]
                self.cidade = linha[7]
                self.estado = linha[8]
                self.telefone = linha[9]
                self.email = linha[10]
                self.login = linha[11]
                self.senha = linha[12]
                self.grupo = linha[13]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do cliente"


    def insert(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(" insert into tb_clientes(nome, endereco, numero, observacao, cep, bairro, cidade, estado, telefone, email, login, senha, grupo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.nome, self.endereco, self.numero, self.observacao, self.cep, self.bairro, self.cidade, self.estado, self.telefone, self.email, self.login, self.senha, self.grupo))
            banco.conexao.commit()
            c.close()
            return "Cliente cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do cliente"

    def update(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update tb_clientes set nome=%s , endereco=%s , numero=%s, observacao=%s, cep=%s, bairro=%s, cidade=%s, estado=%s, telefone=%s, email=%s, login=%s, senha=%s, grupo=%s where id_cliente = %s",(self.nome, self.endereco, self.numero, self.observacao, self.cep, self.bairro, self.cidade, self.estado, self.telefone, self.email, self.login, self.senha, self.grupo, self.id_cliente)) 
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def delete(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from tb_clientes where id_cliente = %s", (self.id_cliente))
            banco.conexao.commit()
            c.close()
            return "Cliente excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do Cliente"