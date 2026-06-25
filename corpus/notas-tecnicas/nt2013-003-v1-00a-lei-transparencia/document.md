![Image](assets/image_000000_5ea50f18afa4fbebab2faeb3926b1c12b29a69e3334c061fb448fc6955f3f163.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_31c8d649980e81589d875ff6b2afd44a0f0f321f8f5c8b42f665260499a6f424.png)

## Nota Técnica 2013/003

## Lei da Transparência dos Tributos Federais, Estaduais e Municipais

![Image](assets/image_000002_0cd5a2793641ba110f4c260e9b64c9bee7ad36c450c08cdbcb5e956c98cfdaf9.png)

## Versão 1.00a Abril 2013

![Image](assets/image_000003_2db74724c4429a026b93640c0e0791f4e0ba0ae6a0527f322c828e5d3c8f3a3c.png)

## 01. Resumo

O  Ajuste  SINIEF  07/2013,  publicado  em  05/04/2013,  dispõe  sobre  os  procedimentos  a  serem adotados  na  emissão  de  documentos  fiscais  para  escl arecimentos  ao  consumidor,  conforme disposto na Lei nº 12.741/12.

Esta Nota Técnica trata desse assunto e alguns outr os itens, conforme segue:

- Criação  de  campo  opcional  para  que  o  contribuinte  possa  informar  o  valor  aproximado correspondente  a  totalidade  dos  tributos  federais,  estaduais  e  municipais,  cuja  incidência influa na formação do respectivo preço de venda, at endendo o disposto na Lei citada;
- Redução da quantidade  máxima de ocorrências dos do cumentos referenciados,  incluindo validações sobre estas ocorrências;
- Validação das chaves dos documentos referenciados;
- Rejeição  do  Pedido  de  Cancelamento  para  NF-e  com  C onhecimento  de  Transporte Eletrônico;
- Ampliação  da  faixa  de  números  do  Pedido  de  Inutili zação,  conforme  solicitação  das empresas.

Prazo para entrada em vigência das alterações:

- Ambiente de Homologação (ambiente de teste das empresas): 15/05/13;
- Ambiente de Produção : 01/06/13.

Nota:  Deverá  ser  observado  o  prazo  previsto  para  a liberação  da  versão,  considerando  as mudanças  relacionadas  com  a  Lei  da  Transparência.  A   maior  parte  das  demais  validações desta NT são opcionais e as SEFAZ poderão optar pel a sua adoção, parcial ou total, mesmo após a publicação da versão.

![Image](assets/image_000004_b187bb992c531eaaa57efbb8d45236b9dbc744528e5a07c1c690915f5a39e16c.png)

## 02. Alteração de Schema XML da NF-e (Anexo I do MOC )

As alterações documentadas incluem a possibilidade  de informação de campos opcionais e trazem algumas  mudanças no Schema XML, mas não alteram a versão atual do leiaute da NF-e. Portanto , não há a intenção de obrigar a mudança da aplicação das empresas de forma massiva.

## 02.1 NFref (B12a) - Redução da quantidade máxima de  ocorrências

| #   | ID   | Campo   | Descrição                                     | Ele Pai Tipo Ocor. Tam.   |       | Observação    |
|-----|------|---------|-----------------------------------------------|---------------------------|-------|---------------|
| 16a | B12a | NFref   | Grupo de informação das NF/NF-e referenciadas | G B01                     | 0-500 | (NT 2013.003) |

## 02.2 Valor Total dos Impostos por Item

| #    | ID   | Campo    | Descrição                                                           | Ele   | Pai   | Tipo   | Ocor.   |   Tam. |   Dec. | Observação    |
|------|------|----------|---------------------------------------------------------------------|-------|-------|--------|---------|--------|--------|---------------|
| 163a | M02  | vTotTrib | Valor aproximado total de tributos federais, estaduais e municipais | E     | M01   | N      | 0-1     |     15 |      2 | (NT 2013.003) |

