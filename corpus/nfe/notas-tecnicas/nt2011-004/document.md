---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2011-004"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "172081ec11d93eb8d2a638e7eaae181b0ba5a6f89d3aa79c9f8e0eb4401ceb05"
converted_at_utc: "2026-06-25T15:25:44.298914+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_70393e623d5c208a50c9b568d3f5d7be90ba2c1a98cdedb2679b2a57092bf088.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_4f3c059e8cf7333b5f4ef81546671c5e9935f6615a9036d429da129206bfdb6d.png)

## Nota Técnica 2011/004

## Divulga atualização de Schema XML da NF-e e novas regras de validação para recepção de NF-e

![Image](assets/image_000002_d44e196a911ea212ddfce58f5e4729f941700d15a08a352dde8364687a0030eb.png)

Julho-2011

![Image](assets/image_000003_1b08ad73f649fe1d7180151459178ccb1ea3cfc05e1cc4d9d306d7400a20b198.png)

## 1.  Resumo

Esta edição divulga atualização do leiaute da NF-e  e das regras de validação da NF-e.

## Prazos de entrada em vigência das alterações:

- Ambiente de homologação 01/10/2011
- Ambiente de produção 01/11/2011

![Image](assets/image_000004_081a557b0a51254c568d40f5e3c1e69ed23f478660733fa1a619ae8a2d241db4.png)

## 2.  Alteração de Schema XML da NF-e

## 2.1 hSaiEnt (B10a) - Hora de Saída ou da Entrada da Mer cadoria/Produto

Aperfeiçoamento do Schema XML para impedir a informação da hSaiEnt sem a correspondente data de saída.

## 2.2 CEP (C13) - CEP do endereço do emitente

| 42   | C13   | CEP   | Código do CEP   | E   | C05   | N   | 1-1   | 8   | Informar os zeros não significativos. (NT2011/004)   |
|------|-------|-------|-----------------|-----|-------|-----|-------|-----|------------------------------------------------------|

Alteração no Schema XML para tornar o CEP campo de informação obrigatória.

## 2.3 fone (D06), nDAR (D08), dEmi (D09) e vDar (D10) - Identificação do Fisco emitente da NF-e

|   55 | D06   | fone   | Telefone                                                     | E   | D01   | N   | 0-1   | 6-14   |    | Preencher com Código DDD + número do telefone (v.2.0) (NT2011/004)   |
|------|-------|--------|--------------------------------------------------------------|-----|-------|-----|-------|--------|----|----------------------------------------------------------------------|
|   57 | D08   | nDAR   | Número do Documento de Arrecadação de Receita                | E   | D01   | C   | 0-1   | 1-60   |    | (NT2011/004)                                                         |
|   58 | D09   | dEmi   | Data de emissão do Documento de Arrecadação                  | E   | D01   | D   | 0-1   | -      |    | Formato 'AAAA-MM-DD' (NT2011/004)                                    |
|   59 | D10   | vDAR   | Valor Total constante no Documento de arrecadação de Receita | E   | D01   | N   | 0-1   | 1-15   |  2 | (NT2011/004)                                                         |

![Image](assets/image_000005_49c050247351da2a2c231c53e4a8465d373b8de1dc876ed9398515d38570ef1b.png)

NT 2011/004

Alteração no Schema XML para permitir a não informação dos campos: fone (D06), nDAR (D08), dEmi (D09) e vDar (D10) do grupo avulsa (informações da NF-e avulsa)  quando inexistentes.

## 2.4 cPais (E14) - código de país

Acréscimo de dois novos códigos de países:

4235 - LEBUAN,ILHAS

4885 - MAYOTTE (ILHAS FRANCESAS)

## 2.5 CFOP (I08) do produto

Acréscimo dos seguintes CFOP: 1128, 2128 e 3128 no rol de CFOP válidos.

## 2.6 qCOM (I10) e qTrib (I14) - Quantidade Comercial e Quantidade Tributável

Alteração de Schema XML com redução da quantidade de dígitos da parte inteira no Schema XML para 11 dígitos conforme previsto no leiaute da NF-e.

## 2.7 DI (I18) - Declaração de Importação - redução do nú mero máximo de ocorrências.

| 117   | I18   | DI   | Declaração de Importação   | G   | I01   | 0-100   | Informar dados da importação (NT2011/004)   |
|-------|-------|------|----------------------------|-----|-------|---------|---------------------------------------------|

## 2.8 nDI (I19) - Número do Documento de Importação DI/DSI/DA

| 118   | I19   | nDI   | Número do Documento de Importação DI/DSI/DA/DRI-E   | E   | I18   | C   | 1-1   | 1-12   | (NT2011/004)   |
|-------|-------|-------|-----------------------------------------------------|-----|-------|-----|-------|--------|----------------|

![Image](assets/image_000006_480f1e110f277b96e1d2411d017610051027f8bd104912ff759438b9cca06118.png)

Alteração de Schema XML com aumento do tamanho do campo da tag nDI para aceitar a DIRE de 12 dígitos, além de alteração das observações com o acréscimo DRI-E no rol de documentos.

## 2.9 adi (I25) - Adições - redução do número máximo de ocorrências.

| 124   | I25   | adi   | Adições   | G   | I18   | 1-100   | (NT2011/004)   |
|-------|-------|-------|-----------|-----|-------|---------|----------------|

## 2.10  motDesICMS (N28) - Motivo da desoneração do ICMS

|   204.01 | N17   | vICMS      | Valor do ICMS                 | E   | N06   | N   | 0-1   |   15 | 2   | O valor do ICMS desonerado será informado apenas nas operações: a) com veículos beneficiados com a desoneração condicional do ICMS. b) destinadas à SUFRAMA, informando-se o valor que seria devido se não houvesse isenção. c) de venda a órgãos da administração pública direta e suas fundações e autarquias com isenção do ICMS. (NT2011/004)   |
|----------|-------|------------|-------------------------------|-----|-------|-----|-------|------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   204.02 | N28   | motDesICMS | Motivo da desoneração do ICMS | E   | N06   | N   | 0-1   |    1 |     | Este campo será preenchido quando o campo anterior estiver preenchido. Informar o motivo da desoneração: 1 - Táxi; 2 - Deficiente Físico; 3 - Produtor Agropecuário;                                                                                                                                                                                |

![Image](assets/image_000007_a3c13257e9af21dea56ae6054d798d3a3db7a86299a9d841b4f5a2e1f00256a9.png)

| 4 - Frotista/Locadora; 5 - Diplomático/Consular; 6 - Utilitários e Motocicletas da Amazônia Ocidental e Áreas de Livre Comércio (Resolução 714/88 e 790/94 - CONTRAN e suas alterações); 7 - SUFRAMA; 8 - Venda a Órgãos Públicos 9 - outros. (NT2011/004)   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Alteração de Schema XML para acréscimo do item 8 - Venda a Órgãos Públicos no rol de motivo da desoneração ( motDesICMS ) .

## 2.11  vBCSTRet (N26) - valor da BC do ICMS ST e vICMSSTRet (N27) - valor do ICMS ST cobrados anteriormente por ST

