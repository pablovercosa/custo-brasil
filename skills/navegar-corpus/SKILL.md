---
name: navegar-corpus
description: Guia de navegação e descoberta de documentos no corpus Custo Brasil, permitindo localizar documentos por tipo, ano, estado, categoria ou assunto.
---

# Skill: Navegar Corpus

Use esta skill quando o usuário precisar localizar documentos no corpus sem saber slugs exatos — por exemplo, "encontre NTs de 2023 sobre NFC-e", "qual a tabela de CFOP mais recente", "existe documento sobre split payment", "documentos do estado de São Paulo".

## Script de busca

Use o script `search_corpus.py` para consultas programáticas. Ele lê o front matter YAML de todos os documentos e aplica filtros:

```bash
# Buscar NTs de 2023
python skills/navegar-corpus/search_corpus.py --year 2023 --type nt

# Buscar por palavra-chave
python skills/navegar-corpus/search_corpus.py --keyword "split payment"

# Documentos de um estado
python skills/navegar-corpus/search_corpus.py --state SP

# Últimos 10 documentos convertidos (com changelog)
python skills/navegar-corpus/search_corpus.py --recent 10 --check-changelog --json

# Documento específico por slug
python skills/navegar-corpus/search_corpus.py --slug nt-2023-001
```

Filtros disponíveis: `--category`, `--year`, `--keyword`, `--state`, `--type` (nt/it/tabela/cbenef/manual), `--source`, `--slug`, `--recent N`.

## Passos

1. **Identifique os filtros do usuário**: categoria, tipo de documento, ano, estado, assunto ou palavra-chave. Use o script `search_corpus.py` com os filtros adequados.

2. **Use a estrutura do corpus** para direcionar a busca:
   - NTs NF-e → `corpus/nfe/notas-tecnicas/`
   - NTs NFC-e → `corpus/nfce/notas-tecnicas/`
   - NTs Reforma Tributária → `corpus/reforma-tributaria/notas-tecnicas/`
   - NTs Combustíveis → `corpus/combustiveis/notas-tecnicas/`
   - Informes NF-e → `corpus/nfe/informes-tecnicos/`
   - Tabelas federais → `corpus/geral/tabelas-federais/`
   - Manuais NF-e → `corpus/nfe/manuais/`
   - Manuais NFC-e → `corpus/nfce/manuais/`
   - Manuais NFAg → `corpus/nfag/manuais/`
   - Manuais NFGas → `corpus/nfgas/manuais/`
   - Manuais NFeABI → `corpus/nfeabi/manuais/`
   - Documentos estaduais → `corpus/nfe/Estado de <UF>/` (SP, RS, ES, DF, GO, PR, RJ)
   - Fórmulas de cálculo → `formulas/`
   - Consulte `agents/CORPUS.md` para a referência completa.

3. **Aplique filtros por slug**:
   - Por ano: slugs começando com `nt-2023` ou `nt2023` para NTs de 2023
   - Por tipo: `nt-` para notas técnicas, `it` para informes, `tabela-` para tabelas, `cbenef-` para cBenef
   - Por modelo: `nfc` no slug indica NFC-e, `nf-e-` indica NF-e

4. **Use o changelog para verificar atividade** — O changelog em `changelog/{categoria}/{subdir}/{slug}.md` registra quando cada documento foi publicado ou atualizado. Use `--check-changelog` no script para incluir dados de versão.

5. **Consulte os schemas para localizar versões de PL** — Schemas estão em `corpus/{categoria}/schema/{PL}/`.

## Saída

Lista de slugs encontrados com título (extraído do front matter de cada documento), path completo no corpus, categoria, data de conversão (`converted_at`), versão do changelog (se disponível) e sugestão de próximos passos (ex: "para detalhes, use a skill `consultar-regra-fiscal`").

## Procedência

Consulte `agents/CORPUS.md` para referência completa da estrutura. Documentos estaduais e federais seguem convenções de nomenclatura diferentes.
