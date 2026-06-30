---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2011-005"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "a232d8ed462e67080446bb74797e25f49abbf556cd230f774ce7e2e1a2b4f12d"
converted_at_utc: "2026-06-25T14:54:06.827178+00:00"
status: "published"
type: "nota_tecnica"
---

## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2011-005/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2011-005/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2011-005.md)
- [Proveniência resumida](../../../../sources/provenance/nt2011-005.json)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_568d3a48617eba6f1a4d192fa218119703fefe442b888f96f3e8b901e63d3d76.png)

Nota Técnica 2011/005

Divulga informações complementares necessárias para implantação da [NT 2011/004](../nt2011-004/document.md) em produção

![Image](assets/image_000002_cbb651cb4ed2e9b6ed9bd55360445781a822ec51f3774c31a835e143776b2ef2.png)

Outubro-2011

![Image](assets/image_000003_bb754588b2e6d203381e8be74af40ed277607ec0772b71c47d30aabea0b38070.png)

## 1.  Resumo

Esta edição divulga as informações complementares n ecessárias para implantação da [NT 2011/004](../nt2011-004/document.md) em produção:

- Data da implantação da [NT 2011/004](../nt2011-004/document.md) em produção - a [NT 2011/004](../nt2011-004/document.md) será  implantada  em  produção  em  01/11/2011,  exceto  a s  seguintes regras de validação que serão implantadas a partir  de 01/02/2012:
- o GI10a Validação do valor unitário de comercialização do item do produto - código de rejeição: 629;
- o GI14a  Validação  do  valor  unitário  de  tributação  do  item  do produto - código de rejeição: 630;
- o GW16 - Validação do valor total da NF - código de rejei ção: 610.
- Aperfeiçoamento  do  Schema  XML  do  campo  placa  do  veículo  e placa do reboque - aperfeiçoamento para possibilitar a informação d as placas dos veículos estrangeiros utilizados nas ope rações de exportação e importação de mercadorias, o PL\_006j.zip deve sub stituir o PL\_006i.zip imediatamente.
- Aperfeiçoamento  das  regras  de  validação  GI10a,  GI14 a  e  GW16 -estas regras serão aplicadas em produção em 01/02/1 2 .

![Image](assets/image_000004_7b87083748ea063b4562401c68494993ee1370a49ecee64ce0eaefaff0318912.png)

## 2.  Implantação da [NT 2011/004](../nt2011-004/document.md) em produção

Os aperfeiçoamentos de schema XML da NF-e e das regras de validação da [NT 2011/004](../nt2011-004/document.md) serão implantadas n o ambiente de produção em 01/11/2011, exceto as seguintes regras de validação que serão implantadas em 01/02/2012:

- GI10a - Validação do valor unitário de comercialização do item do produto - código de rejeição: 629;
- GW16 - Validação do valor total da NF - código de rejei ção: 610.
- GI14a - Validação do valor unitário de tributação do item do produto - código de rejeição: 630;

## 3.  Aperfeiçoamento de Schema XML da NF-e

## 'item 2.9 Placa (X19/X23) - Placa do Veículo/Placa  do Reboque'

|   374 | X19   | placa   | Placa do Veículo   | E   | X18   | C   | 1-1   | 6-7   | Inf ormar em um dos seguintes formatos: XXX9999, XXX999, XX9999 ou XXXX999 Informar a placa em informações complementares quando a placa do veículo tenha lei de formação diversa. (NT2011/005)   |
|-------|-------|---------|--------------------|-----|-------|-----|-------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   378 | X23   | placa   | Placa do Veículo   | E   | X22   | C   | 1-1   | 6-7   | Inf ormar em um dos seguintes formatos: XXX9999, XXX999, XX9999 ou XXXX999 Informar a placa em informações                                                                                        |

![Image](assets/image_000005_65ce9c768f72f72fc2a86d024ad7dd748eed03b643611a70f23aea76509f881c.png)

| complementares quando a placa do veículo tenha lei de formação diversa. (NT2011/005)   |
|----------------------------------------------------------------------------------------|

Alteração  do  Schema  XML  para  padronização  do  preenc himento  da  placa  do  veículo.  As  placas  de  veículos  brasileiros  devem  ser informadas no formato XXX9999, o PL\_006j.zip deve substituir o PL\_006i.zip imediatamente.