|    216 | N26   | vBCSTRet   | Valor da BC do ICMS ST retido   | E   | N08   | N   | 0-1   |   15 |   2 | Valor da BC do ICMS ST cobrado anteriormente por ST (v2.0). O valor pode ser omitido quando a legislação não exigir a sua informação. (NT2011/004)   |
|--------|-------|------------|---------------------------------|-----|-------|-----|-------|------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------|
|    217 | N27   | vICMSSTRet | Valor do ICMS ST retido         | E   | N08   | N   | 0-1   |   15 |   2 | Valor do ICMS ST cobrado anteriormente por ST (v2.0). O valor pode ser omitido quando a legislação não exigir a sua informação. (NT2011/004)         |
| 245.50 | N26   | vBCSTRet   | Valor da BC do ICMS ST retido   | E   | N10g  | N   | 0-1   |   15 |   2 | Valor da BC do ICMS ST cobrado anteriormente por ST (v2.0). O                                                                                        |

![Image](assets/image_000008_480f1e110f277b96e1d2411d017610051027f8bd104912ff759438b9cca06118.png)

|        |     |            |                         |    |      |    |     |    |    | valor pode ser omitido quando a legislação não exigir a sua informação. (NT2011/004)                                                         |
|--------|-----|------------|-------------------------|----|------|----|-----|----|----|----------------------------------------------------------------------------------------------------------------------------------------------|
| 245.51 | N27 | vICMSSTRet | Valor do ICMS ST retido | E  | N10g | N  | 0-1 | 15 |  2 | Valor do ICMS ST cobrado anteriormente por ST (v2.0). O valor pode ser omitido quando a legislação não exigir a sua informação. (NT2011/004) |

Alteração do Schema XML para possibilitar a não informação dos campos quando a legislação não exigir a informação. Ambos campos devem ser informados ou omitidos.

## 2.12  CFOP (X16) do grupo de retTransp (x11)

Acréscimo dos seguintes CFOP: 5931, 5932, 6931 e 6932 no rol de CFOP válidos.

## 2.13  Placa (X19/X23) - Placa do Veículo/Placa do Reboque

|   374 | X19   | placa   | Placa do Veículo   | E   | X18   | C   | 1-1   |   7 | Informar no formato: XXX9999 (NT2011/004)   |
|-------|-------|---------|--------------------|-----|-------|-----|-------|-----|---------------------------------------------|
|   378 | X23   | placa   | Placa do Veículo   | E   | X22   | C   | 1-1   |   7 | Infor mar no formato: XXX9999 (NT2011/004)  |

Alteração do Schema XML para exigir o preenchimento da placa no formato XXX9999.

![Image](assets/image_000009_49c050247351da2a2c231c53e4a8465d373b8de1dc876ed9398515d38570ef1b.png)

## 2.14  dup (Y07) - Grupo da Duplicata - redução do número máximo de ocorrências.

| 395   | Y07 dup   | Grupo da Duplicata   | G   | Y01   | 0-120   | (NT2011/004)   |
|-------|-----------|----------------------|-----|-------|---------|----------------|

## 2.15  xNEmp (ZB02) - Nota de Empenho

| 406   | ZB02   | xNEmp   | Nota de Empenho   | E   | ZB01   | C   | 0-1   | 1-22   | Informar a identificação da Nota de Empenho, quando se tratar de compras públicas (NT2011/004)   |
|-------|--------|---------|-------------------|-----|--------|-----|-------|--------|--------------------------------------------------------------------------------------------------|

Alteração do tamanho máximo permitido para 22 caracteres.

## 3.  Alteração do Schema XML do retorno do Pedido de Con sulta de Recibo de Lote

| BR06b cMsg   | E BR01   | N   | 0-1   | 1-4   | Código da Mensagem (v2.0) Campo de uso da SEFAZ para enviar mensagem de interesse da SEFAZ para o emissor.   |
|--------------|----------|-----|-------|-------|--------------------------------------------------------------------------------------------------------------|

Alteração do tamanho do campo para tamanho variável.

## 4.  Novas regras de validação

## 4.1 Validação NF-e / CPF do Destinatário

| #           | Campo Regra de Validação                                                                              | Aplic.   |   Msg | Efeito   | Descrição Erro                                         |
|-------------|-------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------|
| G1E17.4 E17 | Se informado IE do Destinatário e CPF: . Acessar Cadastro Contribuinte (Chave: IE / CPF destinatário) | Facult.  |   623 | Rej.     | Rejeição: CPF Destinatário não cadastrado (NT2011/004) |

![Image](assets/image_000010_a3c13257e9af21dea56ae6054d798d3a3db7a86299a9d841b4f5a2e1f00256a9.png)

| - CPF Destinatário não cadastrado      |         |     |      |                                                             |
|----------------------------------------|---------|-----|------|-------------------------------------------------------------|
| - IE destinatário não vinculada ao CPF | Facult. | 624 | Rej. | Rejeição: IE Destinatário não vinculada ao CPF (NT2011/004) |

## 4.2 Validação do DV do cEAN e cEANTrib

| #    | Campo Regra de Validação   | Campo Regra de Validação                                                                       | Aplic.   |   Msg | Efeito   | Descrição Erro                           |
|------|----------------------------|------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------|
| GI03 | I03                        | Se informada a TAG cEAN: - cEAN com zeros ou dígito de controle inválido (NT2011/004)          | Facult.  |   611 | Rej.     | Rejeição: cEAN inválido (NT2011/004)     |
| GI12 | I12                        | Se informada a TAG cEANTrib: - cEANTrib com zeros ou dígito de controle invál ido (NT2011/004) | Facult.  |   612 | Rej.     | Rejeição: cEANTrib inválido (NT2011/004) |

## 4.3 Validação da existência dos grupos IPI e II em oper ações de importação

| #       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Aplic.   |   Msg | Efeito   | Descrição Erro                                                         |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------------|
| GI08.7a | Campo Regra de Validação I08 CFOP de Importação (inicia por 3) e não informado o grupo de IPI Exceção: a regra não se aplica para os seguintes C FOP: 3.201 - Devolução de venda de produção do estabelec imento 3.202 - Devolução de venda de mercadoria adquirida ou recebida de terceiros 3.211 - Devolução de venda de produção do estabelec imento sob o regime de 'drawback' 3.503 - Devolução de mercadoria exportada que tenha sido recebida com fim específico de exportação 3.553 - Devolução de venda de bem do ativo imobilizado (NT2011.004) | Facult.  |   597 | Rej.     | Rejeição: CFOP de Importação e não informado dados de IPI (NT2011/004) |
| GI08.7b | I08 CFOP de Importação (inicia por 3) e não informado o grupo de II Exceção: a regra não se aplica para os seguintes C FOP: 3.201 - Devolução de venda de produção do estabelec imento                                                                                                                                                                                                                                                                                                                                                                    | Facult.  |   599 | Rej.     | Rejeição: CFOP de Importação e não informado dados de II (NT2011/004)  |

![Image](assets/image_000011_480f1e110f277b96e1d2411d017610051027f8bd104912ff759438b9cca06118.png)

| 3.202 - Devolução de venda de mercadoria adquirida ou recebida de terceiros 3.211 - Devolução de venda de produção do estabelec imento sob o regime de 'drawback' 3.503 - Devolução de mercadoria exportada que tenha sido recebida com fim específico de exportação 3.553 - Devolução de venda de bem do ativo imobilizado (NT2011.004)   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## 4.4 Validação dos Valores Unitários de Comercialização e de Tributação do item de produto