## 02.3 Valor Total dos Impostos, total da NF-e

| #    | ID   | Campo    | Descrição                                                           | Ele Pai   |     | Tipo   | Ocor.   |   Tam. |   Dec. | Observação    |
|------|------|----------|---------------------------------------------------------------------|-----------|-----|--------|---------|--------|--------|---------------|
| 341a | W16a | vTotTrib | Valor aproximado total de tributos federais, estaduais e municipais | E         | W02 | N      | 0-1     |     15 |      2 | (NT 2013.003) |

![Image](assets/image_000005_a14778869faab8e20f8bb13db0abd3c4dfd9d8ea617e7ef5d0217c3b8910e3e1.png)

## 03. Regras de Validação da NF-e (item 4.1.9.4 do MO C)

## 03.1 NF Complementar

| #      | Campo Regra de validação   | Campo Regra de validação                                                                                                   | Aplic.   |   Msg | Efeito   | Descrição Erro                                                  |
|--------|----------------------------|----------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-----------------------------------------------------------------|
| GB25.3 | B25                        | Se NF-e Complementar (finNFe=2): - UF da NF-e referenciada diferente da UF do emitente (NF-e ou NF modelo 1) (NT 2013.003) | Facult.  |   678 | Rej.     | Rejeição: NF referenciada com UF diferente da NF-e complementar |

## 03.2 NF-e, NF, CT-e e ECF Referenciado

| #      | Campo   | Regra de validação                                                                                                                                        | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                             |
|--------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------------------------|
| GB13a  | B13     | Se informada NF-e referenciada (tag: refNFe): - Modelo da NF-e referenciada diferente de 55                                                               | Facult.  |   679 | Rej.     | Rejeição: Modelo da NF-e referenciada diferent e de 55                                     |
| GB13b  | B13     | - Verificar duplicidade da NF-e referenciada (duplicidade da tag refNFe)                                                                                  | Facult.  |   680 | Rej.     | Rejeição: Duplicidade de NF-e referenciada (Ch ave de Acesso referenciada mais de uma vez) |
| GB20   | B20     | Se informada NF Modelo 1 referenciada (tag: refNF): - Verificar duplicidade de Nota Fiscal Modelo 1 referenciada (mesmo CNPJ, Modelo, Série, Número)      | Facult.  |   681 | Rej.     | Rejeição: Duplicidade de NF Modelo 1 referenci ada (CNPJ, Modelo, Série e Número)          |
| GB20ha | B20ha   | Se informada NF de Produtor referenciada (tag: refNFP): - Verificar duplicidade de Nota Fiscal de Produtor referenciada (mesma IE, Modelo, Série, Número) | Facult.  |   682 | Rej.     | Rejeição: Duplicidade de NF de Produtor refere nciada (IE, Modelo, Série e Número)         |
| GB20ia | B20i    | Se informado CT-e referenciado (tag: refCTe): - Modelo de CT-e referenciado diferente de 57                                                               | Facult.  |   683 | Rej.     | Rejeição: Modelo do CT-e referenciado diferent e de 57                                     |
| GB20m  | B20m    | Se informado Cupom Fiscal referenciado (tag: refECF): - Verificar duplicidade de Cupom Fiscal referenciado (mesmo Modelo, Número de Ordem e COO)          | Facult.  |   684 | Rej.     | Rejeição: Duplicidade de Cupom Fiscal referenc iado (Modelo, Número de Ordem e COO)        |

## 03.3 Validação dos Campos de Total da NF-e

| #     | Campo   | Regra de validação                                                                                                                                                                                        | Aplic.   |   Msg | Efeito Descrição Erro                                                                |
|-------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|--------------------------------------------------------------------------------------|
| GW16b | W16a    | Total do valor aproximado dos tributos (id:W16a) difere do somatório dos itens (id:M02) Obs.: O campo 'vTotTrib' é opcional para o Item e p ara o grupo de Totais. Considerar valor=0, se não informa do. | Facult.  |   685 | Rej. Rejeição: Total do Valor Aproximado dos Tribut os difere do somatório dos itens |