Nas operações de comércio exterior cujo transporte seja realizado por veículo estrangeiro, as placas d os veículos devem ser informadas em um dos seguintes formatos:

- XXX999 (Argentina, Paraguai e Uruguai);
- XXXX999 (Colômbia e Uruguai);
- XX9999 (Chile e Uruguai);

A placa do veículo estrangeiro deverá ser informada em  informações  complementares  quando for diferente  dos formatos  XXX9999, XXX999, XX9999 ou XXXX999.

## 4.  Aperfeiçoamento das Regras de Validação

## 'item 4.4 Validação dos Valores Unitários de Comerc ialização e de Tributação do item de produto'

| #          | Campo Regra de Validação                                                              | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                     |
|------------|---------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------------------------------------------------|
| GI10a I10a | Se NF-e Normal (finNFe=1) : vProd (id:I11) difere de vUnCom (id:I10a) * qCom (id:I10) | Facult.  |   629 | Rej.     | Rejeição: Valor do Produto difere do produto Valor Unitário de Comercialização e Quantidade Comercial (NT2011/005) |

![Image](assets/image_000006_8750f11b23b8af1032529e7ab8cae39d9dc46c56a4effdebfe2b7ad87b5632df.png)

|       |      | Obs.: 1. O valor resultante de vUnCom (id:I10a) * qCom (id:I10) deve ser arredondado para um valor numérico com duas decimais; 2. Considerar uma tolerância de R$ 0,01 para mais ou para menos na validação.                                                                                           |         |     |      |                                                                                                                |
|-------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-----|------|----------------------------------------------------------------------------------------------------------------|
| GI14a | I14a | Se NF-e Normal (finNFe=1) : vProd (id:I11) difere de vUnTrib (id:I14a) * qTrib (id:I14) Obs.: 1. O valor resultante de vUnTrib (id:I14a) * qTrib (id:I14) deve ser arredondado para um valor numérico com duas decimais; 2. Considerar uma tolerância de R$ 0,01 para mais ou para menos na validação. | Facult. | 630 | Rej. | Rejeição: Valor do Produto difere do produto Valor Unitário de Tributação e Quantidade Tributável (NT2011/005) |

## Observação:

- As regras não serão aplicadas para a NF de Ajuste  e nem para a NF Complementar;
- Estas regras serão aplicadas no ambiente de produç ão a partir de 01/02/2012.

## 'item 4.9 Validação do valor total da NF'

| #    | Campo   | Regra de Validação          | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                 |
|------|---------|-----------------------------|----------|-------|----------|------------------------------------------------------------------------------------------------|
|      |         | W-Total da NF-e             |          |       |          |                                                                                                |
| GW16 |         | Se NF-e de Saída (tpNF=1) : | Facult.  |   610 | Rej.     | Rejeição: Total da NF difere do somatório dos Valores compõe o valor Total da NF. (NT2011/005) |

![Image](assets/image_000007_61f8fbe6710de144de05067ffa96bb6d3718465adb1c5943087141509b90bd0b.png)

| #   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Aplic.   | Msg   | Efeito   | Descrição Erro   |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------|
|     | (+) vFrete (id:W08) (+) vSeg (id:W09) (+) vOutro (id:W15) (+) vII (id:W11) (+) vIPI (id:W12) (+) vServ (id:W18) (*3) Exceção - Faturamento direto de veículos novos: Se NF-e de Saída (tpNF=1, id:B11) e se informada operação de Faturamento Direto para veículos novos (tpOp = 2, id:J02): Total do vNF (id:W16) difere do somatório de: (+) vProd (id:W07) (-) vDesc (id:W10) (+) vFrete (id:W08) (+) vSeg (id:W09) (+) vOutro (id:W15) (+) vII (id:W11) (+) vIPI (id:W12) (+) vServ (id:W18) (*3) |          |       |          |                  |

## Observações:

- A regra será aplicada somente nas notas fiscais de  saída;
- A validação do valor total das notas fiscais de fa turamento de veículos novos não deve considerar o valor informado no campo vST ( id:W06);
- Esta regra será aplicada no ambiente de produção a  partir de 01/02/2012.

## Documentos relacionados
_Nenhum documento relacionado conhecido._