| #     | Campo Regra de Validação   | Campo Regra de Validação                                                                                                                                                                                                                                                    | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                     |
|-------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------------------------------------------------|
| GI10a | I10a                       | vProd (id:I11) difere de vUnCom (id:I10a) * qCom (id:I10) Obs.: 1. O valor resultante de vUnCom (id:I10a) * qCom (id:I10) deve ser arredondado para um valor numérico com dua s decimais; 2. Considerar uma tolerância de R$ 0,01 para mais ou para menos na validação.     | Facult.  |   629 | Rej.     | Rejeição: Valor do Produto difere do produto Valor Unitário de Comercialização e Quantidade Comercial (NT2011/004) |
| GI14a | I14a                       | vProd (id:I11) difere de vUnTrib (id:I14a) * qTrib (id:I14) Obs.: 1. O valor resultante de vUnTrib (id:I14a) * qTrib (id:I14) deve ser arredondado para um valor numérico com dua s decimais; 2. Considerar uma tolerância de R$ 0,01 para mais ou para menos na validação. | Facult.  |   630 | Rej.     | Rejeição: Valor do Produto difere do produto Valor Unitário de Tributação e Quantidade Tributável (NT2011/004)     |

![Image](assets/image_000012_081a557b0a51254c568d40f5e3c1e69ed23f478660733fa1a619ae8a2d241db4.png)

## 4.5 Validação da desoneração condicional do ICMS

| #      | Campo Regra de Validação   | Campo Regra de Validação                                          | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                            |
|--------|----------------------------|-------------------------------------------------------------------|----------|-------|----------|-------------------------------------------------------------------------------------------|
| GN28   | N28                        | Se informado motDesICMS = 7 ISUF (id:E18) deve ser informado      | Facult.  |   625 | Rej.     | Rejeição: Inscrição SUFRAMA deve ser informada na venda com isenção para ZFM (NT2011/004) |
| GN28.1 | N28                        | Se informado motDesICMS = 7 CFOP deve ser 6109 ou 6110            | Facult.  |   626 | Rej.     | Rejeição: O CFOP de operação isenta para ZFM deve ser 6109 ou 6110 (NT2011/004)           |
| GN28.2 | N28                        | Se informado motDesICMS, o vICMS (id:N17) deve ser maior que zero | Facult.  |   627 | Rej.     | Rejeição: O valor do ICMS desonerado deve ser informado (NT2011/004)                      |

## 4.6 Validação do valor da NF-e

| #     | Campo Regra de Validação                                                                                                        | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                               |
|-------|---------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------------------------------------------------------|
| GW16a | Verificar se o valor total da NF-e é superior ao va lor limite estabelecido pela SEFAZ, o valor limite deve ser parametrizável. | Facult.  |   628 | Rej.     | Rejeição: Total da NF superior ao valor limite estabelecido pela SEFAZ [Limite] (NT2011/004) |

## 4.7 Ampliar a validação do somatório dos valores dos it ens sujeitos ao ICMS com os valores informados no grupo ICMSTot

| #    | Campo   | Regra de Validação                                                         | Aplic.   |   Msg | Efeito   | Descrição Erro                                                   |
|------|---------|----------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------|
|      |         | W-Total da NF-e                                                            |          |       |          |                                                                  |
| GW11 |         | Total do vII (id:W11) difere do somatório do valor dos itens (id:P04) (*3) | Facult.  |   601 | Rej.     | Rejeição: Total do II difere do somatório dos itens (NT2011/004) |
| GW13 |         | Total do vPIS (id:W13) difere do somatório do valor dos itens              | Facult.  |   602 | Rej.     | Rejeição: Total do PIS difere do somatório dos itens             |

![Image](assets/image_000013_fc631bb6d7d2cf5321fd8158724b1aab00e848b70bdc0dc428d21ef23f483f54.png)

| #    | Campo   | Regra de Validação                                                                                                         | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                        |
|------|---------|----------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------------------------------------|
|      |         | (id:Q09) (*3) de item sujeito ao ICMS (existe grupo ICMS)                                                                  |          |       |          | sujeitos ao ICMS (NT2011/004)                                                         |
| GW14 |         | Total do vCOFINS (id:W14) difere do somatório do valor dos itens (id:S11) (*3) de item sujeito ao ICMS (existe grupo ICMS) | Facult.  |   603 | Rej.     | Rejeição: Total do COFINS difere do somatório dos itens sujeitos ao ICMS (NT2011/004) |
| GW15 |         | Total do vOutro (id:W15) difere do somatório do valor dos itens (id:I17a) (*3)                                             | Facult.  |   604 | Rej.     | Rejeição: Total do vOutro difere do somatório dos itens (NT2011/004)                  |

## 4.8 Novas regras de validação do somatório dos valores  dos itens sujeitos ao ISSQN com os valores informados no grupo ISSQNtot

| #    | Campo   | Regra de Validação                                                                                             | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                 |
|------|---------|----------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------------------------------------|
|      |         | I - Produtos e Serviços                                                                                        |          |       |          |                                                                                                |
| GW18 |         | Total do vServ (id:W18) difere do somatório do valor dos itens do vProd (id:I11) de item sujeito ao ISSQN (*3) | Facult.  |   605 | Rej.     | Rejeição: Total do vServ difere do somatório do vProd dos itens sujeitos ao ISSQN (NT2011/004) |
| GW19 |         | Total do vBC (id:W19) difere do somatório do valor dos itens (id:U02) de item sujeito ao ISSQN (*3)            | Facult.  |   606 | Rej.     | Rejeição: Total do vBC do ISS difere do somatório dos itens (NT2011/004)                       |
| GW20 |         | Total do vISS (id:W20) difere do somatório do valor dos itens (id:U04) de item sujeito ao ISSQN (*3)           | Facult.  |   607 | Rej.     | Rejeição: Total do ISS difere do somatório dos itens (NT2011/004)                              |
| GW21 |         | Total do vPIS (id:W21) difere do somatório do valor dos itens (id:Q09) de item sujeito ao ISSQN (*3)           | Facult.  |   608 | Rej.     | Rejeição: Total do PIS difere do somatório dos itens sujeitos ao ISSQN (NT2011/004)            |
| GW22 |         | Total do vCOFINS (id:W22) difere do somatório do valor dos itens (id:S11) de item sujeito ao ISSQN (*3)        | Facult.  |   609 | Rej.     | Rejeição: Total do COFINS difere do somatório dos itens sujeitos ao ISSQN (NT2011/004)         |

## 4.9 Validação do valor total da NF

| #    | Campo   | Regra de Validação                                                                                   | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                 |
|------|---------|------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------------------------------------|
|      |         | W-Total da NF-e                                                                                      |          |       |          |                                                                                                |
| GW16 |         | Total do vNF (id:W16) difere do somatório de: (+) vProd (id:W07) (-) vDesc (id:W10) (+) vST (id:W06) | Facult.  |   610 | Rej.     | Rejeição: Total da NF difere do somatório dos Valores compõe o valor Total da NF. (NT2011/004) |

