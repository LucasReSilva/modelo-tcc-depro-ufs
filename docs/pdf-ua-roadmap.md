# Roteiro de acessibilidade PDF/UA

## Situação atual

O ramo `feature/pdf-ua` ativa o PDF management e o tagging automático junto com PDF/A-2u e PDF/UA-1. A compilação avançou após adaptações aos dados de título, ao float `quadro` e ao exemplo `listings`, mas ainda falha ao encerrar o documento com erro de contagem dos hooks de parágrafo do `tagpdf`. Portanto, este ramo é um protótipo e não gera atualmente um PDF final nem demonstra conformidade PDF/UA.

Os testes no TeX Live 2026 indicaram `Package tagpdf Error: The number of automatic begin (...) and end (...) text para hooks differ` ao final do documento. Repetir com LuaLaTeX manteve a falha; desativar a marcação automática de parágrafos também não resolveu. A causa deve ser isolada em um exemplo mínimo antes de tentar novos ajustes na classe. O projeto Tagged PDF lista `abntex2` e `memoir` como incompatíveis no estado consultado em 2026-11-20.

## Bloqueios identificados

- `pdfx` está classificado pelo projeto de marcação do LaTeX como incompatível com o PDF management. O protótipo já o substituiu por `\DocumentMetadata` e removeu o placeholder de `\tagpdfsetup`.
- `abntex2` estende `memoir`; ambos estão classificados como incompatíveis com tagging automático. O erro de contagem dos hooks de parágrafo confirma que a incompatibilidade afeta o documento completo e ainda não foi resolvida.
- `listings` é parcialmente compatível; o código-fonte e sua lista precisam ser conferidos na árvore de estrutura e na ordem de leitura.
- `tikz` é parcialmente compatível; cada diagrama precisa de texto alternativo significativo. Figuras, tabelas/quadros, matemática, listas, sumário e elementos pré-textuais também precisam de revisão semântica.
- A validação automática cobre requisitos verificáveis por máquina. A ordem de leitura, a utilidade dos textos alternativos e a leitura de fórmulas ainda exigem inspeção humana com tecnologia assistiva.

## Estratégia inicial

Manter PDF/A-2u como requisito do projeto e investigar primeiro PDF/UA-1 (ISO 14289-1), que usa a base PDF 1.7 da ISO 32000-1. A alternativa PDF/UA-2 (ISO 14289-2) oferece suporte mais rico para matemática, mas usa PDF 2.0 e exigiria reavaliar a escolha atual de PDF/A-2u; não será adotada implicitamente.

O protótipo deve usar a implementação atual do LaTeX Tagged PDF, habilitada antes de `\documentclass`, e remover o `pdfx` e o placeholder antes de ativar as chamadas reais de `\tagpdfsetup`. A classe `abntex2` permanece um risco de compatibilidade que precisa ser tratado e comprovado; habilitar o tagging sem essa verificação não é suficiente.

## Etapas de implementação

1. Criar um caso mínimo com `abntex2` e `memoir` e acrescentar gradualmente capa, folha de rosto, resumo, floats e listas até identificar qual componente desequilibra os hooks de parágrafo.
2. Corrigir ou contornar a incompatibilidade da classe sem deixar conteúdo textual fora da árvore estrutural; se isso exigir uma classe alternativa ou uma adaptação extensa do `memoir`, documentar o impacto antes de trocar a base do modelo.
3. Adaptar os elementos próprios do modelo, preservando a apresentação ABNT, e confirmar a compilação completa com tagging habilitado.
4. Incluir validações informativas no CI para os perfis PDF/A-2u e PDF/UA-1, mantendo a publicação do PDF independente da validação informativa.
5. Revisar o PDF com leitor de tela/visualização da árvore de estrutura, além do veraPDF, antes de afirmar conformidade.

## Referências técnicas

- [LaTeX Tagged PDF: instruções de uso](https://tagging-project.latex-project.org/documentation/usage-instructions/)
- [Estado de compatibilidade de classes e pacotes com tagging](https://latex3.github.io/tagging-project/tagging-status/)
- [veraPDF: validação PDF/UA e limites dos testes automatizados](https://docs.verapdf.org/validation/)
- [ISO 19005-2:2011 — PDF/A-2](https://www.iso.org/standard/50655.html)
- [ISO 14289-1 — PDF/UA-1](https://www.iso.org/standard/64599.html)
- [ISO 14289-2:2024 — PDF/UA-2](https://www.iso.org/standard/82278.html)
