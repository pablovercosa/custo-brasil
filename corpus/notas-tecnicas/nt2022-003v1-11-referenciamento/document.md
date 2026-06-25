![Image](assets/image_000000_8afe677f9dd113448e8dd3ae683f6aa665a8f4dcd640aad1ef968bf963da8286.png)

![Image](assets/image_000001_5dd5d5e16748c7abcded3a0035d3a12ebd8073cdc66cfc62ca495386dd8ab477.png)

## Projeto Nota Fiscal Eletrônica

Nota Técnica 2022.003

Novos Campos e Regras de Validação NT 2022.003 v1.11 - Regras de Validação e Novos Campos

![Image](assets/image_000002_f7a38cbe2013e980079d1ef89f330cfc1e8c2b16f31beed0e573c9f71816b144.png)

![Image](assets/image_000003_b1eeba97115b031a27671ec58f09a7d4eb840d55032020fa8409bd25e4cdc9a1.png)

## Sumário

| Controle de Versões                                                                                                                                                                                                                                    | ............................................................................................................................3   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Histórico de Alterações / Cronograma..................................................................................................3                                                                                                                |                                                                                                                                 |
| 1. Resumo ...........................................................................................................................................4                                                                                                 |                                                                                                                                 |
| 2. Visão Geral......................................................................................................................................5                                                                                                  |                                                                                                                                 |
| 2.1. Alterações de Campos ..............................................................................................................5                                                                                                              |                                                                                                                                 |
| 2.1.1. Inclusão do Referenciamento de NF-e por Chave com código numérico zerado (Campo refNFeSig). ................................................................................................................................................. 5 |                                                                                                                                 |
| 2.1.2. Alteração do número máximo de ocorrências do grupo de Documentos Fiscais Referenciados (tag: NFref) ......................................................................................................................................      | 5                                                                                                                               |
| 2.2. Alterações de Regras de Validação...........................................................................................5                                                                                                                     |                                                                                                                                 |
| 2.2.1. Criação das Regras de Validação BA02a-10, BA02a-20, BA02a-30, BA02a-40, BA02a-50, BA02a- 60, BA02a-70, BA02a-80, BA02a-90, BA02a-100..................................................................                                          | 5                                                                                                                               |
| 2.2.2. Alteração das Regras de Validação: C02a-04, C02a-08, C02a-14 ..................................................                                                                                                                                 | 5                                                                                                                               |
| 2.2.3. Criação da Regra de Validação I08-186 ...........................................................................................                                                                                                               | 5                                                                                                                               |
| 2.2.4. Alteração das Regras de Validação: I08-194 e I08-198....................................................................                                                                                                                        | 5                                                                                                                               |
| 2.2.5. Alteração da Regra de Validação: N17c-30......................................................................................                                                                                                                  | 5                                                                                                                               |
| 2.2.6. Alteração da Regra de Validação: ZD02-10......................................................................................                                                                                                                  | 5                                                                                                                               |
| 2.2.7. Criação da Regra de Validação 3BA02a-10 .....................................................................................                                                                                                                   | 6                                                                                                                               |
| 2.2.8. Alteração da Regra de Validação: 7C21-10......................................................................................                                                                                                                  | 6                                                                                                                               |
| 2.3. Alterações introduzidas na versão 1.10.....................................................................................6                                                                                                                      |                                                                                                                                 |
| 2.3.1. Criação das Regras de Validação BA02-60 e BA02a-110................................................................                                                                                                                             | 6                                                                                                                               |
| 2.3.2. Criação das Regras de Validação BA02-70 e BA02-80....................................................................                                                                                                                           | 6                                                                                                                               |
| 2.3.3. Criação da Regra de Validação BA02a-74 .......................................................................................                                                                                                                  | 6                                                                                                                               |
| 2.3.4. Alteração da documentação da Regra BA02a-90.............................................................................                                                                                                                        | 6                                                                                                                               |
| 2.3.5. Criação da Regra de Validação BA02a-120 .....................................................................................                                                                                                                   | 6                                                                                                                               |
| 2.3.6. Exclusão da Regra I08-186...............................................................................................................                                                                                                        | 6                                                                                                                               |
| 2.3.7. Alteração da descrição da Regra de Validação N17c-30 .................................................................                                                                                                                          | 6                                                                                                                               |
| 2.4. Alterações introduzidas na versão 1.11.....................................................................................6                                                                                                                      |                                                                                                                                 |
| 3. Leiaute da Nota Fiscal Eletrônica.....................................................................................................7                                                                                                             |                                                                                                                                 |
| 3.1. Grupo BA. Documento Fiscal Referenciado ..............................................................................7                                                                                                                           |                                                                                                                                 |
| 4. Regras de Validação........................................................................................................................9                                                                                                        |                                                                                                                                 |
| 4.1. BA. Documento Fiscal Referenciado.........................................................................................9                                                                                                                       |                                                                                                                                 |
| 4.2. C. Identificação do Emitente....................................................................................................11                                                                                                                |                                                                                                                                 |
| 4.3. I. Produtos e Serviços                                                                                                                                                                                                                            | .............................................................................................................11                 |
| 4.4. N. Item / Tributo: ICMS............................................................................................................12                                                                                                             |                                                                                                                                 |
| 4.5. ZD. Informações do Responsável Técnico ..............................................................................12                                                                                                                           |                                                                                                                                 |
| 4.6. 3A. Banco de Dados: NF-e Referenciada................................................................................13                                                                                                                           |                                                                                                                                 |
| 4.7. 7. Banco de Dados: Cadastro da SEFAZ ................................................................................13                                                                                                                           |                                                                                                                                 |
| 5. Novos códigos de Rejeição............................................................................................................15                                                                                                             |                                                                                                                                 |