![Image](assets/image_000014_480f1e110f277b96e1d2411d017610051027f8bd104912ff759438b9cca06118.png)

| #   | Campo   | Regra de Validação                                                                                                   | Aplic.   | Msg   | Efeito   | Descrição Erro   |
|-----|---------|----------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------|
|     |         | (+) vFrete (id:W08) (+) vSeg (id:W09) (+) vOutro (id:W15) (+) vII (id:W11) (+) vIPI (id:W12) (+) vServ (id:W18) (*3) |          |       |          |                  |

## 4.10  Validação de duplicidade de NF-e

| #       | Campo Regra de                   | Validação Aplic.                                                 |   Msg | Efeito   | Descrição Erro                                                                 |
|---------|----------------------------------|------------------------------------------------------------------|-------|----------|--------------------------------------------------------------------------------|
| G1B08.5 | B08 NF-e com mesmo processamento | número e série já transmitida e aguarda ndo (NT2011/004) Facult. |   635 | Rej.     | Rejeição: NF-e com mesmo número e série transmitida e aguardando processamento |

## 4.11  Validação do Cancelamento da NF-e (Item 4.3.7 -d, d o Manual)

| H07b   | Chave de Acesso difere da existente em BD (opcionalmente a descrição do erro, campo xMotivo, tem concatenada a Chave de Acesso) (NT2011/004)   | Obrig.   | 613   | Rej.   |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|--------|

## 4.12  Consulta Situação da NF-e (Item 4.5.7 -b, do Manual )

| J02a   | Chave de Acesso com dígito verificador inválid o (NT2011/004)                   | Obrig.   |   236 | Rej.   |
|--------|---------------------------------------------------------------------------------|----------|-------|--------|
| J02b   | Chave de Acesso inválida (Código UF inválido) (NT2011/004)                      | Obrig.   |   614 | Rej.   |
| J02c   | Chave de Acesso inválida (Ano < 05 ou Ano maio r que Ano corrente) (NT2011/004) | Obrig.   |   615 | Rej.   |
| J02d   | Chave de Acesso inválida (Mês =0 ou Mês > 2)1 (NT2011/004)                      | Obrig.   |   616 | Rej.   |
| J02e   | Chave de Acesso inválida (CNPJ zerado ou dígit o inválido) (NT2011/004)         | Obrig.   |   617 | Rej.   |

já

![Image](assets/image_000015_480f1e110f277b96e1d2411d017610051027f8bd104912ff759438b9cca06118.png)

| J02f   | Chave de Acesso inválida (modelo diferente de 55) (NT2011/004)                                                                                                                         | Obrig.   |   618 | Rej.   |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|--------|
| J02g   | Chave de Acesso inválida (número NF = 0) (NT20 11/004)                                                                                                                                 | Obrig.   |   619 | Rej.   |
| J06    | Chave de Acesso difere da existente em BD (opcionalmente a descrição do erro, campo xMotivo, tem concatenada a Chave de Acesso, quando o autor da consulta for o emissor) (NT2011/004) | Obrig.   |   613 | Rej.   |

## 5.  Alteração das regras de validações existentes

## 5.1 Verificação de CFOP interno para destinatário contr ibuinte do ICMS de outra UF

| #      | Campo   | Regra de Validação                                                                                                                                                                                                                                                              | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                             |
|--------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------------------------------------------------------------------------------------|
|        |         | I - Produtos e Serviços                                                                                                                                                                                                                                                         |          |       |          |                                                                                                                            |
| GI08.3 | I08     | CFOP de Operação no Estado (inicia com 5) e UF emitente diferente UF destinatário e destinatário contribuin te do ICMS (tem IE) Exceção: Verificar se a tag UFCons (id:L120) foi informada com a mesma UF do emitente, neste caso o CFOP iniciado com 5 é válid o. (NT2010/007) | Facult.  |   521 | Rej.     | Rejeição: CFOP de Operação Estadual e UF do emitente difere da UF do destinatário para destinat ário contribuinte do ICMS. |
|        |         | Exceção: Verificar se a tag modFrete (id:X02) foi informada com 9- Sem frete, neste caso o CFOP iniciado com 5 é válid o. (NT2011/004)                                                                                                                                          |          |       |          |                                                                                                                            |

Alteração realizada para permitir a venda de peças e material de consumo para contribuinte do ICMS localizada em outra UF.

## 5.2 Validação do Total dos Produtos e Serviços de itens  do ICMS

| #   | Regra de Validação   | Aplic. Msg Efeito   |
|-----|----------------------|---------------------|

![Image](assets/image_000016_94595a09249789e18850d662b603d6ccf6a338f2eee6de8b5af418dee0a02b29.png)

| #    | Campo   | Regra de Validação                                                                                                                                                                                | Aplic.   |   Msg | Efeito   | Descrição Erro                                                     |
|------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------|
|      |         | I - Produtos e Serviços                                                                                                                                                                           |          |       |          |                                                                    |
| GW07 |         | Total dos Produtos e Serviços (id:W07) difere do somatório do valor dos itens (id:I11) sujeitos ao ICMS. Considerar somente os valores dos itens com a TAG indTot (id:I17b) = 1 (*3) (NT2011/004) | Facult.  |   564 | Rej.     | Rejeição: Total do Produto / Serviço difere do somatório dos itens |

## 5.3 Eliminação do Ano do controle de duplicidade da NF- e

|         |     | Banco de Dados: Chave da NF-e                                                                                                                                                           |         |     |      |                                                                                                             |
|---------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-----|------|-------------------------------------------------------------------------------------------------------------|
| G1B08   | B08 | Acesso BD NFE (Chave: CNPJ Emitente, Modelo, Série , Nro): - NF-e já cadastrada, com diferença na Chave de Acesso (Código Numérico ou outras posições da Chave de Acesso). (NT2011/004) | Facult. | 539 | Rej. | Rejeição: Duplicidade de NF-e, com diferença na Chave de Acesso [99999999999999999999999999999999999999999] |
| G1B08.4 | B08 | Acesso BD de Inutilização (Chave: CNPJ, Modelo, Série, Nro): - Numeração da NF-e está inutilizada (NT2011/00 4)                                                                         | Obrig.  | 206 | Rej. | Rejeição: NF-e já está inutilizada na Base de dados da SEFAZ                                                |

## 5.4 Eliminação do Ano do no WS de inutilização de numer ação

|     | Banco de Dados: Chave da NF-e                                                                                                                      |        |     |      |                                                                               |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----|------|-------------------------------------------------------------------------------|
| I07 | Acesso BD NFE-Inutilização (Chave: CNPJ Emit, Modelo, Série, nNFIni, nNFFin): - Verificar se já existe um Pedido de inutilizaçãoigual (NT2011/004) | Obrig. | 563 | Rej. | Rejeição: Já existe pedido de Inutilização com a me sma faixa de inutilização |

## 6.  Eliminação das regras de validações existentes

## 6.1 Regras de validação do CNPJ e IE do destinatário pa ra NF-e emitida em ambiente de homologação

![Image](assets/image_000017_480f1e110f277b96e1d2411d017610051027f8bd104912ff759438b9cca06118.png)

