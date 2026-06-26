![Image](assets/image_000000_cfd4fb08704df84a071ebb68a17c4e24ad6871c2edcbbadda0912822e6a25cf7.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_26163751079de2623d9a0ca08a87fb73fa87b77dfdd1516369c7b5b617c4cc87.png)

Nota Técnica 2015/003

## ICMS em Operações Interestaduais de Vendas a Consumidor Final

![Image](assets/image_000002_0304dca5020d7da8058779ffaa4716a0f7f21fed85cf54fa8a1a8f52561d7cea.png)

Versão 1.94 Junho/2017

![Image](assets/image_000003_bb32f238eef8605bf8a9bb9ee874e3d2849ef546266f7f11692bcfdf81247209.png)

## Nota Fiscal eletrônica

## Sumário

| Histórico de Alterações........................................................................................................................3     |                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Alterações introduzidas na versão 1.10...........................................................................................3                   |                                                                                                                       |
| Alterações introduzidas na versão 1.20...........................................................................................3                   |                                                                                                                       |
| Alterações introduzidas na versão 1.30...........................................................................................4                   |                                                                                                                       |
| Alterações introduzidas na versão 1.40...........................................................................................4                   |                                                                                                                       |
| Alterações introduzidas na versão 1.50...........................................................................................4                   |                                                                                                                       |
| Alterações introduzidas na versão 1.60...........................................................................................5                   |                                                                                                                       |
| Alterações introduzidas na versão 1.70...........................................................................................5                   |                                                                                                                       |
| Alterações introduzidas na versão 1.71...........................................................................................6                   |                                                                                                                       |
| Alterações introduzidas na versão 1.80...........................................................................................6                   |                                                                                                                       |
| Alterações introduzidas na versão 1.90...........................................................................................6                   |                                                                                                                       |
| Alterações introduzidas na versão 1.91...........................................................................................7                   |                                                                                                                       |
| Alterações introduzidas na versão 1.92...........................................................................................7                   |                                                                                                                       |
| 01. Resumo.........................................................................................................................................8 |                                                                                                                       |
| 02. Serviço: Autorização de Uso da NF-e / NFC-e (item 4.1 do MOC)                                                                                    | ................................................9                                                                     |
| 2.1 Leiaute da Nota Fiscal Eletrônica ..............................................................................................9                |                                                                                                                       |
| A. Campo CEST - Código Especificador da Substituição Tributária.............................................9                                        |                                                                                                                       |
| B. Grupo de Tributação do ICMS para a UF de destino...............................................................9                                  |                                                                                                                       |
| C. Total da Nota Fiscal                                                                                                                              | ..............................................................................................................10      |
| 2.2 Regras de Validação (RV) da Nota Fiscal Eletrônica...............................................................11                              |                                                                                                                       |
| E. Identificação do Destinatário .................................................................................................11                 |                                                                                                                       |
| LA. Item / Combustível...............................................................................................................13              |                                                                                                                       |
| N. Item / Tributo: ICMS..............................................................................................................14              |                                                                                                                       |
| NA. Item / ICMS para a UF de Destino ......................................................................................18                        |                                                                                                                       |
| W. Total da Nota Fiscal..............................................................................................................21              |                                                                                                                       |
| 2.3 CFOP Específicos                                                                                                                                 | ...................................................................................................................22 |
| Anexo XIII - CFOP Específicos.........................................................................................................22             |                                                                                                                       |
| Anexo XIII.04 - CFOP de Retorno de Mercadoria..........................................................................22                            |                                                                                                                       |
| Anexo XIII.05 - CFOP de Anulação de Valor                                                                                                            | .................................................................................23                                   |
| Anexo XIII.06 - CFOP de Remessa de Mercadoria........................................................................23                              |                                                                                                                       |

![Image](assets/image_000004_8718aa4049a00bdd9429d3bd4e38150c3a8daaebe8d13d96bc5d4527745b220c.png)

## Histórico de Alterações

## Alterações introduzidas na versão 1.10

-  Alterada a denominação do termo descrito na versão anterior de 'ICMS de Partilha' para 'ICMS em Operações Interestaduais'.
-  Incluída exceção na regra N12-70 para tratar o CST nas vendas de veículos novos a grandes consumidores ou para faturamento direto.
-  Incluída regra de validação E16a-30 para evitar erro na indicação de contribuinte como Isento de IE para as SEFAZ que não permitem esse tipo de situação (ou seja, para essas SEFAZ, todo contribuinte tem que ter IE).
-  Incluída  regra  de  validação  N23-10  para  exigir  o  preenchimento  do  campo  CEST  se  houver destaque do ICMS-ST (campo vICMSST), exceto para o grupo de Partilha do ICMS (campo ICMSPart).
-  Incluídas as exceções na regra NA01-20 para não exigir o grupo do ICMS interestadual nos casos de vendas de veículos novos a grandes consumidores ou para faturamento direto quando tiver o preenchimento do Grupo de Partilha do ICMS (campo ICMSPart).
-  Retirada das regras de validação NA15-10 (cálculo do valor do ICMS interestadual para a UF de destino) e NA17-10 (cálculo do valor do ICMS interestadual para a UF do remetente), visando o aguardo de publicação legislativa esclarecendo detalhes acerca da metodologia de cálculo. Nova versão desta nota técnica será publicada contendo as respectivas regras de validação.
-  Incluídos campos para identificar o valor devido exclusivamente à UF de destino em decorrência do  percentual  de  ICMS  relativo  ao  Fundo  de  Combate  à  Pobreza,  previsto  na  Constituição Federal, no Art. 82 do ADCT - Ato das Disposições Constitucionais Transitórias;
-  Incluídas novas regras de validação relacionadas com os novos campos.
-  Esclarecimentos sobre a validação, no ambiente de homologação, quanto as regras que só terão efeito em produção a partir de 01/01/2016.
-  Incluídos códigos de erros não indicados na versão anterior
-  Publicado Schema XML através de Pacote de Liberação PL\_008h.

## Alterações introduzidas na versão 1.20

-  Publicado Schema XML através do Pacote de Liberação PL\_008h1, sem alteração de leiaute mas validando os valores possíveis da alíquota interestadual (4%, 7% ou 12%).
-  Melhor documentada a exceção da regra de validação E16a-30.
-  Alterada  a  regra  de  validação  N12-70  criando  uma  exceção  para  operações  de  importação. Alterada a data de implantação para 01-jan-2016.
-  Alterada a regra de validação N12a-70 criando uma exceção para operações de importação e eliminando o CSOSN=300-Imune. Alterada a data de implantação para 01-jan-2016.
-  Alterada a regra de validação N16-20 para não aplicar a validação no caso de devolução de mercadorias
-  Alterada a regra de validação N23-10 aperfeiçoando o controle do ICMS ST para o campo CEST. Esta regra não será implementada no dia 01-01-2016 e sim em data futura a ser divulgada.
-  Alterada a regra de validação NA01-20 para não exigir a informação do grupo de tributação do destino nos casos de devolução de mercadorias remetidas antes de 2016 ou de nota de entrada. Também foi aperfeiçoada a mensagem de rejeição.
-  Alterada a regra de validação NA01-30 criando uma exceção para devolução de não-contribuinte. Também foi aperfeiçoada a mensagem de rejeição.
-  Retirada a regra de validação NA07-10.
-  Alterada a regra de validação NA09-30 para não aplicar a validação nos casos de devolução ou de nota de entrada.

![Image](assets/image_000005_1074f7aa24786bf2e23b8cbbaa860c9d37702b4e3219cd14a4cae15dc9f16500.png)

## Alterações introduzidas na versão 1.30

-  Alterada a regra de validação E16a-30, incluindo a exceção 2, para tratar a informação do ICMSST  retido  anteriormente,  a  ser  aplicada  a  partir  de  01/01/2016,  possibilitando  prazo  para adequação das empresas emissoras de NF-e destinadas a Contribuintes Isentos de Inscrição Estadual.

## Alterações introduzidas na versão 1.40

-  Apresenta a sistemática de cálculo aplicada nas operações e prestações que destinem bens  e serviços a consumidor final, conforme definido na 162ª reunião ordinária da Comissão Técnica Permanente do ICMS - COTEPE, com fundamento na cláusula 2ª do Convênio ICMS 93/2015.
-  Alterada a regra de validação N23-10 obrigando a informação do CEST na NFC-e nas mesmas condições da NF-e.

## Alterações introduzidas na versão 1.50

Esta  versão  da  NT  retira  a  tabela  da  sistemática  de  cálculo  de  base  dupla,  anteriormente aprovada na 159ª. Reunião Ordinária do CONFAZ, uma vez que o Convênio ICMS 152, de 11/12/2015, redefiniu o uso de base de cálculo única a partir do valor da operação. Esta alteração não trará nenhum impacto para as aplicações das Sefaz Autorizadoras e Empresas Emissoras de NF-e, uma vez que desde a versão 1.10 todas as regras de validação, envolvendo o cálculo do ICMS Interestadual, já haviam sido retiradas.

Registramos que todos os ambientes de autorização das Sefaz e o Programa Emissor Gratuito já estão preparados para autorizar NF-e em ambiente de homologação, portanto é importante que as empresas  emissoras  intensifiquem  os  seus  testes,  pois  todos  os  processos  definidos  nesta  Nota Técnica serão implementados, em ambiente de produção, na data definida pela EC 87/2015, ou seja, 01/01/2016.

Conforme sintetizado a seguir, algumas regras de validação também foram aperfeiçoadas para evitar rejeições, facilitando o processo de emissão sem a necessidade de alterações nas aplicações das empresas emissoras:

-  Publicado Schema XML no Pacote de Liberação PL\_008h2, sem alteração de leiaute, eliminando a relação dos códigos da ANP;
-  Incluída regra de validação LA02-10, passando a verificar a existência dos códigos de produto da ANP, conforme tabela atualizada e publicada no site da ANP (existem novos códigos que a versão anterior do Schema não contemplava);
-  Alteradas as regras de validação N12-70, N12-80 e N12a-70 para não aplicar a validação nas operações de entrada nem nos casos de CFOP de conserto ou reparo de mercadoria;
-  Alterada a regra de validação N12a-70 inserindo o CSOSN=300-Imune;
-  Melhor documentada a regra de validação N16-04 especificando as operações de devolução e retorno;
-  Alterada a regra de validação N16-20 para não aplicar a validação nas operações de venda com entrega em terceiro por conta do adquirente (venda à ordem);
-  Alteradas as regras de validação N16-20, NA01-20 e NA09-30 para não aplicar a validação no caso de retorno de mercadorias;
-  Alterada a regra de validação N23-10, retirando a Exceção 2, incluído o CSOSN 500 (ICMS cobrado anteriormente por substituição tributária ou por antecipação) e alterada a condição do CSOSN 900 (Outros) para não considerar os casos em que o campo esteja zerado;
-  Alterada  a  regra  de  validação  NA01-20  para  não  aplicar  a  validação  nas  operações  com lubrificantes ou combustíveis derivados de petróleo;

