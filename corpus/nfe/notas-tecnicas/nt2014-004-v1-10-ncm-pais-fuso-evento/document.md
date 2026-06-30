---
title: "Projeto Nota Fiscal Eletrônica - NF-e"
slug: "nt2014-004-v1-10-ncm-pais-fuso-evento"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "90fb4944e0b19a5404d184db81f468e2d251a3e004e8189ab231764dfd057b06"
converted_at_utc: "2026-06-25T16:09:50.175690+00:00"
status: "published"
type: "nota_tecnica"
---

## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2014-004-v1-10-ncm-pais-fuso-evento/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2014-004-v1-10-ncm-pais-fuso-evento/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2014-004-v1-10-ncm-pais-fuso-evento.md)
- [Proveniência resumida](../../../../sources/provenance/nt2014-004-v1-10-ncm-pais-fuso-evento.json)

## Projeto Nota Fiscal Eletrônica - NF-e

![Image](assets/image_000001_79553d5481d20260de472eb44946c7eff315fab133f018f50863a03c74ee8b3d.png)

Nota Técnica 2014/004

## Validação NCM Novos códigos de País Fuso horário do Evento da NF-e Mensagem de consulta da NF-e

![Image](assets/image_000002_3a2f19248942900389f60e711a14426e14449c03475494178cc3c2184146f506.png)

Versão 1.10 Agosto 2014

![Image](assets/image_000003_af93093f6ff4a0d78b974281849ea8750081ea50a10f3cc2af3e0f2d6cb09b51.png)

## Histórico de Alterações

## Alterações efetuadas na versão 1.10

-  Incluídas orientações sobre os locais onde podem ser encontradas instruções e informações sobre a correta classificação segundo a NCM;
-  Incluída  a  possibilidade  de  informar  o  código  '00000000'  para  a  NCM,  quando  o  item  da nota se referir a mercadoria ou outra operação que não possa ser classificada segundo a tabela da NCM;
-  Alterado o Schema XML para não acusar falha de Schema quando for informado o código '00000000'.

## 1.  Resumo

Esta Nota Técnica aborda os seguintes itens:

-  Obrigatoriedade de informação do NCM em cada item da NF-e;
-  Alteração do Schema da NF-e, permitindo a informação de novos códigos de País, conforme alteração correspondente na tabela de países do Banco Central;
-  Alteração  do Schema de  Eventos  da  NF-e  permitindo  a  informação  de  Data  e  Hora  de qualquer região do mundo (faixa de horário UTC de -11:00 a +12:00) e não apenas as faixas de horário do Brasil;
-  Alteração do Schema da NF-e para não acusar falha na consulta situação da NF-e caso seja consultada uma chave de acesso enviada na versão 3.10 da NF-e utilizando a mensagem de consulta na versão 2.01.

## 2.  Prazos

Os prazos previstos para entrada em operação destas alterações são os seguintes:

-  Alteração do Schema da NF-e para códigos de país: já  foi  implementada em produção pelas SEFAZ Autorizadoras;
-  Alteração do Schema da  NF-e e Schema de  Eventos: a  utilização  dos novos Schemas pelas SEFAZ Autorizadoras deverá ser efetivada o mais cedo possível, já que esta mudança não traz impacto para os serviços de autorização de uso das SEFAZ, nem das empresas;
-  Mudanças em regras de validação:
- o Ambiente de Homologação (ambiente de teste das empresas): 15/07/14;
- o Ambiente de Produção : 01/08/14.

Nota: As regras de validação têm o objetivo de auxiliar o contribuinte a montar corretamente o arquivo  XML  da  NF-e.  O  fato  de  as  regras  de  validação  serem  implementadas  nos respectivos sistemas autorizadores em data posterior ao início da vigência da legislação não autoriza o descumprimento desta legislação.

![Image](assets/image_000004_7dee0d807cdea73d11ece2421bb42def4e3c8150ea5f52d16b75afe7df8aa0ef.png)