![Image](assets/image_000006_c5a0ea8ff8f925ef7122f2f9c985e590b9438fe336010bac885b7138d4acbb99.png)

## 03.4 Validação Banco de Dados: NF-e Complementar

Eliminar as validações de NF-e Complementar existen tes:

- 267 - NF Complementar referencia uma NF-e inexistente;
- 268 - NF Complementar referencia uma outra NF-e Complementar

As regras de validações citadas acima serão reinclu ídas dentro do grupo de validação da 'Nota Fiscal Referenciada' (ver próximo item desta NT).

## 03.5 Validação Banco de Dados: NF-e Referenciada

| #       | Campo   | Regra de validação                                                                                                                                                                                                                                                                                                                            | Aplic.   |   Msg | Efeito   | Descrição Erro                                                   |
|---------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------|
| G1B13   | B13     | Para cada NF-e referenciada (tag: refNFe), se a UF da Chave de Acesso referenciada for igual a UF do Emitente: - Acessar BD NFE com Chave de Acesso referenciada - NF-e referenciada inexistente Exceção somente para 'finNFe" diferente de 2: - A NF-e referenciada pode não existir no caso de Emissão em Contingência (tpEmis = 2, 4 ou 5) | Facult.  |   267 | Rej.     | Rejeição: Chave de Acesso referenciada inexist ente [nRef: xxx]  |
| G1B13.1 | B13     | - NF-e Complementar (finNFe=2) referencia uma outra NF-e Complementar (finNFe=2)                                                                                                                                                                                                                                                              | Facult.  |   268 | Rej.     | Rejeição: NF Complementar referencia uma outra NF-e Complementar |
| G1B13.2 | B13     | - NF-e Complementar (finNFe=2) referencia uma NF-e cancelada                                                                                                                                                                                                                                                                                  | Facult.  |   686 | Rej.     | Rejeição: NF Complementar referencia uma NF-e cancelada          |
| G1B13.3 | B13     | - NF-e Complementar (finNFe=2) referencia uma NF-e denegada                                                                                                                                                                                                                                                                                   | Facult.  |   687 | Rej.     | Rejeição: NF Complementar referencia uma NF-e denegada           |

## 03.6 Validação Banco de Dados: NF de Produtor Refer enciada

| #       | Campo   | Regra de validação                                                                                             | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                |
|---------|---------|----------------------------------------------------------------------------------------------------------------|----------|-------|----------|-----------------------------------------------------------------------------------------------|
| G1B25   | B20f    | Para cada NF de Produtor referenciada (tag: refNFP): - Acessar Cadastro da SEFAZ: - IE de Produtor inexistente | Facult.  |   688 | Rej.     | Rejeição: NF referenciada de Produtor com IE i nexistente [nRef: xxx]                         |
| G1B25.1 | B20f    | - IE de Produtor não vinculada ao CNPJ / CPF                                                                   | Facult.  |   689 | Rej.     | Rejeição: NF referenciada de Produtor com IE n ão vinculada ao CNPJ/CPF informado [nRef: xxx] |

![Image](assets/image_000007_e41747ef1ac776dce091c4f8bde75aeb9f8d5c1ef5a1242a162ea0035bd6b78e.png)

## 04. Pedido de Inutilização (item 4.4 do MOC)

## 04.1 Validação das Regras de Negócio (item 4.4.7.4  do MOC)

| #   | Regra de validação                                                                                                              | Aplic.   |   Msg | Efeito   | Descrição Erro                                                          |
|-----|---------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-------------------------------------------------------------------------|
| I04 | Quantidade máxima de numeração a inutilizar ult rapassa o limite (10.000 números)                                               | Obrig.   |   201 | Rej.     | Rejeição: Número máximo de numeração a inutili zar ultrapassou o limite |
| I08 | Acessar BD NFE (Chave: CNPJ Emit, Modelo, Série , Nro) - Verificar se existe NF-e utilizada na faixa de inutilização solicitada | Obrig.   |   241 | Rej.     | Rejeição: Um número da faixa já foi utilizado                           |