![Image](assets/image_000006_1a1f9f3eca97c075c79a78e294ebca633b10da49ec587eb400b9258574fca646.png)

-  Alterada a regra de validação NA01-30 para aplicar a validação nas operações com lubrificantes ou combustíveis derivados de petróleo;
-  Estabelece a data da regra de validação do CEST (N23-10) para 01/04/2016 (em ambiente de produção), conforme definido no Convênio ICMS 139/2015.

## Alterações introduzidas na versão 1.60

-  Alterada a observação do campo NA15 para que o valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) não seja somado ao valor do ICMS Interestadual para a UF de destino;
-  Aperfeiçoada a mensagem de rejeição da RV LA02-10;
-  Alteradas as regras de validação N12-70, N12-80 e N12a-70 para não aplicar a validação nos casos de remessa para demonstração dentro do Estado.
-  Alterada a regra de validação N16-20 para não aplicar a validação no caso de anulação de valor;
-  Alteradas as regras de validação N16-20 e NA01-20 para não aplicar a validação nos casos de entrega da mercadoria dentro do Estado;
-  Inseridos CFOP de anulação de valor relativo a aquisição de serviço de transporte no Anexo XIII.05.

Em razão do disposto no inciso II da Cláusula terceira do Convênio ICMS 152/15, que altera o Convênio 93/15, o qual,  por  sua  vez,  dispõe  sobre  os  procedimentos  a  serem  observados  nas operações e prestações que destinem bens e serviços a consumidor final não contribuinte do ICMS, localizado em outra unidade federada,

' Cláusula terceira Acordam os Estados e o Distrito Federal que até 30 de junho de 2016: [...] II - a fiscalização relativa ao descumprimento das obrigações acessórias previstas  neste  Convênio  será  de  caráter  exclusivamente  orientador,  desde  que ocorra o pagamento do imposto',

-  Foi alterado o prazo limite para implantação em produção das seguintes regras de validação: E16a-30,  N12-70,  N12a-70,  N16-04,  N16-20,  NA01-20,  NA09-10,  NA09-20  e  NA09-30,  e,  a critério da UF, a regra N12-80.

A  postergação  do  início  de  aplicabilidade  destas  regras  de  validação  não  implica,  de  nenhuma maneira, a desobrigação ou o adiamento da aplicabilidade dos respectivos dispositivos legais.

## Alterações introduzidas na versão 1.70

-  Alterada a observação do campo W04e esclarecendo que, em consonância com a forma de preenchimento do campo NA15, o valor do ICMS do Fundo de Combate à Pobreza (FCP) não deve ser somado ao valor do ICMS Interestadual para a UF de destino;
-  Incluída regra de validação E16a-40 para rejeitar operação com não contribuinte, que não seja consumidor final;
-  Aperfeiçoado do texto da RV N12-70 para vincular a exceção aplicada às operações internas de remessa em demonstração ao CST de suspensão do imposto, a exemplo do que já ocorria na RV N12-80;
-  Alteradas as RV N12-80 e N16-20 retirando a aplicação opcional por UF de algumas exceções, por ter sido identificado que elas se aplicam a todas as UF;
-  Alteradas as RV N16-04 e N16-20 para identificar se a operação é interestadual pelo identificador de local de destino, tag idDest, ao invés de utilizar o CFOP;
-  Alterado para 01/10/16 o prazo para implantação em produção da regra de validação N23-10 e modificada a condição do CST 90 (Outros) para não considerar os casos em que o campo esteja zerado;

![Image](assets/image_000007_1869533b19c39a83f6ae5c923d3b5e8949664cfb42ac53c7e930432e8ae1178d.png)

-  Alterada a regra de validação NA01-20 para não aplicar a validação nos casos de remessa de mercadoria, de mercadoria não tributada ou imune, nem no caso de alguns CFOP específicos;
-  Alterado para 01/07/16 o prazo para implantação em produção da regra de validação NA01-30 e modificada  a  RV  para  não  aplicar  a  validação  nos  casos  de  entrega  da  mercadoria  fora  do Estado;
-  Orientado o preenchimento do campo de Informações Complementares da NF-e, com os valores totais descritos no grupo de tributação do ICMS para a UF de destino. Incluídos exemplos sobre a apresentação desta informação no DANFE (Item 70);
-  Apresentados exemplos da sistemática de cálculo aplicada nas operações e prestações que destinem bens e serviços a consumidor final não contribuinte  do ICMS,  localizado  em  outra unidade federada, considerando a aplicação da base de cálculo única, conforme estabelecido pelo parágrafo primeiro da cláusula segunda do Convênio ICMS 93/2015 (item 90).

## Alterações introduzidas na versão 1.71

-  Alterada a regra de validação E16a-40 para só aplicar a validação em operações que não sejam com exterior;

## Alterações introduzidas na versão 1.80

-  Alterada a regra de validação E16a-30 para
- o somente aplicar a validação em operações interestaduais;
- o complementar a mensagem de rejeição para especificar essa alteração;
- o não aplicar a validação nos casos de isenção, imunidade ou não-tributação;
-  Alterada a regra N12-70 para
- o possibilitar a discriminação dos acessórios em itens separados na venda de veículos novos;
- o não aplicar  a  validação  em  operações  interestaduais  com  lubrificantes derivados  de petróleo enquadrados no regime de substituição tributária e  antecipação do imposto com o encerramento de tributação;
- o possibilitar devoluções (finNFe=4) em situações de suspensão e diferimento;
-  Alterada a regra NA01-20 para não aplicar a validação nos casos de isenção, imunidade ou não tributação, e nem nos casos de NF-e Complementar ou de Ajuste.

## Alterações introduzidas na versão 1.90

-  Alterada as regras de validação E12-30, E12-40, N16-20 e NA09-30, para:
- o considerar,  quando  existentes,  o  endereço  de  entrega  na  validação  da  UF  do destinatário e o endereço de retirada na validação da UF do emitente,
- o restringir a validação às operações com nota fiscal de saída;
-  Incluídas as regras de validação E12-50 e E12-60 para aplicar, nas operações com nota fiscal de entrada, validação similar à das RV E12-30 e E12-40 (na nota fiscal de entrada, o endereço de  entrega  substitui  o  do  emitente  e  o  endereço  de  retirada  substitui  o  do  destinatário,  ao contrário do que ocorre na nota fiscal de saída);
-  Alterada  a  regra  de  validação  E16a-30  para  considerar  a  UF=PA  como  uma  das  que  não permite a indicação de contribuinte isento de IE nas operações interestaduais;
-  Incluída a regra de validação E16a-35 para evitar, nas operações internas, erro na indicação do destinatário como contribuinte isento de IE em UF que não permite esse tipo de situação;

![Image](assets/image_000008_1a1f9f3eca97c075c79a78e294ebca633b10da49ec587eb400b9258574fca646.png)

## Nota Fiscal eletrônica

-  Alterada a regra de validação N12-70 para:
- o ampliar a abrangência da exceção 2 a todas as operações de remessa ou de retorno de mercadorias;
- o ampliar a abrangência da exceção 5 a todos combustíveis derivados de petróleo;
- o permitir que as operações internas de retorno de mercadoria depositada em depósito fechado ou armazém geral e as operações com CFOP 5.123, 5.922, 6.123 e 6.922 possam ser realizadas com diferimento do imposto;
- o a critério da UF, permitir operações internas com cobrança de ST a não-contribuinte;
-  Alterada a regra de validação N12-80 para:
- o não aplicar a validação nas operações de entrada com CFOP de conserto ou reparo de mercadoria;
- o a critério da UF, permitir operações com diferimento a contribuinte pessoa jurídica isento de inscrição estadual nas operações internas;
-  Alteradas as regras de validação N16-04 e N16-20 para não aplicar a validação:
- o nas operações com veículos novos de venda direta para grandes consumidores ou de faturamento  direto  para  consumidor  final,  quando  existir  ao  menos  um  item  dessas operações;
- o nas operações de venda a ordem (CFOP 6.118, 6.119, 6.122 e 6.123);
-  Alterada  a  regra  de  validação  N23-10  para,  em  ambiente  de  produção,  postergar  para 01/07/2017 a exigência do CEST (Convênio ICMS nº 90 de 2016);
-  Alterada a regra de validação NA01-20 para não aplicar a validação quando o emitente for optante do Simples Nacional (CRT=1);
-  Alteradas  as  regras  de  validação  NA01-20  e  NA01-30  para  incluir  o  Xisto  (código  ANP 560101001) como combustível não derivado de petróleo;
-  Incluídas  as  regras  de  validação  NA15-10  e  NA17-10  para  validar  os  valores  do  ICMS Interestadual para a UF de destino e para a UF do remetente;

## Alterações introduzidas na versão 1.91

-  Regras de validação NA15-10 e NA17-10 ficaram para implementação futura.
-  Corrigidos os códigos de rejeição das RV E16a-35, NA15-10 e NA17-10, para evitar conflitos com outras RV, e alteradas as mensagens de rejeição das RV E16a-30 e E16a-35, para permitir o reaproveitamento de códigos de rejeição.

## Alterações introduzidas na versão 1.92

-  Alterada  a  regra  de  validação  NA11-10  para  considerar  o  ano  da  NF  referenciada  nas operações de devolução ou com CFOP de retorno de mercadorias.

## Alterações introduzidas na versão 1.93

Alterada a regra de validação NA11-10 para também considerar o ano da NF referenciada nas operações com NF complementar ou NF de ajuste.

## Alterações introduzidas na versão 1.94

-  Postergada  a  validação  do  CEST  para  01-abril-2018,  em  atendimento  ao  Convênio  ICMS 60/2017.

NT 2015.003 (ICMS Interestadual)

![Image](assets/image_000009_8e8c60dbdb1d07f75d0283b5be15f29fda00bf3e61db2752322a984fccf4836e.png)

## 01. Resumo