| GE02.3   | E02   | Se tpAmb (B24) = 2: o CNPJ (E02) deve ser 99.999.999/0001-91 ou ter conteúdovazio (NT 2011.002)   | Facult.   |   597 | Rej.   | Rejeição: NF-e emitida em ambiente de homologação com CNPJ do destinatário diferente 99999999000191   |
|----------|-------|---------------------------------------------------------------------------------------------------|-----------|-------|--------|-------------------------------------------------------------------------------------------------------|
| GE17.2   | E17   | Se tpAmb (B24) = 2: a IE (E17) deve ter conteúdo vazio (NT 2011.002)                              | Facult.   |   599 | Rej.   | Rejeição: NF-e emitida em ambiente de homologação com IE do destinatário diferente de vazio           |

## 6.2 Regras de validação da Carta de Correção eletrônica

| GA02 Verificar NF-e autorizada há mais de 30 dias (720) horas   | Obrig.   | 501   | Rej.   |
|-----------------------------------------------------------------|----------|-------|--------|

## 7.  Aperfeiçoamento de Web Services

## 7.1 Devolução do Número do Recibo do Lote em caso de duplicidade no processo de autorização da NF-e

Em algumas situações a empresa perde o Número do Recibo do Lote e não consegue obter de forma normal o  resultado do Lote. Nestes casos a empresa normalmente reenvia o Lote e acaba recebendo a informação de NF-e duplicada, mas não consegue consultar o resultado do processame nto do lote por não possuir o Número do Recibo do Lote e geralmente é obrigada a cancelar a NF-e.

Decidido em reunião retornar o número do Recibo de Lote na mensagem de erro de duplicidade da NF-e, de forma opcional por SEFAZ, conforme modelo proposto:

|   cStat | xMotivo                                                                                                                          |
|---------|----------------------------------------------------------------------------------------------------------------------------------|
|     204 | Duplicidade de NF-e [nRec:999999999999999]                                                                                       |
|     205 | NF-e está denegada na base de dados da SEFAZ [n Rec:999999999999999]                                                             |
|     218 | NF-e já está cancelada na base de dados da SEFA Z [nRec:999999999999999]                                                         |
|     539 | Duplicidade de NF-e com diferença na Chave de Acesso [chNFe: 99999999999999999999999999999999999999999999][nRec:999999999999999] |

## 7.2 Devolução dos dados da homologação do pedido de can celamento em duplicidade

de Retornar os dados do Protocolo de homologação do cancelamento no caso do Pedido de cancelamento duplicado (Erro 420 - Rejeição: Cancelamento para NF-e já  cancelada).

![Image](assets/image_000018_a3c13257e9af21dea56ae6054d798d3a3db7a86299a9d841b4f5a2e1f00256a9.png)

## 7.3 Devolução dos dados da homologação do pedido de inu tilização em duplicidade

Retornar os dados do Protocolo de homologação da Inutilização no caso do Pedido de Inutilização duplic ado (Erro 563-Já existe um pedido de Inutilização c om a mesma faixa de inutilização).

## 8.  ORIENTAÇÕES PARA PREENCHIMENTO DE NF-e DESTINADA À ZONA FRANCA DE MANAUS (ZFM)

A emissão NF-e para acobertar operações incentivadas destinadas à Zona Franca de Manaus (ZFM) e Áreas de Livre Comércio (ALC) deverá observar, para o preenchimento dos campos do documento fiscal, as recomendações que seguem:

Os exemplos de preenchimento tomam com base a seguinte operação hipotética:

- UF do remetente: SP (alíquota interestadual de 7%)
- Valor bruto do produto sem descontos: R$ 1.000,00
- Desconto comercial: R$ 200,00
- Base de Cálculo do ICMS para fins de cálculo do abatimento: R$ 800,00 (R$ 1.000,00 - R$ 200,00)
- Valor do ICMS abatido: R$ 56,00 (7% sobre R$ 800,00)
- Valor da Nota: R$ 744,00 (R$ 1.000,00 - R$ 200,00 - R$ 56,00)

## 1) Grupo de Identificação do Destinatário

Informar obrigatoriamente a Inscrição na SUFRAMA.

## 2) Grupo do Detalhamento de Produtos e Serviços

2.1 Informar um dos seguintes CFOP:

- 6.109 (Venda de produção do estabelecimento destinada à Zona Franca de Manaus ou Áreas de Livre Comércio)
- 6.110 (Venda de mercadoria, adquirida ou recebida de terceiros, destinada à Zona Franca de Manaus ou Áreas de Livre Comércio)

![Image](assets/image_000019_1719b3f112bd7bbffc498edd8e7e2a1cd08eb241358c9a6826aeea078134f171.png)

- 2.2 Informar no campo 'Valor Total Bruto dos Produtos ou Serviços' o valor do produto sem a desoneração do ICMS .
- 2.3. Informar no campo 'Valor do Desconto' o valor da desoneração do ICMS e demais descontos.
- 2.4. Informar no campo 'Informações adicionais do produto' o valor da desoneração do ICMS e demais descontos.

Exemplo de XML:

&lt;vProd&gt;1000.00&lt;/vProd&gt;

```
Exemplo de XML: <vDesc>256.00</vDesc>
```

Obs. R$ 200,00 referentes ao desconto comercial e R$ 56,00 de abatimento do ICMS

Exemplo de XML:

&lt;infAdProd&gt;Valor do ICMS abatido: R$ 56,00 (7% sobre R$ 800,00) . Valor do desconto comercial: R$ 200,00.&lt;/infAdProd&gt;

Obs. R$ 200,00 referentes ao desconto comercial e R$ 56,00 de abatimento do ICMS

## 3) Grupo de Tributação do ICMS

- 3.1 Preencher o grupo de tributação do ICMS 40
- Origem da Mercadoria: '0' ('nacional')
- Valor do ICMS: informar o valor do ICMS que foi abatido na operação.
- CST: '40' ('isenta')
- Motivo da desoneração do ICMS: '7' ('SUFRAMA')

```
Exemplo de XML: <ICMS40> <orig>0</orig> <CST>40</CST> <vICMS>56.00</vICMS> <motDesICMS>7</motDesICMS> </ICMS40>
```

![Image](assets/image_000020_1719b3f112bd7bbffc498edd8e7e2a1cd08eb241358c9a6826aeea078134f171.png)

## 4) Grupo de Tributação do PIS

Preencher o grupo de tributação do PIS não tributado

CST: 06 - Operação Tributável (alíquota zero)

Exemplo de XML:

&lt;PISNT&gt;

&lt;CST&gt;06&lt;/CST&gt;

&lt;PISNT&gt;

## 5) Grupo de Tributação da COFINS

Preencher o grupo de tributação da COFINS não tributada CST: 06 - Operação Tributável (alíquota zero)

Exemplo de XML:

&lt;COFINSNT&gt;

&lt;CST&gt;06&lt;/CST&gt;

&lt;/COFINSNT&gt;

## 6) Grupo de Valores Totais da NF-e

Valor Total do ICMS:

&lt;ICMSTot&gt;

&lt;vBC&gt;0.00&lt;/vBC&gt;

&lt;vICMS&gt;0.00&lt;/vICMS&gt;

&lt;vProd&gt;1000.00&lt;/vProd&gt;