![Image](assets/image_000004_02fca134f695c2e32ef51f532b5e0eea994c0b11545d0be7d9613bdfc06c0e6e.png)

## Controle de Versões

|   Versão | Publicação    | Descrição                                                                                                                                                                                                                                        |
|----------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1.00 | Novembro 2022 | Publicação da NT.                                                                                                                                                                                                                                |
|     1.10 | Dezembro 2022 | Alteração da descrição da Regra N17c-30, para constar que ela somente se aplica ao estado do Ceará Exclusão Rejeição da Regra I08-160 Correção da documentação da Regra BA02a-90 Novas Regras para garantir a consistência de NF-e referenciadas |
|     1.11 | Janeiro 2023  | Melhoria da redação da explicação acerca da utilização do campo refNFeSig Melhoria da documentação das Regras BA02-60 e BA02a-110                                                                                                                |

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações                                                                                                                                                                                    | Implantação Teste   | Implantação Produção   |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|------------------------|
|     1.00 | Novas regras de validação e novos campos                                                                                                                                                                     | 07/02/2023          | 03/04/2023             |
|     1.10 | Alteração da descrição da Regra N17c-30 Exclusão da Regra I08-186 Correção na documentação da Regra BA02a-90 Criação das novas Regras de Validação BA02-60, BA02-70, BA02-80, BA02a-74, BA02a-110, BA02a-120 | 07/02/2023          | 03/04/2023             |
|     1.11 | Alteração meramente documental                                                                                                                                                                               | 07/02/2023          | 03/04/2023             |

![Image](assets/image_000005_d1bc49a2fb934983eab18c20f3d4a2cd4934290ad0fb3f6ea7e58ba3999aa974.png)

## 1. Resumo

Essa Nota Técnica divulga novos campos e Regras de Validação da NF-e versão 4.0.

O prazo previsto para a implementação das mudanças é:

- o Ambiente de Homologação (ambiente de teste das empresas): 07/02/2023
- o Ambiente de Produção : 03/04/2023

Para a versão 1.10, como a publicação ocorreu com antecedência, os prazos para implementação se mantêm:

- o Ambiente de Homologação (ambiente de teste das empresas): 07/02/2023
- o Ambiente de Produção : 03/04/2023

A versão 1.11 traz alterações meramente documentais e na explicação acerca dos novos campos. Portanto, os prazos para implementação se mantêm:

- o Ambiente de Homologação (ambiente de teste das empresas): 07/02/2023
- o Ambiente de Produção : 03/04/2023

![Image](assets/image_000006_9afb0d16c0a7de558366bb393b0c00e506d504c184447f819a0b21c04a1b18a4.png)

## 2. Visão Geral

## 2.1. Alterações de Campos

## 2.1.1. Inclusão do Referenciamento de NF-e por Chave com código numérico zerado (Campo refNFeSig).

Criação de campo específico no grupo de Documento Fiscal Referenciado (NFref) para permitir ao contribuinte referenciar Nota Fiscal Eletrônica, modelo 55, informando a Chave da NF-e com o código numérico zerado.   Essa alteração visa garantir a manutenção do Sigilo Fiscal da NF-e referenciada. A referência pela chave de acesso completa (campo: refNFe) ainda continua obrigatória nos casos de NF-e de devolução, complementar e quando a legislação exigir.

## 2.1.2. Alteração do número máximo de ocorrências do grupo de Documentos Fiscais Referenciados (tag: NFref)