Esta Nota Técnica altera o leiaute da NF-e para receber as informações correspondentes ao ICMS devido  para  a  Unidade  da  Federação  de  Destino,  nas  operações  interestaduais  de  venda  para consumidor final não contribuinte, atendendo as definições da Emenda Constitucional 87/2015.

Também visa atender à necessidade de identificar o Código Especificador da Substituição Tributária - CEST, que estabelece a sistemática de uniformização e identificação das mercadorias e bens passíveis de sujeição aos regimes de substituição tributária e de antecipação de recolhimento do ICMS  com  o  encerramento  de  tributação,  relativos  às  operações  subsequentes,  conforme definições do Convênio ICMS 92, de 20 de agosto de 2015.

O prazo previsto para a implementação das mudanças é:

-  Ambiente de Homologação (ambiente de teste das empresas): 01/10/15;
-  Ambiente de Produção : 01/12/2015.
- o A implantação do novo schema XML em produção será efetuada no dia 30-nov-2015 após às 12h desse dia em todos os ambientes de autorização.
- o A implantação da nova versão da aplicação das SEFAZ autorizadoras será feita no dia 01-dez-2015 até às 12h desse dia em todos os ambientes de autorização.
- Nota 1 : Observado que, embora a publicação em produção esteja prevista para a data 01/12/2015, o novo grupo de informações do ICMS para a UF de destino somente poderá ser utilizado, em produção,  a  partir  de  01/01/2016,  respeitando  a  legislação  vigente.  As  regras  poderão  ser testadas no ambiente de homologação.

Nota 2 : O grupo de tributação do ICMS para a UF de destino poderá ser utilizado para ajustes de lançamentos  realizados  para  consumidor  final  não  contribuinte  de  outras  UFs,  como  por exemplo, nota fiscal de entrada de devoluções de mercadorias emitida pelo remetente da UF de origem.

- O prazo para implantação das alterações trazidas pela versão 1.94 desta NT é:
-  Ambiente de Homologação (ambiente de teste das empresas): 28-jun-2017;
-  Ambiente de Produção : 30-jun-2017.

![Image](assets/image_000010_83c84c36f0017b91b184ef55f1b8717007ddb643c47ed12f90cdf5ad0ccf6922.png)

## 02. Serviço: Autorização de Uso da NF-e / NFC-e (item 4.1 do MOC)

## 2.1 Leiaute da Nota Fiscal Eletrônica

## A. Campo CEST - Código Especificador da Substituição Tributária

Incluído campo CEST (Código Especificador da Substituição Tributária), que estabelece a sistemática de uniformização e identificação das mercadorias e bens passíveis de sujeição aos regimes de substituição tributária e de antecipação de recolhimento do ICMS com o encerramento de tributação, relativos às operações subsequentes, conforme definições do Convênio ICMS 92, de 20 de agosto de 2015

## I. Produtos e Serviços da NF-e

| #    | ID   | Campo   | Descrição                                  | Ele   | Pai   | Tipo   | Ocor.   | Observação                                                                                                                                                                                                                                                |
|------|------|---------|--------------------------------------------|-------|-------|--------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 104d | I05c | CEST    | Código CEST                                | E     | I01   | N      | 0-1     | Tam. 7 Código Especificador da Substituição Tributária - CEST, que estabelece a sistemática de uniformização e identificação das mercadorias e bens passíveis de sujeição aos regimes de substituição tributária e de antecipação de recolhimento do ICMS |
| 110  | I11  | vProd   | Valor Total Bruto dos Produtos ou Serviços | E     | I01   | N      | 1-1     | 13v2 O valor do ICMS faz parte do Valor Total Bruto                                                                                                                                                                                                       |

## B. Grupo de Tributação do ICMS para a UF de destino

Foi criado um novo grupo de informações no item, para identificar o ICMS Interestadual nas operações de venda para consumidor final, atendendo ao disposto na Emenda Constitucional 87 de 2015. Este grupo não deve ser utilizado nas operações com veículos automotores novos efetuadas por meio de faturamento direto para o consumidor (Convênio ICMS 51/00), as quais possuem grupo de campos próprio (ICMSPart).

## NA. ICMS para a UF de destino

| #       | ID   | Campo      | Descrição                                                                        | Ele   | Pai   | Tipo   | Ocor. Tam.   | Observação                                                                                                                                                                                                                                                                                                                         |
|---------|------|------------|----------------------------------------------------------------------------------|-------|-------|--------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 245a.01 | NA01 | ICMSUFDest | Informação do ICMS Interestadual                                                 | G     | M01   | 0-1    |              | Grupo a ser informado nas vendas interestaduais para consumidor final, não contribuinte do ICMS. Observação : Este grupo não deve ser utilizado nas operações com veículos automotores novos efetuadas por meio de faturamento direto para o consumidor (Convênio ICMS 51/00), as quais possuem grupo de campos próprio (ICMSPart) |
| 245a.03 | NA03 | vBCUFDest  | Valor da BC do ICMS na UF de destino                                             | E     | NA01  | N 1-1  | 13v2         | Valor da Base de Cálculo do ICMS na UF de destino.                                                                                                                                                                                                                                                                                 |
| 245a.05 | NA05 | pFCPUFDest | Percentual do ICMS relativo ao Fundo de Combate à Pobreza (FCP) na UF de destino | E     | NA01  | N 1-1  | 3v2- 4       | Percentual adicional inserido na alíquota interna da UF de destino, relativo ao Fundo de Combate à Pobreza (FCP) naquela UF. Nota: Percentual máximo de 2%, conforme a legislação.                                                                                                                                                 |

![Image](assets/image_000011_5c0b2801c787794976165480f5deca11b15e7fd3bcc9ec8606fb84922c29109c.png)

| #       | ID   | Campo          | Descrição                                                                   | Ele   | Pai   | Tipo Ocor.   | Tam.                                                                                                                                                                                                                                                                                         |
|---------|------|----------------|-----------------------------------------------------------------------------|-------|-------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 245a.07 | NA07 | pICMSUFDest    | Alíquota interna da UF de destino                                           | E     | NA01  | N 1-1        | Observação 3v2- 4 Alíquota adotada nas operações internas na UF de destino para o produto / mercadoria. A alíquota do Fundo de Combate a Pobreza, se existente para o produto / mercadoria, deve ser informada no campo próprio (pFCPUFDest) não devendo ser somada à essa alíquota interna. |
| 245a.09 | NA09 | pICMSInter     | Alíquota interestadual das UF envolvidas                                    | E     | NA01  | N 1-1        | 2v2 Alíquota interestadual das UF envolvidas: - 4% alíquota interestadual para produtos importados; - 7% para os Estados de origem do Sul e Sudeste (exceto ES), destinado para os Estados do Norte, Nordeste, Centro-Oeste e Espírito Santo; - 12% para os demais casos.                    |
| 245a.11 | NA11 | pICMSInterPart | Percentual provisório de partilha do ICMS Interestadual                     | E     | NA01  | N 1-1        | 3v2- 4 Percentual de ICMS Interestadual para a UF de destino: - 40% em 2016; - 60% em 2017; - 80% em 2018; - 100% a partir de 2019.                                                                                                                                                          |
| 245a.13 | NA13 | vFCPUFDest     | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) da UF de destino | E     | NA01  | N 1-1        | 13v2 Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) da UF de destino.                                                                                                                                                                                                            |
| 245a.15 | NA15 | vICMSUFDest    | Valor do ICMS Interestadual para a UF de destino                            | E     | NA01  | N 1-1        | 13v2 Valor do ICMS Interestadual para a UF de destino (sem o valor do ICMS relativo ao FCP).                                                                                                                                                                                                 |
| 245a.17 | NA17 | vICMSUFRemet   | Valor do ICMS Interestadual para a UF do remetente                          | E     | NA01  | N 1-1        | 13v2 Valor do ICMS Interestadual para a UF do remetente. Nota: A partir de 2019, este valor será zero.                                                                                                                                                                                       |

## C. Total da Nota Fiscal

Criados  novos  campos  no  grupo  de  totais  da  Nota  Fiscal,  para  identificar  a  distribuição  do  ICMS  Interestadual  para  a  UF  de  destino  na  operação interestadual de venda para consumidor final não contribuinte, atendendo ao disposto na Emenda Constitucional 87 de 2015.

|      # | ID   | Campo        | Descrição                                                                      | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                              |
|--------|------|--------------|--------------------------------------------------------------------------------|-------|-------|--------|---------|--------|---------------------------------------------------------------------------------------------------------|
| 329.03 | W04c | vFCPUFDest   | Valor total do ICMS relativo Fundo de Combate à Pobreza (FCP) da UF de destino | E     | W02   | N      | 0-1     | 13v2   | Valor total do ICMS relativo ao Fundo de Combate à Pobreza (FCP) para a UF de destino.                  |
| 329.05 | W04e | vICMSUFDest  | Valor total do ICMS Interestadual para a UF de destino                         | E     | W02   | N      | 0-1     | 13v2   | Valor total do ICMS Interestadual para a UF de destino (sem o valor do ICMS relativo ao FCP).           |
| 329.07 | W04g | vICMSUFRemet | Valor total do ICMS Interestadual para a UF do remetente                       | E     | W02   | N      | 0-1     | 13v2   | Valor total do ICMS Interestadual para a UF do remetente. Nota: A partir de 2019, este valor será zero. |

![Image](assets/image_000012_5c0b2801c787794976165480f5deca11b15e7fd3bcc9ec8606fb84922c29109c.png)

## 2.2 Regras de Validação (RV) da Nota Fiscal Eletrônica

Resumidamente as mudanças em regras de validação estão relacionadas com o ICMS devido a UF de destino na operação interestadual de venda para consumidor final não contribuinte. Seguem as alterações em regras de validação:

## E. Identificação do Destinatário

