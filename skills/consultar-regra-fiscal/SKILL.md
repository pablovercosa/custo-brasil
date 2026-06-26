---
name: consultar-regra-fiscal
description: Consulta a base normativa do corpus para localizar e explicar regras fiscais, campos, condições, exceções ou alíquotas com evidência documental rastreável.
---

# Skill: Consultar Regra Fiscal

Use esta skill para consultas fiscais pontuais: obrigatoriedade de campo, alíquota aplicável, código de CFOP/NCM, benefício fiscal, condição de emissão, prazo ou exceção.

## Passos

1. **Identifique o tipo de consulta** e a categoria de documento mais provável:
   - Regra de leiaute/validação NF-e → `corpus/nfe/notas-tecnicas/`
   - Tabela de código (CFOP, NCM, município, FCP) → `corpus/geral/tabelas-federais/` ou `corpus/nfe/informes-tecnicos/`
   - Benefício fiscal estadual → `corpus/nfe/Estado de <UF>/`
   - Alíquota CBS → `corpus/reforma-tributaria/` ou `corpus/geral/tabelas-federais/aliquotas-cbs-2026/`
   - Manual de especificação → `corpus/nfe/manuais/`
   - Consulte `agents/CORPUS.md` para a árvore completa.

2. **Extraia o front matter** do(s) documento(s) candidato(s) para confirmar: `slug`, `canonical_id`, `category`, `status`, `source_family`, `source_url`, `original_sha256`, `converted_at`. Estes campos garantem a rastreabilidade da resposta.

3. **Responda com a regra localizada**, citando: documento, seção, versão (`converted_at`), hash do original (`original_sha256`) e página/seção relevante dentro do `document.md`.

4. **Não invente regra**. Se nenhum documento no corpus contiver a regra solicitada:
   - Informe que a evidência não foi encontrada no corpus.
   - Não crie regra, código, prazo, alíquota, exceção ou obrigação.
   - Diferencie entre "não documentado no corpus" e "não existe".

5. **Diferencie orientação documental de validação formal** — Um campo pode ser opcional no schema XSD (estrutura) mas obrigatório por regra de negócio (NT). Consulte ambos: schema em `corpus/{categoria}/schema/{PL}/` e NT em `corpus/{categoria}/notas-tecnicas/`.

## Saída

Resposta objetiva + slug, path, `source_url`, `original_sha256` e `converted_at` da fonte.

## Procedência

Consulte `agents/CORPUS.md` para navegação. Use `sources/source-pages.json` para identificar URLs de origem das páginas do Portal NF-e.
