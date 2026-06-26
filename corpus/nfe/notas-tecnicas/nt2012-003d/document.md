---
title: "Projeto Nota Fiscal Eletrônica Projeto Nota Fiscal Eletrônica Projeto Nota Fiscal Eletrônica"
slug: "nt2012-003d"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "a245cdb984ac5391fcdb6b7e00f71d572116cbc516ba4b12ebbe04f9ef81c1eb"
converted_at_utc: "2026-06-25T15:00:15.457939+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_aa151bc9da2012b094d92ac97e3228b7b994832df46da807a7b6a96ce390c3b0.png)

## Projeto Nota Fiscal Eletrônica Projeto Nota Fiscal Eletrônica Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_292b97ccec90f5b8ec4880199262b9865ff6ad522930ad4abc62169b042a2e2d.png)

## Nota Técnica Nota Técnica  2012/003

Divulga novas regras para as NF atualização do Schema XML, novas regras de validação. Divulga novas regras para as NF-e de Combustível, atualização do Schema XML, novas regras de validação. e de Combustível, atualização do Schema XML,

![Image](assets/image_000002_ca331348782115c47a4036f0fcbb194dc2aabebe47eefe3d5a2a1e142598324e.png)

Versão 1.00d Agosto 2012

![Image](assets/image_000003_f032ab1fa4b35e1d95fd8804366c0492ec346d2ee5567b680dc524834ad8b36c.png)

## 01. Resumo

Esta edição divulga atualização do Schema da NF-e e  de novas regras de validação.

Prazo para entrada em vigência das alterações:

- Ambiente de Homologação (ambiente de teste das empresas): 01/10/12;
- Ambiente de Produção : 19/11/12.

![Image](assets/image_000004_83c87a20a04a0545c1239f60e003c8c5930e463ef8f9f937ac72c1943567b6b0.png)

## 02. Alteração de Schema XML da NF-e

As alterações documentadas trazem algum melhorament o no Schema XML, mas não alteram o leiaute atual da  NF-e. Portanto, é esperado que a grande parte das empresas não seja afetada pela mud ança no Schema.

## 02.1 e-mail do destinatário (E19)

Mudança no Schema XML para impedir o preenchimento com caractere branco no final do campo.

## 02.2 NFref (B12a) - Redução da quantidade máxima de  ocorrências

| #   | ID   | Campo   | Descrição                                    | Ele Pai Tipo Ocor. Tam. Dec. Observação   |
|-----|------|---------|----------------------------------------------|-------------------------------------------|
| 16a | B12a | NFref   | Grupo de informação das NF/NF-e G B01 0-5000 | (NT 2012.003)                             |

## 02.3 vol (X26) - Redução da quantidade máxima de oc orrências

|   # | ID Campo   | Descrição     | Ele Pai Tipo Ocor. Tam. Dec. Observação   | Ele Pai Tipo Ocor. Tam. Dec. Observação   | Ele Pai Tipo Ocor. Tam. Dec. Observação   |
|-----|------------|---------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| 381 | X26 vol    | Grupo Volumes | G X01                                     | 0-5000                                    | (NT 2012.003)                             |

## 02.4 lacres (X33) - Redução da quantidade máxima de  ocorrências

| #    | ID         | Campo           | Descrição Ele Pai Tipo Ocor. Tam. Dec. Observação   |
|------|------------|-----------------|-----------------------------------------------------|
| 387a | X33 lacres | Grupo de Lacres | G X26 0-5000 (NT 2012.003)                          |

## 02.5 procRef (Z10) - Redução da quantidade máxima d e ocorrências

| #    | ID Campo    | Descrição                            | Ele Pai Tipo Ocor. Tam. Dec. Observação   |
|------|-------------|--------------------------------------|-------------------------------------------|
| 401g | Z10 procRef | Grupo do processo referenciado G Z01 | 0-100 (NT 2012.003)                       |

![Image](assets/image_000005_83c87a20a04a0545c1239f60e003c8c5930e463ef8f9f937ac72c1943567b6b0.png)

## 02.6 qVol (X27) - Campo obrigatório, se informado o grupo 'vol' (*1)

O  grupo  de  informação  sobre  'volumes  transportados'   é  opcional,  mas,  se  este  grupo  de  informações  constar  no  XML,  deverá  ser  informada  a Quantidade de Volumes transportados.

|   # | ID   | Campo   | Descrição                   | Ele Pai Tipo Ocor. Tam.   |     |    |     |      | Dec.   | Observação    |
|-----|------|---------|-----------------------------|---------------------------|-----|----|-----|------|--------|---------------|
| 382 | X27  | qVol    | Quantidade de transportados | volumes E                 | X26 | N  | 1-1 | 1-15 |        | (NT 2012.003) |

## 02.7 vDup (Y10) - Campo obrigatório, se informado o grupo 'dup'

O grupo de informação sobre 'duplicatas' é opcional, mas, se este grupo de informações constar no XML,  deverá ser informado o Valor da Duplicata.

|   # | ID       | Campo              | Descrição        | Ele Pai Tipo Ocor. Tam. Dec. Observação   |
|-----|----------|--------------------|------------------|-------------------------------------------|
| 398 | Y10 vDup | Valor da duplicata | E Y07 N 1-1 15 2 | (NT 2012.003)                             |

## 02.8 cProdANP (L102) - Valores tabelas para o Código do Combustível da ANP