| Campo-Seq   |   Modelo Regra de Validação | Modelo Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                          | Aplic.   |   Msg | Efeito   | Descrição Erro                                                        |
|-------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-----------------------------------------------------------------------|
| E12-30      |                          55 | Se Nota Fiscal é de Saída (tpNF=1) e operação é Interestadual (tag:idDest = 2): - UF do destinatário (tag: enderDest/UF) igual à UF do emitente (tag: enderEmit/UF) eCNPJemissor diferentedoCNPJ destinatário (NT 2013/005). Observação : Não rejeitar se existir algum item com a tag UFCons (id:L120) diversa da UF do emitente. Exceção 1: A regra de validação não se aplica se informada UF do local de entrega (tag: entrega/UF) diferente da UF do emitente | Obrig.   |   772 | Rej.     | Rejeição: Operação Interestadual e UF de destino igual à UF de origem |
|             |                             | (tag: enderEmit/UF) e não informada UF do local de retirada (tag: retirada/UF);                                                                                                                                                                                                                                                                                                                                                                                    |          |       |          |                                                                       |
|             |                             | Exceção 2: A regra de validação não se aplica se informada UF do local de retirada (tag: retirada/UF) diferente da UF do destinatário (tag: enderDest/UF) e não informada UF do local de entrega (tag: entrega/UF); Exceção 3: A regra de validação não se aplica se informadas UF do                                                                                                                                                                              |          |       |          |                                                                       |
|             |                             | local de entrega (tag: entrega/UF) e UF do local de retirada (tag: retirada/UF) diferentes entre si;                                                                                                                                                                                                                                                                                                                                                               |          |       |          |                                                                       |
| E12-40      |                          55 | Se Nota Fiscal é de Saída (tpNF=1), operação é Interna no Estado (tag:idDest = 1) e operação não é com Consumidor final: - UF do destinatário (tag: enderDest/UF) difere da UF do emitente (tag: enderEmit/UF). Exceção 1 : Se a tag UFCons (id:LA06) foi informada com a mesma                                                                                                                                                                                    | Obrig.   |   773 | Rej.     | Rejeição: Operação Interna e UF de destino difere da UF de origem     |
|             |                             | UF do emitente não se aplica esta regra (NT 2013/005) Exceção 2: A regra de validação não se aplica se informada UF do                                                                                                                                                                                                                                                                                                                                             |          |       |          |                                                                       |
|             |                             | local de entrega (tag: entrega/UF) igual à UF do emitente (tag: enderEmit/UF) e não informada UF do local de retirada (tag: retirada/UF);                                                                                                                                                                                                                                                                                                                          |          |       |          |                                                                       |
|             |                             | Exceção 3: A regra de validação não se aplica se informada UF do local de retirada (tag: retirada/UF) igual à UF do destinatário (tag: enderDest/UF) e não informada UF do local de entrega (tag: entrega/UF);                                                                                                                                                                                                                                                     |          |       |          |                                                                       |

![Image](assets/image_000013_1463d7876f6080166463963a8326ab9ff14f049c734f620ed42537c6559483fd.png)

| Campo-Seq   |   Modelo Regra de Validação | Modelo Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                       |
|-------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------------------------------------------------------------------------------|
|             |                             | Exceção 4: A regra de validação não se aplica se informadas UF do local de entrega (tag: entrega/UF) e UF do local de retirada (tag: retirada/UF) iguais entre si;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |          |       |          |                                                                                                                      |
| E12-50      |                          55 | Se Nota Fiscal é de Entrada (tpNF=0) e operação é Interestadual (tag:idDest = 2): -UF do destinatário (tag: enderDest/UF) igualàUF do emitente (tag: enderEmit/UF) e CNPJ emissor diferente do CNPJ destinatário. Observação : Não rejeitar se existir algum item com a tag UFCons (id:L120) diversa da UF do emitente. Exceção 1: A regra de validação não se aplica se informada UF do local de entrega (tag: entrega/UF) diferente da UF do destinatário (tag: enderDest/UF) e não informada UF do local de retirada (tag: retirada/UF); Exceção 2: A regra de validação não se aplica se informada UF do local de retirada (tag: retirada/UF) diferente da UF do emitente (tag: enderEmit/UF) e não informada UF do local de entrega (tag: entrega/UF); Exceção 3: A regra de validação não se aplica se informadas UF do local de entrega (tag: entrega/UF) e UF do local de retirada (tag: retirada/UF) diferentes entre si; | Obrig.   |   772 | Rej.     | Rejeição: Operação Interestadual e UF de destino igual à UF de origem                                                |
| E12-60      |                          55 | Se Nota Fiscal é de Entrada (tpNF=0), operação é Interna no Estado (tag:idDest = 1) e operação não é com Consumidor final: - UF do destinatário (tag: enderDest/UF) difere da UF do emitente (tag: enderEmit/UF). Exceção 1 : Se a tag UFCons (id:LA06) foi informada com a mesma UF do emitente não se aplica esta regra; Exceção 2: A regra de validação não se aplica se informada UF do local de entrega (tag: entrega/UF) igual à UF do destinatário (tag: enderDest/UF) e não informada UF do local de retirada (tag: retirada/UF); Exceção 3: A regra de validação não se aplica se informada UF do local de retirada (tag: retirada/UF) igual à UF do emitente (tag: enderEmit/UF) e não informada UF do local de entrega (tag: entrega/UF); Exceção 4: A regra de validação não se aplica se informadas UF do local de entrega (tag: entrega/UF) e UF do local de retirada (tag: retirada/UF) iguais entre si;            | Obrig.   |   773 | Rej.     | Rejeição: Operação Interna e UF de destino difere da UF de origem                                                    |
| E16a-30     |                          55 | Informado destinatário como Contribuinte Isento de Inscrição Estadual (indIEDest=2-ISENTO) em UF que não permite esta situação nas operações interestaduais (idDest=2), conforme abaixo:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Obrig    |   805 | Rej.     | Rejeição: A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual em operações interestaduais. |

![Image](assets/image_000014_adf0b1bacd89cb396f8bf9382262f9d097cceb0d2bf66717f1344209afc0fc96.png)

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                 |
|-------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------------------------------------------------------------------------|
|             |          | - AM, BA, CE, GO, MG, MS, MT, PA, PE, RN, SE, SP Exceção 1 : Esta regra de validação não se aplica quando houver destaque do ICMS-ST (campo vICMSST) em pelo menos um item da NF-e. Exceção 2 : Esta regra de validação não se aplica quando houver informação do ICMS-ST retido anteriormente (campo vICMSSTRet) em pelo menos um item da NF-e. Exceção 3: A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016. Exceção 4: Esta regra de validação não se aplica nas operações isentas (CST=40-Isenta ou CSOSN=103-Isento), imunes ou não tributadas (CST=41-Não tributada, ou CSOSN=300-Imune, ou CSOSN=400-Não tributada pelo Simples Nacional).                                                                                                                  |          |       |          |                                                                                                                |
| E16a-35     |       55 | Informado destinatário como Contribuinte Isento de Inscrição Estadual (indIEDest=2-ISENTO) em UF que não permite esta situação nas operações internas (idDest=1). Exceção 1 : Esta regra de validação não se aplica quando houver destaque do ICMS-ST (campo vICMSST) em pelo menos um item da NF-e. Exceção 2 : Esta regra de validação não se aplica quando houver informação do ICMS-ST retido anteriormente (campo vICMSSTRet) em pelo menos um item da NF-e. Exceção 3: A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016. Exceção 4: Esta regra de validação não se aplica nas operações isentas (CST=40-Isenta ou CSOSN=103-Isento), imunes ou não tributadas (CST=41-Não tributada, ou CSOSN=300-Imune, ou CSOSN=400-Não tributada pelo Simples Nacional). | Facult.  |   805 | Rej.     | Rejeição: A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual em operações internas. |
| E16a-40     |       55 | Informado indicador de IE do Destinatário não-contribuinte (tag: indIEDest=9) e não é operação com consumidor final (tag: indFinal<>1) em operação que não é com exterior (idDest<>3).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Obrig.   |   696 | Rej.     | Rejeição: Operação com não contribuinte deve indicar operação com consumidor final                             |

## LA. Item / Combustível

| Campo-Seq   | Modelo Regra de Validação                                                                                                                                                                                 | Aplic.   |   Msg | Efeito   | Descrição Erro                                          |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------|
| LA02-10     | 55/65 Código do Produto da ANP (tag: cProdANP) inexistente na tabela de codificação de produtos do Sistema de Informações de Movimentação de Produtos (SIMP), disponibilizada pela ANP, para uso na NF-e. | Obrig    |   761 | Rej.     | Rejeição: Código de Produto ANP inexistente [nItem:999] |

![Image](assets/image_000015_adf0b1bacd89cb396f8bf9382262f9d097cceb0d2bf66717f1344209afc0fc96.png)

## N. Item / Tributo: ICMS

| Campo-Seq Modelo Regra de Validação   |   Campo-Seq Modelo Regra de Validação | Campo-Seq Modelo Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Aplic.   |   Msg | Efeito Descrição Erro                                                   |
|---------------------------------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|-------------------------------------------------------------------------|
| N12-70                                |                                    55 | Operação com Não Contribuinte (indIEDest=9) e CST difere da relação abaixo: - 00-Tributada integralmente; - 20-Com redução da Base de Cálculo; - 40-Isenta; - 41-Não tributada; - 60-ICMS cobrado anteriormente por substituição tributária; Exceção 1 : A regra de validação acima não se aplica para NF-e de entrada (tpNF=0-Entrada). Exceção 2 : A regra de validação acima não se aplica, para o CST=50 (Suspensão), nas operações com CFOPdeRetorno de Mercadorias (Anexo XIII.04), nem nas operações com CFOP de Remessa de Mercadorias (Anexo XIII.06), e nem nas operações com CFOP 5.949 ou 6.949. Exceção 3: A regra de validação acima não se aplica quando houver ao menos um item de venda de veículos novos (grupo 'veicProd'). Exceção 4 : A regra de validação não se aplica, em produção, para | Obrig.   |   508 | Rejeição: CST incompatível na operação com Não Contribuinte [nItem:999] |

![Image](assets/image_000016_adf0b1bacd89cb396f8bf9382262f9d097cceb0d2bf66717f1344209afc0fc96.png)

