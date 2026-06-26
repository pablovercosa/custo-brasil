---
name: navegar-corpus
description: Guia de navegação e descoberta de documentos no corpus Custo Brasil, permitindo localizar documentos por tipo, ano, estado, categoria ou assunto.
---

# Skill: Navegar Corpus

Use esta skill quando o usuário precisar localizar documentos no corpus sem saber slugs exatos — por exemplo, "encontre NTs de 2023 sobre NFC-e", "qual a tabela de CFOP mais recente", "existe documento sobre split payment", "documentos do estado de São Paulo".

## Passos

1. **Identifique os filtros do usuário**: categoria, tipo de documento, ano, estado, assunto ou palavra-chave.

2. **Use a estrutura do corpus** para direcionar a busca:
   - NTs NF-e → `corpus/nfe/notas-tecnicas/` (filtre slugs por ano: `nt-2023` prefix)
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
   - Consulte `agents/CORPUS.md` para a referência completa.

3. **Aplique filtros por slug**:
   - Por ano: slugs começando com `nt-2023` ou `nt2023` para NTs de 2023
   - Por tipo: `nt-` para notas técnicas, `it` para informes, `tabela-` para tabelas, `cbenef-` para cBenef
   - Por modelo: `nfc` no slug indica NFC-e, `nf-e-` indica NF-e

4. **Use o changelog para verificar atividade** — O changelog em `changelog/{categoria}/{subdir}/{slug}.md` registra quando cada documento foi publicado ou atualizado. Útil para encontrar documentos recentes.

5. **Consulte os schemas para localizar versões de PL** — Schemas estão em `corpus/{categoria}/schema/{PL}/`. Cada PL pode conter múltiplos arquivos XSD. Consulte `agents/CORPUS.md` para a lista de PLs por categoria.

## Saída

Lista de slugs encontrados com título (extraído do front matter de cada documento), path completo no corpus, categoria, data de conversão (`converted_at`) e sugestão de próximos passos (ex: "para detalhes, use a skill `consultar-regra-fiscal`").

## Procedência

Consulte `agents/CORPUS.md` para referência completa da estrutura. Documentos estaduais e federais seguem convenções de nomenclatura diferentes.