## 3.  Obrigatoriedade de informação do NCM

O Ajuste SINIEF 22/13, publicado em 06/12/2013, estabelece que a partir de 01 de Julho de 2014, para  o  modelo  55,  e  a  partir  de  01  de  janeiro  de  2015,  para  o  modelo  65,  a  identificação  das mercadorias na NF-e deverá conter o seu correspondente código estabelecido na Nomenclatura Comum do Mercosul (NCM) completo, não sendo mais aceita a possibilidade de informar apenas o capítulo (dois dígitos).

Serão implementadas regras de validação para exigir, em um primeiro momento, o preenchimento de  oito  dígitos  no  campo  relativo  ao  código  NCM  (regra  GI05).  Em  futuro  próximo  será implementada  a  validação  GI05.1,  e  somente  serão  aceitos  valores  de  NCM  que  existam  na tabela  correspondente,  publicada  pelo  Ministério  do  Desenvolvimento,  Indústria  e  Comércio Exterior - MDIC.

Detalhes  sobre  esta  Nomenclatura,  incluindo  a  estrutura  da  codificação  e  todos  os  códigos disponíveis  para  utilização  podem  ser  encontrados  na  página  do  MDIC,  nos  itens  'Regras  de interpretação' e 'Notas Explicativas do Sistema Harmonizado de Codificação e Classificação de Mercadorias  (NESH)'.  Em  especial,  as  mercadorias  que  não  possam  ser  classificadas  por aplicação  das  Regras  acima  enunciadas  classificam-se  na  posição  correspondente  aos  artigos mais semelhantes.

A solução de consultas sobre classificação fiscal de mercadorias é de competência da Receita Federal  do  Brasil  (RFB),  por  intermédio  da  Coordenação-Geral  do  Sistema  Aduaneiro  e  da Superintendência Regional da Receita Federal. Em caso de dúvidas sobre a correta classificação fiscal  de  mercadorias,  o  interessado  deverá  contatar  a  Unidade  da  Receita  Federal  do  seu domicílio fiscal, formulando consulta por escrito, de acordo com as orientações constantes no site dessa Secretaria, na seguinte página: http://www.receita.fazenda.gov.br/guiacontribuinte/consclassfiscmerc.htm .

## Outros esclarecimentos:

1.  Caso o item da nota se refira a um serviço tributado pelo ISS ou a nota seja de ajuste, neste campo deverá ser informado o código '00' (dois zeros)
2.  Em caso de nota complementar que se refira a um daqueles dois casos também poderá ser informado o código '00' neste campo
3.  Se o item da nota se referir a mercadoria ou outra operação que não possa ser classificada segundo a tabela da NCM, seguidas as normas do MDIC, este campo deverá ser preenchido com o código '00000000' (oito zeros)

Alterado  o Schema XML  para  não  acusar  falha  de Schema quando  for  informado  o  código '00000000'.

## 4.  Novos códigos de país

Alteração do Schema XML da NF-e permitindo a informação de novos códigos de País, conforme alteração correspondente na tabela de países do Banco Central. Os novos Países são:

-  5780 - Palestina;
-  7600 - Sudão do Sul.

Esta alteração de Schema foi publicada no Portal da NF-e faz algum tempo e já foi adotada pelas SEFAZ, evitando a rejeição de NF-e para as empresas que comercializam com estes países; a publicação nesta Nota Técnica visa a documentar a alteração já realizada.

![Image](assets/image_000005_7df8b82e85de57e93d087b98a638d3121b8d5beb2f40a8893de3eb85081bf22e.png)

## 5.  Informação de Data e Hora de qualquer região do mundo

A faixa de fusos horários do Brasil compreende também o fuso de -05:00 horas, que passou a ser adotado pelo Acre em 10/11/2013. Para atender esta realidade, foi alterado o Schema de Eventos da NF-e permitindo a informação de Data e Hora de qualquer região do mundo (faixa de horário UTC de -11:00 a +12:00).