O grupo de Documentos Fiscais Referenciados (tag: NFref) passou de um máximo de 500 para 999 ocorrências,  para  atender  situações  em  que  era  necessário referenciar  mais  que  500  documentos numa mesma NF-e.

## 2.2. Alterações de Regras de Validação

## 2.2.1. Criação das Regras de Validação BA02a-10, BA02a-20, BA02a-30, BA02a-40, BA02a-50, BA02a-60, BA02a-70, BA02a-80, BA02a-90, BA02a-100

Essas regras visam garantir a consistência da Chave Referenciada com código numérico zerado (tag: refNFeSig) além de evitar que esse referenciamento aconteça em uma NF-e com finalidade diferente de normal.

## 2.2.2. Alteração das Regras de Validação: C02a-04, C02a-08, C02a-14

Atualmente existe um controle das SEFAZ no credenciamento individual para emissão da Nota Fiscal pelos Contribuintes Pessoa Física (CPF). Eliminadas as Regras de Validação que controlam a opção da UF em aceitar ou não a emissão de Nota Fiscal para os Contribuintes emitentes Pessoa Física.

## 2.2.3. Criação da Regra de Validação I08-186

O objetivo desta regra é impedir o referenciamento de ECF em uma NF-e com CFOP 5929 ou 6929, uma vez que em algumas unidades federadas o ECF já foi completamente substituído por NFC-e e não existe mais a possibilidade de seu referenciamento para estas operações.

## 2.2.4. Alteração das Regras de Validação: I08-194 e I08-198

Algumas SEFAZ concedem IE para não Contribuinte do ICMS, mas limitam a emissão de NF-e de venda unicamente pelo Emissor de Nota Fiscal Avulsa disponibilizado pela própria SEFAZ.

## 2.2.5. Alteração da Regra de Validação: N17c-30

Conforme a legislação estadual, algumas SEFAZ controlam a informação dos valores vinculados ao Fundo de Combate à Pobreza (FCP) no processo de apuração do imposto, impedindo essa informação individualizada em cada NF-e.

## 2.2.6. Alteração da Regra de Validação: ZD02-10

Melhorada a documentação da RV, efetuando a validação unicamente se a informação do CNPJ do Responsável Técnico for informada.

![Image](assets/image_000007_9afb0d16c0a7de558366bb393b0c00e506d504c184447f819a0b21c04a1b18a4.png)

## 2.2.7. Criação da Regra de Validação 3BA02a-10

Regra de validação para verificar a existência da Chave Referenciada com código numérico zerado na base de dados de NF-e da UF emitente do documento.

## 2.2.8. Alteração da Regra de Validação: 7C21-10

A RV 7C21-10 controla a informação na Nota Fiscal do CRT ou CSOSN, conforme o cadastro do Contribuinte na SEFAZ. Alterada esta Regra de Validação para ser opcional por UF.

## 2.3. Alterações introduzidas na versão 1.10

## 2.3.1. Criação das Regras de Validação BA02-60 e BA02a-110

Estas regras visam garantir que quando houver uma Chave referenciada (tag: refNFe) ou uma Chave Referenciada com código numérico zerado (tag: refNFeSig), o tipo de emissão da chave referenciada seja válido.

## 2.3.2. Criação das Regras de Validação BA02-70 e BA02-80

Estas regras visam evitar que sejam referenciados documentos eletrônicos diferentes do modelo 55 em devoluções internas de mercadoria e também em devoluções envolvendo consumidor final. Regras com implementação futura.

## 2.3.3. Criação da Regra de Validação BA02a-74

Esta regra visa garantir que, quando houver uma Chave Referenciada com código numérico zerado (tag: refNFeSig), o código numérico seja efetivamente zerado.

## 2.3.4. Alteração da documentação da Regra BA02a-90

A coluna de modelo desta regra havia sido deixada em branco equivocadamente, alterada para constar sua aplicabilidade somente para o modelo 55.

## 2.3.5. Criação da Regra de Validação BA02a-120

Esta regra visa evitar que seja utilizado o campo de Nota Referenciada com código numérico zerado (tag: refNFeSig) em UF que não permite tal referência.

## 2.3.6. Exclusão da Regra I08-186

Esta regra foi removida pois a UF que assim desejar pode bloquear Cupom Fiscal referenciado através da  ativação  da  Regra  BA20-30  (NT  2019.001).  Como  a  Regra  I08-196  sequer  chegou  a  ser implementada, o código de Rejeição inicialmente alocado a ela foi reaproveitado nesta mesma NT.

