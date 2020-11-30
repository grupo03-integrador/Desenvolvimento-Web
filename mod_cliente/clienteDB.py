from BancoBD import Banco 

class Clientes(object):
    def __init__(self, id_cliente=0, nome="", cpf="", data_pagamento="", telefone="", senha="", compra_fiado=""):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.data_pagamento = data_pagamento
        self.telefone = telefone
        self.senha = senha
        self.compra_fiado = compra_fiado
    
    def selectALL(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "select id_cliente,nome,cpf,data_pagamento,telefone,senha,compra_fiado from tb_cliente"
            _sql_data = ()
            c.execute(_sql,_sql_data)
            result = c.fetchall()
            return result
        except Exception as e:
            return "Ocorreu um erro na busca do cliente"
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()


    def selectONE(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "select id_cliente,nome,cpf,data_pagamento,telefone,senha,compra_fiado from tb_cliente where id_cliente = %s" 
            _sql_data = (self.id_cliente,)
            c.execute(_sql,_sql_data)
            for linha in c:
                self.id_cliente = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.data_pagamento = linha[3]
                self.telefone = linha[4]
                self.senha = linha[5]
                self.compra_fiado = linha[6]
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do cliente"
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()


    def insert(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "INSERT INTO tb_cliente (nome, cpf, data_pagamento, telefone, senha, compra_fiado) VALUES (%s,%s,%s,%s,%s,%s)"
            _sql_data = (self.nome, self.cpf, self.data_pagamento,self.telefone,self.senha,self.compra_fiado,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()
            return "Cadastro realiado com sucesso!" 
        except Exception as e:
            raise Exception('Erro ao tentar cadastrar produto!', str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def update(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "update tb_cliente set nome=%s,cpf=%s,data_pagamento=%s,telefone=%s,senha=%s,compra_fiado=%s where id_cliente = %s"
            _sql_data = (self.nome, self.cpf, self.data_pagamento,self.telefone,self.senha,self.compra_fiado,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()
            return "Edição efetuada com sucesso!"
        except Exception as e:
            raise Exception("Erro ao editar produto!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def delete(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "delete from tb_cliente where id_cliente = %s"
            _sql_data = (self.id_cliente,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()
            return "Registro excluido com sucesso!"
        except Exception as e:
            raise Exception("Erro ao tentar excluir produto!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()