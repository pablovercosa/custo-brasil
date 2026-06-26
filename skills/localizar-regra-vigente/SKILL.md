---
name: localizar-regra-vigente
description: Localiza a versão aplicável de uma regra fiscal para uma data de referência específica, usando o changelog e versões documentadas no corpus.
---

# Skill: Localizar Regra Vigente

Use esta skill quando o usuário perguntar qual versão de uma regra, tabela, alíquota ou obrigação estava (ou estará) vigente em uma data específica.

## Passos

1. **Exija uma data de referência** do usuário ("vigente em dd/mm/aaaa"). Sem data, a skill não pode determinar vigência. Neste caso, retorne a versão mais recente disponível no corpus.

2. **Localize todos os documentos relacionados** ao assunto no corpus. Use `agents/CORPUS.md` para navegar:
   - Notas Técnicas → `corpus/{categoria}/notas-tecnicas/`
   - Informes Técnicos → `corpus/{categoria}/informes-tecnicos/`
   - Tabelas → `corpus/geral/tabelas-federais/` (ex: `tabela-cfop-2023`, `tabela-ncm-2022`)
   - Alíquotas CBS → `corpus/geral/tabelas-federais/aliquotas-cbs-2026/`
   - Benefícios fiscais estaduais → `corpus/nfe/Estado de <UF>/`

3. **Consulte o changelog** de cada candidato em `changelog/{categoria}/{subdir}/{slug}.md`. O changelog contém o histórico cronológico de publicações. Compare as datas de publicação com a data de referência.

4. **Informe a regra localizada** com:
   - Slug e título do documento vigente na data de referência
   - Data de vigência documentada no changelog
   - Slug do documento substituído (se houver)
   - `converted_at` e `original_sha256` do front matter

5. **Trate como inconclusivo** se:
   - Nenhum documento tiver data de vigência clara (diferencie `converted_at` — data de conversão — de data de efeito legal)
   - O changelog não registrar a substituição
   - Apenas similaridade semântica indicar vigência (não usar apenas similaridade semântica para determinar vigência)

## Saída

Regra + slug aplicável, data de vigência, documento substituído (se aplicável), nível de confiança.

## Procedência

Consulte `agents/CORPUS.md` para navegação. O changelog é a fonte primária para histórico de versões. A data `converted_at` no front matter é a data de conversão para Markdown, não necessariamente a data de vigência legal.