## 2.3.7. Alteração da descrição da Regra de Validação N17c-30

Alterada a descrição da RV N17c-30 para que fique claro que ela somente se aplica, neste momento, para o Ceará. O Estado do Ceará realiza o controle do FCP de forma diferente das demais UF, o que acarreta na necessidade de implementação desta regra.

## 2.4. Alterações introduzidas na versão 1.11

Essa versão trouxe somente uma adequação ao texto do item 2.1.1 e alterações na documentação das Regras  BA02-60 e BA02a-110 que impactam somente as SEFAZ autorizadoras.

![Image](assets/image_000008_9afb0d16c0a7de558366bb393b0c00e506d504c184447f819a0b21c04a1b18a4.png)

## 3. Leiaute da Nota Fiscal Eletrônica

## 3.1. Grupo BA. Documento Fiscal Referenciado

| #      | ID    | Campo     | Descrição                                                                           | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                                                        |
|--------|-------|-----------|-------------------------------------------------------------------------------------|-------|-------|--------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 29x.1  | BA01  | NFref     | Informação de Documentos Fiscais referenciados                                      | G     | B01   |        | 0-999   |        | Grupo com informações de Documentos Fiscais referenciados. Informação utilizada nas hipóteses previstas na legislação. (Ex.: Devolução de mercadorias, Substituição de NF cancelada, Complementação de NF, etc.). |
| 29x.2  | BA02  | refNFe    | Chave de acesso da NF-e referenciada                                                | CE    | BA01  | N      | 1-1     | 44     | Referencia uma NF-e (modelo 55) emitida anteriormente, vinculada a NF-e atual, ou uma NFC-e (modelo 65)                                                                                                           |
| 29x.2a | BA02a | refNFeSig | Chave da NF-e com o código numérico zerado.                                         | CE    | BA01  | N      | 1-1     | 44     | Referencia uma NF-e (modelo 55) emitida anteriormente pela sua Chave de Acesso com código numérico zerado, permitindo manter o sigilo da NF-e referenciada.                                                       |
| 29x.3  | BA03  | refNF     | Informação da NF modelo 1/1A ou NF modelo 2 referenciada (alterado pela NT2016.002) | CG    | BA01  |        | 1-1     |        |                                                                                                                                                                                                                   |
| 29x.4  | BA04  | cUF       | Código da UF do emitente                                                            | E     | BA03  | N      | 1-1     | 2      | Utilizar a Tabela do IBGE (Seção 8.1 do MOC Visão Geral- Tabela de UF, Município e País)                                                                                                                          |
| 29x.5  | BA05  | AAMM      | Ano e Mês de emissão da NF-e                                                        | E     | BA03  | N      | 1-1     | 4      | AAMMda emissão da NF                                                                                                                                                                                              |
| 29x.6  | BA06  | CNPJ      | CNPJ do emitente                                                                    | E     | BA03  | N      | 1-1     | 14     | Informar o CNPJ do emitente da NF                                                                                                                                                                                 |
| 29x.7  | BA07  | mod       | Modelo do Documento Fiscal                                                          | E     | BA03  | N      | 1-1     | 2      | 01=modelo 01 02=modelo 02 (incluído na NT2016.002)                                                                                                                                                                |
| 29x.8  | BA08  | serie     | Série do Documento Fiscal                                                           | E     | BA03  | N      | 1-1     | 1 - 3  | Informar zero se não utilizada Série do documento fiscal.                                                                                                                                                         |
| 29x.9  | BA09  | nNF       | Número do Documento Fiscal                                                          | E     | BA03  | N      | 1-1     | 1 - 9  | Faixa: 1 - 999999999                                                                                                                                                                                              |
| 29x.10 | BA10  | refNFP    | Informações da NF de produtor rural referenciada                                    | CG    | BA01  |        | 1-1     |        |                                                                                                                                                                                                                   |
| 29x.11 | BA11  | cUF       | Código da UF do emitente                                                            | E     | BA10  | N      | 1-1     | 2      | Utilizar a Tabela do IBGE (Seção 8.1 do MOC - Visão Geral, Tabela de UF, Município e País) (v2.0)                                                                                                                 |
| 29x.12 | BA12  | AAMM      | Ano e Mês de emissão da NF-e                                                        | E     | BA10  | N      | 1-1     | 4      | AAMMda emissão da NF de produtor (v2.0)                                                                                                                                                                           |
| 29x.13 | BA13  | CNPJ      | CNPJ do emitente                                                                    | CE    | BA10  | N      | 1-1     | 14     | Informar o CNPJ do emitente da NF de produtor (v2.0)                                                                                                                                                              |
| 29x.14 | BA14  | CPF       | CPF do emitente                                                                     | CE    | BA10  | N      | 1-1     | 11     | Informar o CPF do emitente da NF de produtor (v2.0)                                                                                                                                                               |
| 29x.15 | BA15  | IE        | IE do emitente                                                                      | E     | BA10  | N      | 1-1     | 2 - 14 | Informar a IE do emitente da NF de Produtor ou o literal 'ISENTO' (v2.0)                                                                                                                                          |