&lt;vDesc&gt;256.00&lt;/vDesc&gt;

&lt;vIPI&gt;0.00&lt;/vIPI&gt;

&lt;vPIS&gt;0.00&lt;/vPIS&gt;

&lt;vCOFINS&gt;0.00&lt;/vCOFINS&gt;

&lt;vNF&gt;744.00&lt;/vNF&gt;

&lt;/ICMSTot&gt;

![Image](assets/image_000021_fc631bb6d7d2cf5321fd8158724b1aab00e848b70bdc0dc428d21ef23f483f54.png)

## 7) Grupo de Informações Adicionais

Informações Adicionais de Interesse do Fisco:

'Remessa para Zona Franca de Manaus ou Área de Livre Comércio. Isenção de ICMS (Convênio ICMS 65/88). Isenção de IPI (Art. 81 do RIPI - Decreto 7.212 de 15 de junho de 2010). Redução a zero das alíquotas do PIS e COFINS (art. 2º da Lei 10.996, de 15/12/2004)'

## 9.  Novas Mensagens de Rejeição

|   CÓDIGO | MOTIVOS DE NÃO ATENDIMENTO DA SOLICITAÇÃO                                          |
|----------|------------------------------------------------------------------------------------|
|      597 | Rejeição: CFOP de Importação e não informado dados de IPI                          |
|      599 | Rejeição: CFOP de Importação e não informado dados de II                           |
|      601 | Rejeição: Total do II difere do somatório dos itens                                |
|      602 | Rejeição: Total do PIS difere do somatório dos iten s sujeitos ao ICMS             |
|      603 | Rejeição: Total do COFINS difere do somatório dos i tens sujeitos ao ICMS          |
|      604 | Rejeição: Total do vOutro difere do somatório dos i tens                           |
|      605 | Rejeição: Total do vServ difere do somatório do vPr od dos itens sujeitos ao ISSQN |
|      606 | Rejeição: Total do vBC do ISS difere do somatório d os itens                       |
|      607 | Rejeição: Total do ISS difere do somatório dos iten s                              |
|      608 | Rejeição: Total do PIS difere do somatório dos iten s sujeitos ao ISSQN            |
|      609 | Rejeição: Total do COFINS difere do somatório dos i tens sujeitos ao ISSQN         |
|      610 | Rejeição: Total da NF difere do somatório dos Valor es compõe o valor Total da NF. |
|      611 | Rejeição: cEAN inválido                                                            |
|      612 | Rejeição: cEANTrib inválido                                                        |
|      613 | Rejeição: Chave de Acesso difere da existente em BD [9999999999999999999999999999] |
|      614 | Rejeição: Chave de Acesso inválida (Código UF i nválido)                           |
|      615 | Rejeição: Chave de Acesso inválida (Ano < 05 ouAno maior que Ano corrente)         |
|      616 | Rejeição: Chave de Acesso inválida (Mês < 1 ouMês > 12)                            |
|      617 | Rejeição: Chave de Acesso inválida (CNPJ zeradoou dígito inválido)                 |

![Image](assets/image_000022_fc631bb6d7d2cf5321fd8158724b1aab00e848b70bdc0dc428d21ef23f483f54.png)

|   CÓDIGO | MOTIVOS DE NÃO ATENDIMENTO DA SOLICITAÇÃO                                                             |
|----------|-------------------------------------------------------------------------------------------------------|
|      618 | Rejeição: Chave de Acesso inválida (modelo dife rente de 55)                                          |
|      619 | Rejeição: Chave de Acesso inválida (número NF = 0)                                                    |
|      621 | Rejeição: CPF Emitente não cadastrado                                                                 |
|      622 | Rejeição: IE emitente não vinculada ao CPF                                                            |
|      623 | Rejeição: CPF Destinatário não cadastrado                                                             |
|      624 | Rejeição: IE Destinatário não vinculada ao CPF                                                        |
|      625 | Rejeição: Inscrição SUFRAMA deve ser informada na v enda com isenção para ZFM                         |
|      626 | Rejeição: O CFOP de operação isenta para ZFM deve s er 6109 ou 6110                                   |
|      627 | Rejeição: O valor do ICMS desonerado deve ser informado                                               |
|      628 | Rejeição: Total da NF superior ao valor limite esta belecido pela SEFAZ [Limite]                      |
|      629 | Rejeição: Valor do Produto difere do produto Valor Unitário de Comercialização e Quantidade Comercial |
|      630 | Rejeição: Valor do Produto difere do produto Valor Unitário de Tributação e Quantidade Tributável     |
|      635 | Rejeição: NF-e com mesmo número e série já transmit ida e aguardando processamento                    |

## 10. Acréscimo / Alteração de Texto da coluna observação  do leiaute da NF-e

| I - Produtos e Serviços da NF-e   | I - Produtos e Serviços da NF-e   | I - Produtos e Serviços da NF-e   | I - Produtos e Serviços da NF-e                      | I - Produtos e Serviços da NF-e   | I - Produtos e Serviços da NF-e   | I - Produtos e Serviços da NF-e   | I - Produtos e Serviços da NF-e   | I - Produtos e Serviços da NF-e   | I - Produtos e Serviços da NF-e   | I - Produtos e Serviços da NF-e                                                        |
|-----------------------------------|-----------------------------------|-----------------------------------|------------------------------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|----------------------------------------------------------------------------------------|
| #                                 | ID                                | Campo                             | Descrição                                            | Ele                               | Pai                               | Tipo                              | Ocorrência                        | tamanho                           | Dec                               | Observação                                                                             |
| 100                               | I01                               | prod                              | Grupo do detalhamento de Produtos e Serviços da NF-e | G                                 | H01                               |                                   | 1-1                               |                                   |                                   |                                                                                        |
| (...)                             |                                   |                                   |                                                      |                                   |                                   |                                   |                                   |                                   |                                   |                                                                                        |
| 116                               | I17                               | vDesc                             | Valor do Desconto                                    | E                                 | I01                               | N                                 | 0-1                               | 15                                | 2                                 | Informar os valores de Descontos e Abatimentos que tem reflexo no valor da NF (id:W16) |
| 116a                              | I17a                              | vOutro                            | Outras despesas acessórias                           | E                                 | I01                               | N                                 | 0-1                               | 15                                | 2                                 | Informar os valores do item que devem compor o valor da NF                             |

![Image](assets/image_000023_a3c13257e9af21dea56ae6054d798d3a3db7a86299a9d841b4f5a2e1f00256a9.png)

| Nota Fiscal Eletrônica   | NT 2011/004   |
|--------------------------|---------------|

| (id:W16) mas não tenham campo de total correspondente no grupo ICMSTot (id:W02) (Ex.: vPIS retido por ST (id:R06), vCOFINS retido por ST (id:T06), vIOF (id:P05), vDespAdu (id:P03), etc.)   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| R - PIS ST   | R - PIS ST   | R - PIS ST   | R - PIS ST                           | R - PIS ST   | R - PIS ST   | R - PIS ST   | R - PIS ST   | R - PIS ST   | R - PIS ST   | R - PIS ST                                             |
|--------------|--------------|--------------|--------------------------------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------------------------------------------------|
| #            | ID           | Campo        | Descrição                            | Ele          | Pai          | Tipo         | Ocorrência   | tamanho      | Dec          | Observação                                             |
| 287          | R01          | PISST        | Grupo de PIS Substituição Tributária | G            | M01          |              | 0-1          |              |              | Informar quando o CST do PIS = 05                      |
| (...)        |              |              |                                      |              |              |              |              |              |              |                                                        |
| 292          | R06          | vPIS         | Valor do PIS                         | E            | R01          | N            | 1-1          | 15           | 2            | O vPIS retido deve ser totalizado em vOutro (id: I17a) |