| Campo-Seq Modelo Regra de Validação   |   Campo-Seq Modelo Regra de Validação | Campo-Seq Modelo Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                                     |
|---------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------------------------------------------------------------------------|
| N12-80                                |                                    55 | Operação com Contribuinte Isento de Inscrição Estadual (indIEDest=2) e CST constante na relação abaixo: - 50-Suspensão na cobrança do ICMS; - 51-Diferimento na cobrança do ICMS. Exceção 1 : A regra de validação acima não se aplica para o CST=50- Suspensão, nas operações com CFOP de conserto ou reparo (CFOP 1915, 1916, 2915, 2916, 5915, 5916, 6915 e 6916) ou de remessa para demonstração dentro do Estado (CFOP 1912, 1913, 5912 e 5913). Exceção 2: A regra de validação acima não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016. Exceção 3: A critério da UF, a regra de validação acima não se aplica para CST=51-Diferimento em operações internas (idDest=1)                                                                                                       | Obrig.   |   529 | Rej.     | Rejeição: CST incompatível na operação com Contribuinte Isento de Inscrição Estadual [nItem:999]                                   |
| N12a-70                               |                                    55 | quando o destinatário for Pessoa Jurídica (tag:dest/CNPJ). Operação com Não Contribuinte (indIEDest=9) e CSOSN difere da relação abaixo: - 102-Tributação SN sem permissão de crédito; - 103-Tributação SN, com isenção para faixa de receita bruta; - 300-Imune; - 400-Não tributada pelo Simples Nacional; - 500-ICMS cobrado anteriormente por substituição tributária ou por antecipação; Exceção 1 : A regra de validação acima não se aplica para NF-e de entrada (tpNF=0-Entrada). Exceção 2 : A regra de validação acima não se aplica nas operações com CFOP de conserto ou reparo (CFOP 5915, 5916, 6915 e 6916) ou de remessa para demonstração dentro do Estado (CFOP 5912 e 5913). Exceção 3 : A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016. | Obrig.   |   600 | Rej.     | Rejeição: CSOSN incompatível na operação com Não Contribuinte [nItem:999]                                                          |
| N16-04                                |                                    55 | Validação alíquota do ICMS na operação interestadual de produtos importados (NT 2012/005 e NT2013/006): - Operação Interestadual de Saída (idDest=2 e tpNF=1); - IE do destinatário difere de 'ISENTO' ou nulo; - Origem da mercadoria = 1, 2, 3 ou 8; - CST de ICMS = 00, 10, 20, 70 ou 90; - Data de Emissão igual ou superior a 01/01/2013; - Valor alíquota do ICMS maior do que '4.00' (4 por cento). Exceção 0 : Para as NF-e com Data de Emissão anterior a 01/07/2016, a regra de validação acima não se aplica para destinatário Não Contribuinte (tag:dest/indIEDest=9).                                                                                                                                                                                                                                       | Facult.  |   663 | Rej.     | Rejeição: Alíquota do ICMS com valor superior a 4 por cento na operação de saída interestadual com produtos importados [nItem:999] |

![Image](assets/image_000017_6a7b1cace414b0010c0345e01f0eebbf069ac74a8012fd5c32d815803ea14f37.png)

| Campo-Seq Modelo Regra de Validação   |   Campo-Seq Modelo Regra de Validação | Aplic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |   Msg | Efeito Descrição Erro                                                                    |
|---------------------------------------|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|------------------------------------------------------------------------------------------|
|                                       |                                       | Exceção 1 : A regra acima não se aplica para as operações de Devolução (finNFe=4). Exceção 2 : A regra de validação acima não se aplica para as operações com CFOP de Retorno de Mercadorias (Anexo XIII.04). Exceção 3: A regra de validação acima não se aplica na venda de veículos novos (grupo 'veicProd') se existir ao menos um item de Venda direta para grandes consumidores (tpOp=3), ou de Faturamento direto para consumidor final (tpOp=2). Exceção 4: Para as NF-e com Data de Emissão anterior a 01/07/2016, mesmo que informada a IE do destinatário, a regra de validação acima não se aplica para as operações com os CFOP 6107, 6108 (Não Contribuinte). Exceção 5: A regra de validação acima não se aplica para a NF Complementar (finNFe=2) quando: - Se referenciada uma NF-e, a NF-e referenciada tem a Data de Emissão anterior a 01/01/13; - Se referenciada uma NF modelo 1, a Data de Emissão é anterior a 1301 (tag refNF/AAMM). Exceção 6 : Para as NF-e com Data de Emissão anterior a 01/07/2016, mesmo que informada a IE do destinatário, a regra de validação acima não se aplica para as operações com o CFOP 6.929 - Lançamento relativo a operação registrada em Cupom Fiscal (NT 2013/004). Exceção 7 : A regra de validação acima não se aplica para destinatário Não Contribuinte (tag:dest/indIEDest=9). Exceção 7: A regra de validação acima não se aplica para as |       |                                                                                          |
| N16-20                                |                                    55 | Validação alíquota do ICMS na operação interestadual de Saída Normal: Obrig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |   693 | Rejeição: Alíquota de ICMS superior à definida para a operação interestadual [nItem:999] |

![Image](assets/image_000018_adf0b1bacd89cb396f8bf9382262f9d097cceb0d2bf66717f1344209afc0fc96.png)

| Campo-Seq Modelo Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Aplic.   |   Msg | Efeito   | Descrição Erro                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------|
| Exceção 2: A regra de validação acima não se aplica na venda de veículos novos (grupo 'veicProd') se existir ao menos um item de Venda direta para grandes consumidores (tpOp=3), ou de Faturamento direto para consumidor final (tpOp=2). Exceção 3: A regra de validação não se aplica nas operações de devolução (finNFe=4); Exceção 3 : A regra de validação acima não se aplica para as operações com CFOP de Retorno de Mercadorias ou Anulação de Valor (Anexos XIII.04 e XIII.05). Exceção 4 : A regra de validação acima não se aplica para as operações de venda à ordem (CFOP 6.118, 6.119, 6.122 e 6.123). Exceção 6: A regra de validação acima não se aplica se informada UF do local de entrega (tag: entrega/UF) igual à UF do emitente (tag: emit/enderEmit/UF) nas operações com não contribuinte (indIEDest=9). Exceção 5: A regra de validação não se aplica se informada UF do local de entrega (tag: entrega/UF) diferente da UF do emitente (tag: enderEmit/UF); Exceção 6: A regra de validação não se aplica se informada UF do local de retirada (tag: retirada/UF) diferente da UF do destinatário (tag: enderDest/UF); |          |       |          |                                                        |
| N23-10 55/65 Operação sem informação do campo CEST, e CST ou CSOSN da relação abaixo: -10-tributada com cobrança de ICMS por substituição tributária -30-isenta ou não tributada com cobrança de ICMS por substituição tributária -60-ICMS cobrado anteriormente por substituição tributária -70-com redução de base de cálculo e cobrança de ICMS por substituição tributária -90-outros, desde que com valor de ICMS retido por substituição tributária (tag: vICMSST diferente de zero) .201-tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por substituição tributária -202-tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por substituição tributária -203-isenção de ICMS do Simples Nacional para a faixa de receita, com cobrança do ICMS por substituição tributária -500-ICMS cobrado anteriormente por substituição tributária ou por antecipação;                                                                                                                                                                                                                    | Obrig.   |   806 | Rej.     | Rejeição: Operação com ICMS-ST sem informação do CEST. |

![Image](assets/image_000019_5c0b2801c787794976165480f5deca11b15e7fd3bcc9ec8606fb84922c29109c.png)

| Campo-Seq Modelo Regra de Validação   | Aplic.                                                                                                                                                                                                                                                                                       | Msg   | Efeito Descrição Erro   |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-------------------------|
|                                       | -900-outros, desde que com valor de ICMS retido por substituição tributária (tag: vICMSST diferente de zero). Exceção 1 : A regra de validação não se aplica se informado o Grupo de Partilha do ICMS (campo ICMSPart). Observação: Esta regra entrará em vigor, em produção, em 01/04/2018. |       |                         |

## NA. Item / ICMS para a UF de Destino

| Campo-Seq Modelo Regra de Validação   |   Campo-Seq Modelo Regra de Validação | Campo-Seq Modelo Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Aplic.   |   Msg Efeito Descrição Erro | Msg Efeito Descrição Erro   | Msg Efeito Descrição Erro                                                |
|---------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------|-----------------------------|--------------------------------------------------------------------------|
| NA01-10                               |                                    65 | Informado grupo 'ICMSUFDest' para a NFC-e                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Obrig.   |                         807 | Rej.                        | Rejeição: NFC-e com grupo de ICMS para a UF do destinatário              |
| NA01-20                               |                                    55 | Não informado grupo de ICMS para a UF de Destino (tag:ICMSUFDest): - Operação Interestadual (idDest=2) e - Operação com Consumidor Final (indFinal=1) e - Operação com Não Contribuinte (indIEDest=9) e - Não é operação de prestação de serviços (não existe tag 'ISSQN'). Exceção 1: Esse grupo não deve ser exigido se o Grupo de Partilha do ICMS (campo ICMSPart) estiver preenchido. Exceção 2 : A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016. Exceção 3 : A regra de validação não se aplica para Devolução de Mercadoria (finNFe=4) que referencie Nota Fiscal com chave de acesso anterior a 2016. Exceção 4 : A regra de validação acima não se aplica para as operações com CFOP de Retorno de Mercadorias (Anexo XIII.04). Exceção 5: A regra de validação acima não se aplica nas NF-e de entrada (tpNF=0). Exceção 6 : A regra de validação acima não se aplica nas operações com combustíveis (tag:comb) derivados de petróleo: código ANP diferente de: 820101001, 820101010, 810102001, 810102004, 810102002, 810102003, 810101002, 810101001, 810101003, 220101003, 220101004, 220101002, 220101001, 220101005, 220101006, 560101001. Exceção 7: A regra de validação acima não se aplica se informada UF do local de entrega (tag: entrega/UF) igual à UF do emitente (tag: emit/enderEmit/UF). | Obrig.   |                         694 | Rej.                        | Rejeição: Não informado o grupo de ICMS para a UF de destino [nItem:999] |

![Image](assets/image_000020_adf0b1bacd89cb396f8bf9382262f9d097cceb0d2bf66717f1344209afc0fc96.png)

