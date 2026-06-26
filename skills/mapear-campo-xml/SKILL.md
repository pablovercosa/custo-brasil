---
name: mapear-campo-xml
description: Localiza e interpreta metadados de campos XML nos schemas XSD e documentação do corpus, diferenciando estrutura de regra de negócio.
---

# Skill: Mapear Campo XML

Use esta skill quando o usuário perguntar sobre a definição, tipo, obrigatoriedade, formato ou valores permitidos de um campo XML de documento fiscal eletrônico.

## Passos

1. **Identifique o caminho do campo XML** (ex: `NFe/infNFe/ide/nNF`, `NFe/infNFe/dest/CNPJ`, `NFe/infNFe/det/prod/CFOP`) e opcionalmente a versão de PL (ex: `PL_009v`, `PL_010`).

2. **Localize o schema XSD** no corpus em `corpus/{categoria}/schema/{PL}/`. Consulte `agents/CORPUS.md` para a lista de PLs por categoria. Se a versão de PL não for especificada, use o schema mais recente disponível para a categoria do documento (NF-e, NFC-e, NFAg etc.).

3. **Extraia do XSD**: tipo (`xs:string`, `xs:decimal`, `xs:dateTime`, etc.), cardinalidade (`minOccurs`, `maxOccurs`), padrão (`pattern` com regex), enumeração (`enumeration` com valores permitidos) e documentação (`xs:documentation`).

4. **Consulte a documentação complementar** para regras de negócio:
   - `corpus/nfe/manuais/anexo-i-leiaute-e-regra-de-valida-o-nf-e-e-nfc-e/` (leiaute completo NF-e/NFC-e)
   - Notas Técnicas específicas em `corpus/nfe/notas-tecnicas/`
   - Consulte o front matter do documento para `source_url` e `original_sha256`

5. **Diferencie estrutura de regra de negócio**:
   - **Estrutura (XSD)**: tipo de dado, tamanho, formato, obrigatoriedade no schema
   - **Regra de negócio (NTs/Manuais)**: valores permitidos em contexto, validações condicionais, relações entre campos

6. **Não declare validade final** — A validação formal de um XML só pode ser atestada por processamento do schema em parser XML. Este skill informa metadados, não validade.

## Saída

Caminho do campo, metadados técnicos (tipo, cardinalidade, padrão, enumeração), PL e arquivo XSD de origem, regras de negócio associadas (quando disponíveis).

## Procedência

Consulte `agents/CORPUS.md` para localização dos schemas. Schemas em `corpus/nfe/schema/` são específicos NF-e (modelo 55). Schemas NFC-e estão em `corpus/nfce/schema/`.