| T - COFINS ST   | T - COFINS ST   | T - COFINS ST   | T - COFINS ST                           | T - COFINS ST   | T - COFINS ST   | T - COFINS ST   | T - COFINS ST   | T - COFINS ST   | T - COFINS ST   | T - COFINS ST                                             |
|-----------------|-----------------|-----------------|-----------------------------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------------------------------------------------|
| #               | ID              | Campo           | Descrição                               | Ele             | Pai             | Tipo            | Ocorrência      | tamanho         | Dec             | Observação                                                |
| 313             | T01             | COFINSST        | Grupo de COFINS Substituição Tributária | G               | M01             |                 | 0-1             |                 |                 | Informar quando o CST do COFINS = 05                      |
| (...)           |                 |                 |                                         |                 |                 |                 |                 |                 |                 |                                                           |
| 318             | T06             | vCOFINS         | Valor da COFINS                         | E               | T01             | N               | 1-1             | 15              | 2               | O vCOFINS retido deve ser totalizado em vOutro (id: I17a) |

| W-Valores Totais da NF-e   | W-Valores Totais da NF-e   | W-Valores Totais da NF-e   | W-Valores Totais da NF-e        | W-Valores Totais da NF-e   | W-Valores Totais da NF-e   | W-Valores Totais da NF-e   | W-Valores Totais da NF-e   | W-Valores Totais da NF-e   | W-Valores Totais da NF-e   | W-Valores Totais da NF-e                                                       |
|----------------------------|----------------------------|----------------------------|---------------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|--------------------------------------------------------------------------------|
| #                          | ID                         | Campo                      | Descrição                       | Ele                        | Pai                        | Tipo                       | Ocorrência                 | tamanho                    | Dec                        | Observação                                                                     |
| 326                        | W01                        | total                      | Grupo de Valores Totais da NF-e | G                          | A01                        |                            | 1-1                        |                            |                            | O grupo de valores totais da NF- e deve ser informado com o somatório do campo |

![Image](assets/image_000024_480f1e110f277b96e1d2411d017610051027f8bd104912ff759438b9cca06118.png)

|     |     |         |                                            |    |     |    |      |    |    | correspondete do item da NF-e                                                                                                    |
|-----|-----|---------|--------------------------------------------|----|-----|----|------|----|----|----------------------------------------------------------------------------------------------------------------------------------|
| 327 | W02 | ICMSTot | Grupo de Valores Totais referentes ao ICMS | G  | W01 |    | 1-1  |    |    | Este grupo deve ser informado com informações dos itens da NF-e que não são sujeitos ao ISSQN                                    |
| 328 | W03 | vBC     | Base de Cálculo do ICMS                    | E  | W02 | N  | 1-1  | 15 |  2 | Informar o somatório do campo vBC de item produto com CST (id:N12) =00, 10, 20, 30, 70 e 90 e CSOSN (id:N12a) = 900.             |
| 329 | W04 | vICMS   | Valor Total do ICMS                        | E  | W02 | N  | 1-1  | 15 |  2 | Informar o somatório do campo vICMS de item produto com CST (id:N12) =00, 10, 20, 30, 70 e 90 e CSOSN (id:N12a)= 900.            |
| 330 | W05 | vBCST   | Base de Cálculo do ICMS ST                 | E  | W02 | N  | 1- 1 | 15 |  2 | Informar o somatório do campo vBCST de item produto com CST (id:N12) =10, 30, 70 e 90 e CSOSN (id:N12a) = 201, 202, 203 e 900.   |
| 331 | W06 | vST     | Valor Total do ICMS ST                     | E  | W02 | N  | 1-1  | 15 |  2 | Informar o somatório do campo vICMSST (id:N23) de item com CST (id:N12) =10, 30, 70 e 90 e CSOSN (id:N12a)= 201, 202, 203 e 900. |
| 332 | W07 | vProd   | Valor Total dos produtos e serviços        | E  | W02 | N  | 1-1  | 15 |  2 | Informar o somatório do campo vProd (id:I11) de item sujeito ao ICMS e indTot (id:I17b) =1.                                      |
| 333 | W08 | vFrete  | Valor Total do Frete                       | E  | W02 | N  | 1-1  | 15 |  2 | Informar o somatório do campo vFrete (id:S15).                                                                                   |
| 334 | W09 | vSeg    | Valor Total do Seguro                      | E  | W02 | N  | 1-1  | 15 |  2 | Informar o somatório do campo                                                                                                    |

![Image](assets/image_000025_1719b3f112bd7bbffc498edd8e7e2a1cd08eb241358c9a6826aeea078134f171.png)

|     |     |          |                                                    |    |     |    |     |    |    | vSeg (id:I16).                                                                                                                                                                      |
|-----|-----|----------|----------------------------------------------------|----|-----|----|-----|----|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 335 | W10 | vDesc    | Valor Total do Desconto                            | E  | W02 | N  | 1-1 | 15 |  2 | Informar o somatório do campo vDesc (id:I17).                                                                                                                                       |
| 336 | W11 | vII      | Valor Total do II                                  | E  | W02 | N  | 1-1 | 15 |  2 | Informar o somatório do campo vII (id:P04).                                                                                                                                         |
| 337 | W12 | vIPI     | Valor Total do IPI                                 | E  | W02 | N  | 1-1 | 15 |  2 | Informar o somatório do campo vIPI (id:O14).                                                                                                                                        |
| 338 | W13 | vPIS     | Valor do PIS                                       | E  | W02 | N  | 1-1 | 15 |  2 | Informar o somatório do campo vPIS (id:Q09)de item sujeito ao ICMS.                                                                                                                 |
| 339 | W14 | vCOFINS  | Valor do COFINS                                    | E  | W02 | N  | 1-1 | 15 |  2 | Informar o somatório do campo vCOFINS (id:S11) de item sujeito ao ICMS.                                                                                                             |
| 340 | W15 | vOutro   | Outras Despesas acessórias                         | E  | W02 | N  | 1-1 | 15 |  2 | Informar o somatório do campo vOutro (id:I17a).                                                                                                                                     |
| 341 | W16 | vNF      | Valor Total da NF-e                                | E  | W02 | N  | 1-1 | 15 |  2 | (+) vProd (id:W07) (-) vDesc (id:W10) (+) vST (id:W06) (+) vFrete (id:W08) (+) vSeg (id:W09) (+) vOutro (id:W15) (+) vII (id:W11) (+) vIPI (id:W12) (+) vServ (id:W18) (NT2011/004) |
| 342 | W17 | ISSQNtot | Grupo de Valores Totais referentes ao ISSQN        | G  | W01 |    | 0-1 |    |    | Este grupo deve ser informado com informações dos itens da NF-e sujeitos ao ISSQN                                                                                                   |
| 343 | W18 | vServ    | Valor Total dos Serviços sob não-incidência ou não | E  | W17 | N  | 0-1 | 15 |  2 | Informar o somatório do campo vProd (id:I11) de item sujeito ao                                                                                                                     |