Nota: Observe que foi eliminado o Ano no acesso ao Banco de Dados para a Regra de Validação 'I08'.

## 05. Evento de Cancelamento (item 4.9 do MOC, conforme NT 2011/006)

## 05.1 Validação das Regras de Negócio específicas do Evento (item 4.9.8 do MOC, conforme NT 2011/006)

| #    | Regra de validação                                                                                      | Aplic.   |   Msg | Efeito   | Descrição Erro                                      |
|------|---------------------------------------------------------------------------------------------------------|----------|-------|----------|-----------------------------------------------------|
| GA12 | Acessar ao BD de Eventos para a Chave de Acesso: - Existe Evento '610600 - CT-e Autorizado' para a NF-e | Obrig.   |   690 | Rej.     | Rejeição: Pedido de Cancelamento para NF-e com CT-e |

![Image](assets/image_000008_b187bb992c531eaaa57efbb8d45236b9dbc744528e5a07c1c690915f5a39e16c.png)

## 06. DANFE (item 7 do MOC)

O 'Valor Aproximado dos Tributos' calculado pela empresa, correspondente a totalidade dos tributos federais, estaduais e municipais, cuja incidência influa na formação do respectivo preço de venda, op cionalmente poderá aparecer no DANFE no campo de In formações Adicionais do Produto (tag: infAdProd, id:V01) e/ou no campo de Informações Com plementares da NF-e (tag: infCpl, id:Z03).

O 'Valor Aproximado dos Tributos', poderá opcionalm ente constar no DANFE em campo próprio, conforme segue:

- Quadro de Cálculo do Imposto: incluir nova coluna  com o 'Valor Aproximado dos Tributos' (item 7.8.1 e 7.8.2 do MOC);
- Quadro Dados dos Produtos / Serviços: incluir nova coluna com o 'Valor Aproximado dos Tributos' (item 7.1.5, 7.8.1 e 7.8.2 do MOC).

## 90. Tabela de códigos de erros e descrição de mensa gens de erro (item 5.1.1 do MOC)

|   Código | DESCRIÇÃO DA MENSAGEM                                                                         |
|----------|-----------------------------------------------------------------------------------------------|
|      267 | Rejeição: Chave de Acesso referenciada inexistente                                            |
|      678 | Rejeição: NF referenciada com UF diferente da UF da NF-e complementar                         |
|      679 | Rejeição: Modelo da NF-e referenciada diferente de 55                                         |
|      680 | Rejeição: Duplicidade de NF-e referenciada (Chave d e Acesso referenciada mais de uma vez)    |
|      681 | Rejeição: Duplicidade de NF Modelo 1 referenciada (CNPJ, Modelo, Série e Número)              |
|      682 | Rejeição: Duplicidade de NF de Produtor referenciad a (IE, Modelo, Série e Número)            |
|      683 | Rejeição: Modelo do CT-e referenciado diferente de 57                                         |
|      684 | Rejeição: Duplicidade de Cupom Fiscal referenciado (Modelo, Número e Ordem e COO)             |
|      685 | Rejeição: Total do Valor Aproximado dos Tributos di fere do somatório dos itens               |
|      686 | Rejeição: NF Complementar referencia uma NF-e cance lada                                      |
|      687 | Rejeição: NF Complementar referencia uma NF-e denegada                                        |
|      688 | Rejeição: NF referenciada de Produtor com IE inexis tente [nRef: xxx]                         |
|      689 | Rejeição: NF referenciada de Produtor com IE não vi nculada ao CNPJ/CPF informado [nRef: xxx] |
|      690 | Rejeição: Pedido de Cancelamento para NF-e com CT-e                                           |