![Image](assets/image_000009_dad84df793db864d817ff7e296f2d6b88cf43afb3ff9a84d16c7c8c2c310e8ee.png)

![Image](assets/image_000010_876e38e047fcd6dc05d48d543dc7e6487039eac7a0c80caef71b1c5afba735ab.png)

| #      | ID   | Campo   | Descrição                                     | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                       |
|--------|------|---------|-----------------------------------------------|-------|-------|--------|---------|--------|----------------------------------------------------------------------------------------------------------------------------------|
| 29x.16 | BA16 | mod     | Modelo do Documento Fiscal                    | E     | BA10  | N      | 1-1     | 2      | 04=NF de Produtor; 01=NF (v2.0)                                                                                                  |
| 29x.17 | BA17 | serie   | Série do Documento Fiscal                     | E     | BA10  | N      | 1-1     | 1 - 3  | Informar a série do documento fiscal (informar zero se inexistente) (v2.0).                                                      |
| 29x.18 | BA18 | nNF     | Número do Documento Fiscal                    | E     | BA10  | N      | 1-1     | 1 - 9  | Faixa: 1 - 999999999                                                                                                             |
| 29x.19 | BA19 | refCTe  | Chave de acesso do CT-e referenciada          | CE    | BA01  | N      | 1-1     | 44     | Utilizar esta TAG para referenciar um CT-e emitido anteriormente, vinculada a NF-e atual - (v2.0).                               |
| 29x.20 | BA20 | refECF  | Informações do Cupom Fiscal referenciado      | CG    | BA01  |        | 1-1     |        | Grupo do Cupom Fiscal vinculado à NF-e (v2.0).                                                                                   |
| 29x.21 | BA21 | mod     | Modelo do Documento Fiscal                    | E     | BA20  | C      | 1-1     | 2      | "2B"=Cupom Fiscal emitido por máquina registradora (não ECF); "2C"=Cupom Fiscal PDV; "2D"=Cupom Fiscal (emitido por ECF) (v2.0). |
| 29x.22 | BA22 | nECF    | Número de ordem sequencial do ECF             | E     | BA20  | N      | 1-1     | 3      | Informar o número de ordem sequencial do ECF que emitiu o Cupom Fiscal vinculado à NF-e (v2.0).                                  |
| 29x.23 | BA23 | nCOO    | Número do Contador de Ordem de Operação - COO | E     | BA20  | N      | 1-1     | 6      | Informar o Número do Contador de Ordem de Operação - COO vinculado à NF-e (v2.0).                                                |

## 4. Regras de Validação

## 4.1. BA. Documento Fiscal Referenciado

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                 | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                                   |
|-------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------------------------------------------------------------------------------------------|
| BA02-60     |       55 | Se informada uma NF-e referenciada (tag:refNFe): - Se modelo da Chave de Acesso = 55 ou 65; - Se Mês-Ano da Chave de Acesso superior a Abril/11; - Chave de Acesso referenciada com Tipo de Emissão Inválido (diferente de 1, 2, 3, 4, 5, 6, 7, 9) | Facul.   |   953 | Rej.     | Rejeição: Chave de Acesso referenciada com tipo de emissão inválido [nOcor:nnn]                                                  |
| BA02-70     |       55 | Se NFe de devolução (finNFe=4) e modelo de NFe referenciada (tag: refNFe) diferente de 55: - Informada uma NF-e referenciada com código da UF diferente da UF do emitente.                                                                         | Facul.   |   954 | Rej      | Rejeição: Chave de Acesso referenciada não permitida para esta operação[nOcor:nnn]                                               |
| BA02-80     |       55 | Se NFe de devolução (finNFe=4) e destinatário consumidor final (indIEDest=9): - Informado código da UF da NF-e referenciada diferente da UF do emitente Observação: Implementação futura.                                                          | Facul.   |   954 | Rej.     | Rejeição: Chave de Acesso referenciada não permitida para esta operação[nOcor:nnn]                                               |
| BA02a-10    |       55 | Se NF-e diferente de normal (fiNFe <> 1) e informada uma NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig):                                                                                                        | Facul.   |   951 | Rej.     | Rejeição: Chave de Acesso referenciada com código numérico zerado não permitida para finalidade diferente de normal. [nOcor:nnn] |
| BA02a-20    |       55 | Se informada uma NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig): -Chave de Acesso referenciada com UF inválida                                                                                                  | Facul.   |   522 | Rej.     | Rejeição: Chave de Acesso referenciada com UF inválida[nOcor:nnn]                                                                |
| BA02a-30    |       55 | Se informada uma NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig): Chave de Acesso referenciada com Ano Emissão < 06 ou > que o Ano corrente.                                                                     | Facul.   |   524 | Rej.     | Rejeição: Chave de Acesso referenciada com Ano-Mês inválido[nOcor:nnn]                                                           |
| BA02a-40    |       55 | Se informada uma NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig): Chave de Acesso referenciada com Mês Emissão < 01 ou > 12                                                                                      | Facul.   |   524 | Rej.     | Rejeição: Chave de Acesso referenciada com Ano-Mês inválido[nOcor:nnn]                                                           |

