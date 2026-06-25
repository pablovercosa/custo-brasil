![Image](assets/image_000000_03ca96dd47c3c944f1e1f5e8116e5ec97276920c675b8587f83e37ae1cc6fe3d.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_7eea3ade68ab7b2ee4b661cbcba30b7c5727c48c66dfc2f0e2a0dc16fdffdca6.png)

## Nota Técnica 2012/005

Operação Interestadual com Bens e Mercadorias Importados do Exterior

![Image](assets/image_000002_a45770cb4195731552b1c4fa4268aac911afb2f871a503ad8503670bd960e716.png)

Versão 1.00c Novembro 2012

![Image](assets/image_000003_e63d153f4044bbd2e0101d9137a654d625b5e415bf65076f5fd9b88408e44d37.png)

## 01. Resumo

A  Resolução  13/2012  do  Senado  Federal  teve  sua  impl ementação  regulamentada  pelo  Ajuste SINIEF 19/2012 e pelo Ajuste SINIEF 20/2012. editados pelo CONFAZ - Conselho Nacional de Política Fazendária.

Esta NT trata da repercussão dessas legislações sob re a NF-e, basicamente pela:

- Criação de regra de validação específica conferindo a aplicação da alíquota de 4% definida na legislação para as operações interestaduais com  mercadorias e bens importados.
- Alteração do campo de Origem da Mercadoria, que pa ssa a assumir novos valores; e

Prazo para entrada em vigência das alterações, em f unção do início da vigência da Resolução 13:

- Ambiente de Homologação (ambiente de teste das empresas): 10/12/12;
- Ambiente de Produção : 01/01/13.

## 01.1 Alterações da versão anterior da NT (versão v1 .00a)

Alterada regra de validação GN16, incluindo exceção  para operações com veículos novos, com tpOp=3.

## 01.2 Alterações da versão anterior da NT (versão 1. 00b)

Alterada a regra de validação GN16, incluindo novas  exceções no controle da alíquota superior a 4% na operação interestadual:

- -não se aplica a regra para os CFOP 6.107 e 6.108 ( Venda para Não Contribuinte);
- -não se aplica a regra para a NF-e Complementar, qu ando a NF referenciada for anterior a 01/01/13.

![Image](assets/image_000004_a2662a9671929ed2e0d7e0e903391e0fa2c0ecf19da62ed1ef605ce8f5bc2b62.png)

## 02. Alteração de Schema XML da NF-e

## 02.1 Campo de Origem da Mercadoria

Esta alteração não altera o leiaute atual da NF-e,  mas permite a informação de novos valores do campo.

|   # | ID   | Campo   | Descrição            | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Dec. Observação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----|------|---------|----------------------|-------|-------|--------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 166 | N11  | orig    | Origem da mercadoria | E     | N02   | N      | 1-1     |      1 | Origem da mercadoria: 0 - Nacional, exceto as indicadas nos códigos 3 a 5; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante em lista da CAMEX. |

## IMPORTANTE:

O detalhamento acima descreve a mudança dos valores do campo 'orig' para o grupo de tributação 'ICMS00 '.

A mesma mudança ocorre para os demais grupos de tributação do ICMS.

![Image](assets/image_000005_9a323ab5c02e7e953a50377cbb6237f1167cdbc96999f38de70ce565b069c26d.png)

## 03. Regras de Validação da NF-e (item 4.1.9.4 do Ma nual)

## 03.1 Operação interestadual com bens e mercadorias  importados

Incluída nova regra de validação, conforme segue:

| #    | Campo   | Regra de validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Aplic.   |   Msg | Efeito Descrição Erro                                                                                                       |
|------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|-----------------------------------------------------------------------------------------------------------------------------|
| GN16 | N16     | CFOP de operação de saída para outra UF (inicia por 6) e - IE do destinatário difere de 'ISENTO' ou nulo - Origem da mercadoria = 1, 2 ou 3 - CST de ICMS = 00, 10, 20, 70 ou 90 - Data de Emissão igual ou superior a 01/01/2013 - Valor alíquota do ICMS maior do que '4.00' (4 por cento) Exceção 1 : A regra acima não se aplica para as NF- e com Data de emissão inferior a 01/04/2013 , nas operações de Retorno / Devolução, com os CFOP: 6201, 6202, 6208, 6209, 6210, 6410, 6411, 6412, 6413, 6503, 6553, 6555, 6556, 6660, 6661, 6662, 6664, 6665, 6902, 6903, 6906, 6907, 6909, 6913, 6916, 6918, 6919, 6921, 6925 Exceção 2: A regra de validação acima não se aplica para operação com gás natural importado (cProdANP= 220101003, 220101004, 220101002, 220101001, 220101005 ou 220101006).' Exceção 3: A regra de validação acima não se aplica n a venda de veículos novos (grupo 'veicProd'), para a Venda direta para grandes consumidores (tpOp=3), ou para Faturamento direto para consumidor final (tpOp=2). Exceção 4: Mesmo que informada a IE do destinatário, a regra de validação acima não se aplica para as operações com os CFOP 6107, 6108 (Não Contribuinte) . Exceção 5: A regra de validação acima não se aplica para a NF Complementar (finNFe=2) quando: - se referenciada uma NF-e, a NF-e referenciada tem a Data de Emissão anterior a 01/01/13; - se referenciada uma NF modelo 1, a Data de Emissão é anterior a 1301 (tag refNF/AAMM). | Facult.  |   663 | Rej. Rejeição: Alíquota do ICMS com valor superior a 4 por cento na operação de saída interestadual com produtos importados |