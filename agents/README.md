# Agents Públicos — Custo Brasil

Agents especializados para consulta e análise do corpus público de documentos fiscais brasileiros.

## Agents disponíveis

| Agent | Descrição | Skill relacionada |
|-------|-----------|-------------------|
| `pesquisador-fiscal` | Localiza e explica evidência normativa no corpus | `consultar-regra-fiscal` |
| `auditor-diff-regulatorio` | Compara versões de documentos normativos | `comparar-notas-tecnicas` |
| `explicador-rejeicao` | Explica códigos de rejeição SEFAZ | `explicar-rejeicao-sefaz` |
| `analisador-schema` | Interpreta metadados de schemas XSD | `mapear-campo-xml` |
| `especialista-reforma-tributaria` | Consulta especializada sobre IBS/CBS | `reforma-tributaria` |

## Base de conhecimento compartilhada

`CORPUS.md` contém a referência completa da estrutura do corpus, campos de front matter, categorias, convenção de slugs e localização de documentos. **Leia este arquivo antes de usar qualquer agent.**

## Skills complementares

Skills públicas em `skills/` fornecem passo-a-passo operacionais para cada domínio. Consulte `skills/README.md`.

## Procedência

Use o front matter YAML dos documentos como fonte primária de autenticidade (`slug`, `canonical_id`, `source_url`, `original_sha256`, `status`, `converted_at`). Consulte `CORPUS.md` para a referência completa dos campos de metadados.

> **Aviso**: Este projeto não substitui a fonte oficial, os schemas XML oficiais, a legislação aplicável ou a validação pelos órgãos competentes.