![Image](assets/image_000011_5740b01e9b7f5d7d975a23f4e12b34fed4d2a0d4c4f2f4249027d0373eaf79be.png)

![Image](assets/image_000012_5740b01e9b7f5d7d975a23f4e12b34fed4d2a0d4c4f2f4249027d0373eaf79be.png)

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                          | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                    |
|-------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------------------------------------------------|
| BA02a-50    |       55 | Se informada uma NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig): -Série = [0-909] e CNPJ zerado ou dígito inválido, ou -Série = [910-969] e CPF zerado ou dígito inválido                                                | Facul.   |   552 | Rej.     | Rejeição: Chave de Acesso referenciada com CNPJ/CPF inválido[nOcor:nnn]                           |
| BA02a-60    |       55 | Se informada uma NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig): -Modelo da NF-e referenciada diferente de 55                                                                                                            | Facul.   |   679 | Rej.     | Rejeição: Chave de Acesso referenciada com Modelo inválido[nOcor:nnn]                             |
| BA02a-70    |       55 | Se informada uma NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig): -Chave de Acesso referenciada com Número zerado                                                                                                         | Facul.   |   683 | Rej.     | Rejeição: Chave de Acesso referenciada com Número inválido[nOcor:nnn]                             |
| BA02a-74    |       55 | Se informada uma NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig): - Chave de Acesso referenciada com Código Numérico não zerado                                                                                           | Facul.   |   955 | Rej.     | Rejeição: Chave de Acesso referenciada com código numérico não zerado [nOcor:nnn]                 |
| BA02a-80    |       55 | Se informada uma NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig): -Verificar duplicidade da NF-e referenciada (duplicidade da tag: refNFeSig) Observação: desconsiderar o Dígito Verificador na comparação de duplicidade | Facul.   |   680 | Rej.     | Rejeição: Chave de Acesso referenciada em duplicidade na NF-e [nOcor:nnn]                         |
| BA02a-90    |       55 | Se informada uma NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig): -Verificar se alguma NF-e referenciada (tag: refNFe) possui mesma Chave Natural                                                                         | Facul.   |   680 | Rej.     | Rejeição: Chave de Acesso referenciada em duplicidade na NF-e [nOcor:nnn]                         |
| BA02a-100   |       55 | Se informada uma NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig): -Nota Fiscal referenciada com a mesma Chave Natural da Nota Fiscal atual (mesma UF, CNPJ/CPF, Série e Nro);                                             | Facul.   |   952 | Rej.     | Rejeição: Chave de Acesso referenciada com a mesma Chave Natural da Nota Fiscal atual [nOcor:nnn] |
| BA02a-110   |       55 | Se informada uma NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig): - Se Mês-Ano da Chave de Acesso superior a Abril/11; - Chave de Acesso referenciada com Tipo de Emissão Inválido (diferente de 1, 2, 3, 4, 5, 6, 7, 9)  | Facul.   |   953 | Rej.     | Rejeição: Chave de Acesso referenciada com tipo de emissão inválido [nOcor:nnn]                   |

![Image](assets/image_000013_876e38e047fcd6dc05d48d543dc7e6487039eac7a0c80caef71b1c5afba735ab.png)

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                   | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                    |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------------------------------------------------|
| BA02a-120   |       55 | Se informada uma NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig) em UF que não permite tal referência: - Chave de Acesso referenciada com código numérico zerado não aplicável para a UF Observação: Essa regra se aplica para as seguintes UF: PE | Facul.   |   956 | Rej.     | Rejeição: Chave de Acesso referenciada com código numérico zerado não permitida na UF [nOcor:nnn] |