| Campo-Seq   |   Modelo Regra de Validação | Modelo Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                        |
|-------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------------------------------------|
|             |                             | Exceção 8 : A regra de validação acima não se aplica para as operações com CFOP de Remessa de Mercadoria (Anexo XIII.06). Exceção 9 : A regra de validação acima não se aplica para os CFOP: - 6.552 - Transferência de bem do ativo imobilizado; - 6.922 - Lançamento efetuado a título de simples faturamento decorrente de venda p/ entrega futura; - 6.929 - Lançamento relativo a Cupom Fiscal. Exceção 10 : Esta regra de validação não se aplica nas operações isentas (CST=40-Isenta ou CSOSN=103-Isento), imunes ou não tributadas (CST=41-Não tributada, ou CSOSN=300-Imune, ou CSOSN=400-Não tributada pelo Simples Nacional). Exceção 11 : A regra de validação acima não se aplica nas NF-e complementares (finNFe=2) nem nas de ajuste (finNFe=3). Exceção 12: A regra de validação acima não se aplica para emitentes optantes pelo Simples Nacional (CRT=1).                                                                                                                                                                                                                                           |          |       |          |                                                                                       |
| NA01-30     |                          55 | Informado indevidamente o grupo de ICMS para a UF de Destino (tag:ICMSUFDest): - Não é operação Interestadual (idDest<>2) ou - Não é operação com Consumidor Final (indFinal<>1) ou - Não é operação com Não Contribuinte (indIEDest<>9) ou - Operação de prestação de serviços (existe tag 'ISSQN') ou - Operação com combustível (tag:comb) derivado de petróleo: código ANP diferente de: 820101001, 820101010, 810102001, 810102004, 810102002, 810102003, 810101002, 810101001, 810101003, 220101003, 220101004, 220101002, 220101001, 220101005, 220101006, 560101001, ou - Data de Emissão anterior a 01/01/2016. Exceção 1: A critério da UF a regra de validação acima não se aplica na devolução (finNFe=4) por NFe Avulsa com IE do Emitente=ISENTO. Exceção 2 : A regra de validação acima não se aplica se informada UF do local de entrega (tag: entrega/UF) diferente da UF do emitente (tag: emit/enderEmit/UF). Exceção 3 : A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016. Se informada alíquota interestadual (tag:pICMSInter) de 4% e | Obrig.   |   695 | Rej.     | Rejeição: Informado indevidamente o grupo de ICMS para a UF de destino [nItem:999]    |
| NA09-10     |                          55 | - Origem da mercadoria difere de produto importado (tag:orig<>1,2,3,8) Exceção : A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Obrig.   |   697 | Rej.     | Rejeição: Alíquota interestadual do ICMS com origem diferente do previsto [nItem:999] |

![Image](assets/image_000021_71f969951ad2cc19470a1f881b5efbde7396a413b88684d2bf247de59081dc3a.png)

| Campo-Seq Modelo Regra de Validação   |   Campo-Seq Modelo Regra de Validação | Campo-Seq Modelo Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                               |
|---------------------------------------|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------------------------------------------------------------------|
| NA09-20                               |                                    55 | Se informada alíquota interestadual (tag:pICMSInter) de 7% ou 12% e - Origem da mercadoria de produto importado (tag:orig=1,2,3,8) Exceção : A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Obrig.   |   697 | Rej.     | Rejeição: Alíquota interestadual do ICMS com origem diferente do previsto [nItem:999]                                        |
| NA09-30                               |                                    55 | Se informada alíquota interestadual (tag:pICMSInter) de 7% ou 12% em NF de Saída Normal (tpNF=1 e finNFe=1) e alíquota interestadual incompatível com as UF envolvidas: - 7% para os Estados de origem do Sul e Sudeste, exceto ES, destinado para os Estados do Norte, Nordeste, Centro-Oeste e Espírito Santo; - 12% para os demais casos. Exceção 1: A regra de validação acima não se aplica nas operações de devolução (finNFe=4) Exceção 1 : A regra de validação acima não se aplica para as operações com CFOP de Retorno de Mercadorias (Anexo XIII.04). Exceção 3: A regra de validação acima não se aplica nas NF-e de entrada (tpNF=0) Exceção 2 : A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016. Exceção 3: A regra de validação não se aplica se informada UF do local de entrega (tag: entrega/UF) diferente da UF do emitente (tag: enderEmit/UF); Exceção 4: A regra de validação não se aplica se informada UF do local de retirada (tag: retirada/UF) diferente da UF do destinatário (tag: enderDest/UF); | Obrig.   |   698 | Rej.     | Rejeição: Alíquota interestadual do ICMS incompatível com as UF envolvidas na operação [nItem:999]                           |
| NA11-10                               |                                    55 | Percentual do ICMS Interestadual para a UF de destino (tag:pICMSInterPart) difere do previsto para o ano da Data de Emissão. Observação : Nas operações que não sejam de finalidade de emissão normal (finNFe<>1) ou nas operações com CFOP de Retorno de Mercadorias (Anexo XIII.04) considerar o ano da NF referenciada em substituição ao ano da Data de Emissão. Exceção : A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/01/2016.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Obrig.   |   699 | Rej.     | Rejeição: Percentual do ICMS Interestadual para a UF de destino difere do previsto para o ano da Data de Emissão [nItem:999] |
| NA13-10                               |                                    55 | Valor do ICMS relativo ao Fundo de Combate à Pobreza na UF de destino (tag:vFCPUFDest) difere de: vBCUFDest * pFCPUFDest (*4) Exceção : A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/01/2016.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Obrig.   |   793 | Rej.     | Rejeição: Valor do ICMS relativo ao Fundo de Combate à Pobreza na UF de destino difere do calculado [nItem:999]              |

![Image](assets/image_000022_5c0b2801c787794976165480f5deca11b15e7fd3bcc9ec8606fb84922c29109c.png)

| Campo-Seq   |   Modelo Regra de Validação | Modelo Regra de Validação                                                                                                                                                        | Aplic.   |   Msg | Efeito Descrição Erro                                                                                                                       |
|-------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|---------------------------------------------------------------------------------------------------------------------------------------------|
| NA15-10     |                          55 | Valor do ICMS Interestadual para UF de Destino (tag: vICMSUFDest) difere de vBCUFDest * (pICMSUFDest - pICMSInter) * pICMSInterPart (*4) 1 Observação : implementação futura     | Obrig    |   815 | Rej. Rejeição: Valor do ICMS Interestadual para UF de Destino difere do calculado [nItem:999] (Valor Informado: XXX, Valor Calculado:XXX)   |
| NA17-10     |                          55 | Valor do ICMS Interestadual para a UF do Remetente (tag: vICMSUFRemet) difere de (vBCUFDest * (pICMSUFDest - pICMSInter)) - vICMSUFDest (*4) 2 Observação : implementação futura | Obrig    |   816 | Rej. Rejeição: Valor do ICMS Interestadual para UF do Remetente difere do calculado [nItem:999] (Valor Informado: XXX, Valor Calculado:XXX) |

## W. Total da Nota Fiscal

| Campo-Seq   |   Modelo Regra de Validação | Modelo Regra de Validação                                                                                                                                                       | Aplic.   |   Msg | Efeito Descrição Erro                                                                                                                |
|-------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|--------------------------------------------------------------------------------------------------------------------------------------|
| W04c-10     |                          55 | Total do ICMS relativo Fundo de Combate à Pobreza (FCP) da UF de destino (tag:vFCPUFDest, id:W04c) difere do somatório do valor dos itens (id:NA13)                             | Obrig.   |   798 | Rej. Rejeição: Valor total do ICMS relativo Fundo de Combate à Pobreza (FCP) da UF de destino difere do somatório do valor dos itens |
| W04e-10     |                          55 | Total do ICMS Interestadual para a UF de destino (tag:vICMSUFDest, id:W04e) difere do somatório do valor dos itens (id:NA15). Nota: Considerar o valor Null como sendo zero.    | Obrig.   |   799 | Rej. Rejeição: Valor total do ICMS Interestadual da UF de destino difere do somatório dos itens                                      |
| W04g-10     |                          55 | Total do ICMS Interestadual para a UF do remetente (tag:vICMSUFRemet, id:W04g) difere do somatório do valor dos itens (id:NA17). Nota: Considerar o valor Null como sendo zero. | Obrig.   |   800 | Rej. Rejeição: Valor total do ICMS Interestadual da UF do remetente difere do somatório dos itens                                    |

![Image](assets/image_000023_9b5cbfcf777423a28e50c5891900ebae0b99e2f6bea7cef5ab2ca9543f1a2a9c.png)

## 2.3 CFOP Específicos

Foram inseridas novas tabelas de CFOP especificando os CFOP de retorno de mercadoria, de anulação de valores, e de remessa de mercadoria:

## Anexo XIII - CFOP Específicos Anexo XIII.04 - CFOP de Retorno de Mercadoria 3

|   CFOP | Descrição CFOP de Retorno de Mercadoria                                                                                                                                       |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1.414 | Retorno de produção do estabelecimento, remetida para venda fora do estabelecimento em operação com produto sujeito ao regime de substituição tributária                      |
|  1.415 | Retorno de mercadoria adquirida ou recebida de terceiros, remetida para venda fora do estabelecimento em operação com mercadoria sujeita ao regime de substituição tributária |
|  1.451 | Retorno de animal do estabelecimento produtor                                                                                                                                 |
|  1.452 | Retorno de insumo não utilizado na produção                                                                                                                                   |
|  1.554 | Retorno de bem do ativo imobilizado remetido para uso fora do estabelecimento                                                                                                 |
|  1.664 | Retorno de combustível ou lubrificante remetido para armazenagem                                                                                                              |
|  1.902 | Retorno de mercadoria remetida para industrialização por encomenda                                                                                                            |
|  1.903 | Entrada de mercadoria remetida para industrialização e não aplicada no referido processo                                                                                      |
|  1.904 | Retorno de remessa para venda fora do estabelecimento                                                                                                                         |
|  1.906 | Retorno de mercadoria remetida para depósito fechado ou armazém geral                                                                                                         |
|  1.907 | Retorno simbólico de mercadoria remetida para depósito fechado ou armazém geral                                                                                               |
|  1.909 | Retorno de bem remetido por conta de contrato de comodato                                                                                                                     |
|  1.913 | Retorno de mercadoria ou bem remetido para demonstração                                                                                                                       |
|  1.914 | Retorno de mercadoria ou bem remetido para exposição ou feira                                                                                                                 |
|  1.916 | Retorno de mercadoria ou bem remetido para conserto ou reparo                                                                                                                 |
|  1.921 | Retorno de vasilhame ou sacaria                                                                                                                                               |
|  1.925 | Retorno de mercadoria remetida para industrialização por conta e ordem do adquirente da mercadoria, quando esta não transitar pelo estabelecimento do adquirente              |
|  2.414 | Retorno de produção do estabelecimento, remetida para venda fora do estabelecimento em operação com produto sujeito ao regime de substituição tributária                      |
|  2.415 | Retorno de mercadoria adquirida ou recebida de terceiros, remetida para venda fora do estabelecimento em operação com mercadoria sujeita ao regime de substituição tributária |
|  2.554 | Retorno de bem do ativo imobilizado remetido para uso fora do estabelecimento                                                                                                 |
|  2.664 | Retorno de combustível ou lubrificante remetido para armazenagem                                                                                                              |
|  2.902 | Retorno de mercadoria remetida para industrialização por encomenda                                                                                                            |
|  2.903 | Entrada de mercadoria remetida para industrialização e não aplicada no referido processo                                                                                      |
|  2.904 | Retorno de remessa para venda fora do estabelecimento                                                                                                                         |
|  2.906 | Retorno de mercadoria remetida para depósito fechado ou armazém geral                                                                                                         |
|  2.907 | Retorno simbólico de mercadoria remetida para depósito fechado ou armazém geral                                                                                               |
|  2.909 | Retorno de bem remetido por conta de contrato de comodato                                                                                                                     |
|  2.913 | Retorno de mercadoria ou bem remetido para demonstração                                                                                                                       |
|  2.914 | Retorno de mercadoria ou bem remetido para exposição ou feira                                                                                                                 |
|  2.916 | Retorno de mercadoria ou bem remetido para conserto ou reparo                                                                                                                 |
|  2.921 | Retorno de vasilhame ou sacaria                                                                                                                                               |
|  2.925 | Retorno de mercadoria remetida para industrialização por conta e ordem do adquirente da mercadoria, quando esta não transitar pelo estabelecimento do adquirente              |
|  5.664 | Retorno de combustível ou lubrificante recebido para armazenagem                                                                                                              |
|  5.665 | Retorno simbólico de combustível ou lubrificante recebido para armazenagem                                                                                                    |
|  5.902 | Retorno de mercadoria utilizada na industrialização por encomenda                                                                                                             |
|  5.903 | Retorno de mercadoria recebida para industrialização e não aplicada no referido processo                                                                                      |
|  5.906 | Retorno de mercadoria depositada em depósito fechado ou armazém geral                                                                                                         |
|  5.907 | Retorno simbólico de mercadoria depositada em depósito fechado ou armazém geral                                                                                               |
|  5.909 | Retorno de bem recebido por conta de contrato de comodato                                                                                                                     |