Nota : A  possibilidade  de  informar  qualquer  fuso  horário  permite  que  as  empresas  utilizem  o horário do seu equipamento servidor, mesmo que este equipamento esteja localizado em outro País.

## 6.  Consulta Situação da NF-e

Algumas empresas conferem o Schema das  mensagens de resposta enviadas pelo Serviço de Autorização  da  SEFAZ.  No  caso  da  Consulta  Situação  da  NF-e,  se  a  empresa  estiver  ainda usando a versão antiga do leiaute (versão 2.01) ela detecta um erro de Schema caso a Chave de Acesso consultada corresponda a uma NF-e da nova versão do leiaute (versão 3.10).

Alterado o Schema XML da Consulta Situação para não acusar falha de Schema nesta situação.

![Image](assets/image_000006_b614d8c97391e3ec0c4a1cba6cb332e85e2c89cfd98b0575311c74d7984a6c68.png)

## 7.  Alteração na documentação do Leiaute da NF-e (Anexo I do MOC)

## Campo NCM

|   # | ID   | Campo   | Descrição                 | Ele   | Pai   | Tipo   | Ocorrência   | tamanho   | Dec   | Observação                                                                                                                                                                                                                |
|-----|------|---------|---------------------------|-------|-------|--------|--------------|-----------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 104 | I05  | NCM     | Código NCM com 8 dígitos. | E     | I01   | N      | 1-1          | 2, 8      |       | Obrigatória informação do NCM completo (8 dígitos). Nota: Em caso de item de serviço ou item que não tenham produto (ex. transferência de crédito, crédito do ativo imobilizado, etc.), informar o valor 00 (dois zeros). |

## 8.  Regras de Validação da NF-e - Versão 2.00 (item 4.1.9.4 do MOC)

## 8.1.  Validação do Código NCM

| #      | Campo   | Regra de validação                                                                                                                                                                                                                                                                                                           | Aplic.   |   Msg | Efeito   | Descrição Erro                                     |
|--------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------------|
| GI05   | I05     | Deve ser informado o NCM para cada item da NF-e (NCM completo, com 8 posições). Exceção : no caso de item de Serviço ou item que não tenha produto (ex. transferência de crédito, crédito do ativo imobilizado, etc.), informar o valor '00' (zeros).                                                                        | Obrig.   |   777 | Rej.     | Rejeição: Obrigatória a informação do NCM completo |
| GI05.1 | I05     | Se informado NCM completo (8 posições): - NCM inexistente na tabela de NCM publicada pelo Ministério do Desenvolvimento, Indústria e Comércio Exterior - MDIC. Nota: Implementação futura.                                                                                                                                   | Obrig.   |   778 | Rej.     | Rejeição: Informado NCM inexistente.               |
| G105.2 | I05     | Se informado NCM = '00': - Não é uma NF-e de Ajuste (tag:finfe <> 3) e não é um item de serviço (item não possui a tag:ISSQN) Nota: A UF autorizadora que aceitar o uso da NF-e modelo 55 para documentar prestações de serviços ocorridas dentro do campo de incidência do ICMS poderá definir outras exceções a esta regra | Obrig.   |   471 | Rej.     | Rejeição: Informado NCM=00 indevidamente           |

![Image](assets/image_000007_f95ba834b37fbc808f5d4630d1fbd4647e0d304adc121c364e368f61dc615cc9.png)

## 8.2.  Desativadas as Regras de Validação

A obrigatoriedade geral da informação do NCM descrita no item anterior permite a desativação das regras de validação que verificavam esta situação em algumas situações específicas (CFOP de operação com exterior e tributação pelo IPI).

Eliminadas as regras de validação abaixo:

| #      | Campo   | Regra de validação                                                                                                                                                                                | Aplic.   |   Msg | Efeito   | Descrição Erro                                                          |
|--------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-------------------------------------------------------------------------|
| GI08.6 | I08     | CFOP de Operação com Exterior (inicia por 3 ou 7) e não informada TAG NCM (id:I05) completo (8 posições) Exceção : O item de Serviço da NF-e (id:U01) conjugada pode ter NCM = '00' ([NT 2010/010](../nt2010-010/document.md)) | Facult.  |   524 | Rej.     | Rejeição: CFOP de Operação com Exterior e não informado NCM completa    |
| GO07   | O07     | Informada tributação do IPI (id:O07) sem informar a TAG NCM (id:I05) completo (8 posições)                                                                                                        | Facult.  |   529 | Rej.     | Rejeição: NCM de informação obrigatória para produto tributado pelo IPI |

## 9.  Regras de Validação da NF-e - Versão 3.10 ([NT 2013.005](../nt2013-005-v1-22/document.md), Anexo II-Regras de Validação)

## 9.1.  Validação do Código NCM

| Campo-Seq#   | Modelo   | Regra de validação                                                                                                                                                                                                                                                                                                           | Aplic.   |   Msg | Efeito   | Descrição Erro                                     |
|--------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------------|
| I05-10       | 55/65    | Deve ser informado o NCM para cada item da NF-e (NCM completo, com 8 posições). Exceção : no caso de item de Serviço ou item que não tenha produto (ex. transferência de crédito, crédito do ativo imobilizado, etc.), informar o valor '00' (zeros).                                                                        | Obrig.   |   777 | Rej.     | Rejeição: Obrigatória a informação do NCM completo |
| I05.20       | 55/65    | Se informado NCM completo (8 posições): - NCM inexistente na tabela de NCM publicada pelo Ministério do Desenvolvimento, Indústria e Comércio Exterior - MDIC. Nota: Implementação futura.                                                                                                                                   | Obrig.   |   778 | Rej.     | Rejeição: Informado NCM inexistente.               |
| 105.24       | 55/65    | Se informado NCM = '00': - Não é uma NF-e de Ajuste (tag:finfe <> 3) e não é um item de serviço (item não possui a tag:ISSQN) Nota: A UF autorizadora que aceitar o uso da NF-e modelo 55 para documentar prestações de serviços ocorridas dentro do campo de incidência do ICMS poderá definir outras exceções a esta regra | Obrig.   |   471 | Rej.     | Rejeição: Informado NCM=00 indevidamente           |

![Image](assets/image_000008_b614d8c97391e3ec0c4a1cba6cb332e85e2c89cfd98b0575311c74d7984a6c68.png)

## 9.2.  Desativadas as Regras de Validação

A obrigatoriedade geral da informação do NCM descrita no item anterior permite a desativação das regras de validação que verificavam esta situação em algumas situações específicas (CFOP de operação com exterior e tributação pelo IPI).

Eliminadas as regras de validação abaixo:

| Campo-Seq#   | Modelo   | Regra de validação                                                                                                                                                                                | Aplic.   |   Msg | Efeito   | Descrição Erro                                                          |
|--------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-------------------------------------------------------------------------|
| I08-100      | 55       | CFOP de Operação com Exterior (inicia por 3 ou 7) e não informada TAG NCM (id:I05) completo (8 posições) Exceção : O item de Serviço da NF-e (id:U01) conjugada pode ter NCM = '00' ([NT 2010/010](../nt2010-010/document.md)) | Facult.  |   524 | Rej.     | Rejeição: CFOP de Operação com Exterior e não informado NCM completa    |
| O07-10       | 55/65    | Informada tributação do IPI (id:O07) sem informar a TAG NCM (id:I05) completo (8 posições)                                                                                                        | Facult.  |   529 | Rej.     | Rejeição: NCM de informação obrigatória para produto tributado pelo IPI |
| I05-40       | 55/65    | Se informado Capítulo do NCM (2 posições): - Capítulo do NCM inválido (77, 98, 99)                                                                                                                | Obrig.   |   779 | Rej.     | Rejeição: Informado Capítulo do NCM inexistente                         |

## Documentos relacionados
_Nenhum documento relacionado conhecido._