## 4.2. C. Identificação do Emitente

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                      | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                      |
|-------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-------------------------------------------------------------------------------------|
| C02a-04     |       65 | Se informado CPF do emitente: - Se NFC-e (modelo 65) (NT 2015.002)                                                                                                                                                                                                      | Obrig.   |   337 | Rej.     | Rejeição: NFC-e para emitente pessoa física                                         |
| C02a-08     |       55 | Se informado CPF do emitente: - Se NF-e (modelo 55) Observação: Regra de validação opcional a critério da UF. (NT 2018.001)                                                                                                                                             | Obrig.   |   652 | Rej.     | Rejeição: NF-e para emitente pessoa física                                          |
| C02a-14     |       55 | Se informado CPF do Emitente: - Série difere da faixa para emitente CPF: 890-899 e 910-919 Observação: Regra de validação opcional a critério da UF. Permite a emissão de NF-e por pessoa física, somente no serviço de Nota Fiscal Avulsa no site da UF. (NT 2018.001) | Obrig.   |   407 | Rej.     | Rejeição: CPF do Emitente somente no serviço de Nota Fiscal Avulsa no site do Fisco |

## 4.3. I. Produtos e Serviços

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                              | Aplic.     | Msg   | Efeito   | Descrição Erro                                                                             |
|-------------|----------|---------------------------------------------------------------------------------------------------------------------------------|------------|-------|----------|--------------------------------------------------------------------------------------------|
| I08-186     |       55 | NF-e (mod=55) com lançamento relativo a Documento Fiscal de Varejo (CFOP=5.929 ou CFOP6.929) com ECF referenciado (tag: refECF) | Facul. 953 |       | Rej.     | Rejeição: Informado ECF referenciado para CFOP 5.929 em UF que não permite essa referência |

![Image](assets/image_000014_5740b01e9b7f5d7d975a23f4e12b34fed4d2a0d4c4f2f4249027d0373eaf79be.png)

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Aplic.   |   Msg | Efeito   | Descrição Erro                                                     |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------|
| I08-194     |       55 | Se emitente for não contribuinte do ICMS (CCC/tpIE=3) - Se operação de Venda, com os CFOP abaixo: 5101, 5102, 5103, 5104, 5105, 5106, 5109, 5110, 5116, 5117,5118, 5119, 5120, 5122, 5123, 5917, 5251, 5252, 5253, 5254, 5255, 5256, 5257, 5258, 5301, 5302, 5303, 5304, 5305, 5306, 5307, 5351, 5352, 5353, 5354, 5355, 5356, 5357, 5932, 5359, 5360, 5401, 5402, 5403, 5405, 5501, 5502, 5124, 5125, 5917, 6101, 6102, 6103, 6104, 6105, 6106, 6107, 6108, 6109, 6110, 6116, 6117, 6118, 6119, 6120, 6122, 6123, 6917, 6151, 6152, 6153, 6155, 6156, 6251, 6252, 6253, 6254, 6255, 6256, 6257, 6258, 6301, 6302, 6303, 6304, 6305, 6306, 6307, 6351, 6352, 6353, 6354, 6355, 6356, 6357, 6359, 6360, 6932, 6401, 6402, 6403, 6404, 6408, 6409, 6501, 6502, 6917, 6124, 6125, 7101, 7102, 7105, 7106, 7127, 7651, 7654, 7667, 7251, 7301, 7358 Exceção : Emissão de Nota Fiscal Avulsa - NFA-e (procEmi=1 ou 2) Observação : : Regra de Validação opcional, a critério da UF. | Facul.   |   475 | Rej      | Rejeição: Operação não permitida para não contribuinte [nItem:999] |
| I08-198     |       55 | Se emitente for não contribuinte do ICMS (CCC/tpIE=3) - Se operação com os CFOP 5949, 6949, 7949 e valor do ICMS diferente de zero (verificar vICMS, vICMSOp, vICMSDif, vICMSRet, vICMSEfet) Exceção : Emissão de Nota Fiscal Avulsa - NFA-e (procEmi=1 ou 2) Observação : : Regra de Validação opcional, a critério da UF.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Facul.   |   475 | Rej      | Rejeição: Operação não permitida para não contribuinte [nItem:999] |