![Image](assets/image_000024_1a1f9f3eca97c075c79a78e294ebca633b10da49ec587eb400b9258574fca646.png)

## Nota Fiscal eletrônica

|   CFOP | Descrição CFOP de Retorno de Mercadoria                                                                                                                            |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  5.913 | Retorno de mercadoria ou bem recebido para demonstração                                                                                                            |
|  5.916 | Retorno de mercadoria ou bem recebido para conserto ou reparo                                                                                                      |
|  5.925 | Retorno de mercadoria recebida para industrialização por conta e ordem do adquirente da mercadoria, quando aquela não transitar pelo estabelecimento do adquirente |
|  6.664 | Retorno de combustível ou lubrificante recebido para armazenagem                                                                                                   |
|  6.665 | Retorno simbólico de combustível ou lubrificante recebido para armazenagem                                                                                         |
|  6.902 | Retorno de mercadoria utilizada na industrialização por encomenda                                                                                                  |
|  6.903 | Retorno de mercadoria recebida para industrialização e não aplicada no referido processo                                                                           |
|  6.906 | Retorno de mercadoria depositada em depósito fechado ou armazém geral                                                                                              |
|  6.907 | Retorno simbólico de mercadoria depositada em depósito fechado ou armazém geral                                                                                    |
|  6.909 | Retorno de bem recebido por conta de contrato de comodato                                                                                                          |
|  6.913 | Retorno de mercadoria ou bem recebido para demonstração                                                                                                            |
|  6.916 | Retorno de mercadoria ou bem recebido para conserto ou reparo                                                                                                      |
|  6.925 | Retorno de mercadoria recebida para industrialização por conta e ordem do adquirente da mercadoria, quando aquela não transitar pelo estabelecimento do adquirente |

## Anexo XIII.05 - CFOP de Anulação de Valor 4

| CFOP Descrição CFOP de Anulação de Valor                               |
|------------------------------------------------------------------------|
| 1.205 Anulação de valor relativo à prestação de serviço de comunicação |
| 1.206 Anulação de valor relativo à prestação de serviço de transporte  |
| 1.207 Anulação de valor relativo à venda de energia elétrica           |
| 2.205 Anulação de valor relativo à prestação de serviço de comunicação |
| 2.206 Anulação de valor relativo à prestação de serviço de transporte  |
| 2.207 Anulação de valor relativo à venda de energia elétrica           |
| 3.205 Anulação de valor relativo à prestação de serviço de comunicação |
| 3.206 Anulação de valor relativo à prestação de serviço de transporte  |
| 3.207 Anulação de valor relativo à venda de energia elétrica           |
| 5.205 Anulação de valor relativo à aquisição de serviço de comunicação |
| 5.206 Anulação de valor relativo à aquisição de serviço de transporte  |
| 5.207 Anulação de valor relativo à compra de energia elétrica          |
| 6.205 Anulação de valor relativo à aquisição de serviço de comunicação |
| 6.206 Anulação de valor relativo à aquisição de serviço de transporte  |
| 6.207 Anulação de valor relativo à compra de energia elétrica          |
| 7.205 Anulação de valor relativo à aquisição de serviço de comunicação |
| 7.206 Anulação de valor relativo à aquisição de serviço de transporte  |
| 7.207 Anulação de valor relativo à compra de energia elétrica          |

## Anexo XIII.06 - CFOP de Remessa de Mercadoria 5

|   CFOP | Descrição CFOP de Remessa de Mercadoria                                                                                                                              |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  5.414 | Remessa de produção do estabelecimento para venda fora do estabelecimento em operação com produto sujeito ao regime de substituição tributária                       |
|  5.415 | Remessa de mercadoria adquirida ou recebida de terceiros para venda fora do estabelecimento, em operação com mercadoria sujeita ao regime de substituição tributária |
|  5.451 | Remessa de animal e de insumo para estabelecimento produtor                                                                                                          |
|  5.501 | Remessa de produção do estabelecimento, com fim específico de exportação                                                                                             |
|  5.502 | Remessa de mercadoria adquirida ou recebida de terceiros, com fim específico de exportação                                                                           |
|  5.504 | Remessa de mercadorias para formação de lote de exportação, de produtos industrializados ou produzidos pelo próprio estabelecimento                                  |
|  5.505 | Remessa de mercadorias, adquiridas ou recebidas de terceiros, para formação de lote de exportação                                                                    |
|  5.554 | Remessa de bem do ativo imobilizado para uso fora do estabelecimento                                                                                                 |

![Image](assets/image_000025_1869533b19c39a83f6ae5c923d3b5e8949664cfb42ac53c7e930432e8ae1178d.png)

## Nota Fiscal eletrônica

## CFOP Descrição CFOP de Remessa de Mercadoria

- 5.657 Remessa de combustível ou lubrificante adquirido ou recebido de terceiros para venda fora do estabelecimento
- 5.663 Remessa para armazenagem de combustível ou lubrificante
- 5.666 Remessa por conta e ordem de terceiros de combustível ou lubrificante recebido para armazenagem
- 5.901 Remessa para industrialização por encomenda
- 5.904 Remessa para venda fora do estabelecimento
- 5.905 Remessa para depósito fechado ou armazém geral
- 5.908 Remessa de bem por conta de contrato de comodato
- 5.910 Remessa em bonificação, doação ou brinde
- 5.911 Remessa de amostra grátis
- 5.912 Remessa de mercadoria ou bem para demonstração
- 5.914 Remessa de mercadoria ou bem para exposição ou feira
- 5.915 Remessa de mercadoria ou bem para conserto ou reparo
- 5.917 Remessa de mercadoria em consignação mercantil ou industrial
- 5.920 Remessa de vasilhame ou sacaria
- 5.923 Remessa de mercadoria por conta e ordem de terceiros, em venda à ordem ou em operações com armazém geral ou depósito fechado
- 5.924 Remessa para industrialização por conta e ordem do adquirente da mercadoria, quando esta não transitar pelo estabelecimento do adquirente
- 5.934 Remessa simbólica de mercadoria depositada em armazém geral ou depósito fechado
- 6.414 Remessa de produção do estabelecimento para venda fora do estabelecimento em operação com produto sujeito ao regime de substituição tributária
- 6.415 Remessa de mercadoria adquirida ou recebida de terceiros para venda fora do estabelecimento, em operação com mercadoria sujeita ao regime de substituição tributária
- 6.501 Remessa de produção do estabelecimento, com fim específico de exportação
- 6.502 Remessa de mercadoria adquirida ou recebida de terceiros, com fim específico de exportação
- 6.504 Remessa de mercadorias para formação de lote de exportação, de produtos industrializados ou produzidos pelo próprio estabelecimento
- 6.505 Remessa de mercadorias, adquiridas ou recebidas de terceiros, para formação de lote de exportação
- 6.554 Remessa de bem do ativo imobilizado para uso fora do estabelecimento
- 6.657 Remessa de combustível ou lubrificante adquirido ou recebido de terceiros para venda fora do estabelecimento
- 6.663 Remessa para armazenagem de combustível ou lubrificante
- 6.666 Remessa por conta e ordem de terceiros de combustível ou lubrificante recebido para armazenagem
- 6.901 Remessa para industrialização por encomenda
- 6.904 Remessa para venda fora do estabelecimento
- 6.905 Remessa para depósito fechado ou armazém geral
- 6.908 Remessa de bem por conta de contrato de comodato
- 6.910 Remessa em bonificação, doação ou brinde
- 6.911 Remessa de amostra grátis
- 6.912 Remessa de mercadoria ou bem para demonstração
- 6.914 Remessa de mercadoria ou bem para exposição ou feira
- 6.915 Remessa de mercadoria ou bem para conserto ou reparo
- 6.917 Remessa de mercadoria em consignação mercantil ou industrial
- 6.920 Remessa de vasilhame ou sacaria
- 6.923 Remessa de mercadoria por conta e ordem de terceiros, em venda à ordem ou em operações com armazém geral ou depósito fechado
- 6.924 Remessa para industrialização por conta e ordem do adquirente da mercadoria, quando esta não transitar pelo estabelecimento do adquirente
- 6.934 Remessa simbólica de mercadoria depositada em armazém geral ou depósito fechado

![Image](assets/image_000026_e8389511cacbddce530d71946d78524b58f80eb0c986ceb65ba0ae4b1c9e6e2f.png)

## 70. SOBRE O DANFE

