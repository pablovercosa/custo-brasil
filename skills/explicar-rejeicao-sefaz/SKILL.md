---
name: explicar-rejeicao-sefaz
description: Explica códigos de rejeição SEFAZ com base nas regras de validação documentadas no corpus, sem inventar causa ou correção.
---

# Skill: Explicar Rejeição SEFAZ

Use esta skill quando o usuário fornecer um código de rejeição (ex: `110`, `217`, `278`, `302`, `656`) ou mensagem de erro retornada por uma SEFAZ ao transmitir ou consultar um documento fiscal eletrônico.

## Passos

1. **Receba o código ou mensagem de rejeição** e o contexto (modelo NF-e ou NFC-e, estado, ambiente).

2. **Consulte as regras de validação** no corpus:
   - NF-e: `corpus/nfe/notas-tecnicas/nt2019-001-v1-70-regras-de-valida-o/`, `nt2020-005-v1-21-regras-de-valida-o/`, `nt2013-005-v1-22/`
   - NFC-e: `corpus/nfce/notas-tecnicas/` (ex: `nt2023-003-v1-20-altera-rv-cfop-nfc-e`)
   - Validação ISSQN: `nt2022-004-v1-10-regras-de-valida-o-issqn/`
   - MOC Anexo I (leiaute completo): `corpus/nfe/manuais/anexo-i-leiaute-e-regra-de-valida-o-nf-e-e-nfc-e/`
   - Verifique o changelog em `changelog/nfe/notas-tecnicas/{slug}.md` para versões atualizadas das regras.
   - Consulte `agents/CORPUS.md` para navegação completa.

3. **Classifique a causa em 3 níveis**:
   - **Causa confirmada**: a regra de validação no corpus contém exatamente o código e a descrição
   - **Causa provável**: o corpus contém regras relacionadas ao mesmo campo/contexto, mas não o código exato
   - **Causa não confirmada**: nenhuma regra no corpus cobre o código ou contexto

4. **Liste campos e condições a verificar** no XML do documento fiscal, com base na documentação encontrada.

5. **Cite a fonte**: slug da NT, path completo, `source_url`, `original_sha256` da regra de validação consultada.

6. **Declare que o retorno oficial da SEFAZ prevalece** sobre qualquer interpretação baseada no corpus. Regras de validação podem variar por estado, versão de schema e ambiente.

## Saída

Código analisado, explicação com fonte, campos relacionados, nível de confiança.

## Procedência

Consulte `agents/CORPUS.md` para localizar regras de validação. Validações estaduais específicas podem não estar documentadas no corpus nacional.