## 4.4. N. Item / Tributo: ICMS

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                               | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                        |
|-------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------------------------------------|
| N17c-30     |       55 | Se Operação Interna ou Operação Interestadual (idDest=1 ou 2) com CST=00 (operação tributada normalmente): - Se informado valor diferente de zero para o FCP (verificar tags vFCP, vFCPST, vFCPSTRet) Observação: Regra de Validação opcional, a critério da UF. | Facul.   |   474 | Rej.     | Rejeição: FCP não deve ser destacado na NF-e conforme legislação estadual [nItem:999] |

## 4.5. ZD. Informações do Responsável Técnico

![Image](assets/image_000015_876e38e047fcd6dc05d48d543dc7e6487039eac7a0c80caef71b1c5afba735ab.png)

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                 | Aplic.   |   Msg | Efeito   | Descrição Erro                                 |
|-------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------|
| ZD02-10     | 55/65    | Se informado CNPJ do responsável técnico e CNPJ inválido (NT 2021.002) - CNPJ com zeros, nulo ou DV inválido Observação : Implementação futura, exceto as UF de AM, MS, PE, PR, SC e TO, nas quais estas regras já estão em vigor em ambiente de teste e entrarão em vigor em ambiente de produção no dia 03 de junho de 2019 (NT 2018.005 v 1.30) | Facul.   |   973 | Rej.     | Rejeição: CNPJ do responsável técnico inválido |

## 4.6. 3A. Banco de Dados: NF-e Referenciada

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Aplic.   |   Msg | Efeito   | Descrição Erro                                                 |
|-------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------------------------|
| 3BA02a-10   |       55 | Para cada NF-e referenciada por Chave de Acesso com código numérico zerado (tag: refNFeSig), se a UF da Chave de Acesso referenciada for igual a UF do Emitente: - Acessar BD NFE com Chave Natural - NF-e referenciada inexistente Exceção: A NF-e referenciada pode não existir no caso de Emissão em Contingência (tpEmis = 2, 4 ou 5) desde que a Chave de Acesso da NF-e referenciada com código numérico zerado tenha o Ano-Mês de Emissão inferior a 1 mês da data atual ou desde que exista o EPEC. | Facul.   |   267 | Rej.     | Rejeição: Chave de Acesso referenciada inexistente [nRef: xxx] |

## 4.7. 7. Banco de Dados: Cadastro da SEFAZ

![Image](assets/image_000016_5740b01e9b7f5d7d975a23f4e12b34fed4d2a0d4c4f2f4249027d0373eaf79be.png)

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                         | Aplic.   |   Msg | Efeito   | Descrição Erro                                                              |
|-------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-----------------------------------------------------------------------------|
| 7C21-10     | 55/65    | Código de Regime Tributário do emitente divergente do cadastrado na SEFAZ (tag: emit/CRT): - CRT='1 - Simples Nacional' para Contribuinte cadastrado como Regime Normal na UF (CCC, regTrib=9); - CRT='3 - Regime Normal' para Contribuinte cadastrado como Simples Nacional na UF (CCC, regTrib=1 ou 2); Observação : Regra de Validação opcional por UF. | Facul.   |   481 | Rej.     | Rejeição: Código Regime Tributário do emitente diverge do cadastro na SEFAZ |

## 5. Novos códigos de Rejeição

|   CÓDIGO | MOTIVO DE NÃO ATENDIMENTO DA SOLICITAÇÃO                                                                                         |
|----------|----------------------------------------------------------------------------------------------------------------------------------|
|      474 | Rejeição: FCP não deve ser destacado na NF-e conforme legislação estadual [nItem:999]                                            |
|      475 | Rejeição: Operação não permitida para não contribuinte [nItem:999]                                                               |
|      951 | Rejeição: Chave de Acesso referenciada com código numérico zerado não permitida para finalidade diferente de normal. [nOcor:nnn] |
|      952 | Rejeição: Chave de Acesso referenciada com a mesma Chave Natural da Nota Fiscal atual [nOcor:nnn]                                |
|      953 | Rejeição: Informado ECF referenciado para CFOP 5.929 em UF que não permite essa referência                                       |
|      953 | Rejeição: Chave de Acesso referenciada com tipo de emissão inválido [nOcor:nnn]                                                  |
|      954 | Rejeição: Chave de Acesso referenciada não permitida para esta operação[nOcor:nnn]                                               |
|      955 | Rejeição: Chave de Acesso referenciada com código numérico não zerado [nOcor:nnn]                                                |
|      956 | Rejeição: Chave de Acesso referenciada com código numérico zerado não permitida na UF [nOcor:nnn]                                |

![Image](assets/image_000017_5740b01e9b7f5d7d975a23f4e12b34fed4d2a0d4c4f2f4249027d0373eaf79be.png)