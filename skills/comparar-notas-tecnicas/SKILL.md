---
name: comparar-notas-tecnicas
description: Compara duas versões de notas técnicas ou manuais do corpus, identificando adições, remoções e modificações com evidência textual e datas de vigência.
---

# Skill: Comparar Notas Técnicas

Use esta skill quando o usuário fornecer dois slugs do corpus (ex: `nt-2015-001-v-1-30` e `nt-2015-002-v141`) ou quando uma consulta exigir identificar diferenças entre versões de um mesmo documento.

## Passos

1. **Localize ambos os documentos** no corpus usando `agents/CORPUS.md` como guia de navegação. Documentos NF-e estão em `corpus/nfe/notas-tecnicas/`. Confirme slugs e `canonical_id` no front matter YAML de cada `document.md`.

2. **Consulte os changelogs** em `changelog/{categoria}/{subdir}/{slug}.md` para cada documento. O changelog fornece o histórico de publicações e alterações. Compare as entradas cronológicas.

3. **Compare os documentos**: leia ambos os `document.md` e identifique:
   - Diferenças textuais (parágrafos adicionados/removidos/modificados)
   - Diferenças estruturais (seções, tabelas, schemas referenciados)
   - Diferenças de vigência (datas de teste/produção, cronogramas)
   - Diferenças de hash (`original_sha256` no front matter)

4. **Não alegue revogação** sem evidência explícita no changelog ou no corpo do documento. Apenas um documento que explicitamente substitui o outro pode ser citado como revogador.

5. **Preserve as referências cruzadas**: se um documento referencia outro (ex: uma NT referencia um informe técnico ou schema), inclua essas referências na análise. Consulte `agents/CORPUS.md` para localizar documentos relacionados por categoria.

## Saída

Lista de adições, remoções e modificações com citação textual, data de vigência de cada versão e nível de confiança.

## Procedência

Consulte `agents/CORPUS.md` para a referência completa do corpus. Documentos estaduais seguem estrutura diferente — verifique slugs em `corpus/nfe/Estado de <UF>/`.