Não haverá alteração no leiaute do  DANFE, mas as empresas remetentes devem informar, no campo de 'Informações Complementares', os valores descritos no grupo de tributação do ICMS para a UF de destino.

Exemplo 1 de preenchimento do DANFE (1ª situação da sistemática de cálculo descrita a seguir):

```
INFORMAÇÕES COMPLEMENTARES: Valores totais do ICMS Interestadual: DIFAL da UF destino R$216,00 + FCP R$40,00; DIFAL da UF Origem R$324,00.
```

Exemplo 2 de preenchimento do DANFE (2ª situação da sistemática de cálculo descrita a seguir):

```
INFORMAÇÕES COMPLEMENTARES: Valores totais do ICMS Interestadual: DIFAL da UF destino R$156,00 + FCP R$40,00; DIFAL da UF Origem R$234,00.
```

![Image](assets/image_000027_acb66a28f207a626255d3af2729d7bb21b37c28f479a66957b92f911542e3bc3.png)

## 90. Sistemática de Cálculo

A sistemática de cálculo definida abaixo não terá regras de validação aplicadas a partir do dia 01/01/2016, estas só serão aplicadas, posteriormente, conforme deliberação do CONFAZ:

## PREENCHIMENTO DA NF-E E SISTEMÁTICA DE CÁLCULO VENDA INTERESTADUAL PARA CONSUMIDOR FINAL NÃO-CONTRIBUINTE - EC 87/2015 (CONVÊNIO ICMS 93/2015 E NT 003.2015 v. 1.70)

## LEGENDA:

BC: BASE DE CÁLCULO DO ICMS

FCP: FUNDO DE COMBATE À POBREZA DO ESTADO DESTINATÁRIO

ALQ: ALÍQUOTA DO IMPOSTO

ALQ INTER:

ALÍQUOTA INTERESTADUAL APLICÁVEL À OPERAÇÃO OU PRESTAÇÃO

ALQ INTRA:

ALÍQUOTA INTERNA NA UF DE DESTINO APLICÁVEL À OPERAÇÃO OU PRESTAÇÃO

DIFAL:

ICMS CORRESPONDENTE À DIFERENÇA ENTRE A ALÍQUOTA INTERNA DO ESTADO DESTINATÁRIO E A ALÍQUOTA INTERESTADUAL

![Image](assets/image_000028_33bc90e3d0b38c2d35755a3212489879b66d1b89881673a0582970b00df7fd1c.png)

## 1ª SITUAÇÃO:

## OPERAÇÕES SUJEITAS À ALÍQUOTA INTERESTADUAL DE 7%

( DE: Sul/Sudeste (exceto ES), E - PARA: Norte/Nordeste/Centro-Oeste/ES)

Operação: ALÍQUOTA INTERESTADUAL DE 7%

VALOR DA OPERAÇÃO

BASE DE CÁLCULO-BC

ALÍQUOTA INTERESTADUAL

ALÍQUOTA INTERNA NO DESTINO

ALÍQUOTA FCP NO DESTINO

ICMS ORIGEM

ICMS DIFAL

PARTILHA DO DIFAL

2016 - 40% PARA DESTINO

ALQ INTER

ALQ INTRA

ALQ FCP

BC * ALQ INTER

[BC * ALQ INTRA] - [BC * ALQ INTER]

PARTILHA DESTINO

PARTILHA ORIGEM

(truncar o resultado

da multiplicação)

40%

60%

ITEM 1

(Importado)

R$   1.000,00

4%

18%

R$         40,00

R$      140,00

R$         56,00

R$         84,00

## PREENCHIMENTO DA NOTA FISCAL ELETRÔNICA - NF-E

| GRUPO        | ICMSUFDest     | ICMSUFDest       | ICMSUFDest   | ICMSUFDest   | ICMSUFDest   | ICMSUFDest   |
|--------------|----------------|------------------|--------------|--------------|--------------|--------------|
| Campos       | vBCUFDest      |                  | R$ 1.000,00  | R$ 1.000,00  | R$ 1.000,00  | R$ 1.000,00  |
|              | pFCPUFDest     |                  | 0%           | 0%           | 2%           | 2%           |
|              | pICMSUFDest    |                  | 18%          | 18%          | 18%          | 25%          |
|              | pICMSInter     |                  | 4%           | 7%           | 7%           | 7%           |
|              | pICMSInterPart | 40% em 2016      | 40%          | 40%          | 40%          | 40%          |
|              | vFCPUFDest     | [vBCUFDest * 2%] | R$ 0,00      | R$ 0,00      | R$ 20,00     | R$ 20,00     |
|              | vICMSUFDest    | (PART DEST)      | R$ 56,00     | R$ 44,00     | R$ 44,00     | R$ 72,00     |
|              | vICMSUFRemet   | (PART ORIGEM)    | R$ 84,00     | R$ 66,00     | R$ 66,00     | R$ 108,00    |
| GRUPO        | ICMSTot        |                  |              |              |              |              |
| Campos (tag) | vFCPUFDest     | (soma dos itens) | R$ 40,00     | R$ 40,00     | R$ 40,00     | R$ 40,00     |
| Campos (tag) | vICMSUFDest    | (soma dos itens) | R$ 216,00    | R$ 216,00    | R$ 216,00    | R$ 216,00    |
| Campos (tag) | vICMSUFRemet   | (soma dos itens) | R$ 324,00    | R$ 324,00    | R$ 324,00    | R$ 324,00    |

ITEM 2

(18%)

R$   1.000,00

7%

18%

R$         70,00

R$      110,00

R$         44,00

R$         66,00

ITEM 3

(18% + FCP)

R$   1.000,00

7%

18%

2%

R$         70,00

R$      110,00

R$         44,00

R$         66,00

ITEM 4

(25% + FCP)

R$   1.000,00

7%

25%

2%

R$         70,00

R$      180,00

R$         72,00

R$      108,00

![Image](assets/image_000029_5c0b2801c787794976165480f5deca11b15e7fd3bcc9ec8606fb84922c29109c.png)

## 2ª SITUAÇÃO:

## OPERAÇÕES SUJEITAS À ALÍQUOTA INTERESTADUAL DE 12%

(DE: Norte/Nordeste/Centro-Oeste/ES, OU - PARA: Sul/Sudeste (exceto ES))

| Operação: ALÍQUOTA INTERESTADUAL DE 12%   | Operação: ALÍQUOTA INTERESTADUAL DE 12%   | Operação: ALÍQUOTA INTERESTADUAL DE 12%   | ITEM 1 (Importado)   | ITEM 1 (Importado)   | ITEM 2 (18%) ITEM (18% +   | ITEM 2 (18%) ITEM (18% +   | 3 FCP) ITEM    | 3 FCP) ITEM    | 4 (25% + FCP)   |
|-------------------------------------------|-------------------------------------------|-------------------------------------------|----------------------|----------------------|----------------------------|----------------------------|----------------|----------------|-----------------|
| VALOR DA OPERAÇÃO                         | BASE DE CÁLCULO-BC                        |                                           | R$ 1.000,00          | R$ 1.000,00          | R$                         | 1.000,00                   | R$ 1.000,00 R$ | R$ 1.000,00 R$ | 1.000,00        |
| ALÍQUOTA INTERESTADUAL                    | ALQ INTER                                 |                                           | 4%                   |                      | 12%                        |                            | 12%            |                | 12%             |
| ALÍQUOTA INTERNA NODESTINO                | ALQ INTRA                                 |                                           |                      | 18%                  | 18%                        |                            | 18%            |                | 25%             |
| ALÍQUOTA FCP NODESTINO                    | ALQ FCP                                   |                                           |                      |                      |                            |                            | 2%             |                | 2%              |
| ICMS ORIGEM                               | BC * ALQ INTER                            | (truncar o resultado da multiplicação)    | R$                   | 40,00                | R$                         | 120,00                     | R$ 120,00      | R$             | 120,00          |
| ICMS DIFAL                                | [BC * ALQ INTRA] - [BC * ALQ INTER]       | (truncar o resultado da multiplicação)    | R$                   | 140,00               | R$                         | 60,00                      | R$ 60,00       | R$             | 130,00          |
| PARTILHA DO DIFAL                         |                                           |                                           |                      |                      |                            |                            |                |                |                 |
| 2016 - 40% PARA DESTINO                   | PARTILHA DESTINO                          | 40%                                       | R$                   | 56,00                | R$                         | 24,00                      | R$ 24,00       | R$             | 52,00           |
| 2016 - 40% PARA DESTINO                   | PARTILHA ORIGEM                           | 60%                                       | R$                   | 84,00                | R$                         | 36,00                      | R$ 36,00       | R$             | 78,00           |

## PREENCHIMENTO DA NOTA FISCAL ELETRÔNICA - NF-E

| GRUPO        | ICMSUFDest     | ICMSUFDest       | ICMSUFDest   | ICMSUFDest   | ICMSUFDest   | ICMSUFDest   |
|--------------|----------------|------------------|--------------|--------------|--------------|--------------|
| Campos (tag) | vBCUFDest      |                  | R$ 1.000,00  | R$ 1.000,00  | R$ 1.000,00  | R$ 1.000,00  |
|              | pFCPUFDest     |                  | 0%           | 0%           | 2%           | 2%           |
|              | pICMSUFDest    |                  | 18%          | 18%          | 18%          | 25%          |
|              | pICMSInter     |                  | 4%           | 12%          | 12%          | 12%          |
|              | pICMSInterPart | 40% em 2016      | 40%          | 40%          | 40%          | 40%          |
|              | vFCPUFDest     | [vBCUFDest * 2%] | R$ 0,00      | R$ 0,00      | R$ 20,00     | R$ 20,00     |
|              | vICMSUFDest    | (PART DEST)      | R$ 56,00     | R$ 24,00     | R$ 24,00     | R$ 52,00     |
|              | vICMSUFRemet   | (PART ORIGEM)    | R$ 84,00     | R$ 36,00     | R$ 36,00     | R$ 78,00     |
| GRUPO        | ICMSTot        |                  |              |              |              |              |
| Campos (tag) | vFCPUFDest     | (soma dos itens) | R$ 40,00     | R$ 40,00     | R$ 40,00     | R$ 40,00     |
|              | vICMSUFDest    | (soma dos itens) | R$ 156,00    | R$ 156,00    | R$ 156,00    | R$ 156,00    |
|              | vICMSUFRemet   | (soma dos itens) | R$ 234,00    | R$ 234,00    | R$ 234,00    | R$ 234,00    |