![Image](assets/image_000026_1719b3f112bd7bbffc498edd8e7e2a1cd08eb241358c9a6826aeea078134f171.png)

|     |     |         | tributados pelo ICMS           |    |     |    |     |    |    | ISSQN.                                                                   |
|-----|-----|---------|--------------------------------|----|-----|----|-----|----|----|--------------------------------------------------------------------------|
| 344 | W19 | vBC     | Base de Cálculo do ISS         | E  | W17 | N  | 0-1 | 15 |  2 | Informar o somatório do campo vBC (id:U02) do ISSQN.                     |
| 345 | W20 | vISS    | Valor Total do ISS             | E  | W17 | N  | 0-1 | 15 |  2 | Informar o somatório do campo vISSQN (id:U04).                           |
| 346 | W21 | vPIS    | Valor do PIS sobre serviços    | E  | W17 | N  | 0-1 | 15 |  2 | Informar o somatório do campo vPIS (id:Q09) de item sujeito ao ISSQN.    |
| 347 | W22 | vCOFINS | Valor do COFINS sobre serviços | E  | W17 | N  | 0-1 | 15 |  2 | Informar o somatório do campo vCOFINS (id:S11) de item sujeito ao ISSQN. |

## 11. Correção de Texto do Manual de Integração

- Item 3.2.1 -b:

Adotar o mesmo texto do Manual de Eventos como segue: 'O documento XML deverá ter uma única declaração de namespace no elemento raiz do documento com o seguinte padrã o: ...'

- Item 4.1.9 - d, linha GE17.1, coluna 'RV' : Trocar texto para:

Se não é Operação com Exterior (UF Destinatário dif ere de 'EX'):

. Se IE Destinatário informada e difere de 'ISENTO'

- IE inválida para a UF: erro no ...
- Item 4.1.9 - d, linha GX07.1, coluna 'RV' : Trocar texto para:

IE do Transportador informada e diferente de 'ISENTO':

- Validar IE, conforme a UF do transportador informada.
- Item 4.3.6: trocar para '... e versaoDados, rejeitando a mensagem recebida em caso de ...';
- Item 4.4.6: trocar para '... e versaoDados, rejeitando a mensagem recebida em caso de ...';
- Item 4.5.1, linha EP01, coluna 'Campo': trocar para 'con s SitNFe';
- Item 4.5.2, linha ER08, coluna 'Ele': trocar para 'G';
- Item 4.5.2, linha ER09, coluna 'Ele': trocar para 'G';
- Item 4.5.6: trocar para '... e versaoDados, rejeitando a mensagem recebida em caso de ...';
- Item 4.6.6: trocar para '... e versaoDados, rejeitando a mensagem recebida em caso de ...';
- Item 4.7.1, linha GP01, coluna 'Campo': trocar para 'ConsCad';
- Item 5.1: trocar para '... de cada Web Se r vice existente.';

![Image](assets/image_000027_fc631bb6d7d2cf5321fd8158724b1aab00e848b70bdc0dc428d21ef23f483f54.png)

- Item 5.6: tabela - trocar de 'órgão gerador' para 'Tipo Auto rizador';
- Item 5.6: trocar para '1 posição para indicar o Tipo Autorizador (1-Secretaria de ....)'; - Anexo I - Layout da NF-e -Linha 24f, coluna Observação : Informar o CPF do emitente da NF de produtor ou 'ISENTO' (v2.0); - Linha 24i, coluna 'Ele' : Trocar para 'CE'; - Linha 24j, coluna 'Ele' : Trocar para 'CG'; - Linha 26, coluna 'Observação' : incluir: 6 - Contingência SVC-AN, emissão em contingência na SEFAZ Virtual do Ambiente Nacional; 7 - Contingência SVC-RS, emissão em contingência na SEFAZ Virtual do RS; - Linha 29d, coluna 'Tam.' : trocar para '15-256'; - Linha 46, coluna 'Tam.' : trocar para '2-14'; - Linha 100, coluna 'Descrição' : trocar para 'Grupo do detalhamento de Produtos e ...'; - Linha 102, coluna 'Tipo' : trocar para 'N'; - Linha 104, coluna 'Tipo' : trocar para 'N'; - Linha 105, coluna 'Tipo' : trocar para 'N'; - Linha 111, coluna 'Tipo' : trocar para 'N'; - Linha 116b, coluna 'Dec.' : trocar para ''; - Linha 117, coluna 'Descrição' : trocar para 'Declaração de Importação'; - Linha 162a, coluna 'Ele' : trocar para 'CG'; - Linha 162e, coluna 'Tipo' : trocar para 'C'; - Linha 162g, coluna 'Campo' : trocar para 'qBC P rod'; - Linha 164, coluna 'Observação' : trocar para '... N10b, N10c, N10d, N10e, N10f, N10g ou N10h com base no ...'; - Linha 204.01, coluna 'Pai' : trocar para 'N06'; - Linha 204.02, coluna 'Pai' : trocar para 'N06'; - Linha 245.01, coluna 'Descrição' : trocar para 'Grupo de partilha do ICMS entre ...'; - Linha 245.17, coluna 'Descrição' : trocar para 'Grupo de repasse do ICMS-ST retido anteriormente entre ...'; - Linha 245.25, coluna 'Campo' : trocar para ' o rig'; (idem para as linhas 245.25, 245.28, 245.39, 245.48, 245.53, - Linha 245.52, coluna 'Descrição' : trocar para 'Grupo CRT=1 - Simples Nacional ...'; - Linha 245.54, coluna 'Tam.' : trocar para '3'; - Linha 245.54, coluna 'Descrição' : trocar para '... 900 - Outros'; - Linha 253, coluna 'Tipo' : trocar para 'N'; - Linha 275, coluna 'Dec.' : trocar para '0-4'; (idem para as demais linhas com 4 casas decimais); - Anexo X - Manual de Contingência: - Item 4.1.2, linha AP04, coluna 'Tam.': trocar para '18'; - Item 8.5.3, linha AR04, coluna 'Tam.': trocar para '21';

![Image](assets/image_000028_fc631bb6d7d2cf5321fd8158724b1aab00e848b70bdc0dc428d21ef23f483f54.png)

- Item 8.5.9 - d, linha F04: eliminar a validação;
- Item 8.6.9 - b, linha H05, coluna RV: eliminar texto 'vide Anexo I -';
- Item 4.2: trocar para '... ser consultada pelo número de Reg istro de DPEC ...';
- Item 8.6.10: eliminar texto 'vide Anexo I -';
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2011-004/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2011-004/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2011-004.md)
- [Proveniência resumida](../../../../sources/provenance/nt2011-004.json)


## Documentos relacionados

- [[nota-t-cnica-2011-001-publicada-em-25-02-2011]]
- [[nota-t-cnica-2011-005-publicada-em-21-10-2011]]
- [[nota-t-cnica-2011-007-publicada-em-26-12-2011]]