Os valores possíveis para o Código do Produto de co mbustível passam a constar no Schema, seguindo a co dificação nacional da ANP, disponível em sua página na Internet ( http://www.anp.gov.br/simp). Eliminada a possibilidade da informação do códig o '999999999'. Alguns exemplos de Códigos possíveis são os relacionados no item 9.2 desta NT.

| #    | ID   | Campo    | Descrição                | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Dec.   | Observação                                                                                                                                  |
|------|------|----------|--------------------------|-------|-------|--------|---------|--------|--------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 162b | L102 | cProdANP | Código de produto da ANP | CE    | L101  | N      | 1-1     |      9 |        | Utilizar a codificação de produtos do Sistema de Informações de Movimentação de produtos - SIMP (http://www.anp.gov.br/simp). (NT 2102/003) |

![Image](assets/image_000006_a612254256487620210007e236beec685214465d7d9bba737756632ff54f4fc6.png)

## 03. Regras de Validação da NF-e (item 4.1.9.4 do Ma nual)

## 03.1 Operações com Combustível

Nas operações com CFOP de combustível será obrigató ria a informação do grupo específico no layout da NF-e (grupo 'comb', id:L101).

| #     | Campo   | Regra de validação                                                                                                                                                                                                                                                                                                                                                                                                                                           | Aplic.                                                      |   Msg | Efeito Descrição Erro                                                           |
|-------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|-------|---------------------------------------------------------------------------------|
| GL101 | L101    | Obrigatória a informação do grupo de combustível para CFOP: 1.651, 1.652, 1.653, 1.658, 1.659, 1.660, 1.662, 1.663, 1.664, 2.651, 2.652, 2.653, 2.658, 2.660, 2.661, 2.662, 2.663, 2.664, 3.651, 3.652, 5.651, 5.652, 5.653, 5.654, 5.655, 5.656, 5.657, 5.659, 5.660, 5.661, 5.662, 5.663, 5.664, 5.665, 5.667, 6.651, 6.652, 6.653, 6.654, 6.655, 6.656, 6.658, 6.659, 6.660, 6.661, 6.662, 6.663, 6.664, 6.666, 6.667, 7.651, 7.654, 7.667. (NT 2012.003) | os 1.661, 2.659, 3.653, 5.658, 5.666, 6.657, 6.665, Facult. |   660 | Rej. Rejeição: CFOP de Combustível e não informado grupo de combustível da NF-e |

## 03.2 Operação Incentivada com a Suframa

Alteradas as regras de validação nas operações ince ntivadas com a Suframa, conforme segue:

| #      | Campo   | Regra de validação                                                                                                                                                                  | Aplic.   |   Msg | Efeito   | Descrição Erro                                                               |
|--------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------------------|
| GN28   | N28     | Se informado motDesICMS = 7 ISUF (id:E18) deve ser informado (NT 2011/004) Exceção: Não exigir a Inscrição Suframa se informado CFOP de entrada (inicia por 1 ou 2) - (NT 2012.003) | Facult.  |   625 | Rej.     | Rejeição: Inscrição SUFRAMA deve ser informada na venda com isenção para ZFM |
| GN28.1 | N28     | Se informado motDesICMS = 7 - deve ser informado CFOP: 1203, 1204, 1208, 1209, 2203, 2204, 2208, 2209, 5109, 5110, 5151, 5152, 6109, 6110, 6151, 6152, 6122 e 6123 (NT 2012.003)    | Facult.  |   626 | Rej.     | Rejeição: CFOP de operação isenta para ZFM d iferente do previsto            |

Nota: Alterada a descrição do erro 626, conforme do cumentado.

![Image](assets/image_000007_c8e555861670a9f42c549b61e6581f0776317093dfcc9acb2d9cf66db45f6e76.png)

## 03.3 Prazo para Recepção de NF-e emitida em conting ência

As NF-e emitidas em contingência devem ser transmit ida para a SEFAZ logo após a cessação dos problemas  técnicos que impediam a transmissão da NF-e de forma normal, respeitando o prazo máximo de finido em legislação.

Durante um período de tempo, será aceita a recepção  de NF-e da versão 2.0, emitida originalmente em co ntingência, em Formulário de Segurança ou DPEC, independentemente da data de emissão da NF-e.  Será informado um código de retorno diferente para  estes casos, conforme segue:

- cStat = 100 - Autorizado o uso da NF-e;
- cStat = 150 - Autorizado o uso da NF-e, autorizaçã o concedida fora de prazo.

Alterada a regra de validação, conforme segue:

| #      | Campo   | Regra de validação                                                                                                                          | Aplic.   | Msg Efeito   | Descrição Erro                           |
|--------|---------|---------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------|------------------------------------------|
| GB09.1 | B09     | Se Tipo de Emissão = 1-Normal ou 3-SCAN (NT 2012.003): - Data de Emissão ocorrida há mais de 30 dias (ou out ro limite definido pela SEFAZ) | Obrig.   | 228 Rej.     | Rejeição: Data de Emissão muito atrasada |

## 03.4 Validação do CPF

Não deverá ser aceito o CPF preenchido com o mesmo  algarismo repetido (111..., 222..., 333..., ..., 999...).

| #       | Campo   | Regra de validação                                                                                                          | Aplic.   |   Msg | Efeito   | Descrição Erro                                          |
|---------|---------|-----------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------|
| GB20e   | B20e    | Se informada a TAG de NF Referenciada de produtor: - CPF com zeros, nulo, 111..., 222..., ..., ou DV inválido (NT 2012.003) | Facult.  |   550 | Rej.     | Rejeição: CPF da NF referenciada de produtor i nválido. |
| GC02a.1 | C02a    | - CPF do Remetente de NF-e Avulsa com zeros, nulo, 111..., 222..., ..., ou DV inválido (NT 2012.003)                        | Obrig.   |   401 | Rej.     | Rejeição: CPF do remetente inválido                     |
| GE03    | E03     | Se informada a TAG CPF: - CPF com zeros, nulo, 111..., 222..., ..., ou DV inválido (NT 2012.003)                            | Obrig.   |   237 | Rej.     | Rejeição: CPF do destinatário inválido                  |
| GF02a   | F02a    | Se informada a TAG CPF: - CPF com zeros, nulo, 111..., 222..., ..., ou DV inválido (NT 2012.003)                            | Facult.  |   540 | Rej.     | Rejeição: CPF do Local de Retirada inválido             |
| GG02a   | G02a    | Se informada a TAG CPF: - CPF com zeros, nulo, 111..., 222..., ..., ou DV inválido (NT 2012.003)                            | Facult.  |   541 | Rej.     | Rejeição: CPF do Local de Entrega inválido              |

![Image](assets/image_000008_83c87a20a04a0545c1239f60e003c8c5930e463ef8f9f937ac72c1943567b6b0.png)

| GX05   | X05   | Se informado CPF do transportador: - CPF com zeros, nulo, 111..., 222..., ..., ou DV inválido (NT 2012.003)   | Obrig.   | 543   | Rej.   | Rejeição: CPF do Transportador inválido   |
|--------|-------|---------------------------------------------------------------------------------------------------------------|----------|-------|--------|-------------------------------------------|

## 03.5 Validação dos Campos de Total da NF-e

Atualmente é aceita uma tolerância de R$ 1,00 na co nferência dos valores totais da NF-e (regras de val idação GW03 a GW22).

Alterada a tolerância para R$ 0,50, compatibilizando este parâmetro com o praticado na Escrituração Fi scal Digital (EFD).

Alterado o Manual do Contribuinte, no final do item '4.1.9.4 - Validação de regras de negócios da NF-e ', conforme segue:

'(*3)  Considerar uma tolerância de R$ 0,50 para mais ou para menos. (NT 2012.003)'

## 03.6 NF-e da Versão 1.10

Durante um tempo o Serviço de Autorização aceitava  NF-e emitidas na versão 1.10 e na versão 2.00. Atua lmente somente são aceitas NF-e na versão 2.00 e as NF-e com versão anterior são rejeitadas c om o erro '239- Versão do arquivo XML não suportada '.

Eliminada as regras de validação que seguem:

| #       | Campo   | Regra de validação                                                                                          | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                       |
|---------|---------|-------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------------------|
| GB09.02 | B09     | Se versão = '1.10' - Data de Emissão posterior à 31/03/2011 (NT 201 1.002)                                  | Obrig.   |   595 | Rej.     | Rejeição: A versão do leiaute da NF- e utilizada não é mais válida                   |
| GB09.03 |         | Se versão = '1.10': - Data de Recepção posterior à 31/03/2011 e tpAmb (B24) = 2 - homologação (NT 2011.002) | Obrig.   |   596 | Rej.     | Rejeição: Ambiente de homologação indisponível para recepção de NF-e da versão 1.10. |

![Image](assets/image_000009_a612254256487620210007e236beec685214465d7d9bba737756632ff54f4fc6.png)

## 04. Regras de Validação - Todos os Web services

## 04.1 Namespace Indevido

Na especificação de todos os Web services existe uma regra de validação específica para verificar a existência de qualquer namespace diverso do namespace padrão da NF-e ( http://www.portalfiscal.inf.br/nfe ). No caso de um namespace diferente, a mensagem recebida é rejeitada com o e rro: '587-Rejeição: Usar somente o namespace padrão da NF-e' (validação #:D01d).

Observado que alguns ambientes de autorização ainda  não implementaram esta rejeição, aceitando NF-e co m namespaces diversos do namespace padrão da NF-e. Todas as SEFAZ Autorizadoras deverã o passar a implementar esta validação de forma comp leta para todos os Web services .

Reforçada a aplicação da regra de validação para to dos os Web services :

| Validação da área de dados da mensagem   | Validação da área de dados da mensagem                                                                                | Validação da área de dados da mensagem   | Validação da área de dados da mensagem   | Validação da área de dados da mensagem   |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|
| #                                        | Regra de Validação                                                                                                    | Aplic.                                   | Msg                                      | Efeito                                   |
| D01d                                     | Verifica a existência de qualquer namespace diverso do namespace padrão da NF-e (http://www.portalfiscal.inf.br/nfe ) | Obrig.                                   | 587                                      | Rej.                                     |

## 04.2 Consumo Indevido

Observado um comportamento indevido da aplicação de  algumas empresas no consumo dos diferentes Web services do Serviço de Autorização da NF-e. Seguem alguns exemplos de 'Consumo Indevido' dos Web services existentes:

| Web service                | Aplicação da empresa                                                                                                                                                                          |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Envio de Lote de NF-e      | Aplicação da empresa em 'loop ' enviando o mesmo Lote de NF-e rejeitado por erro de Schema, ou em 'loop' com NF-e rejeitada por um erro específico.                                           |
| Consulta Resultado do Lote | Aplicação da empresa efe tua 'loop' consultando os números de Recibo de Lote em se quência, mesmo para Número Recibo que não foram gerados para sua empresa.                                  |
| Cancelamento de NF-e       | Aplicação da empresa em 'loop' enviando o mesmo Pedido de Cancelamento, que sempre é rejeitado.                                                                                               |
| Inutilização de Numeração  | Idem para o Pedido de Inu tilização de Numeração.                                                                                                                                             |
| Consulta Situação da NF-e  | Algumas empresas utilizam esta consulta para verificar a disponibilidade dos serviços da SEFAZ Autorizadora, consultando a mesma Chave de Acesso, em 'loop'.                                  |
|                            | Algumas empresas mantém em 'loop' uma consulta as Chaves de Acesso de NF-e destinadas para sua empresa. Em alguns casos, fica sendo consultada uma Chave de Acesso inexistente durante meses. |
| Consulta Status Serviço    | Aplicação em 'loop' consumindo o Web service em uma frequência maior do que a prevista.                                                                                                       |

![Image](assets/image_000010_a612254256487620210007e236beec685214465d7d9bba737756632ff54f4fc6.png)

A critério da SEFAZ Autorizadora, as mensagens com  erro poderão ser rejeitadas com o erro '656-Rejeiçã o: Consumo indevido', independentemente de outras medidas saneadoras do erro detectado.

| Validação da s Regras de Negócio   | Validação da s Regras de Negócio              | Validação da s Regras de Negócio   | Validação da s Regras de Negócio   | Validação da s Regras de Negócio   |
|------------------------------------|-----------------------------------------------|------------------------------------|------------------------------------|------------------------------------|
| #                                  | Regra de Validação                            | Aplic.                             | Msg                                | Efeito                             |
|                                    | Verificação de Consumo Indevido (NT 2012.003) | Facult.                            | 656                                | Rej.                               |

## 05. Cancelamento de NF-e (item 4.3 do Manual)

## 05.1 Final do Processamento (item 4.3.8 do Manual)

O prazo do cancelamento da NF-e definido no Manual a princípio é de 1 dia, considerando também a exceç ão de prazo definida na legislação estadual.

A SEFAZ autorizadora poderá aceitar o cancelamento  fora de prazo, mantendo um código de retorno diferente para estes casos, conforme segue:

- cStat = 151 - Cancelamento de NF-e homologado fora de prazo.
- cStat = 101 - Cancelamento de NF-e homologado;

## Nota:

O  mesmo  procedimento  se  aplica  para  o Web Service de  'Evento  de  Cancelamento'.  Para  o  Web  Service  de  Evento,  no  caso  do  Evento  de Cancelamento ter sido recebido fora de prazo, deverá ser utilizado o Status '155-Cancelamento homologa do fora de prazo'.

## 06. Consulta Situação da NF-e (item 4.5 do Manual)

## 06.1 Mensagem de Entrada (item 4.5.1 do Manual)

Eliminada a versão 2.00 da mensagem de entrada, con forme já previsto no próprio Manual. Permanece a me nsagem na versão 2.01.

## 06.2 Mensagem de Retorno (item 4.5.2 do Manual)

Eliminada a versão 2.00 da mensagem de retorno, con forme já previsto no próprio Manual. Permanece a me nsagem na versão 2.01.

![Image](assets/image_000011_0ea15792b6677c9034a9774439014771e7e6b8ea8b581a24081cb92c373cc05a.png)

Incluídos os novos valores para as operações fora de prazo, conforme segue:

| #    | Campo      | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Dec.   | Descrição/Obse rvação                                                                                                                                                                                       |
|------|------------|-------|-------|--------|---------|--------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ER08 | protNFe    | G     | ER01  | xml    | 0-1     | -      |        | Protocolo de autorização ou denegação de uso do NF-e (vide item 4.2.2). Informar se localizado uma NF-e com cStat = 100-uso autorizado, 150-uso autorizado fora de prazo ou 110-uso denegado. (NT 2012.003) |
| ER09 | retCancNFe | G     | ER01  | xml    | 0-1     | -      |        | Protocolo de homologação de cancelamento de NF-e (vide item 4.3.2). Informar se localizado uma NF-e com cStat = 101-cancelado ou 151-cancelado fora de prazo. (NT 2012.003)                                 |

## 06.3 Regras de Validação

Corrigida a validação do Ano inicial da primeira NF -e autorizada.

| # Regra de Validação                                                                 | Aplic.   |   Msg | Efeito   |
|--------------------------------------------------------------------------------------|----------|-------|----------|
| J02c Chave de Acesso inválida (Ano < 06 ou Ano maior que Ano corrente) (NT 2012.003) | Obrig.   |   615 | Rej.     |

## 07. Evento de Carta de Correção (item 4.8 do Manual )

## 07.1 Regras de Validação - parte Geral

Alteração de regras de validação com o objetivo de:

- -Identificar de forma mais clara a rejeição, no cas o de Chave de Acesso inválida ou inexistente;
- -Permitir uma tolerância no horário do evento infor mado (campo dhEvento), evitando a rejeição motivada  pela diferença no sincronismo de horário entre o servidor da empresa e o servidor da SEFAZ;
- -Não permitir a emissão de Carta de Correção para C ontribuinte descredenciado.

| #                                                                                                   | Regra de Validação   |   Aplic. | Msg Efeito   |
|-----------------------------------------------------------------------------------------------------|----------------------|----------|--------------|
| G04 CPF do autor do evento informado inválido (DV,Zeros, 111..., 222..., ..., 999...) (NT 2012.003) | Obrig.               |      490 | Rej.         |
| G05a Chave de Acesso com dígito verificador inválido (NT 2012.003)                                  | Obrig.               |      236 | Rej.         |
| G05b Chave de Acesso inválida (Código UF inválido) (NT 2 012.003)                                   | Obrig.               |      614 | Rej.         |

![Image](assets/image_000012_a612254256487620210007e236beec685214465d7d9bba737756632ff54f4fc6.png)

| #    | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                         | Aplic.   |   Msg | Efeito   |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|
| G05c | Chave de Acesso inválida (Ano < 06 ou Ano maior queAno corrente) (NT 2012.003)                                                                                                                                                                                                                                                                                                             | Obrig.   |   615 | Rej.     |
| G05d | Chave de Acesso inválida (Mês = 0 ou Mês > 12) (NT 2012.003)                                                                                                                                                                                                                                                                                                                               | Obrig.   |   616 | Rej.     |
| G05e | Chave de Acesso inválida (CNPJ zerado ou dígito inv álido) (NT 2012.003)                                                                                                                                                                                                                                                                                                                   | Obrig.   |   617 | Rej.     |
| G05f | Chave de Acesso inválida (modelo diferente de 55) ( NT 2012.003)                                                                                                                                                                                                                                                                                                                           | Obrig.   |   618 | Rej.     |
| G05g | Chave de Acesso inválida (número NF = 0) (NT 2012.0 03)                                                                                                                                                                                                                                                                                                                                    | Obrig.   |   619 | Rej.     |
| G06  | Acesso BD NFE (Chave: CNPJ Emitente, Modelo, Série e Nro): - Chave Acesso inexistente para o tpEvento que exige a existência da NF-e Obs.: Caso exista uma NF-e no banco de dados, com Chave de Acesso divergente, opcionalmente, deve-se concatenar a Chave de Acesso existente na descrição do erro, cas o o CNPJ do Autor do evento seja o mesmo CNPJ da Chave de Acesso. (NT 2012.003) | Obrig.   |   494 | Rej.     |
| G08  | Se evento do emissor verificar se CNPJ do Autor diferente do CNPJ da Chave de Acesso da NF-e                                                                                                                                                                                                                                                                                               | Obrig.   |   574 | Rej.     |
| G12  | Data do evento não pode ser maior que a data de processamento (aceitar uma tolerância de até 5 minutos) (NT 2012.003)                                                                                                                                                                                                                                                                      | Obrig.   |   578 | Rej.     |

Excluídas as regras de validação abaixo que são específicas para eventos gerados pelo destinatário, ou por outros Órgãos, não se aplicando para o caso da Carta de Correção Eletrônica. Excluídas as regras de validação:

- -'G09 - Se evento do destinatário verificar se CNPJ  do Autor diferente do CNPJ base do destinatário da  NF-e';
- -'G10 - Se evento do Fisco/RFB/Outros órgãos, verif icar se CNPJ do Autor consta da tabela de órgãos au torizados a gerar evento'.

## 07.2 Regras de Validação específicas do evento Carta de Correção

| #    | Regra de Validação                                | Aplic.   |   Msg | Efeito   |
|------|---------------------------------------------------|----------|-------|----------|
| GA04 | Acesso Cadastro Contribuinte:                     | Obrig.   |   203 | Rej.     |
|      | - Verificar Emitente não autorizado a emitir NF-e |          |       |          |
| GA05 | - Verificar Situação Fiscal irregular do Emitente | Obrig.   |   240 | Rej.     |

## 08. Serviço de Recepção de DPEC (item 8.5.1 do Manu al)

## 08.1 Regras de Validação (item 8.5.9.4 do Manual)

| #    | Regra de Validação                                                                | Aplic.   |   Msg | Efeito   |
|------|-----------------------------------------------------------------------------------|----------|-------|----------|
| G11  | DV da Chave de acesso inválido                                                    | Obrig.   |   236 | Rej.     |
| G11a | Chave de Acesso inválida (modelo diferente de55) (NT 2012.003)                    | Obrig.   |   618 | Rej.     |
| G11b | Chave de Acesso inválida (número NF = 0) (NT 2 012.003)                           | Obrig.   |   619 | Rej.     |
| G11c | Tipo de Emissão da Chave de Acesso difere de ' 4' (posição 35 da Chave de Acesso) | Obrig    |   484 | Rej.     |

![Image](assets/image_000013_83c87a20a04a0545c1239f60e003c8c5930e463ef8f9f937ac72c1943567b6b0.png)

## Nota Fiscal eletrônica

| #     | Regra de Validação                                                                                                                                       | Aplic.   |   Msg | Efeito   |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|
| G12   | Se Operação com Exterior (UF Destinatário = 'EX '): - não informada tag CNPJ ou CNPJ <> nulo                                                             | Obrig.   |   507 | Rej.     |
| G12.1 | Se não é Operação com Exterior (UF Destinatár io <> 'EX'): - CNPJ destinatário é nulo e CPF destinatário é nulo                                          | Obrig.   |   508 | Rej.     |
| G12.2 | Se informada Tag CNPJ: -CNPJ com zeros ou dígito de controle inválido                                                                                    | Obrig.   |   208 | Rej.     |
|       | Se informada Tag CPF: -CPF com zeros, 111..., 222..., ..., 999..., ou dígito de controle inválido                                                        | Obrig.   |   237 | Rej.     |
| G13   | Acesso ao BD DPEC (Chave: CNPJ Emitente, Sériee Nro) (NT 2012.003): - Número de DPEC já existe no cadastro de DPEC                                       | Obrig.   |   485 | Rej.     |
| G13.1 | Acesso ao BD NFE (Chave: CNPJ Emitente, Modelo=55, Série e Nro): - NF-e já existente para o número da DPEC inform ado (NT 2012.003)                      | Obrig.   |   661 | Rej.     |
| G13.2 | Acesso ao BD de Inutilização (Chave: CNPJ Emitente, Modelo=55, Série e Nro): - Numeração da DPEC está inutilizada na Base deDados da SEFAZ (NT 2012.003) | Obrig.   |   662 | Rej.     |

Nota:  Alterado  o  código  de  erro  do  dígito  verificad or  da  Chave  de  Acesso  para  '236-  Rejeição:  Chave  de   Acesso  com  dígito  verificador  inválido'.

![Image](assets/image_000014_372a71678a30e531942cb03fb37c2d38ecac286e6b039c6920f0c573503f007b.png)

## DOCUMENTACIONAL

## D01. Orientação para as Empresas

## D01.1 Emissão do DANFE em Contingência / Formulário de Segurança

O Manual do Contribuinte prevê a possibilidade de e missão do DANFE em contingência, usando Formulário de Segurança, com posterior envio da NF- e. Neste caso, logo após a cessação dos problemas técnicos que impediam a transmissão da NF-e de forma normal, esta NF-e deverá ser transmitida, usando  a  mesma  Chave  de  Acesso  que  foi  impressa  no  DANFE  emitido  em contingência .

Esta já era a orientação existente, mas é reforçada , alterando o Manual do Contribuinte, no item 8.1.2, como segue:

- a Chave de Acesso da NF-e é a mesma Chave de Acesso  do DANFE emitido em Formulário de Segurança;
- transmitir as NF-e imediatamente após a cessação d os problemas técnicos que impediam a transmissão da NF-e, observando o prazo limite de t ransmissão na legislação;

## D01.2 Emissão da NF-e em Contingência / DPEC

O Manual do Contribuinte prevê a possibilidade de e missão do DANFE em contingência, após a autorização  da  DPEC,  com  posterior  envio  da  NF-e.  N este  caso,  logo  após  a  cessação  dos problemas técnicos que impediam a transmissão da NF-e de forma normal, esta NF-e deverá ser transmitida, usando  a  mesma  Chave  de  Acesso  que  foi  impressa  DANFE  emitido  em contingência .

Esta já era a orientação existente, mas é reforçada , alterando o Manual do Contribuinte, no item 8.1.4, como segue:

- transmitir as NF-e emitidas em Contingência Eletrô nica para a SEFAZ de origem, observando o prazo limite de transmissão na legisla ção;
- a Chave de Acesso da NF-e é a mesma Chave de Acesso  da DPEC autorizada;

## D01.3 Código Numérico da Chave de Acesso com Autorização de Uso

O Manual do Contribuinte documenta a composição da  Chave de Acesso (item 5.4 do Manual), mostrando que o campo 'Código Numérico' (Campo 'cNF' do leiaute da NF-e, id:B03), é um dos campos que compõem a Chave de Acesso.

A empresa gera uma NF-e e envia esta NF-e para o serviço de autorização de uso da SEFAZ. Eventualmente a NF-e é rejeitada por um motivo qual quer e a empresa corrige a informação e reenvia a mesma NF-e para a SEFAZ, obtendo a autorização de uso. Observado que algumas empresas alteram o Código Numérico da Chave de Acesso sempre que enviam a NF-e para o serviço de autorização de uso e, em alguns casos, a  empresa acaba imprimindo o DANFE onde a Chave de Acesso representa o Código Numérico da NF-e que foi rejeitada.

Alertamos que o DANFE deve conter a Chave de Acesso da NF-e que foi autorizada pela SEFAZ, além do respectivo Protocolo de Autorização de Uso fornecido pela SEFAZ.

O DANFE impresso com uma Chave de Acesso divergente daquela que foi autorizada na SEFAZ está em desacordo com a legislação e traz contratem pos operacionais para a própria empresa, para o destinatário da NF-e e para o controle da pa ssagem de mercadorias nos Postos Fiscais.

![Image](assets/image_000015_58e99b888119aa5c2db56951b92db56c2ed9f0eb8302c7d02586a4c3022af6b5.png)

Nota: Observado que algumas empresas acessam o Web service de Consulta da Situação da NFe  para  verificar  se  a  Chave  de  Acesso  impressa  no  DANFE  recebido  do  seu  fornecedor  foi realmente  autorizada  na  SEFAZ.  Nestes  casos  da  Chave  de  Acesso  divergente,  o  serviço  de verificação  da  empresa destinatária acaba se manten do em 'loop' consultando inúmeras vezes uma Chave de Acesso que não representa a NF-e que f oi realmente autorizada. pelo emitente.

## D02. Documentação do Manual do Contribuinte

Seguem  mudanças  no  Manual  do  Contribuinte  com  o  objetivo  de  atualizar  e/ou  melhorar  a documentação.

## D02.1 Mensagens de Erro

Alterada tabela de Códigos de Erros e Descrições de  Mensagens de Erro, no item 5.1.1 do Manual do Contribuinte, conforme segue:

|   Código | RESULTADO DO PROCESSAMENTO DA SOLICITAÇÃO                                           |
|----------|-------------------------------------------------------------------------------------|
|      150 | Autorizado o uso da NF-e, autorização fora de prazo                                 |
|      151 | Cancelamento de NF-e homologado fora de prazo                                       |
|      479 | Rejeição: Emissor em situação irregular perante o f isco                            |
|      480 | Rejeição: CNPJ da Chave de acesso da NF-e informada diverge do CNPJ do emitente     |
|      481 | Rejeição: UF da Chave de acesso diverge do código d a UF informada                  |
|      482 | Rejeição: AA da Chave de acesso inválida                                            |
|      483 | Rejeição: MMda chave de acesso inválido                                             |
|      484 | Rejeição: DPEC com tipo de emissão diferente de '4' (posição 35 da Chave de Acesso) |
|      485 | Rejeição: Número de DPEC já existe no cadastro de D PEC                             |
|      486 | Rejeição: DPEC não localizada para o número de registro de DPEC informado           |
|      487 | Rejeição: Nenhuma DPEC localizada para a chave de a cesso informada                 |
|      488 | Rejeição: Requisitante de Consulta não tem o mesmo CNPJ base do emissor da DPEC     |
|      615 | Rejeição: Chave de Acesso inválida (Ano < 06 ou Anomaior que Ano corrente)          |
|      626 | Rejeição: CFOP de operação isenta para ZFM diferent e do previsto                   |
|      656 | Rejeição: Consumo indevido                                                          |
|      660 | Rejeição: CFOP de Combustível e não informado grupo de combustível da NF-e          |
|      661 | Rejeição: NF-e já existente para o número da DPEC i nformada                        |
|      662 | Rejeição: Numeração da DPEC está inutilizada na Base de Dados da SEFAZ              |

## Excluído os Códigos abaixo:

|   Código | RESULTADO DO PROCESSAMENTO DA SOLICITAÇÃO                                            |
|----------|--------------------------------------------------------------------------------------|
|      595 | Rejeição: A versão do leiaute da NF-e utilizada não é mais válida                    |
|      596 | Rejeição: Ambiente de homologação indisponível para recepção de NF-e da versão 1.10. |

![Image](assets/image_000016_58e99b888119aa5c2db56951b92db56c2ed9f0eb8302c7d02586a4c3022af6b5.png)

## D02.2 Tabela de Códigos de Produto da ANP (Combustíveis e Lubrificantes)

Exemplo de alguns Códigos da ANP para combustíveis e lubrificantes.

| Produto                                                       | Código              |
|---------------------------------------------------------------|---------------------|
| ÁLCOOL METÍLICO                                               | 810201001           |
| BIODIESEL B100                                                | 820101001           |
| BIODIESEL FORA DE ESPECIFICAÇÃO                               | 820101010           |
| BRIGHT STOCK                                                  | 610101009           |
| BUTADIENO                                                     | 210202003           |
| BUTANO                                                        | 210202001           |
| BUTANO ESPECIAL                                               | 210202002           |
| CICLO DIESEL                                                  | 620501002           |
| CICLO OTTO                                                    | 620501001           |
| CILINDRO I                                                    | 610101005           |
| CILINDRO II                                                   | 610101006           |
| CORRENTE DE MOTOSSERRA                                        | 620601003           |
| DERIVADOS LEVES INTERMEDIÁRIOS                                | 340101002           |
| DERIVADOS PESADOS INTERMEDIÁRIOS                              | 560101002           |
| DIESEL B S1800 PARA GERAÇÃO DE ENERGIA ELÉTRICA               | 820 101026          |
| DIESEL B S50 PARA GERAÇÃO DE ENERGIA ELÉTRICA                 | 82010 1032          |
| DIESEL B S500 PARA GERAÇÃO DE ENERGIA ELÉTRICA                | 8201 01027          |
| DIESEL B10                                                    | 820101004           |
| DIESEL B15                                                    | 820101005           |
| DIESEL B2 ESPECIAL - 200 PPM ENXOFRE                          | 820101022           |
| DIESEL B20 S1800 - ADITIVADO                                  | 820101014           |
| DIESEL B20 S1800 - COMUM                                      | 820101006           |
| DIESEL B20 S50 ADITIVADO                                      | 820101031           |
| DIESEL B20 S50 COMUM                                          | 820101030           |
| DIESEL B20 S500 - ADITIVADO                                   | 820101016           |
| DIESEL B20 S500 - COMUM                                       | 820101015           |
| DIESEL B30                                                    | 820101025           |
| DIESEL B4 S1800 - ADITIVADO                                   | 820101007 820101002 |
| DIESEL B4 S1800 - COMUM                                       | 820101009           |
| DIESEL B4 S500 - ADITIVADO                                    | 820101008           |
| DIESEL B4 S500 - COMUM                                        |                     |
| DIESEL MARÍTIMO - DMA B2                                      | 820101017           |
| DIESEL MARÍTIMO - DMB B2                                      | 820101019           |
| DIESEL MARÍTIMO - DMB B5                                      | 820101020           |
| DIESEL NÁUTICO B2 ESPECIAL - 200 PPM ENXOFRE                  | 820101 021          |
| DMA- MGO                                                      | 420201001           |
| DMB- MDO                                                      | 420201003           |
| ENGRENAGENS E SISTEMAS CIRCULATÓRIOS                          | 620101002           |
| ESTAMPAGEM                                                    |                     |
|                                                               | 620101007           |
| ETANOL                                                        |                     |
| ETANO ANIDRO                                                  | 210301001 810102001 |
| ETANOL ANIDRO COM CORANTE                                     | 810102004           |
| ETANOL ANIDRO FORA DE ESPECIFICAÇÃO                           | 810102002           |
| ETANOL ANIDRO PADRÃO                                          | 810102003           |
| ETANOL HIDRATADO ADITIVADO                                    | 810101002           |
| ETANOL HIDRATADO COMUM ETANOL HIDRATADO FORA DE ESPECIFICAÇÃO | 810101001 810101003 |
| ETENO                                                         | 210301002           |

![Image](assets/image_000017_58e99b888119aa5c2db56951b92db56c2ed9f0eb8302c7d02586a4c3022af6b5.png)

| Produto                                              | Código              |
|------------------------------------------------------|---------------------|
| GÁS ÁCIDO                                            | 210302004           |
| GÁS COMBUSTÍVEL                                      | 210101001           |
| GÁS DE XISTO                                         | 210302003           |
| GÁS INTERMEDIÁRIO                                    | 210302002           |
| GÁS LIQUEFEITO INTERMEDIÁRIO                         | 210204001           |
| GÁS NATURAL COMPRIMIDO                               | 220101003           |
| GÁS NATURAL LIQUEFEITO                               | 220101004           |
| GÁS NATURAL SECO                                     | 220101002           |
| GÁS NATURAL ÚMIDO                                    | 220101001           |
| GÁS NATURAL VEICULAR                                 | 220101005           |
| GÁS NATURAL VEICULAR PADRÃO                          | 220101006           |
| GASÓLEOS                                             | 520101001           |
| GASOLINA A COMUM                                     | 320101001           |
| GASOLINA A FORA DE ESPECIFICAÇÃO                     | 320101003           |
| GASOLINA A PREMIUM                                   | 320101002           |
| GASOLINA AUTOMOTIVA PADRÃO                           | 320103001           |
| GASOLINA C ADITIVADA                                 | 320102002           |
| GASOLINA C COMUM                                     | 320102001           |
| GASOLINA C FORA DE ESPECIFICAÇÃO                     | 320102004           |
| GASOLINA C PREMIUM                                   | 320102003           |
| GASOLINA DE AVIAÇÃO                                  | 320201001           |
| GASOLINA DE AVIAÇÃO FORA DE ESPECIFICAÇÃO            | 320201002           |
| GASOLINA NATURAL (C5+)                               | 220102001           |
| GASOLINA PARA EXPORTAÇÃO                             | 320301002           |
| GLP GLP FORA DE ESPECIFICAÇÃO                        | 210203001 210203002 |
| GRAXAS MINERAIS                                      | 650101001           |
| HIDRÁULICO                                           | 620101001           |
| HIDROGENADO LEVE                                     | 610201001           |
| HIDROGENADO MÉDIO                                    | 610201002           |
| HIDROGENADO PESADO                                   | 610201003           |
| ISOLANTE TIPO A                                      | 620101004           |
| ISOLANTE TIPO B                                      | 620101005           |
| LÍQUIDO DE GÁS NATURAL                               | 220102002           |
| MACROOLEOSAS                                         | 640201001           |
| MICROOLEOSAS                                         | 640101001           |
| MOTORES 2 TEMPOS                                     | 620502001           |
| NEUTRO LEVE                                          | 610101002           |
| NEUTRO LEVE RR                                       | 610401002           |
| NEUTRO MÉDIO                                         | 610101003           |
| NEUTRO MÉDIO RR                                      | 610401003           |
| NEUTRO PESADO                                        | 610101004           |
| NEUTRO PESADO RR                                     | 610401004           |
| ÓLEO COMBUSTÍVEL A FORA DE ESPECIFICAÇÃO             | 510101003           |
| ÓLEO COMBUSTÍVEL A1                                  | 510101001           |
| ÓLEO COMBUSTÍVEL A2                                  | 510101002           |
| ÓLEO COMBUSTÍVEL B FORA DE ESPECIFICAÇÃO             | 510102003           |
| ÓLEO COMBUSTÍVEL B1                                  | 510102001           |
| ÓLEO COMBUSTÍVEL B2                                  | 510102002           |
| ÓLEO COMBUSTÍVEL MARÍTIMO                            | 510201001           |
| ÓLEO COMBUSTÍVEL MARÍTIMO FORA DE ESPECIFICAÇÃO      | 510 201002          |
| ÓLEO COMBUSTÍVEL MARÍTIMO MISTURA (MF)               | 510201003           |
| ÓLEO COMBUSTÍVEL PARA GERAÇÃO ELÉTRICA ÓLEO DE XISTO | 510301003           |
|                                                      | 560101001           |

![Image](assets/image_000018_f900291e401bbbeb47d56879a3510dd31b9bd9c37436c935db9125e1363cdc48.png)

| Produto                                                                   | Código              |
|---------------------------------------------------------------------------|---------------------|
| ÓLEO DIESEL A S10                                                         | 420105001           |
| ÓLEO DIESEL A S1800 - ADITIVADO                                           | 420101005           |
| ÓLEO DIESEL A S1800 - COMUM                                               | 420101004           |
| ÓLEO DIESEL A S1800 - FORA DE ESPECIFICAÇÃO                               | 4201010 03          |
| ÓLEO DIESEL A S50                                                         | 420102006           |
| ÓLEO DIESEL A S500 - ADITIVADO                                            | 420102005           |
| ÓLEO DIESEL A S500 - COMUM                                                | 420102004           |
| ÓLEO DIESEL A S500 - FORA DE ESPECIFICAÇÃO                                | 42010200 3          |
| ÓLEO DIESEL AUTOMOTIVO ESPECIAL - ENXOFRE 200 PPM                         | 4 20104001          |
| ÓLEO DIESEL B S10 - ADITIVADO                                             | 820101033           |
| ÓLEO DIESEL B S10 - COMUM                                                 | 820101034           |
| ÓLEO DIESEL B S1800 - ADITIVADO                                           | 820101011           |
| ÓLEO DIESEL B S1800 - COMUM                                               | 820101003           |
| ÓLEO DIESEL B S50 - ADITIVADO                                             | 820101028           |
| ÓLEO DIESEL B S50 - COMUM                                                 | 820101029           |
| ÓLEO DIESEL B S500 - ADITIVADO                                            | 820101013           |
| ÓLEO DIESEL B S500 - COMUM                                                | 820101012           |
| ÓLEO DIESEL FORA DE ESPECIFICAÇÃO                                         | 420301003           |
| ÓLEO DIESEL MARÍTIMO FORA DE ESPECIFICAÇÃO                                | 42020100 2          |
| ÓLEO DIESEL NÁUTICO ESPECIAL - ENXOFRE 200 PPM                            | 4202 02001          |
| ÓLEO DIESEL PADRÃO                                                        | 420301001           |
| ÓLEOS BÁSICOS - GRUPO II                                                  | 610601001           |
| ÓLEOS BÁSICOS - GRUPO III                                                 | 610701001           |
| ÓLEOS COMBUSTÍVEIS PARA EXPORTAÇÃO                                        | 510301002           |
| ÓLEOS EXTENSORES E PLASTIFICANTES                                         | 620601001           |
| ÓLEOS LUB. PARAF E GRAXAS INTERMEDIÁRIOS ÓLEOS LUBRIFICANTES FERROVIÁRIOS | 660101001 620401001 |
| ÓLEOS LUBRIFICANTES MARÍTIMOS                                             | 620301001           |
| ÓLEOS LUBRIFICANTES PARA AVIAÇÃO                                          | 620201001           |
| ÓLEOS LUBRIFICANTES USADOS OU CONTAMINADOS                                | 63010100 1          |
| OUTRAS GASOLINAS                                                          | 320301001           |
| OUTRAS GASOLINAS AUTOMOTIVAS                                              | 320103002           |
| OUTRAS GRAXAS                                                             | 650101002           |
| OUTRAS PARAFINAS                                                          | 640401001           |
| OUTROS ALCOÓIS                                                            | 810201002           |
| OUTROS DERIVADOS LEVES OUTROS DERIVADOS PESADOS                           | 340101003           |
|                                                                           | 560101003           |
| OUTROS GASES                                                              | 210302001           |
| OUTROS GASES LIQUEFEITOS OUTROS NAFTÊNICOS                                | 210204002           |
| OUTROS ÓLEOS COMBUSTÍVEIS                                                 | 610201004           |
| OUTROS ÓLEOS DIESEL                                                       | 510301001           |
|                                                                           | 420301002           |
| OUTROS ÓLEOS LUBRIFICANTES ACABADOS                                       | 620601004           |
| OUTROS ÓLEOS LUBRIFICANTES AUTOMOTIVOS                                    | 620505001           |
| OUTROS ÓLEOS LUBRIFICANTES BÁSICOS                                        | 610501001           |
| OUTROS ÓLEOS LUBRIFICANTES INDUSTRIAIS                                    | 620101008           |
| OUTROS PARAFÍNICOS                                                        | 610101010           |
| OUTROS SINTÉTICOS                                                         | 610302001           |
| POLIALFAOLEFINA                                                           | 610301001 620101003 |
| PROCESSO                                                                  |                     |
| PROPANO                                                                   | 210201001           |
| PROPANO ESPECIAL PROPENO                                                  | 210201002 210201003 |
| PULVERIZAÇÃO AGRÍCOLA                                                     | 620601002           |

![Image](assets/image_000019_58e99b888119aa5c2db56951b92db56c2ed9f0eb8302c7d02586a4c3022af6b5.png)

| Produto                                  |    Código |
|------------------------------------------|-----------|
| RESÍDUO AROMÁTICO (RARO)                 | 550101001 |
| RESÍDUO ASFÁLTICO(RASF)                  | 550101005 |
| RESÍDUO ATMOSFÉRICO (RAT)                | 550101002 |
| RESÍDUO DE VÁCUO                         | 550101003 |
| RESÍDUO DE VÁCUO DE ALTO TEOR DE ENXOGRE | 550101004 |
| SPINDLE                                  | 610101001 |
| SPINDLE RR                               | 610401001 |
| TÊXTIL / AMACIANTE DE FIBRAS             | 620101006 |
| TRANSMISSÃO AUTOMÁTICA                   | 620504001 |
| TRANSMISSÕES E SISTEMAS HIDRÁULICOS      | 620503001 |
| TURBINA LEVE                             | 610101007 |
| TURBINA PESADO                           | 610101008 |
| VASELINA                                 | 640301001 |