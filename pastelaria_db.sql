CREATE DATABASE pastelaria_db;

USE pastelaria_db;

CREATE TABLE tb_cliente
(
	id_cliente INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome	VARCHAR(100) NOT NULL,
    cpf 	VARCHAR(11) NOT NULL UNIQUE,
    data_pagamento DATETIME,
    telefone CHAR(11) NOT NULL,
    senha VARCHAR(200) NULL DEFAULT NULL,
    compra_fiado TINYINT(4)
);
 

CREATE TABLE tb_funcionario
(
	id_funcionario INT  NOT NULL PRIMARY KEY AUTO_INCREMENT,
    matricula  CHAR(10) NOT NULL,
    grupo TINYINT(4),
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    telefone CHAR(11) NOT NULL,
    senha VARCHAR(200) NOT NULL,
	compra_fiado TINYINT(4),
    data_pagamento DATE 
);



CREATE TABLE tb_produto
(
	id_produto INT  NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    nome	VARCHAR(100) NOT NULL ,
    descricao	VARCHAR(200) NOT NULL,
    valor_unitario	DECIMAL(11,2) NOT NULL,
    foto BLOB
);


CREATE TABLE tb_empresa
(
	id_empresa INT  NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    multa_atraso	DECIMAL(11,2),
    taxa_juro_diaria	DECIMAL(11,2)
);

CREATE TABLE tb_comanda
(
	id_comanda INT  NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    funcionario_id INT  NOT NULL, 
    cliente_id INT  NOT NULL,
    valor_cobrado DECIMAL(11,2) NULL,
    -- valor_total DECIMAL(11,2) NULL DEFAULT NULL,
    numero_comanda VARCHAR(100) NOT  NULL,
    data_hora DATETIME NOT NULL,
    data_assinatura_fiado DATE,
    status_pagamento TINYINT,
    status_comanda TINYINT,
    
    
    CONSTRAINT KF_tb_funcionario__tb_comanda
	FOREIGN KEY (funcionario_id)
    REFERENCES tb_funcionario(id_funcionario),
    
    CONSTRAINT KF_tb_cliente__tb_comanda
    FOREIGN KEY (cliente_id)
    REFERENCES tb_cliente(id_cliente)
    
);

CREATE TABLE tb_comanda_produto
(
	id_comanda_produto INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    funcionario_id INT NOT NULL,
    produto_id INT  NOT NULL,
    comanda_id INT  NOT NULL,
    quantidade TINYINT,
	valor_unitario DECIMAL(11,2),
    
	CONSTRAINT  FK_tb_comanda__tb_comanda_produto
	FOREIGN KEY (comanda_id)
	REFERENCES tb_comanda(id_comanda),
   
	CONSTRAINT FK_tb_produto__tb_comanda_produto
	FOREIGN KEY (produto_id)
	REFERENCES tb_produto(id_produto),
   
	CONSTRAINT FK_tb_funcionario__tb_comanda_Produto
	FOREIGN KEY (funcionario_id)
	REFERENCES tb_funcionario(id_funcionario)
    
);


CREATE TABLE tb_recebimento
(
	id_recebimento 	INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_funcionario INT(11) NOT NULL,
    total_comandas 	INT,
    tipo 			TINYINT,
    valor_acrescimo DECIMAL(11,2) NULL DEFAULT NULL,
    valor_desconto DECIMAL(11,2) NULL DEFAULT NULL,
    data_hora		DATETIME,
    valor_total DECIMAL(11,2) NULL DEFAULT NULL,
    
    CONSTRAINT fk_tb_recebimento_tb_funcionario1
	FOREIGN KEY (id_funcionario)
	REFERENCES tb_funcionario (id_funcionario)
);


CREATE TABLE tb_comanda_recebimento 
(
   id_comanda_recebimento INT  NOT NULL PRIMARY KEY AUTO_INCREMENT,
   recebimento_id INT  UNIQUE NOT NULL,
   comanda_id INT  UNIQUE NOT NULL,
   
   CONSTRAINT FK_tb_comanda__tb_comanda_recebimento
   FOREIGN KEY  (comanda_id)
   REFERENCES tb_comanda(id_comanda),
   
   CONSTRAINT FK_tb_recebimento__tb_comanda_recebimento
   FOREIGN KEY (recebimento_id)
   REFERENCES tb_recebimento(id_recebimento)
);

-- ------------------------------------------------------
INSERT INTO tb_funcionario
(matricula, grupo, nome, cpf, telefone, senha, compra_fiado, data_pagamento)
VALUES
(1234567890,0,'grupo03','12345678990',49991000000,'abcbolinhas',0,'2020-12-15');


-- ----------------------------------------------------------

INSERT INTO tb_cliente
(nome, cpf, data_pagamento, telefone, senha, compra_fiado)
VALUES
('Fulano','15975345680', '2020-12-15',49123456789,1234556,1);

-- -------------------------------------------------------------

INSERT INTO tb_produto
(nome, descricao, valor_unitario)
VALUES
('Pastel de Frango','Frango Caipira', 3.50);