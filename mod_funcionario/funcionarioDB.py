from BancoBD import Banco 

class Funcionario(object):
    def __init__(self, id_funcionario=0, matricula=0, grupo=0, nome="", cpf="", telefone="", senha="", compra_fiado="", data_pagamento=""):
        self.id_funcionario = id_funcionario
        self.matricula = matricula
        self.grupo = grupo
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone    
        self.senha = senha
        self.compra_fiado = compra_fiado
        self.data_pagamento = data_pagamento
     
    
    def selectALL(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "select id_funcionario, matricula, grupo, nome, cpf, telefone, senha, compra_fiado, data_pagamento from tb_funcionario"
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
            _sql = "select id_funcionario, matricula, grupo, nome, cpf, telefone, senha, compra_fiado, data_pagamento from tb_funcionario where id_fincionario = %s" 
            _sql_data = (self.id_funcionario,)
            c.execute(_sql,_sql_data)
            for linha in c:
                self.id_funcionario = linha[0]
                self.matricula = linha[1]
                self.grupo = linha[2]
                self.nome = linha[3]
                self.cpf = linha[4]
                self.telefone = linha[5]
                self.senha = linha[6]
                self.compra_fiado = linha[7]
                self.data_pagamento = linha[8]
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
            print(self.imagem)
            c = banco.conexao.cursor()
            _sql = "insert into tb_funcionario (matricula, grupo, nome, cpf, telefone, senha, compra_fiado, data_pagamento) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            _sql_data = (self.matricula, self.grupo, self.nome, self.cpf, self.telefone, self.senha, self.compra_fiado, self.data_pagamento,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()
            return "Funcionario inserido com sucesso!" 
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
            _sql = "update tb_funcionario set matricula=%s,grupo=%s,nome=%s,cpf=%s,telefone=%s,senha=%s,compra_fiado=%s,data_pagamento=%s where id_funcionario = %s"
            _sql_data = (self.matricula, self.grupo, self.nome, self.cpf, self.telefone, self.senha, self.compra_fiado, self.data_pagamento,self.id_funcionario,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()
            return "Edição feita com sucesso!"
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
            _sql = "delete from tb_funcionario where id_funcionario = %s"
            _sql_data = (self.id_funcionario,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()
            return "Exclusão feita com sucesso!"
        except Exception as e:
            raise Exception("Erro ao tentar excluir produto!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()